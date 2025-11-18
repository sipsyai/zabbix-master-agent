#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix LSASS monitoring items
"""

import os
import sys
from pathlib import Path

# Windows console encoding fix
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

from zabbix_utils import ZabbixAPI


def load_env_file():
    """Load environment variables from .env file"""
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent.parent
    env_file = project_root / '.env'

    if not env_file.exists():
        print(f"[-] .env file not found at: {env_file}")
        return False

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value

    return True


def main():
    """Fix LSASS items"""
    if not load_env_file():
        sys.exit(1)

    url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    try:
        print("\n[+] Connecting to Zabbix API...")
        api = ZabbixAPI(url=url, user=username, password=password)
        print(f"[+] Connected! Zabbix version: {api.version}")

        # Get DC01 host
        print("\n[+] Getting DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("[-] DC01 host not found!")
            api.logout()
            return

        hostid = hosts[0]['hostid']
        print(f"[+] DC01 Host ID: {hostid}")

        print("\n[+] Getting LSASS items...")
        items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'type'],
            search={'name': 'LSASS'}
        )

        print(f"[+] Found {len(items)} LSASS items")
        print("=" * 100)

        # Try different counter formats for LSASS
        fixes = [
            {
                'itemid': None,
                'name': 'LSASS: CPU Usage',
                'old_key': r'perf_counter_en["\Process(lsass)\% Processor Time"]',
                'new_key': r'perf_counter_en["\Process(lsass*)\% Processor Time"]'
            },
            {
                'itemid': None,
                'name': 'LSASS: Memory Usage',
                'old_key': r'perf_counter_en["\Process(lsass)\Working Set"]',
                'new_key': r'perf_counter_en["\Process(lsass*)\Working Set"]'
            }
        ]

        # Find item IDs
        for item in items:
            for fix in fixes:
                if item['key_'] == fix['old_key']:
                    fix['itemid'] = item['itemid']
                    print(f"[+] Found: {item['name']} (ID: {item['itemid']})")

        print("\n[+] Attempting fixes...")
        print("=" * 100)

        for fix in fixes:
            if fix['itemid']:
                print(f"\n[*] Fixing: {fix['name']}")
                print(f"    Old key: {fix['old_key']}")
                print(f"    New key: {fix['new_key']}")

                try:
                    # Try with wildcard first
                    api.item.update(
                        itemid=fix['itemid'],
                        key_=fix['new_key']
                    )
                    print(f"    [OK] Updated with wildcard")
                except Exception as e:
                    print(f"    [INFO] Wildcard failed: {e}")
                    print(f"    [*] Trying alternative: disabling item")

                    try:
                        # If wildcard doesn't work, disable the item
                        api.item.update(
                            itemid=fix['itemid'],
                            status=1  # Disabled
                        )
                        print(f"    [OK] Item disabled - manual check needed")
                    except Exception as e2:
                        print(f"    [FAIL] Could not disable: {e2}")

        print("\n" + "=" * 100)
        print("[+] RECOMMENDATIONS:")
        print("""
LSASS Process Monitoring Issues:

The Process performance counter for LSASS may have different names:
1. Try these counter names on DC01 manually:
   - Open Command Prompt as Administrator
   - Run: typeperf -q | findstr /i lsass

2. This will show the exact counter names available

3. Common variations:
   - lsass
   - lsass#1
   - lsass#2 (if multiple instances)

4. Alternative: Use WMI-based monitoring instead of performance counters
        """)

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

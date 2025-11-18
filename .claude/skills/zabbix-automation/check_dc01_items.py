#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check DC01 items for errors and fix invalid parameters
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta

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
    """Check and fix DC01 items"""
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

        # Get all items with their state
        print("\n[+] Getting all items with error states...")
        items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'status', 'type', 'state', 'error', 'lastclock', 'lastvalue'],
            sortfield='name',
            selectHosts=['host']
        )

        print(f"[+] Found {len(items)} total items")
        print("=" * 100)

        # Check items
        unsupported_items = []
        working_items = []
        disabled_items = []
        no_data_items = []

        current_time = datetime.now()
        one_hour_ago = current_time - timedelta(hours=1)

        for item in items:
            status = item['status']  # 0 = enabled, 1 = disabled
            state = item['state']    # 0 = normal, 1 = not supported
            error = item.get('error', '')
            lastclock = int(item.get('lastclock', 0))

            if status == '1':
                disabled_items.append(item)
            elif state == '1':
                unsupported_items.append(item)
            elif lastclock == 0:
                no_data_items.append(item)
            elif lastclock < one_hour_ago.timestamp():
                no_data_items.append(item)
            else:
                working_items.append(item)

        # Summary
        print(f"\n[+] ITEM STATUS SUMMARY:")
        print(f"    Working correctly: {len(working_items)}")
        print(f"    Unsupported/Error: {len(unsupported_items)}")
        print(f"    No data (>1h):     {len(no_data_items)}")
        print(f"    Disabled:          {len(disabled_items)}")

        # Show unsupported items in detail
        if unsupported_items:
            print("\n" + "=" * 100)
            print("[!] UNSUPPORTED/ERROR ITEMS:")
            print("=" * 100)

            for item in unsupported_items:
                print(f"\nItem ID: {item['itemid']}")
                print(f"Name: {item['name']}")
                print(f"Key: {item['key_']}")
                print(f"Type: {item['type']}")
                print(f"Error: {item.get('error', 'N/A')}")

        # Show no data items
        if no_data_items:
            print("\n" + "=" * 100)
            print("[!] ITEMS WITH NO RECENT DATA (>1 hour):")
            print("=" * 100)

            for item in no_data_items:
                lastclock = int(item.get('lastclock', 0))
                if lastclock > 0:
                    last_check = datetime.fromtimestamp(lastclock).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    last_check = "Never"

                print(f"\nItem ID: {item['itemid']}")
                print(f"Name: {item['name']}")
                print(f"Key: {item['key_']}")
                print(f"Type: {item['type']}")
                print(f"Last check: {last_check}")

        # Now let's check specifically the items we just added
        print("\n" + "=" * 100)
        print("[+] CHECKING RECENTLY ADDED CRITICAL ITEMS:")
        print("=" * 100)

        critical_item_keys = [
            r'perf_counter_en["\NTDS\DRA Pending Replication Synchronizations"]',
            r'perf_counter_en["\NTDS\DRA Inbound Objects/sec"]',
            r'perf_counter_en["\NTDS\DRA Outbound Objects/sec"]',
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache % Hit"]',
            r'perf_counter_en["\NTDS\LDAP Client Sessions"]',
            r'perf_counter_en["\DNS\Total Query Received/sec"]',
            'proc.cpu.util[lsass.exe]',
            'proc.mem[lsass.exe,,,,rss]',
            r'vfs.dir.count["C:\Windows\SYSVOL\domain\Policies"]',
        ]

        for key in critical_item_keys:
            matching_items = [i for i in items if i['key_'] == key]
            if matching_items:
                item = matching_items[0]
                lastclock = int(item.get('lastclock', 0))
                if lastclock > 0:
                    last_check = datetime.fromtimestamp(lastclock).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    last_check = "Never"

                status_icon = "✓" if item['state'] == '0' and lastclock > 0 else "✗"
                print(f"\n{status_icon} {item['name']}")
                print(f"  Key: {key}")
                print(f"  State: {'NORMAL' if item['state'] == '0' else 'UNSUPPORTED'}")
                print(f"  Last value: {item.get('lastvalue', 'N/A')}")
                print(f"  Last check: {last_check}")
                if item.get('error'):
                    print(f"  Error: {item['error']}")

        # Fix common issues
        print("\n" + "=" * 100)
        print("[+] FIXING COMMON ISSUES:")
        print("=" * 100)

        fixes_applied = []

        # Check for items that should be active agent type instead of passive
        for item in unsupported_items:
            # If item is using eventlog, it should be active
            if 'eventlog[' in item['key_'] and item['type'] == '0':
                print(f"\n[*] Fixing: {item['name']}")
                print(f"    Changing from passive (0) to active (7) agent")
                try:
                    api.item.update(
                        itemid=item['itemid'],
                        type=7  # Zabbix agent (active)
                    )
                    print(f"    [OK] Fixed")
                    fixes_applied.append(item['name'])
                except Exception as e:
                    print(f"    [FAIL] Error: {e}")

        # Check for performance counters with wrong encoding
        for item in unsupported_items:
            if 'perf_counter' in item['key_']:
                # Try to suggest the correct key
                print(f"\n[*] Checking: {item['name']}")
                print(f"    Current key: {item['key_']}")
                print(f"    Error: {item.get('error', 'N/A')}")

                # Common fixes:
                # 1. Database ==> Instances - might need different syntax
                if 'Database ==> Instances' in item['key_']:
                    print(f"    [INFO] This counter might not exist or need admin privileges")
                    print(f"    [INFO] Try checking Performance Monitor on DC01 manually")

        if fixes_applied:
            print(f"\n[+] Applied {len(fixes_applied)} fixes:")
            for name in fixes_applied:
                print(f"    ✓ {name}")
        else:
            print("\n[+] No automatic fixes applied")

        # Save detailed report
        report_file = Path(__file__).parent / 'dc01_item_check_report.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': current_time.isoformat(),
                'summary': {
                    'total': len(items),
                    'working': len(working_items),
                    'unsupported': len(unsupported_items),
                    'no_data': len(no_data_items),
                    'disabled': len(disabled_items)
                },
                'unsupported_items': [
                    {
                        'itemid': i['itemid'],
                        'name': i['name'],
                        'key': i['key_'],
                        'type': i['type'],
                        'error': i.get('error', '')
                    } for i in unsupported_items
                ],
                'no_data_items': [
                    {
                        'itemid': i['itemid'],
                        'name': i['name'],
                        'key': i['key_'],
                        'lastclock': i.get('lastclock', 0)
                    } for i in no_data_items
                ]
            }, f, indent=2, ensure_ascii=False)

        print(f"\n[+] Detailed report saved to: {report_file}")

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix incorrect item parameters on DC01
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
    """Fix DC01 items"""
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

        # Get all items
        print("\n[+] Getting items...")
        items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'type', 'state', 'error'],
            filter={'state': '1'}  # Only unsupported items
        )

        print(f"[+] Found {len(items)} unsupported items")
        print("=" * 100)

        fixed_items = []
        deleted_items = []
        failed_items = []

        # Define fixes
        fixes = {
            # service.state -> service.info (Windows uses service.info)
            'service.state[NTDS]': {
                'action': 'update',
                'key_': 'service.info[NTDS,state]'
            },
            'service.state[ADWS]': {
                'action': 'update',
                'key_': 'service.info[ADWS,state]'
            },
            'service.state[DFSR]': {
                'action': 'update',
                'key_': 'service.info[DFSR,state]'
            },
            'service.state[DNS]': {
                'action': 'update',
                'key_': 'service.info[DNS,state]'
            },
            'service.state[IsmServ]': {
                'action': 'update',
                'key_': 'service.info[IsmServ,state]'
            },
            'service.state[KDC]': {
                'action': 'update',
                'key_': 'service.info[KDC,state]'
            },
            'service.state[Netlogon]': {
                'action': 'update',
                'key_': 'service.info[Netlogon,state]'
            },

            # proc.cpu.util -> perf_counter (Windows doesn't support proc.cpu.util)
            'proc.cpu.util[lsass.exe]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Process(lsass)\% Processor Time"]'
            },

            # proc.mem -> perf_counter (Windows uses different format)
            'proc.mem[lsass.exe,,,,rss]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Process(lsass)\Working Set"]'
            },

            # Database counters - correct paths
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache % Hit"]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache % Hit"]',
                'description': 'May need ESE provider installation or different Windows version'
            },
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache Size (MB)"]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\Database Cache Size (MB)"]',
                'description': 'May need ESE provider installation'
            },
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Reads/sec"]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Reads/sec"]',
                'description': 'May need ESE provider installation'
            },
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Writes/sec"]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Database Writes/sec"]',
                'description': 'May need ESE provider installation'
            },
            r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Log Writes/sec"]': {
                'action': 'update',
                'key_': r'perf_counter_en["\Database ==> Instances(lsass/NTDS)\I/O Log Writes/sec"]',
                'description': 'May need ESE provider installation'
            },

            # Kerberos counters - check if counter name is correct
            r'perf_counter_en["\Kerberos Key Distribution Center\AS Requests/sec"]': {
                'action': 'disable',
                'reason': 'Counter not available on this system. Enable manually if counter exists.'
            },
            r'perf_counter_en["\Kerberos Key Distribution Center\TGS Requests/sec"]': {
                'action': 'disable',
                'reason': 'Counter not available on this system. Enable manually if counter exists.'
            }
        }

        # Apply fixes
        for item in items:
            key = item['key_']

            if key in fixes:
                fix = fixes[key]
                action = fix['action']

                print(f"\n[*] Processing: {item['name']}")
                print(f"    Current key: {key}")
                print(f"    Error: {item.get('error', 'N/A')}")

                try:
                    if action == 'update':
                        new_key = fix['key_']
                        if new_key != key:
                            print(f"    Action: Updating key to: {new_key}")
                            api.item.update(
                                itemid=item['itemid'],
                                key_=new_key
                            )
                            print(f"    [OK] Item updated")
                            fixed_items.append(item['name'])
                        else:
                            print(f"    [INFO] {fix.get('description', 'Cannot fix automatically')}")
                            # Disable these problematic items
                            print(f"    Action: Disabling item")
                            api.item.update(
                                itemid=item['itemid'],
                                status=1  # Disabled
                            )
                            print(f"    [OK] Item disabled")
                            fixed_items.append(item['name'] + " (disabled)")

                    elif action == 'disable':
                        print(f"    Action: Disabling - {fix['reason']}")
                        api.item.update(
                            itemid=item['itemid'],
                            status=1  # Disabled
                        )
                        print(f"    [OK] Item disabled")
                        fixed_items.append(item['name'] + " (disabled)")

                    elif action == 'delete':
                        print(f"    Action: Deleting - {fix['reason']}")
                        api.item.delete(item['itemid'])
                        print(f"    [OK] Item deleted")
                        deleted_items.append(item['name'])

                except Exception as e:
                    print(f"    [FAIL] Error: {e}")
                    failed_items.append({'name': item['name'], 'error': str(e)})

        # Summary
        print("\n" + "=" * 100)
        print("[+] FIX SUMMARY")
        print(f"    Fixed/Updated: {len(fixed_items)}")
        print(f"    Deleted: {len(deleted_items)}")
        print(f"    Failed: {len(failed_items)}")

        if fixed_items:
            print("\n[+] Fixed items:")
            for name in fixed_items:
                print(f"    ✓ {name}")

        if deleted_items:
            print("\n[+] Deleted items:")
            for name in deleted_items:
                print(f"    ✗ {name}")

        if failed_items:
            print("\n[-] Failed items:")
            for item in failed_items:
                print(f"    ✗ {item['name']}")
                print(f"      Error: {item['error']}")

        # Recommendations
        print("\n" + "=" * 100)
        print("[+] RECOMMENDATIONS:")
        print("""
1. Database counters require ESE (Extensible Storage Engine) performance counters
   - These may not be available on all Windows Server versions
   - Check Performance Monitor on DC01: perfmon.exe -> Add Counter -> Database

2. If Kerberos counters exist on DC01:
   - Open Performance Monitor and verify counter names
   - Re-enable the items with correct counter names

3. Monitor items for 5-10 minutes to verify they are now working

4. Check Zabbix agent log on DC01: C:\\Program Files\\Zabbix Agent\\zabbix_agentd.log
        """)

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

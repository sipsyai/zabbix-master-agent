#!/usr/bin/env python3
"""
Check ADLogon plugin items on DC01 host
"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from zabbix_utils import ZabbixAPI

# Load environment variables from root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
env_path = os.path.join(root_dir, '.env')
load_dotenv(env_path)

ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

if not all([ZABBIX_URL, ZABBIX_USER, ZABBIX_PASSWORD]):
    print(f"[FAIL] Missing environment variables!")
    print(f"Looking for .env at: {env_path}")
    print(f"ZABBIX_URL: {ZABBIX_URL}")
    print(f"ZABBIX_USERNAME: {ZABBIX_USER}")
    sys.exit(1)

def main():
    print("=" * 80)
    print("ADLogon Plugin Items Status Check")
    print("=" * 80)

    # Connect to Zabbix
    print(f"\nConnecting to Zabbix at {ZABBIX_URL}...")

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Authenticated successfully")

        # Get DC01 host
        print("\nSearching for DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name', 'status']
        )

        if not hosts:
            print("[FAIL] DC01 host not found!")
            sys.exit(1)

        host = hosts[0]
        print(f"[OK] Found host: {host['host']} (ID: {host['hostid']})")
        print(f"     Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")

        # Get all ADLogon items
        print("\nGetting ADLogon items...")
        items = api.item.get(
            hostids=host['hostid'],
            search={'key_': 'ad.logon'},
            output=['itemid', 'name', 'key_', 'status', 'state', 'lastvalue', 'lastclock', 'error'],
            selectLastEvent=['eventid', 'value']
        )

        if not items:
            print("[WARN] No ad.logon items found!")
            sys.exit(0)

        print(f"[OK] Found {len(items)} ADLogon items\n")

        # Display item status
        print("=" * 80)
        print("ITEM STATUS")
        print("=" * 80)

        for item in items:
            status = 'Enabled' if item['status'] == '0' else 'Disabled'
            state = {
                '0': 'Normal',
                '1': 'Not supported'
            }.get(item['state'], 'Unknown')

            print(f"\n{'='*80}")
            print(f"Item: {item['name']}")
            print(f"Key:  {item['key_']}")
            print(f"Status: {status}")
            print(f"State:  {state}")

            if item.get('lastclock') and item['lastclock'] != '0':
                last_time = datetime.fromtimestamp(int(item['lastclock']))
                print(f"Last Check: {last_time.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Last Value: {item.get('lastvalue', 'N/A')}")
            else:
                print("Last Check: Never")
                print("Last Value: No data yet")

            if item.get('error'):
                print(f"ERROR: {item['error']}")

        # Summary
        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)

        enabled = sum(1 for i in items if i['status'] == '0')
        normal = sum(1 for i in items if i['state'] == '0')
        has_data = sum(1 for i in items if i.get('lastclock') and i['lastclock'] != '0')
        errors = sum(1 for i in items if i.get('error'))

        print(f"Total Items:    {len(items)}")
        print(f"Enabled:        {enabled}")
        print(f"Normal State:   {normal}")
        print(f"Has Data:       {has_data}")
        print(f"With Errors:    {errors}")

        if errors > 0:
            print("\n⚠️  Some items have errors - check logs!")
        elif has_data == 0:
            print("\n⏳ Waiting for first data collection...")
        elif has_data < len(items):
            print("\n⏳ Partial data collected, waiting for more...")
        else:
            print("\n✅ All items collecting data successfully!")

    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        api.logout()

if __name__ == '__main__':
    main()

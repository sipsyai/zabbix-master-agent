#!/usr/bin/env python3
"""
Remove all AD items from DC01 host
"""

import os
import sys
from dotenv import load_dotenv
from zabbix_utils import ZabbixAPI

# Load environment variables from root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
env_path = os.path.join(root_dir, '.env')
load_dotenv(env_path)

ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

def main():
    print("=" * 80)
    print("Remove AD Items from DC01 Host")
    print("=" * 80)

    try:
        # Connect to Zabbix
        print(f"\nConnecting to Zabbix at {ZABBIX_URL}...")
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Authenticated successfully")

        # Get DC01 host
        print("\nSearching for DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("[FAIL] DC01 host not found!")
            sys.exit(1)

        host = hosts[0]
        print(f"[OK] Found host: {host['host']} (ID: {host['hostid']})")

        # Get all AD items (items with "ad.logon" key or "AD:" in name)
        print("\nSearching for AD items...")
        items = api.item.get(
            hostids=host['hostid'],
            search={'key_': 'ad.logon'},
            output=['itemid', 'name', 'key_']
        )

        if not items:
            print("[INFO] No AD items found!")
            sys.exit(0)

        print(f"[OK] Found {len(items)} AD items to remove:\n")

        # Display items to be deleted
        for i, item in enumerate(items, 1):
            print(f"  {i}. {item['name']}")
            print(f"     Key: {item['key_']}")
            print(f"     ID: {item['itemid']}\n")

        # Confirm deletion
        print("=" * 80)
        response = input(f"\nAre you sure you want to delete {len(items)} items? (yes/no): ")

        if response.lower() != 'yes':
            print("\n[CANCELLED] No items were deleted.")
            sys.exit(0)

        # Delete items
        print("\nDeleting items...")
        item_ids = [item['itemid'] for item in items]

        result = api.item.delete(*item_ids)

        print(f"\n[OK] Successfully deleted {len(result['itemids'])} items!")

        # Summary
        print("\n" + "=" * 80)
        print("DELETION COMPLETE")
        print("=" * 80)
        print(f"Host: {host['host']}")
        print(f"Items deleted: {len(result['itemids'])}")
        print("=" * 80)

    except Exception as e:
        print(f"\n[FAIL] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        api.logout()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Link SNMP templates to devices
"""
import os
import sys
from dotenv import load_dotenv
from zabbix_utils import ZabbixAPI

# Set UTF-8 encoding for output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Load environment variables
load_dotenv()

ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

# Template mappings
TEMPLATE_MAPPINGS = {
    'CORE-SWITCH-01': {'template': 'Cisco IOS by SNMP', 'template_id': '10218'},
    'EDGE-ROUTER-01': {'template': 'Cisco IOS by SNMP', 'template_id': '10218'},
    'PERIMETER-FW-01': {'template': 'Generic by SNMP', 'template_id': '10563'},
}

def main():
    """Link templates to hosts"""

    print("=" * 70)
    print("Linking SNMP Templates to Devices")
    print("=" * 70)
    print()

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print()

        for hostname, config in TEMPLATE_MAPPINGS.items():
            print(f"Processing: {hostname}")
            print("-" * 70)

            # Get host
            hosts = api.host.get(filter={'host': hostname})
            if not hosts:
                print(f"  [ERROR] Host not found!")
                print()
                continue

            host_id = hosts[0]['hostid']
            print(f"  Host ID: {host_id}")
            print(f"  Template: {config['template']} (ID: {config['template_id']})")

            # Link template
            try:
                result = api.host.update(
                    hostid=host_id,
                    templates=[{'templateid': config['template_id']}]
                )
                print(f"  [OK] Template linked successfully!")
                print()

            except Exception as e:
                print(f"  [ERROR] Failed to link template: {e}")
                print()
                continue

        print("=" * 70)
        print("Waiting for data collection (this may take a few minutes)...")
        print("=" * 70)
        print()

        # Check if data is being collected
        import time
        time.sleep(5)  # Wait a bit for Zabbix to start collecting

        for hostname in TEMPLATE_MAPPINGS.keys():
            hosts = api.host.get(
                filter={'host': hostname},
                selectItems=['itemid', 'name', 'key_', 'lastvalue', 'lastclock', 'state'],
                selectInterfaces=['available']
            )

            if hosts:
                host = hosts[0]
                items = host.get('items', [])
                enabled_items = [i for i in items if i['state'] == '0']

                print(f"{hostname}:")
                print(f"  Total items: {len(items)}")
                print(f"  Enabled items: {len(enabled_items)}")

                if host.get('interfaces'):
                    availability = host['interfaces'][0].get('available', '0')
                    avail_text = {'0': 'Unknown', '1': 'Available', '2': 'Unavailable'}.get(availability, availability)
                    print(f"  Interface availability: {avail_text}")

                # Show some items with data
                items_with_data = [i for i in enabled_items if i.get('lastvalue')]
                if items_with_data:
                    print(f"  Items with data: {len(items_with_data)}")
                    print(f"  Sample data:")
                    for item in items_with_data[:5]:
                        print(f"    - {item['name']}: {item.get('lastvalue', 'N/A')}")
                else:
                    print(f"  [INFO] No data collected yet. Please wait a few minutes.")

                print()

        print("=" * 70)
        print("[OK] Template linking completed!")
        print("[INFO] Check Zabbix web interface for full details")
        print("=" * 70)

        api.logout()

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

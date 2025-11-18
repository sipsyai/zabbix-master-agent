#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Delete Network Discovery Rules
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

# Zabbix connection details
ZABBIX_URL = os.getenv('ZABBIX_API_URL')
ZABBIX_USER = os.getenv('ZABBIX_USERNAME')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

def main():
    """Main function"""
    print("Deleting Network Discovery Rules...")

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")

        # Get all discovery rules with CDP or LLDP
        discovery_rules = api.discoveryrule.get(
            output=['itemid', 'name', 'key_'],
            filter={'key_': ['cdp.neighbor.discovery', 'lldp.neighbor.discovery']}
        )

        if discovery_rules:
            print(f"[INFO] Found {len(discovery_rules)} discovery rules to delete")
            rule_ids = [rule['itemid'] for rule in discovery_rules]

            for rule in discovery_rules:
                print(f"  - {rule['name']} (ID: {rule['itemid']})")

            # Delete discovery rules
            api.discoveryrule.delete(rule_ids)
            print(f"[OK] Deleted {len(discovery_rules)} discovery rules")
        else:
            print("[INFO] No discovery rules found to delete")

        api.logout()

    except Exception as e:
        print(f"[ERROR] Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

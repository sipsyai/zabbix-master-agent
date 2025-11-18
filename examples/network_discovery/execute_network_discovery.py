#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Execute Network Discovery Rules (CDP & LLDP)
Manually triggers discovery rules to collect neighbor information
"""
import os
import sys
import time
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

    print("=" * 70)
    print("Execute Network Discovery Rules (CDP & LLDP)")
    print("=" * 70)
    print()

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print(f"[OK] Zabbix version: {api.version}")
        print()

        # Get SNMP devices
        device_names = ['CORE-SWITCH-01', 'EDGE-ROUTER-01', 'PERIMETER-FW-01']

        # Get hosts
        hosts = api.host.get(
            filter={'host': device_names},
            output=['hostid', 'host', 'name']
        )

        if not hosts:
            print("[ERROR] No SNMP devices found!")
            api.logout()
            sys.exit(1)

        print(f"[INFO] Found {len(hosts)} SNMP devices")
        print()

        executed_count = 0

        # Execute discovery for each host
        for host in hosts:
            print(f"Processing: {host['name']}")

            # Get discovery rules for this host
            discovery_rules = api.discoveryrule.get(
                hostids=host['hostid'],
                filter={'key_': ['cdp.neighbor.discovery', 'lldp.neighbor.discovery']},
                output=['itemid', 'name', 'key_']
            )

            if discovery_rules:
                for rule in discovery_rules:
                    print(f"  Executing: {rule['name']}...", end=' ')
                    try:
                        # Execute discovery rule
                        # Note: Zabbix API doesn't have direct "execute now" method
                        # We'll use task.create to schedule immediate execution
                        api.task.create(
                            type=6,  # Check now
                            request={
                                'itemid': rule['itemid']
                            }
                        )
                        print("[OK]")
                        executed_count += 1
                        time.sleep(0.5)
                    except Exception as e:
                        print(f"[FAILED] {e}")
            else:
                print(f"  [WARN] No discovery rules found")

            print()

        print("=" * 70)
        print(f"[OK] Executed {executed_count} discovery rules")
        print("=" * 70)
        print()
        print("[INFO] Discovery is running in background...")
        print("[INFO] Check results in a few minutes at:")
        print("        Monitoring -> Latest data -> Filter by host")
        print()

        api.logout()

    except Exception as e:
        print(f"[ERROR] Failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()

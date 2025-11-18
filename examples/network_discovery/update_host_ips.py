#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update host IP addresses in Zabbix
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

# New IP address (Windows host IP that Zabbix can reach)
HOST_IP = '192.168.1.7'

# Host configurations
HOSTS = [
    {'name': 'CORE-SWITCH-01', 'port': '2001'},
    {'name': 'EDGE-ROUTER-01', 'port': '2002'},
    {'name': 'PERIMETER-FW-01', 'port': '2003'},
]

def main():
    """Update host IPs"""

    print("=" * 70)
    print("Updating Host IP Addresses")
    print("=" * 70)
    print(f"New IP: {HOST_IP}")
    print()

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print()

        for host_config in HOSTS:
            hostname = host_config['name']
            port = host_config['port']

            print(f"Processing: {hostname}")
            print("-" * 70)

            # Get host with interfaces
            hosts = api.host.get(
                filter={'host': hostname},
                selectInterfaces='extend'
            )

            if not hosts:
                print(f"  [ERROR] Host not found!")
                print()
                continue

            host = hosts[0]
            host_id = host['hostid']

            # Find SNMP interface
            snmp_interface = None
            for iface in host['interfaces']:
                if iface['type'] == '2':  # SNMP
                    snmp_interface = iface
                    break

            if not snmp_interface:
                print(f"  [ERROR] SNMP interface not found!")
                print()
                continue

            print(f"  Host ID: {host_id}")
            print(f"  Current IP: {snmp_interface['ip']}:{snmp_interface['port']}")
            print(f"  New IP: {HOST_IP}:{port}")

            # Update interface
            try:
                api.hostinterface.update(
                    interfaceid=snmp_interface['interfaceid'],
                    ip=HOST_IP,
                    port=port
                )
                print(f"  [OK] Interface updated successfully!")
                print()

            except Exception as e:
                print(f"  [ERROR] Failed to update interface: {e}")
                print()
                continue

        print("=" * 70)
        print("[OK] All host IPs updated!")
        print("[INFO] Wait a few minutes for Zabbix to start collecting data")
        print("=" * 70)

        api.logout()

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

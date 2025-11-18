#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add SNMP simulator devices to Zabbix
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

# SNMP Devices to add
devices = [
    {
        'hostname': 'CORE-SWITCH-01',
        'visible_name': 'CORE-SWITCH-01 (Cisco C2960 Switch)',
        'ip': '127.0.0.1',
        'port': '2001',
        'snmp_community': 'custom/public',
        'description': 'Cisco IOS Switch (C2960) - Server Room - Rack 1',
        'location': 'Server Room - Rack 1',
    },
    {
        'hostname': 'EDGE-ROUTER-01',
        'visible_name': 'EDGE-ROUTER-01 (Cisco 2800 Router)',
        'ip': '127.0.0.1',
        'port': '2002',
        'snmp_community': 'custom/public',
        'description': 'Cisco IOS Router (2800) - Network Room - DMZ',
        'location': 'Network Room - DMZ',
    },
    {
        'hostname': 'PERIMETER-FW-01',
        'visible_name': 'PERIMETER-FW-01 (Firewall)',
        'ip': '127.0.0.1',
        'port': '2003',
        'snmp_community': 'custom/public',
        'description': 'Firewall Simulator - Perimeter Security',
        'location': 'Network Room - Perimeter',
    },
]

def main():
    """Main function to add SNMP devices to Zabbix"""

    print("=" * 70)
    print("Zabbix SNMP Device Addition Script")
    print("=" * 70)
    print(f"Zabbix URL: {ZABBIX_URL}")
    print(f"Username: {ZABBIX_USER}")
    print()

    # Connect to Zabbix API
    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Successfully connected to Zabbix API")
        print(f"[OK] Zabbix version: {api.version}")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to connect to Zabbix API: {e}")
        sys.exit(1)

    # Get or create host group
    try:
        groups = api.hostgroup.get(filter={'name': 'SNMP Devices'})
        if groups:
            group_id = groups[0]['groupid']
            print(f"[OK] Found existing group 'SNMP Devices' (ID: {group_id})")
        else:
            result = api.hostgroup.create(name='SNMP Devices')
            group_id = result['groupids'][0]
            print(f"[OK] Created new group 'SNMP Devices' (ID: {group_id})")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to get/create host group: {e}")
        api.logout()
        sys.exit(1)

    # Add each device
    for device in devices:
        print(f"Processing: {device['hostname']}")
        print("-" * 70)

        try:
            # Check if host already exists
            existing_hosts = api.host.get(filter={'host': device['hostname']})
            if existing_hosts:
                print(f"  [WARN] Host '{device['hostname']}' already exists (ID: {existing_hosts[0]['hostid']})")
                print(f"  -> Skipping...")
                print()
                continue

            # Create host with SNMP interface
            host_params = {
                'host': device['hostname'],
                'name': device['visible_name'],
                'interfaces': [
                    {
                        'type': 2,  # SNMP interface
                        'main': 1,
                        'useip': 1,
                        'ip': device['ip'],
                        'dns': '',
                        'port': device['port'],
                        'details': {
                            'version': 2,  # SNMPv2
                            'community': device['snmp_community'],
                        }
                    }
                ],
                'groups': [{'groupid': group_id}],
                'description': device['description'],
                'inventory_mode': 0,  # Disabled
                'inventory': {
                    'location': device['location']
                }
            }

            result = api.host.create(**host_params)
            host_id = result['hostids'][0]

            print(f"  [OK] Host created successfully!")
            print(f"  -> Host ID: {host_id}")
            print(f"  -> Name: {device['visible_name']}")
            print(f"  -> IP: {device['ip']}:{device['port']}")
            print(f"  -> SNMP Community: {device['snmp_community']}")
            print(f"  -> Location: {device['location']}")
            print()

        except Exception as e:
            print(f"  [ERROR] Failed to create host '{device['hostname']}': {e}")
            print()
            continue

    # Logout
    try:
        api.logout()
        print("=" * 70)
        print("[OK] Successfully logged out from Zabbix API")
        print("=" * 70)
    except Exception as e:
        print(f"[WARN] Warning: Failed to logout: {e}")

if __name__ == '__main__':
    main()

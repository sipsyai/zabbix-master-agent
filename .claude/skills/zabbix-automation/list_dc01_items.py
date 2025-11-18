#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
List all items for DC01 host
"""

import os
import sys
import json
from zabbix_utils import ZabbixAPI

# Force UTF-8 encoding for stdout
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Load .env file manually
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
env_path = os.path.join(project_root, '.env')

# Parse .env file
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
else:
    print(f"Warning: .env file not found at {env_path}")

def main():
    # Get configuration from environment
    zabbix_url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    # Debug output
    print(f"Debug - URL: {zabbix_url}")
    print(f"Debug - Username: {username}")
    print(f"Debug - Password: {'***' if password else 'None'}")
    print()

    if not all([zabbix_url, username, password]):
        print("Error: Missing required environment variables")
        print("Required: ZABBIX_API_URL, ZABBIX_USERNAME, ZABBIX_PASSWORD")
        sys.exit(1)

    print(f"Connecting to Zabbix: {zabbix_url}")
    print("=" * 80)

    try:
        # Connect to Zabbix API and login
        api = ZabbixAPI(url=zabbix_url, user=username, password=password)
        print(f"[OK] Successfully logged in as {username}\n")

        # Get DC01 host
        hosts = api.host.get(
            filter={"host": "DC01"},
            output=['hostid', 'host', 'name', 'status']
        )

        if not hosts:
            print("Error: Host 'DC01' not found")
            api.logout()
            sys.exit(1)

        host = hosts[0]
        print(f"Host Information:")
        print(f"  Host ID: {host['hostid']}")
        print(f"  Host Name: {host['host']}")
        print(f"  Display Name: {host['name']}")
        print(f"  Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")
        print("\n" + "=" * 80)

        # Get all items for DC01
        items = api.item.get(
            hostids=host['hostid'],
            output=['itemid', 'name', 'key_', 'type', 'value_type', 'delay', 'status', 'lastvalue', 'lastclock'],
            sortfield='name',
            sortorder='ASC'
        )

        print(f"\nFound {len(items)} items for host DC01:\n")

        # Display items
        for idx, item in enumerate(items, 1):
            status = "[ENABLED]" if item['status'] == '0' else "[DISABLED]"

            # Item type mapping
            type_map = {
                '0': 'Zabbix agent',
                '1': 'SNMPv1 agent',
                '2': 'Zabbix trapper',
                '3': 'Simple check',
                '4': 'SNMPv2 agent',
                '5': 'Zabbix internal',
                '7': 'Zabbix agent (active)',
                '10': 'External check',
                '11': 'Database monitor',
                '12': 'IPMI agent',
                '13': 'SSH agent',
                '14': 'TELNET agent',
                '15': 'Calculated',
                '16': 'JMX agent',
                '17': 'SNMP trap',
                '18': 'Dependent item',
                '19': 'HTTP agent',
                '20': 'SNMP agent',
                '21': 'Script'
            }

            item_type = type_map.get(item['type'], f"Unknown ({item['type']})")

            print(f"{idx}. {item['name']}")
            print(f"   Key: {item['key_']}")
            print(f"   Type: {item_type}")
            print(f"   Status: {status}")
            print(f"   Update Interval: {item['delay']}")

            if item.get('lastvalue'):
                print(f"   Last Value: {item['lastvalue']}")

            print()

        # Summary
        enabled_items = sum(1 for item in items if item['status'] == '0')
        disabled_items = len(items) - enabled_items

        print("=" * 80)
        print(f"\nSummary:")
        print(f"  Total Items: {len(items)}")
        print(f"  Enabled: {enabled_items}")
        print(f"  Disabled: {disabled_items}")

        # Logout
        api.logout()
        print("\n[OK] Logged out successfully")

    except Exception as e:
        import traceback
        print(f"Error: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inspect DC01 host and list all monitoring items
"""

import os
import sys
import json
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

    print(f"[+] Loading credentials from: {env_file}")

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                os.environ[key] = value
                if 'PASSWORD' not in key:
                    print(f"    {key} = {value}")

    return True


def main():
    """Inspect DC01 host"""
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
        print("\n[+] Searching for DC01 host...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name', 'status'],
            selectInterfaces=['interfaceid', 'type', 'ip', 'dns', 'port'],
            selectHostGroups=['groupid', 'name'],
            selectParentTemplates=['templateid', 'name']
        )

        if not hosts:
            print("[-] DC01 host not found!")
            api.logout()
            return

        host = hosts[0]
        print(f"\n[+] Host found:")
        print(f"    ID: {host['hostid']}")
        print(f"    Hostname: {host['host']}")
        print(f"    Display name: {host['name']}")
        print(f"    Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")

        # Print interfaces
        print(f"\n[+] Interfaces:")
        for iface in host['interfaces']:
            iface_type = {
                '1': 'Agent',
                '2': 'SNMP',
                '3': 'IPMI',
                '4': 'JMX'
            }.get(iface['type'], 'Unknown')
            print(f"    Type: {iface_type}, IP: {iface['ip']}, Port: {iface['port']}")

        # Print host groups
        print(f"\n[+] Host Groups:")
        for group in host.get('hostgroups', []):
            print(f"    - {group['name']}")

        # Print templates
        print(f"\n[+] Linked Templates:")
        for template in host['parentTemplates']:
            print(f"    - {template['name']}")

        # Get items
        print(f"\n[+] Getting monitoring items...")
        items = api.item.get(
            hostids=host['hostid'],
            output=['itemid', 'name', 'key_', 'status', 'type', 'value_type', 'delay'],
            selectTriggers=['triggerid', 'description', 'priority'],
            sortfield='name'
        )

        print(f"\n[+] Found {len(items)} items:")
        print("-" * 100)

        # Group items by category
        categories = {}
        for item in items:
            # Extract category from item name or key
            if ':' in item['name']:
                category = item['name'].split(':')[0]
            else:
                category = "General"

            if category not in categories:
                categories[category] = []
            categories[category].append(item)

        # Print items by category
        for category, category_items in sorted(categories.items()):
            print(f"\n{category} ({len(category_items)} items):")
            for item in category_items:
                status = 'Enabled' if item['status'] == '0' else 'Disabled'
                item_type = {
                    '0': 'Zabbix agent',
                    '2': 'Zabbix trapper',
                    '3': 'Simple check',
                    '7': 'Zabbix agent (active)',
                    '10': 'External check',
                    '11': 'Database monitor',
                    '12': 'IPMI agent',
                    '13': 'SSH agent',
                    '14': 'TELNET agent',
                    '15': 'Calculated',
                    '16': 'JMX agent',
                    '18': 'Dependent item',
                    '19': 'HTTP agent',
                    '20': 'SNMP agent',
                    '21': 'Script'
                }.get(item['type'], f"Type {item['type']}")

                trigger_count = len(item.get('triggers', []))
                trigger_info = f" [{trigger_count} triggers]" if trigger_count > 0 else ""

                print(f"  - {item['name']}")
                print(f"    Key: {item['key_']}")
                print(f"    Type: {item_type}, Status: {status}, Delay: {item['delay']}{trigger_info}")

        # Save to JSON
        output_file = Path(__file__).parent / 'dc01_inspection.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'host': host,
                'items': items
            }, f, indent=2, ensure_ascii=False)
        print(f"\n[+] Full inspection data saved to: {output_file}")

        api.logout()
        print("\n[+] Done!")

    except Exception as e:
        print(f"[-] Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check SNMP devices status and configure templates
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

    print("=" * 70)
    print("Zabbix SNMP Device Status Check & Configuration")
    print("=" * 70)
    print()

    # Connect to Zabbix API
    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print(f"[OK] Zabbix version: {api.version}")
        print()
    except Exception as e:
        print(f"[ERROR] Failed to connect: {e}")
        sys.exit(1)

    # Get our SNMP devices
    device_names = ['CORE-SWITCH-01', 'EDGE-ROUTER-01', 'PERIMETER-FW-01']

    try:
        # Get hosts
        hosts = api.host.get(
            filter={'host': device_names},
            output=['hostid', 'host', 'name', 'status'],
            selectInterfaces=['interfaceid', 'ip', 'port', 'type', 'details', 'available'],
            selectItems=['itemid', 'name', 'key_', 'lastvalue', 'lastclock', 'state'],
            selectTemplates=['templateid', 'name']
        )

        print(f"[INFO] Found {len(hosts)} hosts")
        print()

        # Display host status
        for host in hosts:
            print("=" * 70)
            print(f"Host: {host['name']} ({host['host']})")
            print("-" * 70)
            print(f"  Host ID: {host['hostid']}")
            print(f"  Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")

            # Show interfaces
            print(f"\n  Interfaces:")
            for iface in host['interfaces']:
                iface_type = get_interface_type(iface['type'])
                availability = get_availability_text(iface.get('available', '0'))
                print(f"    - {iface_type}: {iface['ip']}:{iface['port']} [{availability}]")
                if 'details' in iface and iface['details']:
                    print(f"      SNMP Version: v{iface['details'].get('version', 'N/A')}")
                    print(f"      Community: {iface['details'].get('community', 'N/A')}")

            # Show templates
            templates = host.get('templates', [])
            print(f"\n  Templates: {len(templates)}")
            if templates:
                for template in templates:
                    print(f"    - {template['name']}")
            else:
                print("    [WARN] No templates linked!")

            # Show items
            items = host.get('items', [])
            print(f"\n  Items: {len(items)}")
            if items:
                enabled_items = [i for i in items if i['state'] == '0']
                print(f"    Enabled: {len(enabled_items)}")
                print(f"    First 5 items:")
                for item in items[:5]:
                    lastvalue = item.get('lastvalue', 'N/A')
                    state = 'Enabled' if item['state'] == '0' else 'Disabled'
                    print(f"      - {item['name']}: {lastvalue} ({state})")
            else:
                print("    [WARN] No items configured!")

            print()

        # Search for SNMP templates
        print("=" * 70)
        print("Searching for SNMP templates...")
        print("-" * 70)

        templates = api.template.get(
            output=['templateid', 'name'],
            search={'name': 'SNMP'},
            searchByAny=True,
            searchWildcardsEnabled=True
        )

        print(f"[INFO] Found {len(templates)} SNMP templates:")
        for i, template in enumerate(templates[:10], 1):
            print(f"  {i}. {template['name']} (ID: {template['templateid']})")

        if len(templates) > 10:
            print(f"  ... and {len(templates) - 10} more")

        print()

        # Find generic SNMP template
        generic_template = None
        for template in templates:
            if 'Generic SNMP' in template['name'] or 'SNMP device' in template['name']:
                generic_template = template
                break

        if generic_template:
            print(f"[INFO] Found generic SNMP template: {generic_template['name']}")
            print(f"[INFO] Template ID: {generic_template['templateid']}")
            print()

            # Ask if we should link templates
            print("=" * 70)
            print("TEMPLATE LINKING")
            print("-" * 70)

            for host in hosts:
                if not host['templates']:
                    print(f"\n[ACTION] Linking template to {host['name']}...")
                    try:
                        api.host.update(
                            hostid=host['hostid'],
                            templates=[{'templateid': generic_template['templateid']}]
                        )
                        print(f"  [OK] Template linked successfully!")
                    except Exception as e:
                        print(f"  [ERROR] Failed to link template: {e}")
                else:
                    print(f"\n[INFO] {host['name']} already has templates, skipping...")

        else:
            print("[WARN] No generic SNMP template found")
            print("[INFO] You may need to manually link appropriate templates")

        print()
        print("=" * 70)
        print("[OK] Check completed")
        print("=" * 70)

        api.logout()

    except Exception as e:
        print(f"[ERROR] Operation failed: {e}")
        import traceback
        traceback.print_exc()
        api.logout()
        sys.exit(1)

def get_availability_text(code):
    """Convert availability code to text"""
    availability = {
        '0': 'Unknown',
        '1': 'Available',
        '2': 'Unavailable'
    }
    return availability.get(code, f'Unknown ({code})')

def get_interface_type(code):
    """Convert interface type code to text"""
    types = {
        '1': 'Agent',
        '2': 'SNMP',
        '3': 'IPMI',
        '4': 'JMX'
    }
    return types.get(code, f'Unknown ({code})')

if __name__ == '__main__':
    main()

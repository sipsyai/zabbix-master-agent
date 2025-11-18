#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
List all available templates in Zabbix
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

def main():
    """List all templates"""

    try:
        api = ZabbixAPI(url=ZABBIX_URL, user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("[OK] Connected to Zabbix API")
        print()

        # Get all templates
        templates = api.template.get(
            output=['templateid', 'name'],
            sortfield='name'
        )

        print(f"Total templates: {len(templates)}")
        print("=" * 70)

        # Filter SNMP related
        snmp_templates = [t for t in templates if 'snmp' in t['name'].lower() or 'network' in t['name'].lower() or 'cisco' in t['name'].lower()]

        print("\nSNMP/Network/Cisco Templates:")
        print("-" * 70)
        for template in snmp_templates:
            print(f"  {template['name']} (ID: {template['templateid']})")

        if not snmp_templates:
            print("  [WARN] No SNMP/Network templates found!")
            print("\n  First 20 available templates:")
            print("  " + "-" * 66)
            for template in templates[:20]:
                print(f"    {template['name']} (ID: {template['templateid']})")

        api.logout()

    except Exception as e:
        print(f"[ERROR] {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

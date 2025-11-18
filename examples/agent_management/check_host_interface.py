#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check host interface configuration
"""

import os
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def check_host_interface():
    """Check host interface configuration"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Checking Host Interface Configuration")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)

        # Get host with interfaces
        hosts = api.host.get(
            output=['hostid', 'host', 'name', 'status'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True,
            selectInterfaces=['interfaceid', 'type', 'ip', 'dns', 'port', 'useip', 'main']
        )

        if not hosts:
            print("\nHost not found")
            return

        host = hosts[0]
        print(f"\nHost: {host['name']}")
        print(f"Host Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")
        print(f"\nInterfaces ({len(host['interfaces'])}):")
        print(f"{'─' * 80}")

        for iface in host['interfaces']:
            type_map = {'1': 'Agent', '2': 'SNMP', '3': 'IPMI', '4': 'JMX'}
            print(f"\n  Type: {type_map.get(iface['type'], 'Unknown')} (Type {iface['type']})")
            print(f"  IP: {iface['ip']}")
            print(f"  DNS: {iface['dns']}")
            print(f"  Port: {iface['port']}")
            print(f"  Use IP: {'Yes' if iface['useip'] == '1' else 'No (use DNS)'}")
            print(f"  Main: {'Yes' if iface['main'] == '1' else 'No'}")

        # Check Zabbix Server IP
        print(f"\n{'=' * 80}")
        print("ZABBIX SERVER IP VERIFICATION")
        print(f"{'=' * 80}")
        print(f"\n  Config API URL: {api_url}")
        print(f"  Config Server (from .env): 192.168.213.141")
        print(f"  Agent Log shows rejected connections from: 192.168.1.7")
        print(f"\n  Host Interface IP: {host['interfaces'][0]['ip'] if host['interfaces'] else 'N/A'}")

        print(f"\n{'─' * 80}")
        print("ANALYSIS:")
        print(f"{'─' * 80}")
        if host['interfaces']:
            if host['interfaces'][0]['ip'] == '192.168.1.7':
                print("\n  ❌ PROBLEM: Host interface IP (192.168.1.7) doesn't match")
                print("     Zabbix Server IP in agent config (192.168.213.141)!")
                print("\n  SOLUTION:")
                print("     1. Update agent config Server= to 192.168.1.7, OR")
                print("     2. Update host interface IP in Zabbix UI to match agent config")
            else:
                print(f"\n  Interface IP: {host['interfaces'][0]['ip']}")
                print("  Check if this matches the real Zabbix Server IP!")

        api.logout()

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Set up path to use venv if exists
    venv_path = os.path.join(os.path.dirname(__file__), '.claude', 'skills', 'zabbix-automation', 'venv')
    if os.path.exists(venv_path):
        if os.name == 'nt':
            site_packages = os.path.join(venv_path, 'Lib', 'site-packages')
        else:
            site_packages = os.path.join(venv_path, 'lib', f'python{sys.version_info.major}.{sys.version_info.minor}', 'site-packages')
        sys.path.insert(0, site_packages)

    check_host_interface()

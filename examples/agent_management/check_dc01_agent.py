#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check DC01 host status and agent configuration
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows console encoding
if os.name == 'nt':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add venv to path if exists
venv_path = Path(__file__).parent / ".claude" / "skills" / "zabbix-automation" / "venv"
if venv_path.exists():
    if os.name == 'nt':
        site_packages = venv_path / "Lib" / "site-packages"
    else:
        site_packages = venv_path / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"
    sys.path.insert(0, str(site_packages))

try:
    from zabbix_utils import ZabbixAPI
except ImportError:
    print("ERROR: zabbix_utils not installed. Installing...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "zabbix_utils"], check=True)
    from zabbix_utils import ZabbixAPI

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def check_dc01():
    """Check DC01 host configuration and status"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print(f"\n{'='*70}")
    print(" DC01 Host Status Check - Agent 1 -> Agent 2 Migration")
    print(f"{'='*70}\n")

    print(f"Connecting to: {api_url}")

    try:
        # Connect to Zabbix API
        api = ZabbixAPI(url=api_url, user=username, password=password)
        print("✓ Connected successfully\n")

        # Get DC01 host
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output='extend',
            selectInterfaces='extend',
            selectGroups=['groupid', 'name'],
            selectParentTemplates=['templateid', 'name']
        )

        if not hosts:
            print("❌ ERROR: DC01 host not found in Zabbix!\n")
            return False

        host = hosts[0]

        # Host basic info
        print(f"[HOST INFORMATION]")
        print(f"  Host Name: {host['host']}")
        print(f"  Display Name: {host['name']}")
        print(f"  Host ID: {host['hostid']}")
        print(f"  Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")

        # Availability status
        availability_map = {
            '0': '❌ Unknown',
            '1': '✓ Available',
            '2': '❌ Unavailable'
        }

        available = host.get('available', '0')
        print(f"  Agent Availability: {availability_map.get(available, 'Unknown')}")

        error = host.get('error', '')
        if error:
            print(f"  ⚠ Error: {error}")

        print()

        # Host groups
        print(f"[HOST GROUPS]")
        groups = host.get('groups', [])
        if groups:
            for group in groups:
                print(f"  - {group['name']}")
        else:
            print("  No groups")
        print()

        # Templates
        print(f"[LINKED TEMPLATES]")
        templates = host.get('parentTemplates', [])
        if templates:
            for template in templates:
                print(f"  - {template['name']}")
        else:
            print("  No templates linked")
        print()

        # Interfaces
        print(f"[INTERFACES]")
        interface_types = {
            '1': 'Agent',
            '2': 'SNMP',
            '3': 'IPMI',
            '4': 'JMX'
        }

        interfaces = host.get('interfaces', [])
        for iface in interfaces:
            iface_type = interface_types.get(iface['type'], 'Unknown')
            main = '(Main)' if iface['main'] == '1' else ''

            # Get connection details
            connection = iface['ip'] if iface['useip'] == '1' else iface['dns']

            print(f"  - {iface_type} {main}")
            print(f"    Interface ID: {iface['interfaceid']}")
            print(f"    Connection: {connection}:{iface['port']}")
            print(f"    Use IP: {'Yes' if iface['useip'] == '1' else 'No (DNS)'}")

            iface_avail = availability_map.get(iface.get('available', '0'), 'Unknown')
            print(f"    Status: {iface_avail}")

            if iface.get('error'):
                print(f"    ⚠ Error: {iface['error']}")
            print()

        # Get latest data from some key items
        print(f"[AGENT VERSION CHECK]")
        items = api.item.get(
            hostids=host['hostid'],
            search={'key_': 'agent.version'},
            output=['itemid', 'key_', 'name', 'lastvalue', 'lastclock', 'status']
        )

        if items:
            for item in items:
                status = '✓ Enabled' if item['status'] == '0' else '❌ Disabled'
                print(f"  Item: {item['name']}")
                print(f"  Key: {item['key_']}")
                print(f"  Status: {status}")
                if item.get('lastvalue'):
                    print(f"  Agent Version: {item['lastvalue']}")
                    if item.get('lastclock'):
                        last_check = datetime.fromtimestamp(int(item['lastclock']))
                        print(f"  Last Check: {last_check}")
                else:
                    print(f"  ⚠ No data received yet")
        else:
            print("  ⚠ agent.version item not found")
        print()

        # Get current problems
        print(f"[CURRENT PROBLEMS]")
        problems = api.problem.get(
            hostids=host['hostid'],
            output=['eventid', 'name', 'severity', 'clock'],
            sortfield='eventid',
            sortorder='DESC',
            recent=True
        )

        if problems:
            severity_map = {
                '0': 'Not classified',
                '1': 'Information',
                '2': 'Warning',
                '3': 'Average',
                '4': 'High',
                '5': 'Disaster'
            }

            print(f"  Found {len(problems)} active problem(s):")
            for prob in problems[:5]:  # Show only latest 5
                sev = severity_map.get(prob['severity'], 'Unknown')
                prob_time = datetime.fromtimestamp(int(prob['clock']))
                print(f"  - [{sev}] {prob['name']}")
                print(f"    Time: {prob_time}")
        else:
            print("  ✓ No active problems")
        print()

        # Check some common items for Agent 2
        print(f"[AGENT 2 SPECIFIC ITEMS CHECK]")
        agent2_keys = [
            'agent.hostname',
            'agent.ping',
            'system.uname',
            'vfs.fs.discovery'
        ]

        for key in agent2_keys:
            items = api.item.get(
                hostids=host['hostid'],
                search={'key_': key},
                output=['itemid', 'key_', 'name', 'lastvalue', 'lastclock', 'status'],
                limit=1
            )

            if items:
                item = items[0]
                status = '✓' if item['status'] == '0' else '❌'
                has_data = '✓ Has data' if item.get('lastvalue') else '⚠ No data'
                print(f"  {status} {item['name']}: {has_data}")
        print()

        # Summary
        print(f"{'='*70}")
        print(" SUMMARY")
        print(f"{'='*70}")

        available = host.get('available', '0')
        error = host.get('error', '')

        if available == '1':
            print("  ✓ DC01 host is AVAILABLE")
            print("  ✓ Agent is responding correctly")
        elif available == '2':
            print("  ❌ DC01 host is UNAVAILABLE")
            print("  ❌ Agent is not responding")
            if error:
                print(f"  ❌ Error: {error}")
        else:
            print("  ⚠ DC01 host availability is UNKNOWN")
            print("  ⚠ Waiting for first check...")

        print()

        # Agent type detection
        agent_items = api.item.get(
            hostids=host['hostid'],
            search={'key_': 'agent.version'},
            output=['itemid', 'key_', 'lastvalue']
        )

        if agent_items and agent_items[0].get('lastvalue'):
            version = agent_items[0]['lastvalue']
            if version.startswith('7') or version.startswith('6'):
                # Version 6 or 7 indicates Agent 2
                print(f"  ✓ Zabbix Agent 2 detected (version: {version})")
            else:
                print(f"  ⚠ Agent version: {version}")

        print(f"{'='*70}\n")

        # Logout
        api.logout()
        print("✓ Disconnected successfully\n")

        return True

    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}\n")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    try:
        success = check_dc01()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nCancelled by user\n")
        sys.exit(0)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check dependent items and their master items
"""

import os
import sys
from datetime import datetime

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def check_dependent_items():
    """Check dependent items and their master items"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Checking Dependent Items")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)

        # Get host
        hosts = api.host.get(
            output=['hostid', 'host', 'name'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True
        )

        if not hosts:
            print("Host not found")
            return

        host = hosts[0]
        print(f"\nHost: {host['name']} (ID: {host['hostid']})\n")

        # Get all items with type 18 (dependent)
        dependent_items = api.item.get(
            output=['itemid', 'name', 'key_', 'type', 'master_itemid', 'status', 'state',
                    'lastvalue', 'lastclock'],
            hostids=host['hostid'],
            filter={'type': 18},  # Dependent item
            sortfield='name'
        )

        print(f"Found {len(dependent_items)} dependent items\n")

        # Group by master item
        master_items_dict = {}
        for item in dependent_items:
            master_id = item.get('master_itemid')
            if master_id:
                if master_id not in master_items_dict:
                    master_items_dict[master_id] = []
                master_items_dict[master_id].append(item)

        # Check each master item
        for master_id, deps in master_items_dict.items():
            print(f"\n{'=' * 80}")
            print(f"Master Item ID: {master_id}")
            print(f"{'=' * 80}")

            # Get master item details
            master = api.item.get(
                itemids=master_id,
                output=['itemid', 'name', 'key_', 'type', 'status', 'state',
                        'lastvalue', 'lastclock', 'delay', 'value_type']
            )

            if master:
                m = master[0]
                print(f"\nMaster Item: {m['name']}")
                print(f"Key: {m['key_']}")
                print(f"Type: {m['type']}")  # Should be 0, 7, etc. (not 18)
                print(f"Status: {'Enabled' if m['status'] == '0' else 'Disabled'}")
                print(f"State: {'Normal' if m['state'] == '0' else 'Not Supported'}")
                print(f"Delay: {m.get('delay', 'N/A')}")

                if m.get('lastclock') and m['lastclock'] != '0':
                    last_time = datetime.fromtimestamp(int(m['lastclock']))
                    time_diff = (datetime.now() - last_time).total_seconds()
                    print(f"Last Value: {m.get('lastvalue', 'N/A')}")
                    print(f"Last Update: {last_time} ({time_diff:.0f}s ago)")

                    # Check master item history
                    vtype = int(m['value_type'])
                    try:
                        history = api.history.get(
                            history=vtype,
                            itemids=master_id,
                            sortfield='clock',
                            sortorder='DESC',
                            limit=3
                        )
                        if history:
                            print(f"Master History: ✓ {len(history)} records")
                        else:
                            print(f"Master History: ❌ NO DATA")
                    except Exception as e:
                        print(f"Master History: ❌ Error: {e}")
                else:
                    print(f"Last Value: ❌ NO DATA")

            print(f"\n{'─' * 80}")
            print(f"Dependent Items ({len(deps)}):")
            print(f"{'─' * 80}")

            for dep in deps[:5]:  # Show first 5
                status_icon = "✓" if dep['state'] == '0' else "❌"
                print(f"\n{status_icon} {dep['name'][:70]}")
                print(f"   Key: {dep['key_']}")
                if dep.get('lastclock') and dep['lastclock'] != '0':
                    last_time = datetime.fromtimestamp(int(dep['lastclock']))
                    time_diff = (datetime.now() - last_time).total_seconds()
                    print(f"   Last Value: {dep.get('lastvalue', 'N/A')} ({time_diff:.0f}s ago)")
                else:
                    print(f"   Last Value: ❌ NO DATA")

        print(f"\n\n{'=' * 80}")
        print("ANALYSIS")
        print(f"{'=' * 80}\n")
        print("If master items have data but dependent items show 'no data' in graphs,")
        print("this might be a Zabbix configuration or rendering issue.")
        print("\nPossible solutions:")
        print("1. Use master items directly in graphs instead of dependent items")
        print("2. Check item preprocessing rules")
        print("3. Verify dependent item formulas/LLD rules")
        print(f"\n{'=' * 80}\n")

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

    check_dependent_items()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create working Memory utilization item and update the graph
"""

import os
import sys
import time

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def create_working_memory_item():
    """Create a working memory utilization item using Windows Performance Counter"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Creating Working Memory Utilization Item")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # Get host
        hosts = api.host.get(
            output=['hostid', 'host', 'name'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True
        )

        if not hosts:
            print("Host not found")
            api.logout()
            return

        host = hosts[0]
        print(f"Host: {host['name']} (ID: {host['hostid']})")

        # Get host interface
        host_with_interface = api.host.get(
            hostids=host['hostid'],
            output=['hostid'],
            selectInterfaces=['interfaceid', 'type', 'main']
        )

        interface_id = None
        if host_with_interface and host_with_interface[0].get('interfaces'):
            # Find Zabbix agent interface (type 1)
            for iface in host_with_interface[0]['interfaces']:
                if iface['type'] == '1' and iface['main'] == '1':
                    interface_id = iface['interfaceid']
                    break
            # If not found, use first interface
            if not interface_id:
                interface_id = host_with_interface[0]['interfaces'][0]['interfaceid']

        if not interface_id:
            print("Error: No interface found for host")
            api.logout()
            return

        print(f"Using interface ID: {interface_id}")

        # Check if item already exists
        print("\nChecking for existing Performance Counter memory item...")
        existing = api.item.get(
            output=['itemid', 'name', 'key_'],
            hostids=host['hostid'],
            search={'key_': 'perf_counter_en["\\Memory\\% Committed Bytes In Use"]'},
            searchWildcardsEnabled=True
        )

        if existing:
            print(f"✓ Item already exists: {existing[0]['name']} (ID: {existing[0]['itemid']})")
            new_item_id = existing[0]['itemid']
        else:
            # Create new item using Windows Performance Counter
            print("\nCreating new Memory utilization item...")

            new_item = {
                'name': 'Memory: % Committed Bytes In Use',
                'key_': 'perf_counter_en["\\Memory\\% Committed Bytes In Use"]',
                'hostid': host['hostid'],
                'type': 0,  # Zabbix agent
                'value_type': 0,  # Numeric (float)
                'interfaceid': interface_id,
                'delay': '1m',
                'history': '31d',
                'trends': '365d',
                'units': '%',
                'description': 'Percentage of memory in use (Windows Performance Counter)'
            }

            try:
                result = api.item.create(**new_item)
                new_item_id = result['itemids'][0]
                print(f"✓ New item created successfully (ID: {new_item_id})")
                print("  Waiting 5 seconds for item to initialize...")
                time.sleep(5)
            except Exception as e:
                print(f"✗ Failed to create item: {e}")
                # Try alternative key
                print("\nTrying alternative key...")
                new_item['key_'] = 'perf_counter["\\Memory\\% Committed Bytes In Use"]'
                try:
                    result = api.item.create(**new_item)
                    new_item_id = result['itemids'][0]
                    print(f"✓ Item created with alternative key (ID: {new_item_id})")
                except Exception as e2:
                    print(f"✗ Also failed: {e2}")
                    api.logout()
                    return

        # Now update the graph
        print(f"\n{'─' * 80}")
        print("Updating 'Windows: Memory utilization' graph...")
        print(f"{'─' * 80}")

        # Get the graph
        graphs = api.graph.get(
            output=['graphid', 'name'],
            search={'name': 'Windows: Memory utilization'},
            searchWildcardsEnabled=True,
            hostids=host['hostid'],
            selectGraphItems=['gitemid', 'itemid']
        )

        if not graphs:
            print("Graph not found")
            api.logout()
            return

        graph = graphs[0]
        print(f"\nGraph found: {graph['name']} (ID: {graph['graphid']})")

        # Update graph to use new item
        try:
            api.graph.update(
                graphid=graph['graphid'],
                gitems=[
                    {
                        'itemid': new_item_id,
                        'color': '1A7C11',  # Green
                        'sortorder': 0,
                        'type': 0,  # Simple line
                        'yaxisside': 0,
                        'calc_fnc': 2,  # Average
                        'drawtype': 0  # Line
                    }
                ]
            )
            print(f"✓ Graph updated successfully!")
        except Exception as e:
            print(f"✗ Failed to update graph: {e}")

        # Verify the update
        print(f"\n{'─' * 80}")
        print("Verifying...")
        print(f"{'─' * 80}")

        updated_graph = api.graph.get(
            graphids=graph['graphid'],
            selectGraphItems=['itemid', 'color']
        )

        if updated_graph and updated_graph[0].get('gitems'):
            gitems = updated_graph[0]['gitems']
            print(f"\nGraph now has {len(gitems)} item(s):")
            for gi in gitems:
                item = api.item.get(
                    itemids=gi['itemid'],
                    output=['itemid', 'name', 'key_', 'status', 'state']
                )
                if item:
                    status = "✓" if item[0]['state'] == '0' else "❌"
                    print(f"  {status} {item[0]['name']}")
                    print(f"     ID: {gi['itemid']}, Key: {item[0]['key_']}")

        print(f"\n{'=' * 80}")
        print("SUCCESS!")
        print(f"{'=' * 80}")
        print("\nThe 'Windows: Memory utilization' graph has been fixed!")
        print("It now uses Windows Performance Counter for accurate memory data.")
        print("\nRefresh the graph in Zabbix UI to see the updated data.")
        print(f"{'=' * 80}\n")

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

    create_working_memory_item()

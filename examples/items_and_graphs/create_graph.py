#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create graph for Memory page faults per second
"""

import os
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def create_memory_graph():
    """Create a graph for Memory page faults"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Creating Memory Page Faults Graph")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # First, check if graph already exists
        print("\nChecking for existing graphs...")
        existing_graphs = api.graph.get(
            output=['graphid', 'name'],
            search={'name': 'Memory page faults'},
            searchWildcardsEnabled=True
        )

        if existing_graphs:
            print(f"\nFound {len(existing_graphs)} existing graph(s) with 'Memory page faults':")
            for g in existing_graphs:
                print(f"  - {g['name']} (ID: {g['graphid']})")

            # Check if our item is in any of these graphs
            for g in existing_graphs:
                graph_items = api.graph.get(
                    graphids=g['graphid'],
                    selectGraphItems=['itemid']
                )
                if graph_items and graph_items[0].get('gitems'):
                    item_ids = [gi['itemid'] for gi in graph_items[0]['gitems']]
                    if '70811' in item_ids:
                        print(f"\n✓ Item 70811 is already in graph: {g['name']}")
                        print("  No need to create a new graph!")
                        api.logout()
                        return

        # Get item details
        print("\nGetting item details...")
        items = api.item.get(
            itemids='70811',
            output=['itemid', 'name', 'key_', 'hostid', 'units'],
            selectHosts=['hostid', 'host', 'name']
        )

        if not items:
            print("Error: Item 70811 not found!")
            api.logout()
            return

        item = items[0]
        host = item['hosts'][0]

        print(f"\nItem Details:")
        print(f"  Name: {item['name']}")
        print(f"  Host: {host['name']}")
        print(f"  Key: {item['key_']}")

        # Create the graph
        print(f"\nCreating graph for {host['name']}...")

        graph_data = {
            'name': f'Memory: Page Faults per Second [{host['host']}]',
            'width': 900,
            'height': 200,
            'yaxismin': 0,
            'yaxismax': 0,  # Auto-scale
            'show_work_period': 1,
            'show_triggers': 1,
            'graphtype': 0,  # Normal graph
            'show_legend': 1,
            'show_3d': 0,
            'percent_left': 0,
            'percent_right': 0,
            'ymin_type': 0,  # Calculated
            'ymax_type': 0,  # Calculated
            'gitems': [
                {
                    'itemid': item['itemid'],
                    'color': '1A7C11',  # Green color
                    'sortorder': 0,
                    'type': 0,  # Simple line
                    'yaxisside': 0,  # Left axis
                    'calc_fnc': 2,  # Average
                    'drawtype': 0  # Line
                }
            ]
        }

        result = api.graph.create(**graph_data)

        if result and result.get('graphids'):
            graph_id = result['graphids'][0]
            print(f"\n{'=' * 80}")
            print("✓ SUCCESS! Graph created successfully!")
            print(f"{'=' * 80}")
            print(f"\nGraph ID: {graph_id}")
            print(f"Graph Name: {graph_data['name']}")
            print(f"\nYou can now view this graph in Zabbix UI:")
            print(f"  1. Go to Monitoring -> Hosts")
            print(f"  2. Find host: {host['name']}")
            print(f"  3. Click on Graphs")
            print(f"  4. Select: {graph_data['name']}")
            print(f"\n{'=' * 80}")
        else:
            print("\n✗ Failed to create graph")
            print(f"Response: {result}")

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

    create_memory_graph()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a new graph for Memory % Committed Bytes In Use
"""

import os
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def create_memory_util_graph():
    """Create graph for Memory % Committed Bytes In Use"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Creating Memory Committed Bytes Graph")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # Check if graph already exists
        existing = api.graph.get(
            output=['graphid', 'name'],
            search={'name': 'Memory: Committed Bytes'},
            searchWildcardsEnabled=True
        )

        if existing:
            print(f"\nGraph already exists: {existing[0]['name']} (ID: {existing[0]['graphid']})")
            api.logout()
            return

        # Create the graph
        graph_data = {
            'name': 'Memory: Committed Bytes In Use (%) [DESKTOP-JK5G34L]',
            'width': 900,
            'height': 200,
            'yaxismin': 0,
            'yaxismax': 100,
            'show_work_period': 1,
            'show_triggers': 1,
            'graphtype': 0,  # Normal graph
            'show_legend': 1,
            'show_3d': 0,
            'percent_left': 0,
            'percent_right': 0,
            'ymin_type': 1,  # Fixed (0%)
            'ymax_type': 1,  # Fixed (100%)
            'gitems': [
                {
                    'itemid': '70899',  # Memory: % Committed Bytes In Use
                    'color': 'C80000',  # Red color for memory usage
                    'sortorder': 0,
                    'type': 0,  # Simple line
                    'yaxisside': 0,  # Left axis
                    'calc_fnc': 2,  # Average
                    'drawtype': 5  # Gradient line
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
            print(f"\nThis graph shows memory usage percentage (0-100%)")
            print(f"\n{'=' * 80}\n")
        else:
            print("\n✗ Failed to create graph")

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

    create_memory_util_graph()

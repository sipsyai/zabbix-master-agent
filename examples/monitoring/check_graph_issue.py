#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Zabbix Graph Issue Checker
Checks why graphs show "no data" despite items receiving data
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

def check_graph_issue():
    """Check Memory page faults item and graph configuration"""

    # Get credentials from environment
    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Zabbix Graph Issue Checker")
    print("=" * 80)
    print(f"\nConnecting to: {api_url}")

    try:
        # Connect to Zabbix API
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("✓ Connected successfully")

        # Get Zabbix version
        version = api.apiinfo.version()
        print(f"✓ Zabbix version: {version}\n")

        # Search for "Memory page faults per second" item
        print("-" * 80)
        print("Searching for 'Memory page faults per second' item...")
        print("-" * 80)

        items = api.item.get(
            output=['itemid', 'name', 'key_', 'hostid', 'status', 'state', 'lastvalue',
                    'lastclock', 'history', 'trends', 'value_type', 'delay'],
            search={'name': 'Memory page faults per second'},
            searchWildcardsEnabled=True,
            selectHosts=['hostid', 'host', 'name']
        )

        if not items:
            print("✗ No items found matching 'Memory page faults per second'")

            # Try broader search
            print("\nSearching for 'page faults'...")
            items = api.item.get(
                output=['itemid', 'name', 'key_', 'hostid', 'status', 'state', 'lastvalue',
                        'lastclock', 'history', 'trends', 'value_type', 'delay'],
                search={'name': 'page faults'},
                searchWildcardsEnabled=True,
                selectHosts=['hostid', 'host', 'name']
            )

        if not items:
            print("✗ No items found. Listing all memory-related items...")
            items = api.item.get(
                output=['itemid', 'name', 'key_', 'hostid', 'status', 'state', 'lastvalue',
                        'lastclock', 'history', 'trends', 'value_type', 'delay'],
                search={'name': 'memory'},
                searchWildcardsEnabled=True,
                selectHosts=['hostid', 'host', 'name'],
                limit=20
            )

        print(f"\n✓ Found {len(items)} item(s)\n")

        for idx, item in enumerate(items, 1):
            host = item['hosts'][0] if item.get('hosts') else {'name': 'Unknown'}

            print(f"\n{'=' * 80}")
            print(f"ITEM #{idx}: {item['name']}")
            print(f"{'=' * 80}")
            print(f"Host:           {host['name']}")
            print(f"Item ID:        {item['itemid']}")
            print(f"Key:            {item['key_']}")
            print(f"Status:         {'Enabled' if item['status'] == '0' else 'Disabled'}")
            print(f"State:          {'Normal' if item['state'] == '0' else 'Not Supported'}")
            print(f"Value Type:     {item['value_type']}")
            print(f"Update Interval: {item.get('delay', 'N/A')}")
            print(f"History:        {item.get('history', 'N/A')} days")
            print(f"Trends:         {item.get('trends', 'N/A')} days")

            # Check last value
            if item.get('lastclock') and item['lastclock'] != '0':
                last_time = datetime.fromtimestamp(int(item['lastclock']))
                print(f"Last Value:     {item.get('lastvalue', 'N/A')}")
                print(f"Last Check:     {last_time}")
            else:
                print(f"Last Value:     No data received yet")

            # Get history data to verify
            print(f"\nChecking recent history...")
            history = api.history.get(
                output='extend',
                itemids=item['itemid'],
                sortfield='clock',
                sortorder='DESC',
                limit=5
            )

            if history:
                print(f"✓ Found {len(history)} recent values:")
                for h in history:
                    h_time = datetime.fromtimestamp(int(h['clock']))
                    print(f"  - {h_time}: {h['value']}")
            else:
                print("✗ No history data found")

            # Check graphs using this item
            print(f"\nSearching for graphs using this item...")
            graphs = api.graph.get(
                output=['graphid', 'name', 'width', 'height', 'show_legend'],
                itemids=item['itemid'],
                selectGraphItems=['itemid', 'sortorder', 'color', 'yaxisside']
            )

            if graphs:
                print(f"✓ Found {len(graphs)} graph(s):")
                for g in graphs:
                    print(f"\n  Graph: {g['name']}")
                    print(f"  Graph ID: {g['graphid']}")
                    print(f"  Dimensions: {g['width']}x{g['height']}")
                    print(f"  Show Legend: {g['show_legend']}")
                    print(f"  Items in graph: {len(g.get('gitems', []))}")

                    # Check graph items configuration
                    for gitem in g.get('gitems', []):
                        print(f"    - Item ID: {gitem['itemid']}, Color: {gitem['color']}")
            else:
                print("✗ No graphs found using this item")
                print("\nThis might be the issue! The item exists but is not added to any graph.")

        # Get all graphs to see if there are graphs without proper item configuration
        print(f"\n{'=' * 80}")
        print("Checking all graphs for potential issues...")
        print(f"{'=' * 80}")

        all_graphs = api.graph.get(
            output=['graphid', 'name'],
            search={'name': 'memory'},
            searchWildcardsEnabled=True,
            selectGraphItems=['itemid']
        )

        if all_graphs:
            print(f"\n✓ Found {len(all_graphs)} memory-related graph(s):")
            for g in all_graphs:
                item_count = len(g.get('gitems', []))
                status = "✓" if item_count > 0 else "✗ NO ITEMS!"
                print(f"{status} Graph: '{g['name']}' (ID: {g['graphid']}) - {item_count} items")

        api.logout()
        print(f"\n{'=' * 80}")
        print("Analysis complete!")
        print(f"{'=' * 80}\n")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    # Set up path to use venv if exists
    venv_path = os.path.join(os.path.dirname(__file__), '.claude', 'skills', 'zabbix-automation', 'venv')
    if os.path.exists(venv_path):
        if os.name == 'nt':
            site_packages = os.path.join(venv_path, 'Lib', 'site-packages')
        else:
            site_packages = os.path.join(venv_path, 'lib', f'python{sys.version_info.major}.{sys.version_info.minor}', 'site-packages')
        sys.path.insert(0, site_packages)

    check_graph_issue()

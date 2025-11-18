#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze all graphs for DESKTOP-JK5G34L host
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

def analyze_all_graphs():
    """Analyze all graphs and their items"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Analyzing All Graphs for DESKTOP-JK5G34L")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # Get the host
        hosts = api.host.get(
            output=['hostid', 'host', 'name'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True
        )

        if not hosts:
            print("\nHost DESKTOP-JK5G34L not found")
            api.logout()
            return

        host = hosts[0]
        print(f"\nHost: {host['name']} (ID: {host['hostid']})")

        # Get all graphs for this host
        print("\nFetching all graphs...")
        graphs = api.graph.get(
            output=['graphid', 'name', 'width', 'height', 'graphtype'],
            hostids=host['hostid'],
            selectGraphItems=['itemid', 'sortorder', 'color', 'type'],
            sortfield='name'
        )

        if not graphs:
            print("No graphs found for this host")
            api.logout()
            return

        print(f"\n{'=' * 80}")
        print(f"Found {len(graphs)} graph(s)")
        print(f"{'=' * 80}\n")

        problems = []
        working_graphs = []

        for idx, graph in enumerate(graphs, 1):
            print(f"\n[{idx}/{len(graphs)}] Graph: {graph['name']}")
            print(f"{'─' * 80}")
            print(f"Graph ID:     {graph['graphid']}")
            print(f"Dimensions:   {graph['width']}x{graph['height']}")

            gitems = graph.get('gitems', [])
            print(f"Items in graph: {len(gitems)}")

            if len(gitems) == 0:
                print("❌ PROBLEM: Graph has NO items!")
                problems.append({
                    'graph': graph['name'],
                    'graphid': graph['graphid'],
                    'issue': 'No items in graph'
                })
                continue

            # Check each item in the graph
            print("\nChecking graph items:")
            item_ids = [gi['itemid'] for gi in gitems]

            items = api.item.get(
                output=['itemid', 'name', 'key_', 'status', 'state', 'lastvalue',
                        'lastclock', 'value_type', 'history'],
                itemids=item_ids
            )

            items_dict = {item['itemid']: item for item in items}

            graph_has_data = False
            disabled_items = []
            unsupported_items = []
            no_data_items = []

            for gitem in gitems:
                item_id = gitem['itemid']
                item = items_dict.get(item_id)

                if not item:
                    print(f"  ❌ Item {item_id} not found!")
                    continue

                status_icon = "✓" if item['status'] == '0' else "❌"
                state_icon = "✓" if item['state'] == '0' else "❌"

                print(f"\n  {status_icon} Item: {item['name'][:60]}")
                print(f"     ID: {item_id}, Status: {'Enabled' if item['status'] == '0' else 'Disabled'}, State: {'Normal' if item['state'] == '0' else 'Not Supported'}")

                if item['status'] != '0':
                    disabled_items.append(item['name'])
                    continue

                if item['state'] != '0':
                    unsupported_items.append(item['name'])
                    continue

                # Check if item has data
                if item.get('lastclock') and item['lastclock'] != '0':
                    last_time = datetime.fromtimestamp(int(item['lastclock']))
                    time_diff = (datetime.now() - last_time).total_seconds()
                    print(f"     Last Value: {item.get('lastvalue', 'N/A')} ({time_diff:.0f}s ago)")

                    # Check history
                    value_type = int(item['value_type'])
                    try:
                        history = api.history.get(
                            history=value_type,
                            itemids=item_id,
                            sortfield='clock',
                            sortorder='DESC',
                            limit=1
                        )

                        if history:
                            graph_has_data = True
                            print(f"     History: ✓ {len(history)} record(s) available")
                        else:
                            no_data_items.append(item['name'])
                            print(f"     History: ❌ No history data!")
                    except Exception as e:
                        print(f"     History: ❌ Error checking history: {e}")
                else:
                    no_data_items.append(item['name'])
                    print(f"     Last Value: ❌ No data received yet")

            # Summary for this graph
            print(f"\n{'─' * 80}")
            if graph_has_data:
                print(f"✓ Graph Status: OK - Has data")
                working_graphs.append(graph['name'])
            else:
                print(f"❌ Graph Status: NO DATA")
                issues = []
                if disabled_items:
                    issues.append(f"{len(disabled_items)} disabled items")
                if unsupported_items:
                    issues.append(f"{len(unsupported_items)} unsupported items")
                if no_data_items:
                    issues.append(f"{len(no_data_items)} items without data")

                problems.append({
                    'graph': graph['name'],
                    'graphid': graph['graphid'],
                    'issue': ', '.join(issues)
                })

        # Final summary
        print(f"\n\n{'=' * 80}")
        print("SUMMARY")
        print(f"{'=' * 80}\n")
        print(f"Total Graphs:     {len(graphs)}")
        print(f"Working Graphs:   {len(working_graphs)}")
        print(f"Problem Graphs:   {len(problems)}")

        if problems:
            print(f"\n{'─' * 80}")
            print("PROBLEM GRAPHS:")
            print(f"{'─' * 80}")
            for p in problems:
                print(f"\n❌ {p['graph']}")
                print(f"   Graph ID: {p['graphid']}")
                print(f"   Issue: {p['issue']}")

        if working_graphs:
            print(f"\n{'─' * 80}")
            print("WORKING GRAPHS:")
            print(f"{'─' * 80}")
            for g in working_graphs:
                print(f"✓ {g}")

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

    analyze_all_graphs()

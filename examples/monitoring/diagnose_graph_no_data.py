#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Diagnose why graphs show "no data" despite items having data
"""

import os
import sys
from datetime import datetime, timedelta

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def diagnose_graph_no_data():
    """Diagnose why graphs show no data"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Diagnosing Graph 'No Data' Issue")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)

        # Get host
        hosts = api.host.get(
            output=['hostid', 'host', 'name', 'status'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True
        )

        if not hosts:
            print("Host not found")
            return

        host = hosts[0]
        print(f"\nHost: {host['name']}")
        print(f"Host ID: {host['hostid']}")
        print(f"Host Status: {'Enabled' if host['status'] == '0' else 'Disabled'}")

        # Get all graphs
        graphs = api.graph.get(
            output=['graphid', 'name', 'graphtype', 'show_legend'],
            hostids=host['hostid'],
            selectGraphItems=['itemid', 'calc_fnc', 'type'],
            sortfield='name'
        )

        print(f"\n{'=' * 80}")
        print(f"Found {len(graphs)} graphs")
        print(f"{'=' * 80}\n")

        # Focus on first few graphs that show "no data"
        problem_graphs = []

        for idx, graph in enumerate(graphs[:5], 1):  # Check first 5 graphs
            print(f"\n[{idx}] {graph['name']}")
            print(f"{'─' * 80}")
            print(f"Graph ID: {graph['graphid']}")
            print(f"Graph Type: {graph['graphtype']}")  # 0=normal, 1=stacked, 2=pie, 3=exploded

            gitems = graph.get('gitems', [])
            print(f"Items in graph: {len(gitems)}")

            if len(gitems) == 0:
                print("❌ Graph has NO items!")
                problem_graphs.append(graph['name'])
                continue

            # Get detailed item info
            item_ids = [gi['itemid'] for gi in gitems]
            items = api.item.get(
                output=['itemid', 'name', 'key_', 'status', 'state', 'lastvalue',
                        'lastclock', 'value_type', 'type', 'delay', 'history', 'trends'],
                itemids=item_ids,
                selectHosts=['host']
            )

            for item in items:
                print(f"\n  Item: {item['name'][:70]}")
                print(f"  Key: {item['key_']}")
                print(f"  Type: {item['type']}")  # 0=Zabbix agent, 7=Zabbix agent(active), etc
                print(f"  Status: {'Enabled' if item['status'] == '0' else 'Disabled'}")
                print(f"  State: {'Normal' if item['state'] == '0' else 'Not Supported'}")
                print(f"  Value Type: {item['value_type']}")
                print(f"  Delay: {item.get('delay', 'N/A')}")

                if item.get('lastclock') and item['lastclock'] != '0':
                    last_time = datetime.fromtimestamp(int(item['lastclock']))
                    time_diff = (datetime.now() - last_time).total_seconds()
                    print(f"  Last Value: {item.get('lastvalue', 'N/A')}")
                    print(f"  Last Update: {last_time} ({time_diff:.0f}s ago)")
                else:
                    print(f"  Last Value: ❌ NO DATA RECEIVED YET")
                    problem_graphs.append(graph['name'])
                    continue

                # Check history with correct value type
                vtype = int(item['value_type'])
                print(f"\n  Checking history (value_type={vtype})...")

                # Try to get history from last 24 hours
                time_from = int((datetime.now() - timedelta(hours=24)).timestamp())
                try:
                    history = api.history.get(
                        history=vtype,
                        itemids=item['itemid'],
                        time_from=time_from,
                        sortfield='clock',
                        sortorder='DESC',
                        limit=10
                    )

                    if history:
                        print(f"  ✓ Found {len(history)} history records in last 24h")
                        # Show first and last record
                        first_time = datetime.fromtimestamp(int(history[-1]['clock']))
                        last_time = datetime.fromtimestamp(int(history[0]['clock']))
                        print(f"    Oldest: {first_time} = {history[-1]['value']}")
                        print(f"    Newest: {last_time} = {history[0]['value']}")
                    else:
                        print(f"  ❌ NO HISTORY in last 24 hours!")
                        problem_graphs.append(graph['name'])

                except Exception as e:
                    print(f"  ❌ Error getting history: {e}")
                    problem_graphs.append(graph['name'])

        # Summary
        print(f"\n\n{'=' * 80}")
        print("DIAGNOSIS SUMMARY")
        print(f"{'=' * 80}\n")

        if problem_graphs:
            unique_problems = list(set(problem_graphs))
            print(f"Graphs with issues: {len(unique_problems)}\n")
            for g in unique_problems:
                print(f"  ❌ {g}")

            print(f"\n{'─' * 80}")
            print("POSSIBLE CAUSES:")
            print(f"{'─' * 80}")
            print("1. Items recently created - no historical data yet")
            print("2. Items are type 'Zabbix agent (active)' but agent not sending data")
            print("3. Host was down during the time period")
            print("4. Housekeeper deleted old data")
            print("5. Item type mismatch with graph expectations")
        else:
            print("✓ All graphs should have data!")

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

    diagnose_graph_no_data()

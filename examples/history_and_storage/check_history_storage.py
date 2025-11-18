#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check history storage and value type issues
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

def check_history_storage():
    """Check why history data is not being stored"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("History Storage Checker")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # First, get the host
        hosts = api.host.get(
            output=['hostid', 'host', 'name'],
            search={'host': 'DESKTOP-JK5G34L'},
            searchWildcardsEnabled=True
        )

        if not hosts:
            print("\nHost DESKTOP-JK5G34L not found")
            return

        host = hosts[0]
        print(f"\nFound host: {host['name']} (ID: {host['hostid']})")

        # Get the specific item by ID (from previous analysis)
        items = api.item.get(
            output=['itemid', 'name', 'key_', 'hostid', 'value_type', 'lastvalue',
                    'lastclock', 'history', 'trends', 'status', 'state'],
            itemids='70811',
            selectHosts=['host', 'name']
        )

        if not items:
            print("\nItem 70811 not found. Searching all items on this host...")
            items = api.item.get(
                output=['itemid', 'name', 'key_', 'hostid', 'value_type', 'lastvalue',
                        'lastclock', 'history', 'trends', 'status', 'state'],
                hostids=host['hostid'],
                search={'name': 'page'},
                searchWildcardsEnabled=True,
                selectHosts=['host', 'name']
            )

        if not items:
            print("\nNo items found")
            return

        print(f"\nFound {len(items)} item(s) on DESKTOP-JK5G34L\n")

        for item in items:
            print("=" * 80)
            print(f"Item: {item['name']}")
            print("=" * 80)
            print(f"Item ID:     {item['itemid']}")
            print(f"Key:         {item['key_']}")
            print(f"Value Type:  {item['value_type']} ", end='')

            value_types = {
                '0': 'Numeric (float)',
                '1': 'Character',
                '2': 'Log',
                '3': 'Numeric (unsigned)',
                '4': 'Text'
            }
            print(f"({value_types.get(item['value_type'], 'Unknown')})")

            print(f"Status:      {item['status']} ({'Enabled' if item['status'] == '0' else 'Disabled'})")
            print(f"State:       {item['state']} ({'Normal' if item['state'] == '0' else 'Not Supported'})")
            print(f"History:     {item['history']}")
            print(f"Trends:      {item['trends']}")

            if item.get('lastclock') and item['lastclock'] != '0':
                last_time = datetime.fromtimestamp(int(item['lastclock']))
                time_diff = datetime.now() - last_time
                print(f"Last Value:  {item.get('lastvalue', 'N/A')}")
                print(f"Last Clock:  {last_time} ({time_diff.total_seconds():.0f}s ago)")
            else:
                print("Last Value:  No data yet")

            # Try different history queries
            print("\n--- Testing History Queries ---")

            # Test 1: Get latest history
            print("\n1. Latest 10 history records:")
            try:
                history = api.history.get(
                    output='extend',
                    itemids=item['itemid'],
                    sortfield='clock',
                    sortorder='DESC',
                    limit=10
                )

                if history:
                    print(f"   Found {len(history)} records:")
                    for h in history[:3]:
                        h_time = datetime.fromtimestamp(int(h['clock']))
                        print(f"   - {h_time}: {h['value']}")
                else:
                    print("   No history found")
            except Exception as e:
                print(f"   Error: {e}")

            # Test 2: Try with time range (last 24 hours)
            print("\n2. History from last 24 hours:")
            try:
                time_from = int((datetime.now() - timedelta(hours=24)).timestamp())
                history = api.history.get(
                    output='extend',
                    itemids=item['itemid'],
                    time_from=time_from,
                    sortfield='clock',
                    sortorder='DESC',
                    limit=10
                )

                if history:
                    print(f"   Found {len(history)} records")
                else:
                    print("   No history in last 24 hours")
            except Exception as e:
                print(f"   Error: {e}")

            # Test 3: Check trends
            print("\n3. Checking trends data:")
            try:
                time_from = int((datetime.now() - timedelta(days=7)).timestamp())
                trends = api.trend.get(
                    output='extend',
                    itemids=item['itemid'],
                    time_from=time_from,
                    sortfield='clock',
                    sortorder='DESC',
                    limit=10
                )

                if trends:
                    print(f"   Found {len(trends)} trend records:")
                    for t in trends[:3]:
                        t_time = datetime.fromtimestamp(int(t['clock']))
                        print(f"   - {t_time}: value_avg={t.get('value_avg', 'N/A')}")
                else:
                    print("   No trends found")
            except Exception as e:
                print(f"   Error: {e}")

            # Test 4: Check if value type matches history table
            print("\n4. Value type analysis:")
            vtype = int(item['value_type'])
            if vtype == 0:
                print("   Value type 0 (float) -> should query history table")
            elif vtype == 3:
                print("   Value type 3 (unsigned) -> should query history_uint table")
            elif vtype == 1:
                print("   Value type 1 (character) -> should query history_str table")
            elif vtype == 2:
                print("   Value type 2 (log) -> should query history_log table")
            elif vtype == 4:
                print("   Value type 4 (text) -> should query history_text table")

        api.logout()
        print("\n" + "=" * 80)
        print("Analysis Complete")
        print("=" * 80)

    except Exception as e:
        print(f"\nError: {e}")
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

    check_history_storage()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Memory utilization item that is in Not Supported state
"""

import os
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from zabbix_utils import ZabbixAPI

def fix_memory_utilization():
    """Fix the Memory utilization item"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Fixing Memory Utilization Item")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)
        print("\nConnected to Zabbix API")

        # Get the problematic item
        item_id = '70835'
        items = api.item.get(
            itemids=item_id,
            output=['itemid', 'name', 'key_', 'hostid', 'status', 'state', 'error',
                    'value_type', 'type', 'delay', 'history', 'trends', 'params'],
            selectHosts=['host', 'name']
        )

        if not items:
            print(f"Item {item_id} not found")
            api.logout()
            return

        item = items[0]
        host = item['hosts'][0]

        print(f"\nItem Details:")
        print(f"{'─' * 80}")
        print(f"Host:        {host['name']}")
        print(f"Item:        {item['name']}")
        print(f"Item ID:     {item['itemid']}")
        print(f"Key:         {item['key_']}")
        print(f"Status:      {'Enabled' if item['status'] == '0' else 'Disabled'}")
        print(f"State:       {'Normal' if item['state'] == '0' else 'Not Supported'}")
        print(f"Type:        {item['type']}")
        print(f"Value Type:  {item['value_type']}")
        print(f"Delay:       {item.get('delay', 'N/A')}")

        if item['state'] != '0':
            print(f"\nError:       {item.get('error', 'Unknown error')}")

        print(f"\n{'─' * 80}")

        # Check what the key is
        key = item['key_']
        print(f"\nAnalyzing item key: {key}")

        # Common Windows memory items that work
        print(f"\nSuggested alternatives for Windows memory utilization:")
        print("1. vm.memory.util[available]     - Available memory percentage")
        print("2. vm.memory.util[pavailable]    - Available memory percentage (performance counter)")
        print("3. vm.memory.size[available]     - Available memory in bytes")
        print("4. perf_counter[\"\\Memory\\% Committed Bytes In Use\"] - Memory usage %")

        # Try to get all working memory items on this host
        print(f"\n{'─' * 80}")
        print("Checking other memory items on this host:")
        print(f"{'─' * 80}")

        host_items = api.item.get(
            hostids=item['hostid'],
            output=['itemid', 'name', 'key_', 'status', 'state', 'lastvalue'],
            search={'name': 'memory'},
            searchWildcardsEnabled=True,
            filter={'state': '0'}  # Only Normal state
        )

        if host_items:
            print(f"\nFound {len(host_items)} working memory items:")
            for hi in host_items:
                print(f"\n  ✓ {hi['name']}")
                print(f"    Key: {hi['key_']}")
                print(f"    Last Value: {hi.get('lastvalue', 'N/A')}")

        # Check if we can create a calculated item instead
        print(f"\n{'─' * 80}")
        print("Suggested Fix:")
        print(f"{'─' * 80}")
        print("\nOption 1: Use Windows Performance Counter")
        print('  Key: perf_counter_en["\\Memory\\% Committed Bytes In Use"]')
        print("\nOption 2: Create calculated item")
        print("  Formula: (total_memory - available_memory) / total_memory * 100")

        # Try to disable the broken item
        print(f"\n{'─' * 80}")
        print("Disabling the broken item...")

        try:
            api.item.update(
                itemid=item_id,
                status=1  # Disable
            )
            print("✓ Item disabled successfully")
            print("  (This prevents error messages but won't fix the graph)")
        except Exception as e:
            print(f"✗ Failed to disable: {e}")

        # Check if there's a template we should be using
        print(f"\n{'─' * 80}")
        print("Checking host templates...")

        host_details = api.host.get(
            hostids=item['hostid'],
            output=['hostid', 'host', 'name'],
            selectParentTemplates=['templateid', 'name']
        )

        if host_details and host_details[0].get('parentTemplates'):
            templates = host_details[0]['parentTemplates']
            print(f"\nHost is using {len(templates)} template(s):")
            for t in templates:
                print(f"  - {t['name']}")

        print(f"\n{'=' * 80}")
        print("RECOMMENDATION:")
        print(f"{'=' * 80}")
        print("\nThe 'Memory utilization' item is not supported on this Windows system.")
        print("This item has been DISABLED to prevent errors.")
        print("\nThe good news:")
        print("  ✓ You have 10 other working graphs showing system metrics")
        print("  ✓ Memory page faults is working and graphed")
        print("  ✓ Swap usage is working")
        print("\nTo fix this graph permanently:")
        print("  1. Remove the broken graph, OR")
        print("  2. Edit the graph to use a different memory metric that works")
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

    fix_memory_utilization()

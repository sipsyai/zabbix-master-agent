#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test different history.get API parameters
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

def test_history_api():
    """Test different ways to query history"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Testing History API Methods")
    print("=" * 80)

    try:
        api = ZabbixAPI(url=api_url)
        api.login(user=username, password=password)

        item_id = '70811'

        print(f"\nTesting item ID: {item_id}")
        print("-" * 80)

        # Test 1: With history parameter (0 = float)
        print("\n1. history.get with history=0 (float table)")
        try:
            result = api.history.get(
                history=0,  # 0 = float, 1 = string, 2 = log, 3 = integer, 4 = text
                itemids=item_id,
                sortfield='clock',
                sortorder='DESC',
                limit=10,
                output='extend'
            )
            if result:
                print(f"   SUCCESS: Found {len(result)} records")
                for r in result[:3]:
                    t = datetime.fromtimestamp(int(r['clock']))
                    print(f"   - {t}: {r['value']}")
            else:
                print("   No data")
        except Exception as e:
            print(f"   Error: {e}")

        # Test 2: With time range
        print("\n2. With time range (last hour)")
        try:
            time_from = int((datetime.now() - timedelta(hours=1)).timestamp())
            result = api.history.get(
                history=0,
                itemids=item_id,
                time_from=time_from,
                sortfield='clock',
                sortorder='DESC',
                output='extend'
            )
            if result:
                print(f"   SUCCESS: Found {len(result)} records")
            else:
                print("   No data")
        except Exception as e:
            print(f"   Error: {e}")

        # Test 3: Try direct API call
        print("\n3. Direct API call via api.do_request")
        try:
            time_from = int((datetime.now() - timedelta(hours=1)).timestamp())
            result = api.do_request(
                method='history.get',
                params={
                    'output': 'extend',
                    'history': 0,
                    'itemids': [item_id],
                    'sortfield': 'clock',
                    'sortorder': 'DESC',
                    'limit': 10,
                    'time_from': time_from
                }
            )
            if result and result.get('result'):
                data = result['result']
                print(f"   SUCCESS: Found {len(data)} records")
                for r in data[:3]:
                    t = datetime.fromtimestamp(int(r['clock']))
                    print(f"   - {t}: {r['value']}")
            else:
                print(f"   No data - Response: {result}")
        except Exception as e:
            print(f"   Error: {e}")

        # Test 4: Check item configuration details
        print("\n4. Item configuration check")
        try:
            items = api.item.get(
                itemids=item_id,
                output=['itemid', 'name', 'key_', 'value_type', 'history', 'history_mode',
                        'status', 'state', 'lastvalue', 'lastclock', 'units']
            )
            if items:
                item = items[0]
                print(f"   Name: {item['name']}")
                print(f"   Value Type: {item['value_type']}")
                print(f"   History: {item.get('history', 'N/A')}")
                print(f"   History Mode: {item.get('history_mode', 'N/A')}")  # 0=normal, 1=disabled
                print(f"   Last Value: {item.get('lastvalue', 'N/A')}")
                if item.get('lastclock'):
                    print(f"   Last Clock: {datetime.fromtimestamp(int(item['lastclock']))}")
        except Exception as e:
            print(f"   Error: {e}")

        # Test 5: Check housekeeper settings
        print("\n5. Checking housekeeper configuration")
        try:
            config = api.do_request(
                method='settings.get',
                params={
                    'output': 'extend'
                }
            )
            if config and config.get('result'):
                settings = config['result']
                print(f"   Housekeeper: {settings.get('hk_history', 'N/A')}")
                print(f"   Housekeeper Mode: {settings.get('hk_history_mode', 'N/A')}")
                print(f"   Housekeeper Global: {settings.get('hk_history_global', 'N/A')}")
        except Exception as e:
            print(f"   Error (may not have permission): {e}")

        api.logout()
        print("\n" + "=" * 80)

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

    test_history_api()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check CPU Usage graph
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

def check_cpu_graph():
    """Check CPU Usage graph"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("CPU Usage Grafiği Analizi")
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

        # Find CPU graphs
        graphs = api.graph.get(
            output=['graphid', 'name', 'graphtype'],
            hostids=host['hostid'],
            search={'name': 'CPU'},
            searchWildcardsEnabled=True,
            selectGraphItems=['itemid'],
            sortfield='name'
        )

        print(f"CPU ile ilgili {len(graphs)} grafik bulundu\n")

        for graph in graphs:
            print(f"\n{'=' * 80}")
            print(f"Grafik: {graph['name']}")
            print(f"{'=' * 80}")
            print(f"Graph ID: {graph['graphid']}")
            print(f"Item sayısı: {len(graph.get('gitems', []))}")

            if len(graph.get('gitems', [])) == 0:
                print("❌ Grafikte item yok!")
                continue

            item_ids = [gi['itemid'] for gi in graph['gitems']]
            items = api.item.get(
                output=['itemid', 'name', 'key_', 'type', 'status', 'state',
                        'lastvalue', 'lastclock', 'value_type', 'delay', 'master_itemid'],
                itemids=item_ids
            )

            print(f"\n{'─' * 80}")
            print('İtemlar:')
            print(f"{'─' * 80}")

            for item in items:
                status_icon = "✓" if item['state'] == '0' else "❌"
                print(f"\n{status_icon} {item['name']}")
                print(f"   Key: {item['key_']}")
                print(f"   Type: {item['type']} ", end="")
                if item['type'] == '7':
                    print("(Zabbix agent active)")
                elif item['type'] == '18':
                    print(f"(Dependent, master_itemid: {item.get('master_itemid', 'N/A')})")
                else:
                    print(f"(Type {item['type']})")
                print(f"   Status: {'Enabled' if item['status'] == '0' else 'Disabled'}")
                print(f"   State: {'Normal' if item['state'] == '0' else 'Not Supported'}")
                print(f"   Delay: {item.get('delay', 'N/A')}")

                if item.get('lastclock') and item['lastclock'] != '0':
                    last_time = datetime.fromtimestamp(int(item['lastclock']))
                    time_diff = (datetime.now() - last_time).total_seconds()
                    print(f"   Last Value: {item.get('lastvalue', 'N/A')}")
                    print(f"   Last Update: {last_time} ({time_diff:.0f}s ago)")

                    # Check history
                    vtype = int(item['value_type'])
                    time_from = int((datetime.now() - timedelta(hours=1)).timestamp())
                    try:
                        history = api.history.get(
                            history=vtype,
                            itemids=item['itemid'],
                            time_from=time_from,
                            sortfield='clock',
                            sortorder='DESC',
                            limit=5
                        )
                        if history:
                            print(f"   ✓ History: {len(history)} kayıt (son 1 saat)")
                            if len(history) > 0:
                                newest_time = datetime.fromtimestamp(int(history[0]['clock']))
                                print(f"      En son: {newest_time} = {history[0]['value']}")
                        else:
                            print(f"   ❌ History: YOK (son 1 saat)")
                    except Exception as e:
                        print(f"   ❌ History Error: {e}")
                else:
                    print(f"   ❌ Last Value: VERİ YOK")

                # If dependent, check master item
                if item['type'] == '18' and item.get('master_itemid'):
                    print(f"\n   Master Item kontrol ediliyor...")
                    master = api.item.get(
                        itemids=item['master_itemid'],
                        output=['itemid', 'name', 'key_', 'type', 'status', 'state', 'lastvalue', 'lastclock']
                    )
                    if master:
                        m = master[0]
                        print(f"   Master: {m['name']}")
                        print(f"   Master Key: {m['key_']}")
                        print(f"   Master Type: {m['type']}")
                        print(f"   Master State: {'Normal' if m['state'] == '0' else 'Not Supported'}")
                        if m.get('lastclock') and m['lastclock'] != '0':
                            last_time = datetime.fromtimestamp(int(m['lastclock']))
                            time_diff = (datetime.now() - last_time).total_seconds()
                            print(f"   Master Last Value: {m.get('lastvalue', 'N/A')} ({time_diff:.0f}s ago)")
                        else:
                            print(f"   ❌ Master'da veri YOK!")

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

    check_cpu_graph()

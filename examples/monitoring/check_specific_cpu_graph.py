#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check specific CPU graph
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

def check_specific_cpu_graph():
    """Check Windows: CPU usage graph"""

    api_url = os.getenv('ZABBIX_API_URL', 'http://192.168.213.141/api_jsonrpc.php')
    username = os.getenv('ZABBIX_USERNAME', 'Admin')
    password = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print("=" * 80)
    print("Windows: CPU usage Grafigi Detayli Analiz")
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

        # Get all graphs
        graphs = api.graph.get(
            output=['graphid', 'name', 'graphtype'],
            hostids=host['hostid'],
            selectGraphItems=['itemid'],
            sortfield='name'
        )

        # Find CPU usage graph
        cpu_graphs = [g for g in graphs if 'CPU' in g['name'].upper()]

        print(f"\nBulunan CPU grafikleri:\n")
        for g in cpu_graphs:
            print(f"  - {g['name']} (ID: {g['graphid']})")

        # Focus on "Windows: CPU usage"
        cpu_usage_graphs = [g for g in cpu_graphs if 'usage' in g['name'].lower()]

        if not cpu_usage_graphs:
            print("\n'Windows: CPU usage' grafigi bulunamadi!")
            return

        graph = cpu_usage_graphs[0]

        print(f"\n{'=' * 80}")
        print(f"Grafik: {graph['name']}")
        print(f"{'=' * 80}")
        print(f"Graph ID: {graph['graphid']}")
        print(f"Item sayisi: {len(graph.get('gitems', []))}")

        if len(graph.get('gitems', [])) == 0:
            print("\nHATA: Grafikte hic item yok!")
            return

        # Get item details
        item_ids = [gi['itemid'] for gi in graph['gitems']]
        items = api.item.get(
            output=['itemid', 'name', 'key_', 'type', 'status', 'state',
                    'lastvalue', 'lastclock', 'value_type', 'delay', 'master_itemid', 'error'],
            itemids=item_ids
        )

        print(f"\n{'=' * 80}")
        print(f"ITEM DETAYLARI:")
        print(f"{'=' * 80}\n")

        for idx, item in enumerate(items, 1):
            status_icon = "OK" if item['state'] == '0' else "HATA"
            print(f"[{idx}] {status_icon}: {item['name']}")
            print(f"    Item ID: {item['itemid']}")
            print(f"    Key: {item['key_']}")
            print(f"    Type: {item['type']} ", end="")
            if item['type'] == '7':
                print("(Zabbix agent active)")
            elif item['type'] == '18':
                print(f"(Dependent, master: {item.get('master_itemid', 'N/A')})")
            elif item['type'] == '0':
                print("(Zabbix agent passive)")
            else:
                print(f"(Type {item['type']})")

            print(f"    Status: {'Enabled' if item['status'] == '0' else 'DISABLED'}")
            print(f"    State: {'Normal' if item['state'] == '0' else 'NOT SUPPORTED'}")

            if item.get('error'):
                print(f"    ERROR: {item['error']}")

            print(f"    Delay: {item.get('delay', 'N/A')}")
            print(f"    Value Type: {item['value_type']}")

            # Check last value
            if item.get('lastclock') and item['lastclock'] != '0':
                last_time = datetime.fromtimestamp(int(item['lastclock']))
                time_diff = (datetime.now() - last_time).total_seconds()
                print(f"    Last Value: {item.get('lastvalue', 'N/A')}")
                print(f"    Last Update: {last_time}")
                print(f"    Time Ago: {time_diff:.0f} seconds")

                # Check history
                vtype = int(item['value_type'])
                time_from = int((datetime.now() - timedelta(hours=2)).timestamp())
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
                        print(f"    OK History: {len(history)} kayit (son 2 saat)")
                        print(f"       En yeni: {datetime.fromtimestamp(int(history[0]['clock']))} = {history[0]['value']}")
                        if len(history) > 1:
                            print(f"       En eski: {datetime.fromtimestamp(int(history[-1]['clock']))} = {history[-1]['value']}")
                    else:
                        print(f"    HATA: History'de veri YOK (son 2 saat)")
                except Exception as e:
                    print(f"    HATA: History alinamadi: {e}")
            else:
                print(f"    HATA: Hic veri alinmamis (lastclock = 0 veya bos)")

            # If dependent item, check master
            if item['type'] == '18' and item.get('master_itemid'):
                print(f"\n    Master Item Kontrolu:")
                try:
                    master = api.item.get(
                        itemids=item['master_itemid'],
                        output=['itemid', 'name', 'key_', 'type', 'status', 'state',
                                'lastvalue', 'lastclock', 'error']
                    )
                    if master:
                        m = master[0]
                        print(f"      Master Name: {m['name']}")
                        print(f"      Master Key: {m['key_']}")
                        print(f"      Master Type: {m['type']}")
                        print(f"      Master State: {'Normal' if m['state'] == '0' else 'NOT SUPPORTED'}")
                        if m.get('error'):
                            print(f"      Master ERROR: {m['error']}")
                        if m.get('lastclock') and m['lastclock'] != '0':
                            last_time = datetime.fromtimestamp(int(m['lastclock']))
                            time_diff = (datetime.now() - last_time).total_seconds()
                            print(f"      Master Last Value: {m.get('lastvalue', 'N/A')}")
                            print(f"      Master Last Update: {last_time} ({time_diff:.0f}s ago)")
                        else:
                            print(f"      HATA: Master'da veri YOK!")
                except Exception as e:
                    print(f"      HATA: Master alinamadi: {e}")

            print()

        api.logout()

        print(f"\n{'=' * 80}")
        print("OZET:")
        print(f"{'=' * 80}")
        working_items = [i for i in items if i['state'] == '0' and i.get('lastclock') and i['lastclock'] != '0']
        broken_items = [i for i in items if i['state'] != '0' or not i.get('lastclock') or i['lastclock'] == '0']

        print(f"Calisir durumda: {len(working_items)} item")
        print(f"Sorunlu: {len(broken_items)} item")

        if broken_items:
            print(f"\nSorunlu itemlar:")
            for item in broken_items:
                print(f"  - {item['name']}")
                if item['state'] != '0':
                    print(f"    Sebep: State = Not Supported")
                if not item.get('lastclock') or item['lastclock'] == '0':
                    print(f"    Sebep: Hic veri alinmamis")

    except Exception as e:
        print(f"\nHATA: {e}")
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

    check_specific_cpu_graph()

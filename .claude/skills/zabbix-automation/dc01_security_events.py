# -*- coding: utf-8 -*-
"""
DC01 Windows Security Event Viewer Logs Query
Zabbix API kullanarak DC01 hostundaki Windows Security eventlerini goruntuler
"""

import sys
import os
from datetime import datetime, timedelta

# .env dosyasını yukleme icin
sys.path.insert(0, os.path.dirname(__file__))

try:
    from dotenv import load_dotenv
    # Ust dizindeki .env dosyasini yukle
    env_path = os.path.join(os.path.dirname(__file__), '../../../zabbix-expert/.env')
    load_dotenv(env_path)
except ImportError:
    print("python-dotenv kutuphanes bulunamadi. pip install python-dotenv ile yukleyiniz.")
    sys.exit(1)

try:
    from zabbix_utils import ZabbixAPI
except ImportError:
    print("zabbix_utils kutuphanes bulunamadi. pip install zabbix-utils ile yukleyiniz.")
    sys.exit(1)


def format_timestamp(timestamp):
    """Unix timestamp'i okunabilir formata cevirir"""
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    except:
        return 'N/A'


def print_section(title):
    """Bolum basligi yazdirir"""
    print("\n" + "="*80)
    print(title)
    print("="*80 + "\n")


def main():
    # Zabbix baglanti bilgilerini .env'den oku
    ZABBIX_URL = os.getenv('ZABBIX_URL', 'http://192.168.213.141/')
    ZABBIX_USER = os.getenv('ZABBIX_USER', 'Admin')
    ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD', 'zabbix')

    print(f"Zabbix sunucusuna baglaniliyor: {ZABBIX_URL}")

    try:
        # Zabbix API baglantisi
        api = ZabbixAPI(url=ZABBIX_URL, validate_certs=False)
        api.login(user=ZABBIX_USER, password=ZABBIX_PASSWORD)
        print("+ Giris basarili\n")

        # Zabbix versiyonunu goster
        version = api.api_version()
        print(f"Zabbix Versiyon: {version}")

        # DC01 hostunu bul
        print("\n'DC01' hostu araniy or...")
        hosts = api.host.get(
            filter={'host': 'DC01'},
            output=['hostid', 'host', 'name', 'status']
        )

        if not hosts:
            print("HATA: DC01 hostu bulunamadi!")
            api.logout()
            return

        host = hosts[0]
        hostid = host['hostid']
        print(f"+ Host bulundu: {host['name']} (ID: {hostid})")

        # Windows Security Event Log itemlarini ara
        print_section("WINDOWS SECURITY EVENT LOG ITEMS")

        # Cesitli anahtar kelimelerle ara
        all_items = []

        # Event log itemlarini ara
        items = api.item.get(
            hostids=hostid,
            output=['itemid', 'name', 'key_', 'lastvalue', 'lastclock', 'value_type', 'state'],
            search={'key_': 'eventlog'},
            searchWildcardsEnabled=True,
            sortfield='name'
        )

        for item in items:
            item_key_lower = item['key_'].lower()
            item_name_lower = item['name'].lower()
            # Security iceren itemlari filtrele
            if 'security' in item_key_lower or 'security' in item_name_lower:
                all_items.append(item)

        # Eger eventlog aramasiyla bulamazsa, daha genis arama yap
        if not all_items:
            print("Eventlog aramasiyla sonuc bulunamadi, daha genis arama yapiliyor...")
            items = api.item.get(
                hostids=hostid,
                output=['itemid', 'name', 'key_', 'lastvalue', 'lastclock', 'value_type', 'state'],
                sortfield='name'
            )

            for item in items:
                item_key_lower = item['key_'].lower()
                item_name_lower = item['name'].lower()
                if any(kw in item_key_lower or kw in item_name_lower
                       for kw in ['security', 'event', 'log']):
                    all_items.append(item)

        if not all_items:
            print("! Windows Security Event Log itemi bulunamadi!\n")
            print("Host'taki tum itemlar (ilk 20):")
            all_host_items = api.item.get(
                hostids=hostid,
                output=['itemid', 'name', 'key_'],
                limit=20,
                sortfield='name'
            )
            for item in all_host_items:
                print(f"  - {item['name']}")
                print(f"    Key: {item['key_']}")
            api.logout()
            return

        print(f"{len(all_items)} adet Security Event Log itemi bulundu:\n")
        for idx, item in enumerate(all_items, 1):
            last_check = format_timestamp(item['lastclock']) if item.get('lastclock') else 'N/A'
            state = 'Aktif' if item.get('state') == '0' else 'Pasif'
            print(f"{idx}. {item['name']}")
            print(f"   Key: {item['key_']}")
            print(f"   Durum: {state}")
            print(f"   Son Kontrol: {last_check}")
            if item.get('lastvalue'):
                last_val = str(item['lastvalue'])
                print(f"   Son Deger: {last_val[:150]}")
            print()

        # Son eventleri getir (Zabbix Events - Problemler ve Trigger eventleri)
        print_section("SON ZABBIX EVENTS (Problemler ve Triggerlar)")

        # Son 7 gunluk verileri al
        time_from = int((datetime.now() - timedelta(days=7)).timestamp())

        events = api.event.get(
            hostids=hostid,
            output='extend',
            sortfield=['clock'],
            sortorder='DESC',
            limit=50,
            time_from=time_from,
            selectRelatedObject='extend'
        )

        if events:
            print(f"Son 50 event (son 7 gun):\n")
            for event in events[:20]:  # Ilk 20 eventi goster
                event_time = format_timestamp(event['clock'])
                event_name = event.get('name', 'N/A')
                severity = event.get('severity', '0')

                severity_map = {
                    '0': '[INFO] Not classified',
                    '1': '[INFO] Information',
                    '2': '[WARN] Warning',
                    '3': '[AVG ] Average',
                    '4': '[HIGH] High',
                    '5': '[CRIT] Disaster'
                }

                severity_text = severity_map.get(str(severity), 'Unknown')

                print(f"[{event_time}] {severity_text}")
                print(f"  {event_name}")
                print(f"  Event ID: {event['eventid']}")
                print()
        else:
            print("! Son 7 gunde event bulunamadi")

        # Ilk Security Event Log iteminin history verisini al (varsa)
        if all_items:
            print_section("SECURITY EVENT LOG HISTORY (Ilk Item)")

            first_item = all_items[0]
            print(f"Item: {first_item['name']}")
            print(f"Key: {first_item['key_']}\n")

            # History verisini cek
            history = api.history.get(
                itemids=first_item['itemid'],
                output='extend',
                sortfield='clock',
                sortorder='DESC',
                limit=20,
                time_from=time_from
            )

            if history:
                print(f"Son 20 kayit:\n")
                for record in history:
                    record_time = format_timestamp(record['clock'])
                    value = record.get('value', '')

                    # Log tipli veriler icin
                    if 'logeventid' in record:
                        log_eventid = record.get('logeventid', '')
                        log_source = record.get('source', '')
                        log_severity = record.get('severity', '')

                        print(f"[{record_time}] Event ID: {log_eventid}")
                        if log_source:
                            print(f"  Source: {log_source}")
                        if log_severity:
                            print(f"  Severity: {log_severity}")
                        if value:
                            print(f"  {value[:250]}")
                    else:
                        print(f"[{record_time}]")
                        if value:
                            print(f"  {value[:250]}")
                    print()
            else:
                print("! History verisi bulunamadi")

        print_section("Islem tamamlandi!")

        # Cikis
        api.logout()
        print("+ Zabbix baglantisi kapatildi")

    except Exception as e:
        print(f"\n! HATA: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

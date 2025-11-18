#!/usr/bin/env python3
"""
Zabbix Agent to Agent2 Migration Helper
Bu script, Agent'tan Agent2'ye geçiş sürecinde yardımcı olur.
"""

import os
from zabbix_utils import ZabbixAPI

def get_zabbix_connection():
    """Zabbix API'ye bağlan"""
    url = os.getenv('ZABBIX_API_URL')
    username = os.getenv('ZABBIX_USERNAME')
    password = os.getenv('ZABBIX_PASSWORD')

    api = ZabbixAPI(url=url)
    api.login(user=username, password=password)
    return api

def list_hosts_with_agent_info(api):
    """Tüm host'ları agent versiyonu ile listele"""
    print("\n=== Zabbix Host'ları ve Agent Bilgileri ===\n")

    hosts = api.host.get(
        output=['hostid', 'host', 'name', 'status'],
        selectInterfaces=['interfaceid', 'ip', 'dns', 'port', 'type', 'main'],
        selectItems=['itemid', 'key_', 'name', 'lastvalue']
    )

    for host in hosts:
        status = "Aktif" if host['status'] == '0' else "Devre Dışı"
        print(f"Host: {host['name']} ({host['host']})")
        print(f"  Status: {status}")
        print(f"  Host ID: {host['hostid']}")

        # Interface bilgileri
        if host['interfaces']:
            for iface in host['interfaces']:
                if iface['type'] == '1':  # Zabbix agent interface
                    print(f"  Agent Interface: {iface['ip']}:{iface['port']}")

        # Agent version kontrolü
        agent_version = None
        for item in host['items']:
            if 'agent.version' in item['key_']:
                agent_version = item.get('lastvalue', 'N/A')
                break

        if agent_version:
            print(f"  Agent Version: {agent_version}")
            if 'agent2' in agent_version.lower() or '2.' in agent_version:
                print(f"  ✓ Agent2 kullanılıyor")
            else:
                print(f"  ⚠ Legacy Agent kullanılıyor - Agent2'ye geçiş önerilir")

        print("-" * 60)

def check_host_connectivity(api, hostname):
    """Belirli bir host'un bağlantısını kontrol et"""
    print(f"\n=== {hostname} Host Bağlantı Kontrolü ===\n")

    hosts = api.host.get(
        filter={'host': hostname},
        output=['hostid', 'host', 'name', 'available'],
        selectInterfaces=['ip', 'port', 'available']
    )

    if not hosts:
        print(f"❌ '{hostname}' host'u bulunamadı!")
        return None

    host = hosts[0]
    availability = {
        '0': '❌ Bilinmiyor',
        '1': '✓ Erişilebilir',
        '2': '⚠ Erişilemiyor'
    }

    print(f"Host: {host['name']}")
    print(f"Durum: {availability.get(host['available'], 'Bilinmiyor')}")

    if host['interfaces']:
        for iface in host['interfaces']:
            iface_status = availability.get(iface['available'], 'Bilinmiyor')
            print(f"Interface {iface['ip']}:{iface['port']} - {iface_status}")

    return host

def update_host_description(api, hostname, add_migration_note=True):
    """Host açıklamasına migration notu ekle"""
    hosts = api.host.get(
        filter={'host': hostname},
        output=['hostid', 'host', 'description']
    )

    if not hosts:
        print(f"❌ '{hostname}' host'u bulunamadı!")
        return

    host = hosts[0]
    current_desc = host.get('description', '')

    if add_migration_note:
        migration_note = "\n[Agent2 Migration Scheduled]"
        new_desc = current_desc + migration_note

        api.host.update(
            hostid=host['hostid'],
            description=new_desc
        )
        print(f"✓ Migration notu eklendi: {hostname}")
    else:
        print(f"Host açıklaması: {current_desc}")

def create_migration_report(api, output_file='migration_report.txt'):
    """Migration raporu oluştur"""
    print(f"\n=== Migration Raporu Oluşturuluyor: {output_file} ===\n")

    hosts = api.host.get(
        output=['hostid', 'host', 'name'],
        selectInterfaces=['ip', 'port'],
        selectItems=['key_', 'lastvalue']
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("ZABBIX AGENT MIGRATION REPORT\n")
        f.write("=" * 80 + "\n\n")

        legacy_count = 0
        agent2_count = 0
        unknown_count = 0

        for host in hosts:
            agent_version = None
            for item in host['items']:
                if 'agent.version' in item['key_']:
                    agent_version = item.get('lastvalue', 'Unknown')
                    break

            if not agent_version:
                agent_version = 'Unknown'
                unknown_count += 1
            elif 'agent2' in agent_version.lower() or '2.' in agent_version:
                agent2_count += 1
            else:
                legacy_count += 1

            f.write(f"Host: {host['name']} ({host['host']})\n")
            f.write(f"  Agent Version: {agent_version}\n")

            if host['interfaces']:
                for iface in host['interfaces']:
                    f.write(f"  IP: {iface['ip']}:{iface['port']}\n")

            f.write("-" * 80 + "\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("SUMMARY\n")
        f.write("=" * 80 + "\n")
        f.write(f"Total Hosts: {len(hosts)}\n")
        f.write(f"Legacy Agent: {legacy_count}\n")
        f.write(f"Agent2: {agent2_count}\n")
        f.write(f"Unknown: {unknown_count}\n")

    print(f"✓ Rapor oluşturuldu: {output_file}")
    print(f"\nÖzet:")
    print(f"  Toplam Host: {len(hosts)}")
    print(f"  Legacy Agent: {legacy_count}")
    print(f"  Agent2: {agent2_count}")
    print(f"  Bilinmeyen: {unknown_count}")

def main():
    """Ana menü"""
    print("=" * 80)
    print("ZABBIX AGENT → AGENT2 MIGRATION HELPER")
    print("=" * 80)

    try:
        api = get_zabbix_connection()
        print(f"\n✓ Zabbix API'ye bağlanıldı (v{api.version})")

        while True:
            print("\n" + "=" * 80)
            print("SEÇENEKLER:")
            print("=" * 80)
            print("1. Tüm host'ları listele (agent bilgileriyle)")
            print("2. Belirli bir host'un bağlantısını kontrol et")
            print("3. Migration raporu oluştur")
            print("4. Host'a migration notu ekle")
            print("5. Çıkış")
            print("=" * 80)

            choice = input("\nSeçiminiz (1-5): ").strip()

            if choice == '1':
                list_hosts_with_agent_info(api)

            elif choice == '2':
                hostname = input("Host adı: ").strip()
                check_host_connectivity(api, hostname)

            elif choice == '3':
                filename = input("Rapor dosya adı (varsayılan: migration_report.txt): ").strip()
                if not filename:
                    filename = 'migration_report.txt'
                create_migration_report(api, filename)

            elif choice == '4':
                hostname = input("Host adı: ").strip()
                update_host_description(api, hostname, add_migration_note=True)

            elif choice == '5':
                print("\n✓ Çıkılıyor...")
                break

            else:
                print("❌ Geçersiz seçim!")

        api.logout()
        print("✓ Zabbix API bağlantısı kapatıldı")

    except Exception as e:
        print(f"\n❌ Hata: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

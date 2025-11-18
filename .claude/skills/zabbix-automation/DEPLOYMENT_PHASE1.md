# ZABBIX DEPLOYMENT - PHASE 1 IMPLEMENTATION GUIDE

## ÖZET
Bu doküman **Module 0 (Foundation)** ve **Module 2 (Network Performance Monitoring)** kurulumu için teknik kılavuzdur.

**Referans:** `/deployment_plan_phase1.md` (Ana proje klasöründe detaylı plan)

---

## HIZLI BAŞLANGIÇ

### 1. Platform Kurulumu (Module 0)

#### Gerekli Bilgiler (.env'den okunacak):
```bash
ZABBIX_API_URL=http://<zabbix-server-ip>/api_jsonrpc.php
ZABBIX_SERVER=<zabbix-server-ip>
ZABBIX_USERNAME=Admin
ZABBIX_PASSWORD=<strong_password>
```

#### Kurulum Scripti:
```python
from zabbix_utils import ZabbixAPI

# API bağlantısı
api = ZabbixAPI(
    url=os.getenv('ZABBIX_API_URL'),
    user=os.getenv('ZABBIX_USERNAME'),
    password=os.getenv('ZABBIX_PASSWORD')
)

# Version check
version = api.apiinfo.version()
print(f"Zabbix Version: {version}")
```

---

## 2. Network Device Ekleme (Module 2)

### Gerekli Parametreler:

```python
# Network cihaz bilgileri
NETWORK_DEVICES = {
    'MERKEZ': {
        'kenar_switches': {
            'count': 20,
            'ip_range': '192.168.1.1-192.168.1.20',
            'snmp_community': '<community_string>',
            'template': 'Template Net Cisco IOS SNMP'
        },
        'omurga_switches': {
            'count': 2,
            'devices': [
                {'name': 'CORE-SW-01', 'ip': '192.168.1.1'},
                {'name': 'CORE-SW-02', 'ip': '192.168.1.2'}
            ]
        },
        'mpls_routers': {
            'count': 2,
            'devices': [
                {'name': 'MPLS-01', 'ip': '192.168.1.254'},
                {'name': 'MPLS-02', 'ip': '192.168.1.253'}
            ]
        }
    },
    'BOLGELER': [
        {
            'name': 'BOLGE-1',
            'switch_count': 3,
            'ap_count': 3,
            'ip_range': '10.1.1.1-10.1.1.10'
        },
        # ... BOLGE-2, 3, 4
    ],
    'ESKISEHIR': {
        'switch_count': 10,
        'access_count': 10,
        'ip_range': '10.10.1.1-10.10.1.20'
    }
}
```

### Host Ekleme Scripti:

```python
from zabbix_utils import ZabbixAPI

api = ZabbixAPI(url=ZABBIX_URL, user=USER, password=PASS)

# Host group oluşturma
def create_host_groups():
    groups = [
        'Network devices',
        'MERKEZ',
        'MERKEZ/Kenar Switches',
        'MERKEZ/Omurga Switches',
        'MERKEZ/MPLS Routers',
        'BOLGE-1',
        'BOLGE-2',
        'BOLGE-3',
        'BOLGE-4',
        'ESKISEHIR'
    ]

    for group_name in groups:
        try:
            api.hostgroup.create(name=group_name)
            print(f"✓ Host group created: {group_name}")
        except:
            print(f"- Host group exists: {group_name}")

# Template ID'lerini alma
def get_template_id(template_name):
    templates = api.template.get(
        filter={'host': template_name}
    )
    if templates:
        return templates[0]['templateid']
    return None

# Host ekleme
def add_network_device(hostname, ip, groups, templates, snmp_community):
    # Host group ID'lerini al
    group_ids = []
    for group in groups:
        result = api.hostgroup.get(filter={'name': group})
        if result:
            group_ids.append({'groupid': result[0]['groupid']})

    # Template ID'lerini al
    template_ids = []
    for template in templates:
        tid = get_template_id(template)
        if tid:
            template_ids.append({'templateid': tid})

    # Host oluştur
    try:
        host = api.host.create(
            host=hostname,
            name=hostname,
            interfaces=[{
                'type': 2,  # SNMP
                'main': 1,
                'useip': 1,
                'ip': ip,
                'dns': '',
                'port': '161',
                'details': {
                    'version': 2,  # SNMPv2
                    'community': snmp_community
                }
            }],
            groups=group_ids,
            templates=template_ids,
            macros=[
                {
                    'macro': '{$SNMP_COMMUNITY}',
                    'value': snmp_community
                }
            ]
        )
        print(f"✓ Host created: {hostname} ({ip})")
        return host
    except Exception as e:
        print(f"✗ Failed to create {hostname}: {str(e)}")
        return None

# Örnek kullanım
create_host_groups()

# MERKEZ omurga switch ekleme
add_network_device(
    hostname='CORE-SWITCH-01',
    ip='192.168.1.1',
    groups=['Network devices', 'MERKEZ', 'MERKEZ/Omurga Switches'],
    templates=['Template Net Cisco IOS SNMP', 'Template Module ICMP Ping'],
    snmp_community='<community_string>'
)

# MPLS router ekleme
add_network_device(
    hostname='MPLS-ROUTER-01',
    ip='192.168.1.254',
    groups=['Network devices', 'MERKEZ', 'MERKEZ/MPLS Routers'],
    templates=['Template Net Cisco IOS SNMP'],
    snmp_community='<community_string>'
)
```

---

## 3. Discovery Rule Oluşturma

```python
# Network discovery rule
def create_discovery_rule(name, ip_range, snmp_community):
    try:
        drule = api.drule.create(
            name=name,
            iprange=ip_range,
            delay='1h',
            dchecks=[
                {
                    'type': 9,  # SNMPv2 agent
                    'snmp_community': snmp_community,
                    'ports': '161',
                    'key_': 'system.uname'
                },
                {
                    'type': 3,  # ICMP ping
                    'ports': ''
                }
            ]
        )
        print(f"✓ Discovery rule created: {name}")
        return drule
    except Exception as e:
        print(f"✗ Failed: {str(e)}")

# MERKEZ için discovery
create_discovery_rule(
    name='Network Discovery - MERKEZ',
    ip_range='192.168.1.1-192.168.1.254',
    snmp_community='<community_string>'
)

# BÖLGE-1 için discovery
create_discovery_rule(
    name='Network Discovery - BOLGE-1',
    ip_range='10.1.1.1-10.1.1.254',
    snmp_community='<community_string>'
)
```

---

## 4. Trigger Configuration

```python
# Kritik trigger'lar oluşturma
def create_triggers(hostid):
    triggers = [
        {
            'description': '{HOST.NAME}: High CPU usage (>90%)',
            'expression': 'avg(/*/system.cpu.util,5m)>90',
            'priority': 3  # Average
        },
        {
            'description': '{HOST.NAME}: Device unavailable',
            'expression': 'max(/*/icmpping,#3)=0',
            'priority': 4  # High
        },
        {
            'description': '{HOST.NAME}: High memory usage (>90%)',
            'expression': 'avg(/*/vm.memory.pused,5m)>90',
            'priority': 3
        }
    ]

    for trigger in triggers:
        try:
            api.trigger.create(
                description=trigger['description'],
                expression=trigger['expression'],
                priority=trigger['priority']
            )
        except Exception as e:
            print(f"Trigger error: {str(e)}")
```

---

## 5. Dashboard Oluşturma

```python
# Network Overview Dashboard
def create_network_dashboard():
    dashboard = api.dashboard.create(
        name='Network Performance Overview',
        display_period=30,
        auto_start=1,
        pages=[{
            'widgets': [
                {
                    'type': 'problems',
                    'name': 'Network Problems',
                    'x': 0,
                    'y': 0,
                    'width': 12,
                    'height': 5,
                    'fields': [{
                        'type': 0,
                        'name': 'severities',
                        'value': '4,5'  # High, Disaster
                    }]
                },
                {
                    'type': 'graph',
                    'name': 'Top Bandwidth Consumers',
                    'x': 0,
                    'y': 5,
                    'width': 12,
                    'height': 5
                }
            ]
        }]
    )
    print(f"✓ Dashboard created: {dashboard}")
```

---

## 6. Email Notification Setup

```python
# Media type (Email) oluşturma
def create_email_mediatype():
    mediatype = api.mediatype.create(
        name='Email Notifications',
        type=0,  # Email
        smtp_server='smtp.company.com',
        smtp_port=587,
        smtp_helo='zabbix.company.com',
        smtp_email='zabbix@company.com',
        smtp_authentication=1,
        username='zabbix@company.com',
        passwd='<smtp_password>',
        smtp_security=1,  # STARTTLS
        message_format=0  # HTML
    )
    print(f"✓ Media type created")

# Action (Notification) oluşturma
def create_notification_action():
    action = api.action.create(
        name='Network Device Alert',
        eventsource=0,  # Trigger
        status=0,  # Enabled
        filter={
            'evaltype': 0,
            'conditions': [{
                'conditiontype': 0,  # Host group
                'operator': 2,  # equals
                'value': '<hostgroup_id>'  # Network devices group
            }]
        },
        operations=[{
            'operationtype': 0,  # Send message
            'esc_period': '0',
            'esc_step_from': 1,
            'esc_step_to': 1,
            'opmessage': {
                'default_msg': 1,
                'mediatypeid': '<mediatype_id>'
            },
            'opmessage_grp': [{
                'usrgrpid': '<usergroup_id>'
            }]
        }]
    )
    print(f"✓ Action created")
```

---

## ÇALIŞMA ADIMLARI

### Adım 1: Environment Setup
```bash
cd C:\Users\Ali\Documents\Projects\zabbix-master-agent
source .env  # veya Windows'ta: set komutları ile

# Zabbix bağlantı testi
python collect_zabbix_info.py
```

### Adım 2: Host Groups Oluştur
```bash
python -c "from zabbix_deployment import create_host_groups; create_host_groups()"
```

### Adım 3: Network Cihazları Ekle
```bash
# Önce manuel olarak kritik cihazları ekle (CORE, MPLS)
python add_critical_devices.py

# Sonra discovery ile otomatik ekleme
python setup_discovery_rules.py
```

### Adım 4: Dashboard ve Trigger Setup
```bash
python setup_dashboards.py
python setup_notifications.py
```

### Adım 5: Doğrulama
```bash
# Tüm host'ları listele
python list_hosts.py

# Problem'leri kontrol et
python check_problems.py
```

---

## GEREKLİ PYTHON SCRIPTS

Aşağıdaki scriptler oluşturulacak:

1. `setup_phase1.py` - Tüm adımları otomatik çalıştırır
2. `add_critical_devices.py` - Kritik cihazları manuel ekler
3. `setup_discovery_rules.py` - Discovery rules oluşturur
4. `setup_dashboards.py` - Dashboard'ları oluşturur
5. `setup_notifications.py` - Email notification setup
6. `list_hosts.py` - Eklenen host'ları listeler
7. `check_problems.py` - Aktif problemleri gösterir

---

## TROUBLESHOOTING

### SNMP Erişim Testi:
```bash
# Linux/Mac
snmpwalk -v2c -c <community_string> <device_ip> system

# Windows (Net-SNMP kurulu olmalı)
snmpwalk.exe -v2c -c <community_string> <device_ip> system
```

### Zabbix Server Log:
```bash
tail -f /var/log/zabbix/zabbix_server.log
```

### Database Connection Test:
```bash
psql -h <db_ip> -U zabbix -d zabbix -c "SELECT count(*) FROM hosts;"
```

---

**Skill Durumu:** ✅ Aktif
**Deployment Plan:** `/deployment_plan_phase1.md`
**Next Steps:** Python automation scripts oluşturulacak

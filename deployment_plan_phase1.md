# Zabbix Deployment Plan - Phase 1
## Module 0 + Module 2: Foundation + Network Performance Monitoring

---

## GENEL BAKIŞ

**Seçilen Modüller:**
- ✅ Module 0: Foundation (Platform Kurulumu)
- ✅ Module 2: Network Performance Monitoring (NPM)

**Toplam Süre:** 2 hafta (10 iş günü)
**Toplam Maliyet:** $9,300 ($4,500 + $4,800)

---

## MODULE 0: FOUNDATION - PLATFORM KURULUMU

### 1. Sunucu Gereksinimleri

#### Zabbix Server VM
```
Hostname: zabbix-server-01
OS: Ubuntu 22.04 LTS Server (veya RHEL 9)
vCPU: 12 core
RAM: 32 GB
Disk: 500 GB SSD
Network:
  - Management: Static IP (örn: 192.168.1.100)
  - Gateway ve DNS yapılandırılmış
```

#### Database Server VM
```
Hostname: zabbix-db-01
OS: Ubuntu 22.04 LTS Server (veya RHEL 9)
vCPU: 16 core
RAM: 64 GB
Disk: 2 TB SSD (RAID 10 önerilen)
Network:
  - Management: Static IP (örn: 192.168.1.101)
  - Zabbix Server ile network connectivity
```

### 2. Network Gereksinimleri

**Firewall Kuralları (Zabbix Server):**
```
Gelen (Inbound):
- TCP 10051: Zabbix trapper (agent → server)
- TCP 80/443: Web interface
- TCP 22: SSH (yönetim için)

Giden (Outbound):
- TCP 10050: Zabbix agent kontrolü
- UDP 161: SNMP polling
- TCP 443: VMware vCenter API
- TCP 3306/5432: Database (eğer ayrı sunucuda)
```

**Firewall Kuralları (Database Server):**
```
Gelen (Inbound):
- TCP 5432: PostgreSQL (veya 3306 MySQL)
- TCP 22: SSH (yönetim için)

Giden (Outbound):
- İnternet erişimi (yum/apt güncellemeleri için)
```

### 3. Kurulum Adımları

#### Adım 1: VM Hazırlığı (1 gün)
```bash
# İki VM oluşturulacak
# ESXi üzerinde kaynak ayırma
# Static IP ataması
# Hostname configuration
# DNS kayıtları
```

**Teslim Edilen:**
- 2 VM (Zabbix Server + Database)
- Network bağlantısı aktif
- SSH erişimi

#### Adım 2: Database Kurulumu (1 gün)
```bash
# PostgreSQL 15 kurulumu
sudo apt update
sudo apt install postgresql-15

# Database oluşturma
sudo -u postgres createuser --pwprompt zabbix
sudo -u postgres createdb -O zabbix zabbix

# Schema import
zcat /usr/share/zabbix-sql-scripts/postgresql/server.sql.gz | \
  sudo -u zabbix psql zabbix

# PostgreSQL tuning (zabbix_db-01)
# shared_buffers = 16GB
# effective_cache_size = 48GB
# work_mem = 256MB
# maintenance_work_mem = 2GB
# max_connections = 500
```

**Teslim Edilen:**
- PostgreSQL 15 kurulu ve çalışır
- Zabbix database oluşturuldu
- Performance tuning yapıldı

#### Adım 3: Zabbix Server Kurulumu (1.5 gün)
```bash
# Repository ekleme (Ubuntu)
wget https://repo.zabbix.com/zabbix/7.4/ubuntu/pool/main/z/zabbix-release/zabbix-release_7.4-1+ubuntu22.04_all.deb
sudo dpkg -i zabbix-release_7.4-1+ubuntu22.04_all.deb
sudo apt update

# Zabbix Server kurulumu
sudo apt install zabbix-server-pgsql zabbix-frontend-php php8.1-pgsql \
  zabbix-nginx-conf zabbix-sql-scripts zabbix-agent

# Konfigürasyon (/etc/zabbix/zabbix_server.conf)
DBHost=192.168.1.101
DBName=zabbix
DBUser=zabbix
DBPassword=<strong_password>
StartPollers=100
StartPollersUnreachable=20
StartTrappers=20
StartPingers=20
CacheSize=2G
HistoryCacheSize=1G
TrendCacheSize=512M
ValueCacheSize=2G

# Service başlatma
sudo systemctl enable zabbix-server zabbix-agent nginx php8.1-fpm
sudo systemctl start zabbix-server zabbix-agent nginx php8.1-fpm
```

**Teslim Edilen:**
- Zabbix Server 7.4 kurulu
- Database bağlantısı aktif
- Service'ler running

#### Adım 4: Web Interface Kurulumu (0.5 gün)
```bash
# Nginx configuration (/etc/nginx/sites-available/zabbix)
server {
    listen 80;
    server_name zabbix.company.com;

    # SSL redirect (sonra yapılacak)
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name zabbix.company.com;

    ssl_certificate /etc/ssl/certs/zabbix.crt;
    ssl_certificate_key /etc/ssl/private/zabbix.key;

    root /usr/share/zabbix;
    index index.php;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }
}

# SSL sertifikası (self-signed veya Let's Encrypt)
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /etc/ssl/private/zabbix.key \
  -out /etc/ssl/certs/zabbix.crt

sudo systemctl restart nginx
```

**Web Setup:**
1. Tarayıcıda https://zabbix-server-ip/ adresine git
2. Setup wizard'ı tamamla
3. Database bilgilerini gir
4. Admin kullanıcısı ile login (Admin/zabbix)

**Teslim Edilen:**
- Web interface erişilebilir
- SSL aktif
- Admin login çalışıyor

#### Adım 5: Kullanıcı Yönetimi (0.5 gün)
```
Oluşturulacak Kullanıcılar:

1. Admin (mevcut)
   - Role: Super admin
   - Tüm yetkiler

2. noc-operator
   - Role: User
   - Read-only dashboard erişimi
   - Problem acknowledgement yetkisi

3. it-engineer
   - Role: Admin
   - Host/item/trigger yönetimi
   - Dashboard oluşturma

User Groups:
- NOC Team (read-only)
- IT Operations (full access)
- Management (dashboard only)
```

#### Adım 6: Email Notification Setup (0.5 gün)
```
Media Type: Email

SMTP Server: smtp.company.com (veya smtp.gmail.com)
SMTP Port: 587 (TLS) veya 465 (SSL)
SMTP Auth: yes
Username: zabbix@company.com
Password: <smtp_password>

Test email gönderimi yapılacak
```

#### Adım 7: Backup Configuration (0.5 gün)
```bash
#!/bin/bash
# /opt/zabbix-backup/backup.sh

# Database backup
pg_dump -h 192.168.1.101 -U zabbix zabbix | \
  gzip > /backup/zabbix-db-$(date +%Y%m%d).sql.gz

# Configuration backup
tar -czf /backup/zabbix-config-$(date +%Y%m%d).tar.gz \
  /etc/zabbix/

# Retention: 30 gün
find /backup/ -name "zabbix-*.gz" -mtime +30 -delete

# Cron job (her gün 02:00)
0 2 * * * /opt/zabbix-backup/backup.sh
```

**Teslim Edilen:**
- Otomatik backup script
- Cron job aktif
- Test backup doğrulandı

---

## MODULE 2: NETWORK PERFORMANCE MONITORING

### 1. İzlenecek Cihazlar

#### MERKEZ (22 + 2 + 2 = 26 cihaz)
```
Kenar Switch: 20 adet
  - Markalar: Cisco, HP, Huawei (belirlenmeli)
  - Model: (belirlenmeli)
  - Yönetim IP aralığı: 192.168.x.x

Omurga Switch: 2 adet
  - Core switch 1: IP
  - Core switch 2: IP

MPLS Router: 2 adet
  - MPLS-1: IP
  - MPLS-2: IP
```

#### BÖLGE 1-4 (12 switch)
```
Bölge 1: 3 switch + 2-3 AP
  - Switch-1: IP
  - Switch-2: IP
  - Switch-3: IP
  - AP: IP aralığı

Bölge 2: 3 switch + 2-3 AP
Bölge 3: 3 switch + 2-3 AP
Bölge 4: 3 switch + 2-3 AP
```

#### ESKİŞEHİR FABRİKA (20 cihaz)
```
Switch: 10 adet
  - IP aralığı: 10.x.x.x

Access/AP: 10 adet
  - IP aralığı: 10.x.x.x
```

**TOPLAM: 54 network cihazı + 8-12 AP = ~62 cihaz**

### 2. Cihaz Gereksinimleri

#### 2.1 SNMP Konfigürasyonu (Tüm Cihazlar)

**SNMP v2c (Basit kurulum):**
```
SNMP Community String: <custom_community_string>
  Örnek: "Zabbix_Monitoring_2024"

SNMP Access:
  - Read-only community
  - ACL: Sadece Zabbix Server IP'sine izin
    access-list 99 permit 192.168.1.100
    snmp-server community <community_string> RO 99
```

**SNMP v3 (Güvenli, önerilen):**
```
SNMP v3 User: zabbix_mon
Security Level: authPriv
Authentication: SHA256
Auth Password: <strong_auth_password>
Privacy: AES256
Privacy Password: <strong_priv_password>

Örnek Cisco config:
snmp-server group zabbix-group v3 priv
snmp-server user zabbix_mon zabbix-group v3 \
  auth sha <auth_password> priv aes 256 <priv_password>
```

#### 2.2 Network Erişim Gereksinimleri

**Zabbix Server'dan tüm network cihazlarına:**
```
Protocol: ICMP (ping)
  - Availability check için

Protocol: SNMP
  - UDP 161: SNMP polling
  - Zabbix Server → All network devices

Routing:
  - Zabbix Server tüm cihazlara erişebilmeli
  - Bölgeler: VPN veya MPLS üzerinden
  - Fabrika: VPN veya MPLS üzerinden
```

#### 2.3 Vendor-Specific Gereksinimler

**Cisco IOS/IOS-XE:**
```
snmp-server community <string> RO
snmp-server enable traps
snmp-server host 192.168.1.100 version 2c <string>
```

**HP Comware:**
```
snmp-agent community read <string>
snmp-agent sys-info version v2c
snmp-agent target-host trap address udp-domain 192.168.1.100 \
  params securityname <string>
```

**Huawei:**
```
snmp-agent community read <string>
snmp-agent sys-info version v2c
```

### 3. Cihaz Ekleme Prosedürü

#### Adım 1: Discovery Rule Oluşturma (Otomatik)

```
Configuration → Discovery → Create discovery rule

Name: Network Device Discovery - MERKEZ
IP range: 192.168.1.1-192.168.1.254
Update interval: 1h
Checks:
  - ICMP ping
  - SNMP v2c community: <community_string>
  - OID check: SNMPv2-MIB::sysDescr.0

Device uniqueness criteria: IP address

Actions:
  - Add host
  - Link template: Template Net Generic Device SNMP
  - Add to group: Network Devices / MERKEZ
```

**Bölgeler ve Fabrika için ayrı discovery rule:**
```
Discovery Rule 2: BÖLGE-1
IP range: 10.1.1.1-10.1.1.254

Discovery Rule 3: BÖLGE-2
Discovery Rule 4: BÖLGE-3
Discovery Rule 5: BÖLGE-4

Discovery Rule 6: ESKİŞEHİR
IP range: 10.10.x.x
```

#### Adım 2: Manuel Host Ekleme (Kritik Cihazlar)

```
Configuration → Hosts → Create host

Host name: CORE-SWITCH-01
Visible name: Merkez Omurga Switch 1
Groups:
  - Network devices
  - MERKEZ
  - Critical Infrastructure

Interfaces:
  Type: SNMP
  IP address: 192.168.1.1
  Port: 161
  SNMP version: SNMPv2
  SNMP community: <community_string>

  (veya SNMPv3 ayarları)

Templates:
  - Template Net Cisco IOS SNMP (vendor-specific)
  - Template Module ICMP Ping

Macros:
  {$SNMP_COMMUNITY} = <community_string>
  {$ICMP_LOSS_WARN} = 20
  {$ICMP_RESPONSE_TIME_WARN} = 200ms

Tags:
  Location: Merkez
  Type: Core
  Priority: Critical
```

#### Adım 3: Template Seçimi

**Vendor ve Model Bazlı Template'ler:**

| Vendor | Model | Template |
|--------|-------|----------|
| Cisco | IOS/IOS-XE | Template Net Cisco IOS SNMP |
| Cisco | Catalyst | Template Net Cisco Catalyst SNMP |
| HP | Comware | Template Net HP Comware SNMP |
| Huawei | VRP | Template Net Huawei VRP SNMP |
| Ubiquiti | EdgeSwitch | Template Net Ubiquiti EdgeSwitch SNMP |
| Ubiquiti | UniFi AP | Template Net Ubiquiti AirMax SNMP |
| Generic | Diğer | Template Net Generic Device SNMP |

**Template Hiyerarşisi:**
```
Template Net Cisco IOS SNMP
  └─ Template Module Interfaces SNMP
  └─ Template Module ICMP Ping
  └─ Template Module Generic SNMP
```

#### Adım 4: Host Group Yapısı

```
Network devices (Ana grup)
├─ MERKEZ
│   ├─ Kenar Switches
│   ├─ Omurga Switches
│   └─ MPLS Routers
├─ BÖLGE-1
│   ├─ Switches
│   └─ Access Points
├─ BÖLGE-2
├─ BÖLGE-3
├─ BÖLGE-4
└─ ESKİŞEHİR
    ├─ Switches
    └─ Access Devices
```

### 4. Monitored Metrics (İzlenecek Metrikler)

#### 4.1 Device Level
```
- Availability (ICMP ping)
  Interval: 30s

- Uptime (sysUpTime)
  Interval: 5m

- CPU Utilization (%)
  Interval: 1m
  Trigger: >80% for 5m (Warning)
  Trigger: >90% for 5m (High)

- Memory Utilization (%)
  Interval: 5m
  Trigger: >85% (Warning)
  Trigger: >95% (High)

- Temperature (Celsius)
  Interval: 5m
  Trigger: >60°C (Average)
  Trigger: >70°C (High)
```

#### 4.2 Interface Level (Her port için)
```
- Interface Status (up/down)
  Interval: 1m
  Trigger: Operational status down

- Interface Speed & Duplex
  Interval: 1h

- Inbound Traffic (bps)
  Interval: 1m
  Preprocessing: Change per second

- Outbound Traffic (bps)
  Interval: 1m

- Interface Utilization (%)
  Calculation: (bps / interface_speed) * 100
  Trigger: >80% for 5m (Warning)
  Trigger: >90% for 5m (High)

- Interface Errors (in/out)
  Interval: 1m
  Preprocessing: Change per second
  Trigger: >10 errors/s (Warning)

- Interface Discards
  Interval: 1m
```

#### 4.3 SNMP Traps (Event-based)
```
- Link Down/Up events
- Configuration change
- Authentication failure
- Cold/Warm start
```

### 5. Trigger Configuration

#### Kritik Alarmlar
```
1. Device Unavailable
   Expression: {ICMP ping fails for 3 attempts}
   Severity: High

2. High CPU Usage
   Expression: {CPU >90% for 5 min}
   Severity: Warning

3. Critical Interface Down
   Expression: {Uplink interface down}
   Severity: High
   Dependencies: Device availability

4. High Bandwidth Utilization
   Expression: {Interface util >90% for 5 min}
   Severity: Warning
```

#### Flapping Prevention
```
Problem Expression: Interface operational status = down
OK Event Expression: Interface operational status = up for 5 min
  (5 dakika up kaldıktan sonra OK kabul et)
```

### 6. Dashboard Configuration

#### Dashboard 1: Network Overview
```
Widgets:
1. Problem Widget
   - Critical network problems
   - Severity: High, Disaster

2. Map Widget
   - Network topology
   - Real-time status

3. Graph Widget (Top 10)
   - Bandwidth utilization (Top consumers)

4. Plain Text Widget
   - Device count
   - Total interfaces
   - Average availability
```

#### Dashboard 2: Interface Statistics
```
Widgets:
1. Top Hosts (by traffic)
   - Top 10 bandwidth consumers

2. Graph Prototype
   - Interface traffic (in/out)
   - Aggregated by location

3. Interface Status Table
   - Up/Down interfaces
   - Groupped by device
```

### 7. Notification Setup

```
Action: Network Device Down
Conditions:
  - Trigger severity >= Warning
  - Host group = Network devices

Operations:
  Step 1: Send to NOC Team (email + Slack)
  Step 2 (15 min): Send to IT Manager (SMS + email)
  Step 3 (30 min): Send to IT Director (phone + email)

Recovery Operations:
  - Notify all: Problem resolved

Message Template:
  Subject: {TRIGGER.STATUS}: {TRIGGER.NAME}
  Body:
    Device: {HOST.NAME}
    IP: {HOST.IP}
    Severity: {TRIGGER.SEVERITY}
    Time: {EVENT.DATE} {EVENT.TIME}
    Details: {TRIGGER.DESCRIPTION}

    Dashboard: https://zabbix.company.com/zabbix.php?action=dashboard.view
```

### 8. Network Map

```
Map Name: Network Topology - Full Infrastructure

Elements:
1. Merkez Omurga (2 core switches)
2. Bağlı kenar switches (20 adet)
3. MPLS routers (2 adet)
4. WAN links → Bölgeler
5. WAN link → Eskişehir

Links:
  - Interface trigger-based coloring
  - Green: OK
  - Yellow: Warning (>80% util)
  - Red: Down / Critical

Icons:
  - Router icon for MPLS
  - Switch icon for switches
  - Cloud icon for WAN
  - Building icon for locations
```

---

## KURULUM TIMELINE

### Hafta 1: Platform Setup (Module 0)
```
Pazartesi: VM hazırlığı
Salı: Database kurulumu
Çarşamba: Zabbix Server kurulumu
Perşembe: Web interface + SSL
Cuma: User management + Email + Backup
```

### Hafta 2: Network Monitoring (Module 2)
```
Pazartesi:
  - SNMP configuration (müşteri ile birlikte)
  - MERKEZ cihazları ekleme (26 cihaz)

Salı:
  - BÖLGE cihazları ekleme (12 switch + AP)
  - Discovery rules

Çarşamba:
  - ESKİŞEHİR cihazları ekleme (20 cihaz)
  - Template tuning

Perşembe:
  - Dashboard oluşturma
  - Network map
  - Trigger optimization

Cuma:
  - Test ve doğrulama
  - Notification test
  - Dokümantasyon
```

---

## MÜŞTERİDEN GEREKENLER

### 1. Sunucu Kaynakları
- [ ] 2 VM hazır (Zabbix + Database)
- [ ] Static IP atamaları yapıldı
- [ ] DNS kayıtları oluşturuldu
- [ ] Firewall kuralları açıldı

### 2. Network Erişim
- [ ] Zabbix Server'dan tüm network cihazlarına ping atılabiliyor
- [ ] VPN/MPLS üzerinden bölge ve fabrika erişimi var
- [ ] SNMP port (UDP 161) açık

### 3. Network Cihaz Bilgileri
- [ ] Tüm cihazların IP listesi (Excel)
- [ ] Vendor ve model bilgileri
- [ ] Yönetim kullanıcı bilgileri (SNMP konfigürasyonu için)

### 4. SNMP Konfigürasyonu
- [ ] SNMP community string belirlendi
- [ ] Network ekibi SNMP yapılandırmasını yapacak
  (veya bizimle birlikte yapacak)

### 5. Koordinasyon
- [ ] Teknik koordinatör belirlendi
- [ ] Kurulum için tarih/saat belirlendi
- [ ] Change window tanımlandı (canlı sistemler için)

---

## TESLIMATLAR (Deliverables)

### Module 0 Teslimatları:
1. ✅ Çalışır Zabbix Server 7.4
2. ✅ PostgreSQL Database
3. ✅ Web interface (HTTPS)
4. ✅ User accounts (Admin, NOC, IT)
5. ✅ Email notification aktif
6. ✅ Backup script kurulu
7. ✅ Dokümantasyon:
   - Server kurulum dokümanı
   - User guide (temel)
   - Backup/restore prosedürü

### Module 2 Teslimatları:
1. ✅ 54+ network cihazı izleniyor
2. ✅ SNMP monitoring aktif
3. ✅ Interface monitoring (bandwidth, errors)
4. ✅ 2x Dashboard:
   - Network Overview
   - Interface Statistics
5. ✅ Network topology map
6. ✅ Notification aktif ve test edildi
7. ✅ Dokümantasyon:
   - Network cihaz listesi
   - SNMP konfigürasyon kılavuzu
   - Trigger listesi
   - Dashboard kullanım kılavuzu

---

## BAŞARI KRİTERLERİ

### Module 0:
- [x] Zabbix Server uptime >99%
- [x] Web interface 2 saniyeden hızlı yanıt veriyor
- [x] Database backup çalışıyor
- [x] Email notification çalışıyor

### Module 2:
- [x] Tüm network cihazları başarıyla eklendi
- [x] SNMP polling çalışıyor (>95% success rate)
- [x] Interface discovery aktif
- [x] Kritik interface'lerde alarm çalışıyor
- [x] Dashboard'lar gerçek zamanlı data gösteriyor
- [x] False-positive oranı <%5

---

## SUPPORT & MAINTENANCE

**İlk 1 Ay Stabilizasyon:**
- Fine-tuning
- False-positive elimination
- Threshold adjustments
- On-demand support (email/remote)

**Sonrası:**
- Extended support package satın alınabilir
- Veya as-needed consulting (saatlik)

---

## İLETİŞİM VE RAPORLAMA

**Haftalık Durum Raporu:**
- Her Cuma günü
- Email ile durum raporu
- Tamamlanan tasks
- Sonraki hafta planı
- Blocker'lar (varsa)

**Kurulum Tamamlama:**
- Final acceptance meeting
- Handover dokumentasyonu
- Knowledge transfer
- Sign-off

---

**Hazırlayan:** Zabbix Implementation Team
**Tarih:** 2025-11-16
**Versiyon:** 1.0
**Durum:** Müşteri onayı bekliyor

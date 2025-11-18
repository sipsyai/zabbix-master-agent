# ADLogon Plugin - Quick Start Guide

Active Directory logon monitoring için Zabbix Agent 2 plugin'ini hızlıca başlatın!

## 🚀 5 Dakikada Kurulum

### 1. Plugin Binary'si Hazır

Plugin başarıyla derlenmiş durumda:
```
ad-logon-plugin/build/zabbix-agent2-plugin-adlogon.exe
```

### 2. Test Ortamı (DC01)

Zabbix Server: `192.168.213.141`
- Username: `Admin`
- Password: `zabbix`
- Host: `dc01` (Active Directory Domain Controller)

### 3. Hızlı Test (Zabbix Agent olmadan)

Plugin versiyonunu kontrol edin:
```powershell
.\build\zabbix-agent2-plugin-adlogon.exe --version
```

Çıktı:
```
Zabbix ADLogon plugin
Version 1.0.0beta1, built with go1.25.4
Protocol version 6.4.0
```

## 📋 Desteklenen Log Türleri

| Kod | Açıklama | Örnek Kullanım |
|-----|----------|----------------|
| `failure` | Başarısız logon denemeleri | ad.logon[failure,24] |
| `dc_activity` | DC logon aktiviteleri | ad.logon[dc_activity,12] |
| `server_activity` | Member server logonları | ad.logon[server_activity,24] |
| `workstation_activity` | Workstation logonları | ad.logon[workstation_activity,6] |
| `user_activity` | Kullanıcı bazlı aktivite | ad.logon[user_activity,24] |
| `recent_users` | Son logon yapan kullanıcılar | ad.logon[recent_users,1] |
| `last_logon` | Workstation bazlı son logon | ad.logon[last_logon,48] |
| `multiple_computers` | Çoklu bilgisayara logon | ad.logon[multiple_computers,24] |
| `radius` | RADIUS/NPS logonları | ad.logon[radius,12] |

## 🎯 Kullanım Örnekleri

### Item Key Format

```
ad.logon[<type>, <hours>, <computer>]
```

**Parametreler:**
- `type` (zorunlu): Log türü (yukarıdaki tablodan)
- `hours` (opsiyonel): Kaç saat geriye bakılacak (varsayılan: 24)
- `computer` (opsiyonel): Spesifik bilgisayar filtresi

### Örnek Item'lar

```
# Son 24 saatteki başarısız logonlar
ad.logon[failure]

# Son 12 saatteki DC aktiviteleri
ad.logon[dc_activity,12]

# Belirli bir bilgisayardaki hatalar
ad.logon[failure,24,DC01]

# Son 1 saatteki kullanıcı aktiviteleri
ad.logon[user_activity,1]
```

## 📤 JSON Çıktı Formatı

```json
{
  "count": 5,
  "start_time": "2025-11-16T14:00:00Z",
  "end_time": "2025-11-17T14:00:00Z",
  "events": [
    {
      "timestamp": "2025-11-17T13:45:23Z",
      "event_id": 4625,
      "computer": "DC01",
      "user": "jdoe",
      "domain": "CONTOSO",
      "logon_type": 3,
      "logon_type_name": "Network",
      "source_ip": "192.168.1.100",
      "status": "failure",
      "failure_reason": "Unknown user name or bad password"
    }
  ]
}
```

## 🔧 Zabbix Server'da Kullanım

### Adım 1: Host'a Item Ekleyin

Zabbix Frontend → Configuration → Hosts → dc01 → Items → Create item

**Örnek Item 1: Başarısız Logon Sayısı**
- Name: `AD: Failed Logons (24h)`
- Type: `Zabbix agent (active)`
- Key: `ad.logon[failure,24]`
- Type of information: `Text`
- Update interval: `5m`
- Preprocessing:
  - JSONPath: `$.count`

**Örnek Item 2: DC Aktivite Detayları**
- Name: `AD: DC Activity Details`
- Key: `ad.logon[dc_activity,12]`
- Type of information: `Text`
- History: `7d`

### Adım 2: Trigger Oluşturun

**Yüksek Sayıda Başarısız Logon**
```
{dc01:ad.logon[failure,1].last()}>10
```
- Name: High number of failed logons
- Severity: Warning

**Çoklu Bilgisayar Erişimi**
```
{dc01:ad.logon[multiple_computers,24].last()}>0
```
- Name: User logged into multiple computers
- Severity: Information

### Adım 3: Graph Oluşturun

Configuration → Hosts → dc01 → Graphs → Create graph

- Name: AD Logon Trends
- Items:
  - ad.logon[failure,24] (kırmızı)
  - ad.logon[dc_activity,24] (yeşil)
  - ad.logon[user_activity,24] (mavi)

## 🏗️ Production Deployment

### DC01'e Kurulum

```powershell
# 1. Plugin'i kopyala
Copy-Item .\build\zabbix-agent2-plugin-adlogon.exe `
    -Destination "\\dc01\C$\Program Files\Zabbix Agent 2\plugins\"

# 2. Konfig dosyasını kopyala
Copy-Item .\adlogon.conf `
    -Destination "\\dc01\C$\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\"

# 3. Agent'ı yeniden başlat
Invoke-Command -ComputerName dc01 -ScriptBlock {
    Restart-Service "Zabbix Agent 2"
}
```

### Konfigürasyon Dosyası (adlogon.conf)

```conf
# Plugin binary yolu
Plugins.ADLogon.System.Path=C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe

# Performans ayarları
Plugins.ADLogon.Timeout=30
Plugins.ADLogon.MaxEvents=1000
Plugins.ADLogon.CacheExpiry=300
Plugins.ADLogon.DefaultHours=24
```

## 🎨 Dashboard Widget Örnekleri

### Widget 1: Başarısız Logon Counter

- Type: Plain text
- Item: `ad.logon[failure,24]`
- Dynamic item: `$.count`

### Widget 2: Son Olaylar Table

- Type: Item value
- Item: `ad.logon[user_activity,12]`
- Show: Latest data

### Widget 3: Logon Trend Graph

- Type: Graph (classic)
- Items: failure, dc_activity, user_activity

## ⚡ Performans İpuçları

### Cache Kullanımı

Sık sorgulanan metrikler için:
```conf
Plugins.ADLogon.CacheExpiry=300  # 5 dakika
```

### Zaman Aralığını Optimize Etme

```
# Kritik: Her 1 dakika, son 1 saat
ad.logon[failure,1]  →  Update interval: 1m

# Normal: Her 5 dakika, son 12 saat
ad.logon[dc_activity,12]  →  Update interval: 5m

# Düşük: Her 15 dakika, son 24 saat
ad.logon[user_activity,24]  →  Update interval: 15m
```

### Event Log Optimizasyonu

```powershell
# Event log boyutunu artır
wevtutil sl Security /ms:1073741824  # 1 GB
```

## 📊 Monitoring Senaryoları

### Güvenlik Monitoring

```
# Brute force detection
ad.logon[failure,1] > 50

# After-hours access
ad.logon[user_activity,1] @ 22:00-06:00

# Unusual RADIUS activity
ad.logon[radius,6] > 0
```

### Compliance Monitoring

```
# Logon audit trail
ad.logon[user_activity,720]  # 30 gün

# Privileged access
ad.logon[dc_activity,24]  # DC access

# Remote access
ad.logon[radius,24]  # VPN/Remote
```

### Operational Monitoring

```
# System health
ad.logon[dc_activity,1]  # DC responsiveness

# User distribution
ad.logon[workstation_activity,12]  # Workload

# Session management
ad.logon[multiple_computers,24]  # Concurrent sessions
```

## 🔍 Troubleshooting

### Plugin Çalışmıyor

```powershell
# Agent log'u kontrol et
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 50

# Plugin'in yüklendiğini doğrula
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -T | Select-String "ADLogon"
```

### Event Döndürmüyor

```powershell
# Event log'da veri var mı?
Get-WinEvent -FilterHashtable @{LogName='Security';ID=4625} -MaxEvents 5

# Audit policy aktif mi?
auditpol /get /category:"Logon/Logoff"
```

### Permission Hatası

```powershell
# Servis hesabını kontrol et
Get-WmiObject Win32_Service | Where-Object {$_.Name -eq "Zabbix Agent 2"} | Select-Object StartName

# Local System'e geç (gerekirse)
sc.exe config "Zabbix Agent 2" obj= "LocalSystem"
Restart-Service "Zabbix Agent 2"
```

## 📚 Ek Kaynaklar

- **Detaylı Kurulum**: [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)
- **Build Rehberi**: [BUILD_GUIDE.md](BUILD_GUIDE.md)
- **Tam Dokümantasyon**: [README.md](README.md)

## 🎓 Hızlı Referans

### Event ID'ler

| ID | Açıklama |
|----|----------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4768 | Kerberos TGT |
| 4769 | Kerberos service ticket |
| 4776 | NTLM authentication |
| 6272 | RADIUS success |
| 6273 | RADIUS failure |

### Logon Type'lar

| Type | Adı | Açıklama |
|------|-----|----------|
| 2 | Interactive | Console logon |
| 3 | Network | Network share access |
| 10 | RemoteInteractive | RDP/Terminal Services |
| 11 | CachedInteractive | Cached credentials |

## ✅ Checklist

- [ ] Plugin derlenmiş ve hazır
- [ ] DC01'e kopyalandı
- [ ] Konfig dosyası ayarlandı
- [ ] Zabbix Agent yeniden başlatıldı
- [ ] Test item oluşturuldu
- [ ] Veri geliyor (Latest data)
- [ ] Trigger'lar tanımlandı
- [ ] Dashboard widget'ları eklendi

## 🚀 Sonraki Adımlar

1. **Template Oluştur**: Tüm DC'ler için paylaşılabilir template
2. **LLD Kur**: Dinamik item discovery
3. **Alert Ayarla**: Email/SMS bildirimleri
4. **Dashboard**: Merkezi monitoring ekranı
5. **Report**: Haftalık/Aylık raporlar

---

**İyi Monitoring'ler! 🎯**

Plugin hakkında sorularınız için BUILD_GUIDE.md ve INSTALLATION_GUIDE.md dosyalarına bakın.

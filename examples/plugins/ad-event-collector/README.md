# AD Event Collector for Zabbix

Active Directory eventlerini Windows Event Log'lardan toplayıp Zabbix'e gönderen sistem.

## 📋 Gereksinimler

- Windows Server (Domain Controller)
- PowerShell 5.1 veya üzeri
- Zabbix Agent 2 kurulu
- Administrator yetkileri

## 🚀 Kurulum Adımları

### 1. Dosyaları DC01'e Kopyalayın

PowerShell ile dosyaları kopyalayın:

```powershell
# Local makineden DC01'e kopyala
$sourcePath = "C:\Users\Ali\Documents\Projects\zabbix-master-agent\ad-event-collector"
$destPath = "\\DC01\C$\Scripts\AD-Event-Collector"

# Klasör oluştur
New-Item -ItemType Directory -Path $destPath -Force

# Dosyaları kopyala
Copy-Item "$sourcePath\Collect-ADEvents.ps1" -Destination $destPath
Copy-Item "$sourcePath\event-mapping.json" -Destination $destPath
```

VEYA DC01'de direkt çalıştırın:

```powershell
# DC01'de PowerShell ile
$scriptPath = "C:\Scripts\AD-Event-Collector"
New-Item -ItemType Directory -Path $scriptPath -Force

# Dosyaları indirin (GitHub veya paylaşılan klasörden)
```

### 2. İlk Test Çalıştırması

DC01'de PowerShell'i **Administrator** olarak açın:

```powershell
cd C:\Scripts\AD-Event-Collector

# Manuel test çalıştırması
.\Collect-ADEvents.ps1 -TimeWindow 60 -ZabbixServer 192.168.213.141 -Verbose
```

**Beklenen Çıktı:**
```
==========================================
AD Event Collector - Starting
==========================================
Time Window: 60 minutes
Zabbix Server: 192.168.213.141:10051
Zabbix Host: DC01
Collecting events since: 2025-11-17 14:00:00
Processing category: User Management
  Found 15 events
Processing category: Logon Activity
  Found 342 events
...
==========================================
Collection Complete
Total Events Collected: 523
Categories Processed: 11
==========================================
```

### 3. Zabbix'te Veriyi Kontrol Et

1. Zabbix UI'da **Monitoring → Latest data** gidin
2. Host: **DC01** seçin
3. Filter: **AD Events** yazın
4. Veriler gelmeye başladı mı kontrol edin

### 4. Scheduled Task Oluşturun (Otomatik Çalıştırma)

DC01'de PowerShell ile:

```powershell
# Scheduled Task oluştur (Her 5 dakikada bir çalışacak)
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File C:\Scripts\AD-Event-Collector\Collect-ADEvents.ps1 -TimeWindow 5"

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 5) -RepetitionDuration ([TimeSpan]::MaxValue)

$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest

$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName "Zabbix AD Event Collector" `
    -Action $action `
    -Trigger $trigger `
    -Principal $principal `
    -Settings $settings `
    -Description "Collects AD events and sends to Zabbix every 5 minutes"
```

### 5. Task'ı Kontrol Et

```powershell
# Task'ı listele
Get-ScheduledTask -TaskName "Zabbix AD Event Collector"

# Manuel çalıştır
Start-ScheduledTask -TaskName "Zabbix AD Event Collector"

# Log dosyasını kontrol et
Get-Content C:\Scripts\AD-Event-Collector\ad-event-collector.log -Tail 50
```

## 📊 Toplanan Event Kategorileri

| Kategori | Event ID'ler | Açıklama |
|----------|-------------|----------|
| **Kullanıcı Yönetimi** | 4720, 4726, 4738, 4722, 4725, 4740, 4767, 4723, 4724 | User hesap işlemleri |
| **Grup Yönetimi** | 4727-4762 | Grup oluşturma, silme, üye ekleme/çıkarma |
| **Bilgisayar Yönetimi** | 4741, 4742, 4743 | Computer hesap işlemleri |
| **OU Yönetimi** | 5137, 5139, 5141 | Organizational Unit işlemleri |
| **GPO Yönetimi** | 5136 | Group Policy değişiklikleri |
| **Oturum Açma/Kapama** | 4624, 4625, 4634, 4647, 4672 | Logon/Logoff eventleri |
| **Dosya Servisi** | 4663, 4670 | Dosya erişimleri ve izin değişiklikleri |
| **Güvenlik ve Yetki** | 4704, 4705, 4706, 4719, 4739 | Security policy değişiklikleri |
| **Schema Değişiklikleri** | 4662 | AD Schema modifications |
| **Workstation Activity** | 4800, 4801, 4802, 4803 | Workstation lock/unlock |
| **Kritik Grup İzleme** | 4728, 4729, 4732, 4733 | Domain Admins, Enterprise Admins vb. |

## 🔧 Konfigürasyon

### Zabbix Server Değiştirme

```powershell
.\Collect-ADEvents.ps1 -ZabbixServer 10.0.0.100 -ZabbixPort 10051
```

### Toplama Sıklığını Ayarlama

```powershell
# 10 dakika geriye git
.\Collect-ADEvents.ps1 -TimeWindow 10

# 1 saat geriye git
.\Collect-ADEvents.ps1 -TimeWindow 60
```

### Event Kategorilerini Özelleştirme

`event-mapping.json` dosyasını düzenleyin:

```json
{
  "categories": {
    "custom_category": {
      "name": "Özel Kategori",
      "description": "Açıklama",
      "events": {
        "1234": "Event Açıklaması"
      }
    }
  }
}
```

## 📈 Zabbix Item Key'leri

Oluşturulan itemler:

- `ad.events[user_management]` - Kullanıcı yönetimi (Raw JSON)
- `ad.events[user_management,count]` - Event sayısı
- `ad.events[group_management]` - Grup yönetimi
- `ad.events[logon_activity]` - Oturum açma/kapama
- `ad.events[summary]` - Genel özet
- `ad.events[total_count]` - Toplam event sayısı

## 🐛 Troubleshooting

### Script çalışmıyor

```powershell
# Execution policy kontrolü
Get-ExecutionPolicy

# Bypass et
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process

# Manuel çalıştır ve hataları gör
.\Collect-ADEvents.ps1 -Verbose
```

### Zabbix'e veri gitmiyor

```powershell
# Zabbix Sender test et
& "C:\Program Files\Zabbix Agent 2\zabbix_sender.exe" `
    -z 192.168.213.141 `
    -p 10051 `
    -s "DC01" `
    -k "ad.events[summary]" `
    -o '{"test": "value"}' `
    -vv
```

### Log dosyasını kontrol et

```powershell
Get-Content C:\Scripts\AD-Event-Collector\ad-event-collector.log -Wait
```

### Event ID'leri test et

```powershell
# Son 1 saatte 4624 (Successful Logon) event'lerini göster
Get-WinEvent -FilterHashtable @{
    LogName='Security'
    ID=4624
    StartTime=(Get-Date).AddHours(-1)
} | Select-Object -First 10
```

## 📊 Grafana Dashboard

Zabbix datasource kullanarak Grafana'da dashboard oluşturabilirsiniz.

**Örnek Panel Query:**

```sql
-- Zabbix datasource ile
SELECT
  itemid,
  clock as time,
  value
FROM history_text
WHERE itemid IN (
  SELECT itemid FROM items WHERE key_ LIKE 'ad.events%'
)
AND clock > $from AND clock < $to
ORDER BY clock
```

## 📝 Log Rotation

Log dosyası büyürse otomatik temizleme:

```powershell
# Log dosyasını temizle (30 günden eski)
$logFile = "C:\Scripts\AD-Event-Collector\ad-event-collector.log"
if ((Get-Item $logFile).Length -gt 10MB) {
    $content = Get-Content $logFile -Tail 1000
    Set-Content $logFile -Value $content
}
```

## 🔐 Güvenlik Notları

- Script SYSTEM hesabı ile çalışır (Scheduled Task)
- Event Log okuma yetkisi gerekir (Administrator)
- Zabbix Sender plaintext iletişim kullanır (güvenli ağda kullanın)
- JSON verileri hassas bilgi içerebilir (kullanıcı adları, IP'ler)

## 📞 Destek

Sorun olursa:
1. Log dosyasını kontrol edin
2. Zabbix server'a erişim olduğundan emin olun
3. Event Log audit policy'si aktif mi kontrol edin

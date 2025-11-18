# ADLogon Plugin - Kurulum Rehberi

Bu rehber, ADLogon plugin'inin Windows Active Directory sunucularında nasıl kurulacağını ve yapılandırılacağını detaylıca açıklar.

## Sistem Gereksinimleri

### Donanım
- **CPU**: 2 core veya üzeri (önerilen)
- **RAM**: 512 MB minimum (1 GB önerilen)
- **Disk**: 50 MB boş alan

### Yazılım
- **İşletim Sistemi**: Windows Server 2012 R2 veya üzeri
  - Windows Server 2016/2019/2022 (önerilen)
- **Zabbix Agent**: Zabbix Agent 2 (6.0 veya üzeri)
- **Roller**: Active Directory Domain Services (isteğe bağlı)
- **İzinler**: Administrator yetkisi (Event Log okuma için)

### Ağ
- Zabbix Server/Proxy ile bağlantı
- Port: 10050 (Zabbix Agent passive mode)
- Port: 10051 (Zabbix Agent active mode)

## Ön Hazırlık

### 1. Zabbix Agent 2 Kurulumu

Eğer Zabbix Agent 2 henüz kurulu değilse:

```powershell
# Zabbix Agent 2'yi indirin
# https://www.zabbix.com/download_agents

# MSI installer'ı çalıştırın
msiexec /i zabbix_agent2-6.0.x-windows-amd64-openssl.msi /qn ^
    SERVER=192.168.1.100 ^
    SERVERACTIVE=192.168.1.100 ^
    HOSTNAME=dc01.example.com

# Servisi başlatın
Start-Service "Zabbix Agent 2"
```

### 2. Event Log Erişim İzinleri

Plugin'in Security event log'u okuyabilmesi için Zabbix Agent 2 servisinin Administrator veya Local System hesabı ile çalışması gerekir.

#### Servis Hesabını Kontrol Etme

```powershell
Get-WmiObject Win32_Service | Where-Object {$_.Name -eq "Zabbix Agent 2"} | Select-Object Name, StartName
```

#### Servis Hesabını Değiştirme (gerekirse)

```powershell
# Local System olarak ayarla
sc.exe config "Zabbix Agent 2" obj= "LocalSystem"

# Veya Administrator hesabı ile
sc.exe config "Zabbix Agent 2" obj= ".\Administrator" password= "YourPassword"

# Servisi yeniden başlat
Restart-Service "Zabbix Agent 2"
```

### 3. Event Log Audit Politikalarını Etkinleştirme

Domain Controller'da logon olaylarının kaydedildiğinden emin olun:

```powershell
# Mevcut audit politikasını kontrol et
auditpol /get /category:"Logon/Logoff"

# Logon events'i etkinleştir
auditpol /set /subcategory:"Logon" /success:enable /failure:enable
auditpol /set /subcategory:"Logoff" /success:enable
auditpol /set /subcategory:"Account Lockout" /failure:enable

# Kerberos authentication
auditpol /set /subcategory:"Kerberos Authentication Service" /success:enable /failure:enable
auditpol /set /subcategory:"Kerberos Service Ticket Operations" /success:enable /failure:enable
```

## Plugin Kurulumu

### Adım 1: Plugin Binary'sini İndirme/Derleme

**Seçenek A: Önceden Derlenmiş Binary (Önerilen)**

```powershell
# GitHub release'den indirin
# https://github.com/yourrepo/ad-logon-plugin/releases

# ZIP'i çıkarın
Expand-Archive -Path adlogon-plugin-1.0.0-beta1.zip -DestinationPath C:\Temp\adlogon
```

**Seçenek B: Kaynak Koddan Derleme**

BUILD_GUIDE.md dosyasına bakın.

### Adım 2: Plugin Dosyalarını Kopyalama

```powershell
# Plugin dizini oluştur
New-Item -ItemType Directory -Force -Path "C:\Program Files\Zabbix Agent 2\plugins"

# Binary'yi kopyala
Copy-Item "C:\Temp\adlogon\zabbix-agent2-plugin-adlogon.exe" `
    -Destination "C:\Program Files\Zabbix Agent 2\plugins\"

# Dosya izinlerini kontrol et
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe"
```

### Adım 3: Plugin Konfigürasyonu

```powershell
# Konfig dizini oluştur (yoksa)
New-Item -ItemType Directory -Force -Path "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d"

# Konfig dosyasını kopyala
Copy-Item "C:\Temp\adlogon\adlogon.conf" `
    -Destination "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\"
```

### Adım 4: Konfigürasyon Dosyasını Düzenleme

`C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf` dosyasını açın:

```conf
# ZORUNLU: Plugin binary yolu
Plugins.ADLogon.System.Path=C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe

# İSTEĞE BAĞLI: Ayarlar (varsayılanlar yeterlidir)
Plugins.ADLogon.Timeout=30
Plugins.ADLogon.MaxEvents=1000
Plugins.ADLogon.CacheExpiry=300
Plugins.ADLogon.DefaultHours=24
# Plugins.ADLogon.DebugMode=false
```

### Adım 5: Zabbix Agent 2'yi Yeniden Başlatma

```powershell
Restart-Service "Zabbix Agent 2"

# Servis durumunu kontrol et
Get-Service "Zabbix Agent 2"
```

### Adım 6: Plugin Testi

```powershell
# Plugin'in yüklendiğini kontrol et
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -T

# Metric testi
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t ad.logon[failure,24]
```

Başarılı bir çıktı şöyle görünmelidir:
```
ad.logon[failure,24] [t|{"count":5,"start_time":"2025-11-16T10:00:00Z",...}]
```

## Zabbix Server/Frontend Konfigürasyonu

### Adım 1: Host'u Ekleyin veya Güncelleyin

1. Zabbix Frontend'e giriş yapın
2. **Configuration → Hosts** menüsüne gidin
3. Domain Controller host'unu bulun veya yeni ekleyin

### Adım 2: Item'lar Oluşturun

**Örnek 1: Logon Failure Count**

- **Name**: AD: Logon Failures (Last 24h)
- **Type**: Zabbix agent (active/passive)
- **Key**: `ad.logon[failure,24]`
- **Type of information**: Text
- **Update interval**: 5m
- **Preprocessing**:
  1. JSONPath: `$.count`
  2. Change per second

**Örnek 2: DC Activity**

- **Name**: AD: Domain Controller Activity
- **Key**: `ad.logon[dc_activity,12]`
- **Type of information**: Text
- **Preprocessing**: JSONPath: `$.count`

**Örnek 3: Failed Logon Details**

- **Name**: AD: Failed Logon Details
- **Key**: `ad.logon[failure,1]`
- **Type of information**: Text
- **History storage period**: 7d
- **No preprocessing** (full JSON)

### Adım 3: Trigger'lar Oluşturun

**Yüksek Sayıda Başarısız Logon**

```
{DC01:ad.logon[failure,1].last()}>10
```

- **Name**: High number of failed logons
- **Severity**: Warning
- **Description**: More than 10 failed logons in the last hour

**Aynı Kullanıcı Çoklu Bilgisayar**

```
{DC01:ad.logon[multiple_computers,24].last()}>0
```

- **Name**: Users logged into multiple computers
- **Severity**: Information

### Adım 4: Graph'lar Oluşturun

1. **Configuration → Hosts → Graphs → Create graph**
2. **Name**: AD Logon Activity
3. Item'ları ekleyin:
   - `ad.logon[failure,24]`
   - `ad.logon[dc_activity,24]`
   - `ad.logon[user_activity,24]`

## İleri Düzey Konfigürasyon

### Low-Level Discovery (LLD)

JSON içindeki event detaylarını parse edip dinamik item'lar oluşturabilirsiniz:

```javascript
// Discovery rule
ad.logon[failure,24]

// Item prototype JSONPath
$.events[*].user
```

### Değer Mapping

Logon type'ları için value mapping oluşturun:

1. **Administration → General → Value mapping**
2. **Create value mapping**
   - Name: AD Logon Types
   - Mappings:
     - 2 → Interactive
     - 3 → Network
     - 10 → RemoteInteractive

### Makro Kullanımı

Host veya template level'da makrolar tanımlayın:

- `{$AD.LOGON.FAILURE.THRESHOLD}` = 10
- `{$AD.LOGON.HOURS}` = 24
- `{$AD.CACHE.EXPIRY}` = 300

Item key'de kullanın:
```
ad.logon[failure,{$AD.LOGON.HOURS}]
```

## Çoklu Sunucu Deployment

### Domain Controller Cluster

Her DC'de aynı konfigurasyon:

```powershell
# Tüm DC'lerde çalıştırılacak script
$DCs = @("DC01", "DC02", "DC03")

foreach ($DC in $DCs) {
    # Plugin'i kopyala
    Copy-Item ".\zabbix-agent2-plugin-adlogon.exe" `
        -Destination "\\$DC\C$\Program Files\Zabbix Agent 2\plugins\" -Force

    # Konfig'i kopyala
    Copy-Item ".\adlogon.conf" `
        -Destination "\\$DC\C$\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\" -Force

    # Servisi yeniden başlat
    Invoke-Command -ComputerName $DC -ScriptBlock {
        Restart-Service "Zabbix Agent 2"
    }
}
```

### Zabbix Template

Tüm DC'lere uygulanacak template oluşturun:

```xml
<!-- Template snippet -->
<template>
    <template>Template AD Logon Monitoring</template>
    <groups>
        <group>
            <name>Templates/Active Directory</name>
        </group>
    </groups>
    <items>
        <!-- Item tanımları -->
    </items>
    <triggers>
        <!-- Trigger tanımları -->
    </triggers>
</template>
```

## Performans Optimizasyonu

### Event Log Boyutu

Büyük event log'lar sorgu performansını etkileyebilir:

```powershell
# Event log boyutunu kontrol et
Get-WinEvent -ListLog Security | Select-Object LogName, FileSize, RecordCount

# Log boyutunu artır (gerekirse)
wevtutil sl Security /ms:1073741824  # 1 GB
```

### Cache Ayarları

Sık sorgulanan metrikler için cache'i etkinleştirin:

```conf
# 5 dakika cache
Plugins.ADLogon.CacheExpiry=300
```

### Query Timeout

Yavaş diskler için timeout'u artırın:

```conf
Plugins.ADLogon.Timeout=60
```

### Item Update Interval

Daha az kritik metrikler için interval'i artırın:

```
# 5 dakika yerine 15 dakika
ad.logon[user_activity,24]  →  Update interval: 15m
```

## Güvenlik Sertleştirma

### 1. TLS Encryption

Zabbix Agent 2'de TLS'i etkinleştirin:

```conf
# zabbix_agent2.conf
TLSConnect=cert
TLSAccept=cert
TLSCAFile=C:\Zabbix\ca.crt
TLSCertFile=C:\Zabbix\agent.crt
TLSKeyFile=C:\Zabbix\agent.key
```

### 2. Firewall Kuralları

```powershell
# Sadece Zabbix Server'dan gelen bağlantılara izin ver
New-NetFirewallRule -DisplayName "Zabbix Agent 2" `
    -Direction Inbound -LocalPort 10050 -Protocol TCP `
    -RemoteAddress "192.168.1.100" -Action Allow
```

### 3. Plugin Binary Güvenliği

```powershell
# Sadece SYSTEM ve Administrators erişimi
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" /inheritance:r
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" /grant "SYSTEM:(F)"
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" /grant "Administrators:(F)"
```

## Sorun Giderme

### Plugin Yüklenmiyor

**Problem**: Plugin listede görünmüyor

**Çözüm**:
```powershell
# Log'u kontrol et
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 50

# Plugin path'i doğrula
Test-Path "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe"

# Konfig syntax'ı kontrol et
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -T
```

### Permission Denied Hatası

**Problem**: "Access is denied" event log hatası

**Çözüm**:
```powershell
# Servis hesabını kontrol et
Get-Service "Zabbix Agent 2" | Select-Object Name, StartName

# Local System'e geç
sc.exe config "Zabbix Agent 2" obj= "LocalSystem"
Restart-Service "Zabbix Agent 2"
```

### Timeout Hataları

**Problem**: Plugin timeout veriyor

**Çözüm**:
```conf
# adlogon.conf
Plugins.ADLogon.Timeout=120  # 2 dakikaya çıkar
Plugins.ADLogon.MaxEvents=500  # Event sayısını azalt
```

### Event Döndürmüyor

**Problem**: Query event döndürmüyor

**Çözüm**:
```powershell
# Event log'da veri var mı kontrol et
Get-WinEvent -FilterHashtable @{LogName='Security';ID=4625} -MaxEvents 10

# Audit policy aktif mi kontrol et
auditpol /get /category:"Logon/Logoff"

# Debug mode'u aç
# adlogon.conf
Plugins.ADLogon.DebugMode=true
```

## Bakım ve Güncelleme

### Plugin Güncelleme

```powershell
# Servisi durdur
Stop-Service "Zabbix Agent 2"

# Eski binary'i yedekle
Copy-Item "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" `
    -Destination "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe.bak"

# Yeni binary'i kopyala
Copy-Item ".\zabbix-agent2-plugin-adlogon.exe" `
    -Destination "C:\Program Files\Zabbix Agent 2\plugins\" -Force

# Servisi başlat
Start-Service "Zabbix Agent 2"

# Test et
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t ad.logon[failure,1]
```

### Log Rotation

```powershell
# Event log arşivleme
wevtutil epl Security C:\EventLogs\Security-$(Get-Date -Format 'yyyyMMdd').evtx
wevtutil cl Security
```

## Destek ve Yardım

### Log Dosyaları

- Zabbix Agent: `C:\Program Files\Zabbix Agent 2\zabbix_agent2.log`
- Windows Event Log: Event Viewer → Security, System

### Diagnostic Komutlar

```powershell
# Plugin bilgisi
& "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" -v

# Zabbix Agent konfigürasyonu
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -T

# Plugin metrik testi
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t ad.logon[failure,1]
```

### Yararlı Kaynaklar

- [Zabbix Dokümantasyonu](https://www.zabbix.com/documentation/)
- [Windows Event Log Referansı](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/)
- [ADLogon GitHub](https://github.com/yourrepo/ad-logon-plugin)

## Checklis

- [ ] Zabbix Agent 2 kurulu ve çalışıyor
- [ ] Event Log audit politikaları etkin
- [ ] Plugin binary kopyalandı
- [ ] Konfigürasyon dosyası oluşturuldu
- [ ] Servis yeniden başlatıldı
- [ ] Plugin yüklendi (zabbix_agent2 -T)
- [ ] Test başarılı (zabbix_agent2 -t ad.logon[...])
- [ ] Zabbix Server'da host tanımlı
- [ ] Item'lar oluşturuldu
- [ ] Trigger'lar yapılandırıldı
- [ ] Veri geliyor (Latest data)

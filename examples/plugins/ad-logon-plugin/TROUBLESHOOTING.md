# ADLogon Plugin - Troubleshooting Guide

## ❌ Agent Servisi Başlamıyor

### Adım 1: Konfig Dosyasını Kontrol Et

```powershell
# DC01 üzerinde PowerShell'i Administrator olarak açın

# Konfig dosyasının varlığını kontrol et
Test-Path "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf"

# Konfig içeriğini görüntüle
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf"
```

### Adım 2: Agent Config Syntax'ını Test Et

```powershell
# Agent konfigürasyonunu test et
cd "C:\Program Files\Zabbix Agent 2"
.\zabbix_agent2.exe -t agent.ping
```

**HATA ALIRSANIZ:**
```
failed to parse configuration file
```
→ Konfig dosyasında syntax hatası var

### Adım 3: Plugin Path'ini Doğrula

```powershell
# Plugin dosyasının var olduğunu kontrol et
Test-Path "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe"

# Dosya boyutunu kontrol et (3-4 MB olmalı)
Get-Item "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" | Select-Object Length
```

### Adım 4: Agent Log'unu İncele

```powershell
# Son 50 satırı göster
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 50

# Hata mesajlarını filtrele
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 100 | Select-String "error|failed|cannot"
```

### Adım 5: Konfig Dosyasını Geçici Olarak Kaldır

```powershell
# Konfig dosyasını yedekle
Copy-Item "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" `
    -Destination "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf.bak"

# Geçici olarak kaldır
Remove-Item "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf"

# Agent'ı başlat
Start-Service "Zabbix Agent 2"

# Çalıştı mı kontrol et
Get-Service "Zabbix Agent 2"
```

**EĞER ÇALIŞIRSA:**
→ Konfig dosyasında sorun var

**EĞER YINE ÇALIŞMAZSA:**
→ Başka bir konfig dosyasında sorun var

## 🔧 Çözümler

### Çözüm 1: Minimal Konfig Kullan

```powershell
# Minimal konfig dosyasını oluştur
@"
# ADLogon Plugin - Minimal Configuration
Plugins.ADLogon.System.Path=C:/Program Files/Zabbix Agent 2/plugins/zabbix-agent2-plugin-adlogon.exe
"@ | Out-File -FilePath "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" -Encoding ASCII

# Agent'ı yeniden başlat
Restart-Service "Zabbix Agent 2"

# Durumu kontrol et
Get-Service "Zabbix Agent 2"
```

### Çözüm 2: Path'i Double Backslash ile Dene

```powershell
# Double backslash versiyonu
@"
Plugins.ADLogon.System.Path=C:\\Program Files\\Zabbix Agent 2\\plugins\\zabbix-agent2-plugin-adlogon.exe
"@ | Out-File -FilePath "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" -Encoding ASCII

Restart-Service "Zabbix Agent 2"
```

### Çözüm 3: Tüm Konfig Dosyalarını Kontrol Et

```powershell
# plugins.d dizinindeki tüm dosyaları listele
Get-ChildItem "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\"

# Her birini tek tek kontrol et
Get-ChildItem "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\*.conf" | ForEach-Object {
    Write-Host "`n=== $($_.Name) ===" -ForegroundColor Cyan
    Get-Content $_.FullName
}
```

### Çözüm 4: Event Viewer'ı Kontrol Et

```powershell
# Zabbix Agent ile ilgili event'leri göster
Get-EventLog -LogName Application -Source "Zabbix*" -Newest 20 | Format-List

# System log'da hata var mı kontrol et
Get-EventLog -LogName System -Newest 50 | Where-Object {$_.Source -like "*Zabbix*"}
```

## 🐛 Yaygın Hatalar ve Çözümleri

### Hata 1: "failed to load plugin"

**Sebep:** Plugin dosyası bulunamıyor

**Çözüm:**
```powershell
# Plugin path'ini doğrula
$pluginPath = "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe"
if (Test-Path $pluginPath) {
    Write-Host "Plugin bulundu" -ForegroundColor Green
} else {
    Write-Host "Plugin BULUNAMADI!" -ForegroundColor Red
    Write-Host "Plugin'i şuraya kopyalayın: $pluginPath"
}
```

### Hata 2: "invalid configuration"

**Sebep:** Konfig dosyasında syntax hatası

**Çözüm:**
```powershell
# UTF-8 BOM olmadan kaydet
$content = @"
Plugins.ADLogon.System.Path=C:/Program Files/Zabbix Agent 2/plugins/zabbix-agent2-plugin-adlogon.exe
Plugins.ADLogon.Timeout=30
"@

[System.IO.File]::WriteAllText(
    "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf",
    $content,
    [System.Text.UTF8Encoding]::new($false)  # BOM olmadan
)
```

### Hata 3: "Access is denied"

**Sebep:** İzin problemi

**Çözüm:**
```powershell
# Dosya izinlerini kontrol et
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe"

# Gerekirse izinleri düzelt
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" /grant "SYSTEM:(RX)"
icacls "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" /grant "Administrators:(RX)"
```

### Hata 4: Servis "Starting" durumunda kalıyor

**Sebep:** Plugin timeout veriyor

**Çözüm:**
```powershell
# Servisi durdurmaya zorla
Stop-Service "Zabbix Agent 2" -Force

# Process'i kontrol et
Get-Process zabbix* -ErrorAction SilentlyContinue | Stop-Process -Force

# Plugin'i test et (standalone)
& "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" --version

# Servisi başlat
Start-Service "Zabbix Agent 2"
```

## ✅ Doğru Kurulum Adımları

### Manuel Kurulum (Önerilen)

```powershell
# 1. Servisi durdur
Stop-Service "Zabbix Agent 2" -Force

# 2. Eski konfig'i sil (varsa)
Remove-Item "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" -ErrorAction SilentlyContinue

# 3. Plugin'i kopyala
Copy-Item "C:\Users\Ali\Documents\Projects\zabbix-master-agent\ad-logon-plugin\build\zabbix-agent2-plugin-adlogon.exe" `
    -Destination "C:\Program Files\Zabbix Agent 2\plugins\" -Force

# 4. Minimal konfig oluştur
@"
Plugins.ADLogon.System.Path=C:/Program Files/Zabbix Agent 2/plugins/zabbix-agent2-plugin-adlogon.exe
Plugins.ADLogon.Timeout=30
"@ | Out-File -FilePath "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" -Encoding ASCII -NoNewline

# 5. Agent config'i test et
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -t agent.ping

# 6. Servisi başlat
Start-Service "Zabbix Agent 2"

# 7. Durumu kontrol et
Start-Sleep 3
Get-Service "Zabbix Agent 2"

# 8. Log'u kontrol et
Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 20
```

## 🔍 Debug Modu

### Agent'ı Debug Mode'da Çalıştır

```powershell
# Servisi durdur
Stop-Service "Zabbix Agent 2"

# Debug mode'da foreground'da çalıştır
& "C:\Program Files\Zabbix Agent 2\zabbix_agent2.exe" -c "C:\Program Files\Zabbix Agent 2\zabbix_agent2.conf" -f
```

Çıktıda plugin yükleme mesajlarını göreceksiniz:
```
loaded plugin support: LogonMonitoring v1.0.0-beta1
starting plugin "ADLogon"
plugin "ADLogon" started successfully
```

**Ctrl+C ile durdurun**

## 📋 Checklist

- [ ] Plugin dosyası doğru yerde (plugins\ klasöründe)
- [ ] Konfig dosyası doğru yerde (plugins.d\ klasöründe)
- [ ] Path forward slash (/) veya double backslash (\\\\) ile yazılmış
- [ ] Konfig dosyası ASCII encoding ile kaydedilmiş
- [ ] Agent servisi durdurulup yeniden başlatılmış
- [ ] Log dosyasında hata yok
- [ ] Plugin yüklendi (zabbix_agent2 -T)
- [ ] Test item çalışıyor

## 🆘 Hala Çalışmıyor?

```powershell
# Tüm diagnostic bilgiyi topla
$output = @"
=== SYSTEM INFO ===
$(Get-ComputerInfo | Select-Object CsName, OsName, OsVersion)

=== SERVICE STATUS ===
$(Get-Service "Zabbix Agent 2" | Format-List)

=== PLUGIN FILE ===
$(Get-Item "C:\Program Files\Zabbix Agent 2\plugins\zabbix-agent2-plugin-adlogon.exe" -ErrorAction SilentlyContinue | Format-List)

=== CONFIG FILE ===
$(Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.d\plugins.d\adlogon.conf" -ErrorAction SilentlyContinue)

=== AGENT LOG (Last 50 lines) ===
$(Get-Content "C:\Program Files\Zabbix Agent 2\zabbix_agent2.log" -Tail 50 -ErrorAction SilentlyContinue)

=== EVENT LOG ===
$(Get-EventLog -LogName Application -Source "Zabbix*" -Newest 10 -ErrorAction SilentlyContinue | Format-List)
"@

# Dosyaya kaydet
$output | Out-File "C:\zabbix_debug.txt"
Write-Host "Debug bilgisi kaydedildi: C:\zabbix_debug.txt"
```

Bu dosyayı support'a gönderin.

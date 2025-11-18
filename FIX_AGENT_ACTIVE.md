# Zabbix Agent Active Mode Sorunu - Çözüm

## Sorun
DESKTOP-JK5G34L makinesindeki Zabbix Agent, active modda veri göndermiyor.

Template: **"Windows by Zabbix agent active"** kullanılıyor
Item Type: **7 (Zabbix agent active)**

Master item "Get filesystems" hiç veri almamış!

## Çözüm Adımları

### 1. Zabbix Agent Durumunu Kontrol Edin

Windows makinesinde:
```cmd
# Zabbix Agent servisini kontrol edin
sc query "Zabbix Agent"

# Zabbix Agent loglarını kontrol edin
type "C:\Program Files\Zabbix Agent\zabbix_agentd.log"
```

### 2. Zabbix Agent Konfigürasyonunu Kontrol Edin

`C:\Program Files\Zabbix Agent\zabbix_agentd.conf` dosyasını açın:

```ini
# Active checks için Server parametresi doğru olmalı
Server=192.168.213.141
ServerActive=192.168.213.141

# Hostname doğru olmalı
Hostname=DESKTOP-JK5G34L

# Active checks aktif olmalı
RefreshActiveChecks=120
```

### 3. Zabbix Agent'ı Yeniden Başlatın

```cmd
net stop "Zabbix Agent"
net start "Zabbix Agent"
```

### 4. Firewall Kontrolü

Zabbix Server'dan agent'a 10050 portu açık olmalı:
```cmd
netsh advfirewall firewall show rule name="Zabbix Agent"
```

### 5. Host Konfigürasyonu Kontrol Edin

Zabbix UI'de:
1. **Configuration → Hosts**
2. **DESKTOP-JK5G34L** host'unu bulun
3. **Interfaces** sekmesini kontrol edin
4. Interface type **"Agent"** olmalı
5. IP: 192.168.213.xxx (doğru IP)
6. Port: 10050

### 6. Template Kontrolü

Host'a doğru template atanmış mı:
- ✅ **"Windows by Zabbix agent active"**
- ❌ "Windows by Zabbix agent" (passive mode - yanlış!)

## Alternatif Çözüm: Passive Mode'a Geçiş

Eğer active mode çalışmıyorsa:

1. Template'i değiştirin:
   - **"Windows by Zabbix agent active"** → **"Windows by Zabbix agent"**

2. Agent config'i passive mode için ayarlayın:
   ```ini
   Server=192.168.213.141
   # ServerActive= (yorum satırı yap)
   Hostname=DESKTOP-JK5G34L
   ```

3. Agent'ı yeniden başlatın

## Hızlı Test

Agent çalışıyor mu test edin:
```bash
# Zabbix Server'dan
zabbix_get -s 192.168.213.xxx -k agent.ping
```

Sonuç: `1` dönerse agent çalışıyor demektir.

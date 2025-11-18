# Network Neighbor Discovery - CDP & LLDP

Bu proje, Zabbix üzerinden SNMP cihazlarındaki komşuluk ilişkilerini (CDP ve LLDP) keşfetmek ve görselleştirmek için geliştirilmiştir.

## Özellikler

- **CDP (Cisco Discovery Protocol)** komşuluk keşfi
- **LLDP (Link Layer Discovery Protocol)** komşuluk keşfi
- Otomatik Low-Level Discovery (LLD) yapılandırması
- Network topology görselleştirmesi
- Real-time komşuluk bilgileri

## Kurulum ve Kullanım

### 1. Ön Gereksinimler

```bash
# Python bağımlılıklarının yüklendiğinden emin olun
pip install python-dotenv zabbix-utils
```

### 2. Ortam Değişkenleri

`.env` dosyasında Zabbix bağlantı bilgilerinizin olduğundan emin olun:

```
ZABBIX_API_URL=http://your-zabbix-server/api_jsonrpc.php
ZABBIX_USERNAME=Admin
ZABBIX_PASSWORD=your-password
```

### 3. Network Discovery Yapılandırması

Komşuluk keşfi için discovery rule'larını ve item prototype'larını oluşturun:

```bash
python configure_network_discovery.py
```

Bu script:
- CDP Discovery Rule oluşturur
- LLDP Discovery Rule oluşturur
- Her protocol için item prototype'ları ekler
- Tüm SNMP cihazlarına (CORE-SWITCH-01, EDGE-ROUTER-01, PERIMETER-FW-01) uygular

### 4. Discovery'yi Manuel Çalıştırma

Discovery rule'larını hemen çalıştırmak için:

```bash
python execute_network_discovery.py
```

Bu script discovery'yi tetikler ve arka planda çalışmasını sağlar.

### 5. Komşuluk Bilgilerini Görüntüleme

Keşfedilen komşulukları ve network topology'yi görüntülemek için:

```bash
python view_network_neighbors.py
```

Bu script:
- Tüm CDP komşulukları gösterir
- Tüm LLDP komşulukları gösterir
- ASCII formatında network topology haritası oluşturur

## CDP Bilgileri

Her CDP komşusu için aşağıdaki bilgiler toplanır:

- **Device ID**: Komşu cihazın adı
- **Platform**: Cihaz platformu (örn: Cisco IOS)
- **Remote Port**: Bağlı olunan uzak port
- **IP Address**: Komşu cihazın IP adresi

## LLDP Bilgileri

Her LLDP komşusu için aşağıdaki bilgiler toplanır:

- **System Name**: Komşu sistemin adı
- **Remote Port ID**: Uzak port ID'si
- **Chassis ID**: Cihazın chassis ID'si
- **Remote Port Description**: Port açıklaması

## Discovery OID'leri

### CDP OID'leri
```
Device ID:    1.3.6.1.4.1.9.9.23.1.2.1.1.4
Device Port:  1.3.6.1.4.1.9.9.23.1.2.1.1.5
Platform:     1.3.6.1.4.1.9.9.23.1.2.1.1.6
IP Address:   1.3.6.1.4.1.9.9.23.1.2.1.1.8
```

### LLDP OID'leri
```
System Name:       1.0.8802.1.1.2.1.4.1.1.7
Remote Port ID:    1.0.8802.1.1.2.1.4.1.1.9
Chassis ID:        1.0.8802.1.1.2.1.4.1.1.4
Port Description:  1.0.8802.1.1.2.1.4.1.1.8
```

## Zabbix UI'da Görüntüleme

### Discovery Rule'ları Kontrol Etme
1. Zabbix UI'a giriş yapın
2. Configuration -> Hosts
3. İlgili host'u seçin (örn: CORE-SWITCH-01)
4. Discovery rules
5. "CDP Neighbor Discovery" ve "LLDP Neighbor Discovery" rule'larını göreceksiniz

### Discovery'yi Manuel Çalıştırma (UI)
1. Discovery rules sayfasında
2. İlgili rule'ın yanındaki "Execute now" düğmesine tıklayın

### Komşuluk Verilerini Görüntüleme
1. Monitoring -> Latest data
2. Host filtresi: İlgili cihazı seçin
3. Name filtresine "CDP" veya "LLDP" yazın
4. Apply
5. Keşfedilen tüm komşuluk bilgilerini göreceksiniz

### Network Map Oluşturma (Zabbix UI)
1. Monitoring -> Maps
2. "Create map" düğmesine tıklayın
3. Host'ları ve bağlantıları manuel olarak ekleyin
4. Komşuluk bilgilerini kullanarak topology'yi oluşturun

## Otomasyonlar

Discovery rule'ları varsayılan olarak **saatte bir** çalışır. Bu ayarı değiştirmek için:

1. Zabbix UI -> Configuration -> Hosts -> Discovery rules
2. İlgili rule'ı seçin
3. "Update interval" alanını istediğiniz değere ayarlayın (örn: 30m, 2h, 1d)

## Troubleshooting

### Discovery Çalışmıyor

1. SNMP bağlantısını kontrol edin:
```bash
python test_snmp_direct.py
```

2. Discovery rule'ların enabled olduğundan emin olun

3. Host'un SNMP interface'i olduğundan emin olun

### Komşuluk Bilgileri Gelmiyor

1. Cihazda CDP/LLDP'nin etkin olduğundan emin olun
2. SNMP OID'lerinin doğru olduğunu kontrol edin
3. Discovery'yi manuel çalıştırın ve birkaç dakika bekleyin
4. Zabbix server loglarını kontrol edin:
```bash
tail -f /var/log/zabbix/zabbix_server.log
```

### Item Prototype'ları Yok

Discovery rule'ları silin ve yeniden oluşturun:
```bash
python delete_discovery_rules.py
python configure_network_discovery.py
```

## Yardımcı Script'ler

| Script | Açıklama |
|--------|----------|
| `configure_network_discovery.py` | Discovery rule'larını ve item prototype'larını oluşturur |
| `execute_network_discovery.py` | Discovery'yi manuel olarak çalıştırır |
| `view_network_neighbors.py` | Komşuluk bilgilerini görüntüler ve topology haritası oluşturur |
| `delete_discovery_rules.py` | Tüm CDP/LLDP discovery rule'larını siler |

## Örnek Çıktı

```
┌─ CORE-SWITCH-01
│  ├─[CDP]─> EDGE-ROUTER-01 (Port: GigabitEthernet0/1)
│  ├─[CDP]─> PERIMETER-FW-01 (Port: FastEthernet0/1)
│  ├─[LLDP]─> EDGE-ROUTER-01 (Port: Gi0/1)
│
┌─ EDGE-ROUTER-01
│  ├─[CDP]─> CORE-SWITCH-01 (Port: GigabitEthernet1/1)
│  ├─[LLDP]─> CORE-SWITCH-01 (Port: Gi1/1)
│
┌─ PERIMETER-FW-01
│  ├─[CDP]─> CORE-SWITCH-01 (Port: GigabitEthernet0/24)
│
```

## Notlar

- Discovery rule'ları her host için ayrı ayrı oluşturulur
- CDP ve LLDP aynı anda çalışabilir
- Bazı cihazlar sadece CDP, bazıları sadece LLDP destekleyebilir
- Simülatör cihazlarında CDP/LLDP verisi manuel olarak yapılandırılmalıdır
- Gerçek cihazlarda CDP/LLDP otomatik olarak keşfedilir

## Lisans

Bu proje dahili kullanım içindir.

## İletişim

Sorularınız için lütfen proje yöneticisine ulaşın.

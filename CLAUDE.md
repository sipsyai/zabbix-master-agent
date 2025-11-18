# Proje Talimatları - Zabbix Master Agent

## Genel Kurallar

Bu projede aşağıdaki kurallara **her zaman** uyulmalıdır:

### 1. Zabbix Master Agent Kullanımı
- Tüm Zabbix işlemleri için **zabbix-master** agentı kullanılmalıdır
- Agent, Zabbix API işlemlerini otomatik olarak yönetir ve güvenli bir şekilde gerçekleştirir
- Doğrudan API çağrıları yerine zabbix-master agent üzerinden işlem yapılmalıdır

### 2. Ortam Değişkenleri (.env)
- Tüm Zabbix bağlantı bilgileri `.env` dosyasında tanımlıdır
- **ASLA** API bilgilerini kodda hardcode etmeyin
- Aşağıdaki ortam değişkenleri kullanılmalıdır:
  - `ZABBIX_API_URL`: Zabbix API endpoint adresi
  - `ZABBIX_SERVER`: Zabbix sunucu IP/hostname
  - `ZABBIX_USERNAME`: Zabbix kullanıcı adı
  - `ZABBIX_PASSWORD`: Zabbix şifresi
  - `ZABBIX_PORT`: Zabbix sunucu portu
  - `ZABBIX_USE_SSL`: SSL kullanımı (true/false)
  - `ZABBIX_TIMEOUT`: API timeout süresi (saniye)

### 3. Güvenlik
- `.env` dosyası **GİZLİ BİLGİ** içerir
- `.env` dosyası asla version control'e (git) eklenmemelidir
- `.gitignore` dosyasında `.env` olduğundan emin olun

### 4. Agent Çağrıları
- Zabbix işlemleri için `zabbix-master` agentını çağırırken, agent otomatik olarak `.env` dosyasındaki bilgileri kullanacaktır
- Agent, kimlik doğrulama, oturum yönetimi ve API çağrılarını otomatik olarak yönetir

## Örnek Kullanım

```bash
# Zabbix master agentını çağırma
# Agent otomatik olarak .env dosyasındaki bilgileri kullanır
```

## Önemli Notlar

- Kod yazarken her zaman zabbix-master agentını kullanın
- Manuel API çağrıları yapmayın
- Tüm konfigürasyonlar .env üzerinden yönetilir
- Güvenlik ve kimlik doğrulama agent tarafından yönetilir

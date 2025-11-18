# ADLogon Plugin - Build Guide

Bu rehber, ADLogon plugin'ini Windows üzerinde nasıl derleyeceğinizi adım adım gösterir.

## Ön Gereksinimler

### 1. Go Kurulumu

Plugin'i derlemek için Go 1.23.0 veya üzeri gereklidir.

#### Go'yu İndirme ve Kurma

1. Go'nun resmi web sitesinden Windows installer'ı indirin:
   - [https://go.dev/dl/](https://go.dev/dl/)
   - `go1.23.x.windows-amd64.msi` dosyasını indirin

2. İndirdiğiniz MSI dosyasını çalıştırın ve kurulum sihirbazını takip edin
   - Varsayılan kurulum dizini: `C:\Program Files\Go`

3. Kurulumu doğrulayın:
   ```powershell
   go version
   ```
   Çıktı: `go version go1.23.x windows/amd64`

#### Go PATH Ayarları

Kurulum otomatik olarak PATH'e eklenmezse:

1. Sistem Değişkenlerini açın:
   - Windows tuşu + "ortam değişkenlerini düzenle" yazın
   - "Sistem ortam değişkenlerini düzenle"yi seçin

2. "Ortam Değişkenleri" butonuna tıklayın

3. "Path" değişkenini bulun ve düzenleyin

4. Şu yolları ekleyin:
   - `C:\Program Files\Go\bin`
   - `%USERPROFILE%\go\bin` (Go modülleri için)

5. Yeni bir PowerShell penceresi açın ve test edin:
   ```powershell
   go version
   ```

## Build Adımları

### Adım 1: Proje Dizinine Gidin

```powershell
cd C:\Users\Ali\Documents\Projects\zabbix-master-agent\ad-logon-plugin
```

### Adım 2: Go Bağımlılıklarını İndirin

```powershell
go mod download
go mod tidy
```

Bu komut şu bağımlılıkları indirecek:
- `golang.zabbix.com/sdk` - Zabbix Agent 2 SDK
- `golang.org/x/sys` - Windows sistem API'leri
- Diğer dolaylı bağımlılıklar

### Adım 3: Plugin'i Derleyin

#### Basit Build:
```powershell
go build -o build\zabbix-agent2-plugin-adlogon.exe .
```

#### Optimized Build (Makefile ile):
```powershell
# Make kullanarak (MinGW/MSYS2 gerektirir)
make build

# Veya direkt PowerShell ile:
mkdir -Force build
go build -trimpath -ldflags "-s -w" -o build\zabbix-agent2-plugin-adlogon.exe .
```

#### Build Parametreleri Açıklaması:
- `-trimpath`: Kaynak kod yollarını binary'den kaldırır (güvenlik)
- `-ldflags "-s -w"`: Debug bilgilerini kaldırır (dosya boyutu küçültme)
  - `-s`: Sembol tablosunu kaldır
  - `-w`: DWARF debug bilgilerini kaldır

### Adım 4: Build'i Doğrulayın

```powershell
# Binary'nin oluşturulduğunu kontrol edin
dir build\zabbix-agent2-plugin-adlogon.exe

# Plugin versiyonunu kontrol edin
.\build\zabbix-agent2-plugin-adlogon.exe -v
```

Beklenen çıktı:
```
zabbix-agent2-plugin-adlogon.exe version 1.0.0-beta1
```

## Build Sorun Giderme

### Go Komutu Bulunamıyor

Hata: `go: command not found` veya `'go' is not recognized`

Çözüm:
1. Go'nun doğru kurulduğunu kontrol edin:
   ```powershell
   where.exe go
   ```

2. PATH'i kontrol edin:
   ```powershell
   $env:Path -split ';' | Select-String "Go"
   ```

3. PowerShell'i yeniden başlatın veya PATH'i manuel ekleyin:
   ```powershell
   $env:Path += ";C:\Program Files\Go\bin"
   ```

### Bağımlılık İndirme Hataları

Hata: `go: downloading golang.zabbix.com/sdk failed`

Çözüm:
1. İnternet bağlantınızı kontrol edin
2. Proxy ayarlarını yapılandırın (gerekiyorsa):
   ```powershell
   $env:HTTP_PROXY = "http://proxy.example.com:8080"
   $env:HTTPS_PROXY = "http://proxy.example.com:8080"
   ```

3. Go modül cache'ini temizleyin:
   ```powershell
   go clean -modcache
   ```

### Build Hataları

Hata: `undefined: eventlog.Event` veya benzer

Çözüm:
1. Tüm dosyaların doğru yerde olduğunu kontrol edin
2. Go modüllerini yeniden indirin:
   ```powershell
   go mod tidy
   go mod download
   ```

## Alternatif Build Yöntemleri

### Cross-Compilation (Linux/Mac'ten Windows için)

Linux veya Mac'ten Windows binary'si oluşturmak için:

```bash
GOOS=windows GOARCH=amd64 go build -o zabbix-agent2-plugin-adlogon.exe .
```

### Docker ile Build

```dockerfile
FROM golang:1.23-windowsservercore

WORKDIR /build
COPY . .

RUN go mod download
RUN go build -o zabbix-agent2-plugin-adlogon.exe .
```

```powershell
docker build -t adlogon-builder .
docker run --rm -v ${PWD}:/out adlogon-builder cmd /c "copy zabbix-agent2-plugin-adlogon.exe \out\"
```

## Test ve Validasyon

### Unit Testleri Çalıştırma

```powershell
# Tüm testleri çalıştır
go test ./...

# Verbose output ile
go test -v ./...

# Coverage raporu ile
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

### Plugin Testi

Plugin'i Zabbix Agent olmadan test edemezsiniz, ancak şu kontrolleri yapabilirsiniz:

1. Binary'nin çalıştığını doğrulayın:
   ```powershell
   .\build\zabbix-agent2-plugin-adlogon.exe -h
   ```

2. Version bilgisini kontrol edin:
   ```powershell
   .\build\zabbix-agent2-plugin-adlogon.exe -v
   ```

## Optimizasyon ve İleri Düzey

### Daha Küçük Binary Boyutu

```powershell
# UPX ile sıkıştırma (isteğe bağlı)
# UPX: https://upx.github.io/
upx --best --lzma build\zabbix-agent2-plugin-adlogon.exe
```

### Build Bilgilerini Binary'e Ekleme

```powershell
$VERSION = "1.0.0-beta1"
$BUILD_TIME = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$GIT_COMMIT = git rev-parse --short HEAD

go build -ldflags "-s -w -X main.version=$VERSION -X main.buildTime=$BUILD_TIME -X main.gitCommit=$GIT_COMMIT" -o build\zabbix-agent2-plugin-adlogon.exe .
```

## Dağıtım Paketi Oluşturma

```powershell
# Dağıtım dizinini oluştur
mkdir -Force dist\adlogon-plugin-1.0.0-beta1

# Dosyaları kopyala
copy build\zabbix-agent2-plugin-adlogon.exe dist\adlogon-plugin-1.0.0-beta1\
copy adlogon.conf dist\adlogon-plugin-1.0.0-beta1\
copy README.md dist\adlogon-plugin-1.0.0-beta1\
copy LICENSE dist\adlogon-plugin-1.0.0-beta1\

# ZIP oluştur
Compress-Archive -Path dist\adlogon-plugin-1.0.0-beta1\* -DestinationPath dist\adlogon-plugin-1.0.0-beta1.zip
```

## Sorun Bildirme

Build ile ilgili sorunlar için:
1. Go versiyonunuzu belirtin (`go version`)
2. Windows versiyonunuzu belirtin
3. Tam hata mesajını ekleyin
4. Build komutunu paylaşın

## Kaynaklar

- [Go Dokümantasyonu](https://go.dev/doc/)
- [Zabbix Agent 2 SDK](https://git.zabbix.com/projects/ZBX/repos/golang-sdk/)
- [Windows Go Build Rehberi](https://go.dev/wiki/WindowsBuild)

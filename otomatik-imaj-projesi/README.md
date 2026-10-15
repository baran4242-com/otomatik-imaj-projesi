# Otomatik Docker İmajı Projesi

Bu proje, `main` dalına her push yapıldığında GitHub Actions ile Docker imajı oluşturur ve GHCR'ye gönderir. İmaj etiketi commit SHA değeridir.

## Dosyalar
- `app.py`: Küçük HTTP servisi; `/` ve `/live` adreslerinde JSON döndürür.
- `Dockerfile`: İmajın nasıl oluşturulacağını anlatır.
- `.github/workflows/docker-build.yml`: Otomatik derleme ve GHCR'ye gönderme adımları.
- `.dockerignore`: Gereksiz/gizli dosyaların derleme bağlamına girmesini önler.

## GitHub'da çalıştırma
1. GitHub'da yeni bir repository oluştur.
2. Bu klasördeki dosyaları ve `.github/workflows/docker-build.yml` dosyasını yükle.
3. Repository > Settings > Actions > General bölümünde workflow izinleri varsayılan ayarda kalabilir; workflow kendi `packages: write` iznini ister.
4. `main` dalına push/commit yap.
5. Actions sekmesinden `Build and publish Docker image` çalışmasının yeşil tikle bittiğini kontrol et.
6. GitHub profilindeki Packages bölümünden GHCR paketini kontrol et.

## İki sürümü göstermek
1. İlk commit'in SHA'sını ve Actions çıktısındaki `Registry digest` ile `Image ID/config digest` değerlerini not et.
2. `app.py` dosyasındaki mesajı değiştirip ikinci commit'i oluştur.
3. İkinci Actions çalışması bitince ikinci commit SHA'sını ve kimlikleri not et.
4. İki commit'in SHA etiketlerini karşılaştır. Kod değiştiği için yeni sürüm farklı bir commit etiketiyle yayımlanır.

## Katman önbelleği
Dockerfile önce `requirements.txt` dosyasını kopyalar ve bağımlılıkları kurar; sonra `app.py` dosyasını kopyalar. Yalnızca `app.py` değişirse bağımlılık kurulum katmanı önbellekten kullanılabilir. `requirements.txt` değişirse bağımlılık kurulum adımı tekrar çalışır.

## Yerel çalıştırma (isteğe bağlı)
Docker kurulu bilgisayarda:
```bash
docker build -t otomatik-imaj:deneme .
docker run --rm -p 8000:8000 otomatik-imaj:deneme
```
Tarayıcıda `http://localhost:8000/live` adresini aç.

# Proje 2 — Toprak Nemi ve Otomatik Sulama

## 🎯 Projenin Amacı
Kapasitif toprak nem sensörü ve röle ile sulama pompasını kontrol etmek; arayüzden manuel müdahale ve eşik ayarı yapmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| Kapasitif toprak nem sensörü | 1 | ≈ 41 TL+ (teyit edilmeli) |
| 1 kanal 5 V röle modülü | 1 | ≈ 75–98 TL |
| Mini dalgıç pompa (5–12 V) | 1 | teyit edilmeli |
| Silikon hortum + klemens | 1 | ≈ 50 TL |

## 🌐 Veri Akışı ve Mimari
Pico nem sensörünü okur, /data ile yüzde verir; /pompa?d=1 adresi röleyi çeker, pompa çalışır. Arayüz eşik altına inince uyarır, manuel anahtarla pompayı açar.

## 🛠️ Nasıl Çalıştırılır?

### 1. Raspberry Pi Pico W (Donanım Katmanı)
1. Pico W cihazınızı USB ile bilgisayara bağlayın ve Thonny IDE'yi açın.
2. `main_pico.py` dosyasındaki `SSID` ve `SIFRE` değişkenlerini kendi kablosuz ağınıza göre düzenleyin.
3. Kodu Pico içerisine `main.py` adıyla kaydedin ve çalıştırın.
4. Thonny konsolunda görünen IP adresini (Örn: `192.168.1.50`) not edin.

### 2. Bilgisayar / Sunucu (NiceGUI Web Arayüzü)
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install nicegui requests
   ```
2. `app_nicegui.py` dosyasındaki `PICO = "http://<pico-ip>:8080"` adresini yukarıdaki IP ile güncelleyin.
3. Donanım bağlı değilse `SIM = True` bırakarak simülasyon verileriyle test edebilirsiniz. Gerçek cihaz için `SIM = False` yapın.
4. Terminalden uygulamayı başlatın:
   ```bash
   python app_nicegui.py
   ```
5. Tarayıcınızda otomatik olarak açılan `http://localhost:8080` adresinden kontrol panelini kullanın.

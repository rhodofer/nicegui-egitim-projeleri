# Proje 1 — Sıcaklık-Nem Paneli (DHT22)

## 🎯 Projenin Amacı
DHT22 sensöründen sıcaklık ve nem okuyup tarayıcıda canlı gösteren ilk paneli kurmak; NiceGUI ile Pico arasındaki veri akışını öğrenmek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| DHT22 sıcaklık-nem sensörü | 1 | ≈ 88–106 TL (Robotistan) |
| 4,7 kΩ direnç (DHT22 pull-up) | 1 | ≈ 1 TL |
| Jumper kablo seti | 1 | ≈ 30–60 TL |

## 🌐 Veri Akışı ve Mimari
Pico W ağa bağlanır ve http://&lt;pico-ip&gt;:8080/data adresinden JSON yayınlar. NiceGUI arayüzü 2 saniyede bir bu adresi okur, değerleri etiketlere yazar ve grafiğe ekler.

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

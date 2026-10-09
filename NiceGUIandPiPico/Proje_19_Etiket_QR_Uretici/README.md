# Proje 19 — Etiket / QR Üretici

## 🎯 Projenin Amacı
Formda malzeme etiketi tasarlamak, QR kodunu anında üretmek ve Pico&#8217;ya bağlı termal yazıcıdan bastırmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| Termal yazıcı (58 mm, TTL/UART) | 1 | ≈ 500–1500 TL (teyit edilmeli) |
| Termal kağıt rulo | 1 | ≈ 50 TL |
| 5–9 V yazıcı beslemesi | 1 | ≈ 150 TL |

## 🌐 Veri Akışı ve Mimari
Arayüz formdan etiket metnini ve QR kodunu üretir (qrcode kütüphanesi, tarayıcıda base64 PNG); &#8216;yazdır&#8217; komutu metni /yaz yoluna gönderir, Pico UART&#8217;tan yazıcıya ESC/POS komutları yazar.

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

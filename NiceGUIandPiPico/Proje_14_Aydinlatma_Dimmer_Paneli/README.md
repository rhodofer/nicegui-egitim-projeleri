# Proje 14 — Aydınlatma Dimmer Paneli

## 🎯 Projenin Amacı
PWM ile bir LED/aydınlatma hattının parlaklığını arayüzden ayarlamak ve saat bazlı program kurmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| MOSFET (IRFZ44N) + 220 Ω direnç | 1 | ≈ 15–20 TL |
| LED şerit veya güç LED&#8217;i | 1 | ≈ 100–300 TL |
| 12 V adaptör ve sigorta | 1 | ≈ 150 TL |

## 🌐 Veri Akışı ve Mimari
Arayüz kaydırıcı ve zaman programı oluşturur; /duty?d=.. komutu Pico&#8217;da PWM görev oranını değiştirir, sayaç değeri geri okunur.

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

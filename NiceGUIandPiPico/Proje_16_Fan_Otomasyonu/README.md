# Proje 16 — Fan Otomasyonu (Sıcaklık Kontrollü)

## 🎯 Projenin Amacı
Sıcaklık eşiğine göre fanı otomatik çalıştırmak, gerektiğinde manuel kontrol sağlamak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| DS18B20 sıcaklık sensörü | 1 | ≈ 40–47 TL |
| 1 kanal röle modülü | 1 | ≈ 75–98 TL |
| 12 V fan | 1 | ≈ 100–200 TL (teyit edilmeli) |

## 🌐 Veri Akışı ve Mimari
Pico sıcaklığı okur, otomatik moddaysa röleyi eşiğe göre sürer ve durumu yayınlar; arayüz mod seçimi ve manuel anahtar sunar.

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

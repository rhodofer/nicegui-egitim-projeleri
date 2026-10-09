# Proje 12 — Motor Kontrol Paneli (L298N PWM)

## 🎯 Projenin Amacı
DC motoru PWM ile hız ve yön kontrolü yapmak; arayüzden kaydırıcı, joystick ve acil durdurma kullanmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| H köprü / motor sürücü kartı (L298N veya MOSFET devresi) | 1 | ≈ 100–200 TL |
| DC motor 6–12 V | 1 | ≈ 100–250 TL |
| Ayrı motor beslemesi + kondansatör | 1 | ≈ 100 TL |

## 🌐 Veri Akışı ve Mimari
Arayüz kaydırıcı ve joystick olaylarını /pwm?d=..&yon=.. isteğine çevirir; Pico PWM görev oranını ve yön pinlerini sürer.

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

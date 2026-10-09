# Proje 11 — Akü Test Tezgahı

## 🎯 Projenin Amacı
Kontrollü deşarj testi yapmak: gerilim ve akımı kaydedip deşarj eğrisini ve toplam enerjiyi çıkarmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| 1 kanal röle modülü (yük anahtarı) | 1 | ≈ 75–98 TL |
| Yük direnci (ör. 12 V 10 W ampul veya 5 Ω 50 W) | 1 | ≈ 50–150 TL |
| ACS712 akım sensörü | 1 | ≈ 100–200 TL (teyit edilmeli) |

## 🌐 Veri Akışı ve Mimari
Arayüzden test başlatılır (/test?b=1) → Pico röleyi çekip yükü devreye alır, gerilim/akım/süre yayınlar; arayüz deşarj eğrisini çizer.

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

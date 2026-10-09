# Proje 15 — Sulama Zamanlayıcı

## 🎯 Projenin Amacı
Saate göre sulama programı kurmak; cihaz saatini ve programı arayüzden yönetmek.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| 1 kanal röle modülü | 1 | ≈ 75–98 TL |
| Solenoid vana veya pompa | 1 | teyit edilmeli |
| RTC modülü (DS3231, opsiyonel) | 1 | ≈ 100–150 TL (teyit edilmeli) |

## 🌐 Veri Akışı ve Mimari
Arayüz program ekler (/ekle?saat=07:30&amp;sure=120), &#8216;şimdi sula&#8217; komutu gönderir; Pico program listesini ve cihaz saatini yayınlar.

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

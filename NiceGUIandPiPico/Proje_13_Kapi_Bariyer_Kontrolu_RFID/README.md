# Proje 13 — Kapı / Bariyer Kontrolü (RC522 RFID)

## 🎯 Projenin Amacı
Yetkili RFID kart ile kapı/bariyer açmak, geçiş kayıtlarını tutmak ve arayüzden uzaktan açmak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| RC522 RFID okuyucu modülü + kart/etiket | 1 | ≈ 54–76 TL (Robotistan) |
| SG90 servo motor (bariyer) | 1 | ≈ 44–72 TL |
| 5 V adaptör (servo beslemesi) | 1 | ≈ 100 TL |

## 🌐 Veri Akışı ve Mimari
Pico kart okunduğunda UID&#8217;yi yetkili listeyle karşılaştırır, servoyu döndürür ve durumu yayınlar; arayüz son kartı, sonucu ve geçiş tablosunu gösterir.

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

# Proje 9 — Ev Enerji Sayacı (SCT-013)

## 🎯 Projenin Amacı
Akım trafosu ile hattan çekilen akımı ölçüp anlık gücü ve kümülatif enerjiyi (kWh) hesaplamak.

## 🔌 Donanım ve Malzeme Listesi
| Malzeme | Adet | Yaklaşık fiyat / temin |
| --- | --- | --- |
| Raspberry Pi Pico W (veya Pico 2 W) | 1 | fiyat teyit edilmeli (Robotistan / Direnc.net) |
| SCT-013-030 akım trafosu (30 A) | 1 | Hepsiburada&#8217;da mevcut — fiyat teyit edilmeli |
| 33 Ω yük direnci + 10 kΩ/10 kΩ gerilim bölücü | 1 | ≈ 10 TL |
| Kondansatör 10 µF (filtre) | 1 | ≈ 5 TL |

## 🌐 Veri Akışı ve Mimari
Pico 200 örnek alıp RMS akımı hesaplar, şebeke gerilimi varsayımıyla gücü ve zamanla enerjiyi (kWh) biriktirir; arayüz anlık güç ve toplam enerji ile çubuk grafik gösterir.

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

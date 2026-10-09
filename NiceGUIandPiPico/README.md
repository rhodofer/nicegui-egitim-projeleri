# NiceGUI ve Raspberry Pi Pico W Entegre IoT Projeleri

Bu dizin, **Raspberry Pi Pico W** mikrodenetleyicisi ile modern **Python NiceGUI** web kütüphanesini entegre eden 19 farklı uçtan uca IoT ve otomasyon projesini içerir.

## 🚀 Genel Mimari
- **Mikrodenetleyici Katmanı (Pico W):** MicroPython ile çalışır. Sensör ve aktüatörleri sürer, yerel ağda hafif bir HTTP REST API (JSON) yayınlar.
- **Web Arayüz Katmanı (NiceGUI):** Bilgisayarda veya sunucuda çalışır. Pico'dan gelen verileri gerçek zamanlı çeker, modern reaktif arayüz bileşenleri (grafikler, sayaçlar, butonlar, anahtarlar) ile görselleştirir.
- **Simülasyon Modu (`SIM = True`):** Tüm NiceGUI kodları fiziksel donanım olmadan da doğrudan çalıştırılabilir.

## 📦 Kurulum
```bash
pip install nicegui requests
```

## 📋 Proje Kataloğu

| No | Proje Adı | Donanım / Sensörler | Proje Dizini |
|---|---|---|---|
| 01 | [Proje 1 — Sıcaklık-Nem Paneli (DHT22)](./Proje_01_Sicaklik_Nem_Paneli/) | `Paneli` | [`Proje_01_Sicaklik_Nem_Paneli`](./Proje_01_Sicaklik_Nem_Paneli/) |
| 02 | [Proje 2 — Toprak Nemi ve Otomatik Sulama](./Proje_02_Toprak_Nemi_Sulama/) | `Sulama` | [`Proje_02_Toprak_Nemi_Sulama`](./Proje_02_Toprak_Nemi_Sulama/) |
| 03 | [Proje 3 — Sera İklim Kontrolü](./Proje_03_Sera_Iklim_Kontrolu/) | `Kontrolu` | [`Proje_03_Sera_Iklim_Kontrolu`](./Proje_03_Sera_Iklim_Kontrolu/) |
| 04 | [Proje 4 — Hava İstasyonu (BME280)](./Proje_04_Hava_Istasyonu_BME280/) | `BME280` | [`Proje_04_Hava_Istasyonu_BME280`](./Proje_04_Hava_Istasyonu_BME280/) |
| 05 | [Proje 5 — Su Deposu Seviyesi (HC-SR04)](./Proje_05_Su_Deposu_Seviyesi/) | `Seviyesi` | [`Proje_05_Su_Deposu_Seviyesi`](./Proje_05_Su_Deposu_Seviyesi/) |
| 06 | [Proje 6 — Gürültü ve Işık Ölçer](./Proje_06_Gurultu_ve_Isik_Olcer/) | `Olcer` | [`Proje_06_Gurultu_ve_Isik_Olcer`](./Proje_06_Gurultu_ve_Isik_Olcer/) |
| 07 | [Proje 7 — Titreşim / Rulman İzleme](./Proje_07_Titresim_Rulman_Izleme/) | `Izleme` | [`Proje_07_Titresim_Rulman_Izleme`](./Proje_07_Titresim_Rulman_Izleme/) |
| 08 | [Proje 8 — Soğuk Zincir Sıcaklık Kaydı (DS18B20)](./Proje_08_Soguk_Zincir_Sicaklik_Kaydi/) | `Kaydi` | [`Proje_08_Soguk_Zincir_Sicaklik_Kaydi`](./Proje_08_Soguk_Zincir_Sicaklik_Kaydi/) |
| 09 | [Proje 9 — Ev Enerji Sayacı (SCT-013)](./Proje_09_Ev_Enerji_Sayaci_SCT013/) | `SCT013` | [`Proje_09_Ev_Enerji_Sayaci_SCT013`](./Proje_09_Ev_Enerji_Sayaci_SCT013/) |
| 10 | [Proje 10 — Solar Şarj İzleyici (INA219)](./Proje_10_Solar_Sarj_Izleyici/) | `Izleyici` | [`Proje_10_Solar_Sarj_Izleyici`](./Proje_10_Solar_Sarj_Izleyici/) |
| 11 | [Proje 11 — Akü Test Tezgahı](./Proje_11_Aku_Test_Tezgahi/) | `Tezgahi` | [`Proje_11_Aku_Test_Tezgahi`](./Proje_11_Aku_Test_Tezgahi/) |
| 12 | [Proje 12 — Motor Kontrol Paneli (L298N PWM)](./Proje_12_Motor_Kontrol_Paneli/) | `Paneli` | [`Proje_12_Motor_Kontrol_Paneli`](./Proje_12_Motor_Kontrol_Paneli/) |
| 13 | [Proje 13 — Kapı / Bariyer Kontrolü (RC522 RFID)](./Proje_13_Kapi_Bariyer_Kontrolu_RFID/) | `RFID` | [`Proje_13_Kapi_Bariyer_Kontrolu_RFID`](./Proje_13_Kapi_Bariyer_Kontrolu_RFID/) |
| 14 | [Proje 14 — Aydınlatma Dimmer Paneli](./Proje_14_Aydinlatma_Dimmer_Paneli/) | `Paneli` | [`Proje_14_Aydinlatma_Dimmer_Paneli`](./Proje_14_Aydinlatma_Dimmer_Paneli/) |
| 15 | [Proje 15 — Sulama Zamanlayıcı](./Proje_15_Sulama_Zamanlayici/) | `Zamanlayici` | [`Proje_15_Sulama_Zamanlayici`](./Proje_15_Sulama_Zamanlayici/) |
| 16 | [Proje 16 — Fan Otomasyonu (Sıcaklık Kontrollü)](./Proje_16_Fan_Otomasyonu/) | `Otomasyonu` | [`Proje_16_Fan_Otomasyonu`](./Proje_16_Fan_Otomasyonu/) |
| 17 | [Proje 17 — RFID Yoklama Sistemi](./Proje_17_RFID_Yoklama_Sistemi/) | `Sistemi` | [`Proje_17_RFID_Yoklama_Sistemi`](./Proje_17_RFID_Yoklama_Sistemi/) |
| 18 | [Proje 18 — Envanter Paneli (Barkod + Ağırlık HX711)](./Proje_18_Envanter_Paneli_Barkod_Agirlik/) | `Agirlik` | [`Proje_18_Envanter_Paneli_Barkod_Agirlik`](./Proje_18_Envanter_Paneli_Barkod_Agirlik/) |
| 19 | [Proje 19 — Etiket / QR Üretici](./Proje_19_Etiket_QR_Uretici/) | `Uretici` | [`Proje_19_Etiket_QR_Uretici`](./Proje_19_Etiket_QR_Uretici/) |

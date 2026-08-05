# 🧠 AI Geliştirme Yol Haritası — Cepte Veterinerlik

Bu belge, projenin yapay zeka (AI) tarafının vizyonunu, mevcut durumunu ve
planlanan geliştirmelerini özetler. Amaç, "AI Destekli Cepte Veterinerlik"
uygulamasını basit bir kayıt sisteminden, çiftçinin gerçek bir dijital
danışmanına dönüştürmektir.

---

## 🎯 Vizyon

Çiftçinin cebinde; sürüsünü sayabilen, verimini tahmin eden, anormal durumları
yakalayan, sorularını yanıtlayan ve havaya/zamana göre uyaran akıllı bir asistan.
Yapay zeka burada "gösteriş" için değil, çiftçinin gerçek kararlarını
kolaylaştırmak için kullanılır.

---

## ✅ Mevcut Durum (Tamamlanan AI Bileşenleri)

| Bileşen | Teknik | Durum |
|---|---|---|
| Sürü sayımı | YOLO (görüntü işleme) | ✅ Çalışıyor (hazır model) |
| Süt verimi tahmini | Regresyon (Linear/RF) | ✅ Çalışan model (R² 0.80) |
| Anomali tespiti | Isolation Forest | ✅ Model kaydedildi |
| Veteriner asistanı | RAG (embedding + LLM) | ✅ 24 konu, LLM ön kontrol |
| Kişiselleştirilmiş asistan | RAG + hayvan verisi | ✅ Hayvana özel cevap |
| Anomali + asistan zinciri | ML + RAG | ✅ Otomatik yorum |
| Konuşma hafızası | Bağlamlı sohbet | ✅ Takip sorularını hatırlıyor |
| Gerçek dökümandan bilgi tabanı | PDF + chunking + RAG | ✅ 66 sayfalık dökümandan cevap |
| Hava durumu danışmanı | API + kural + RAG | ✅ Canlı veri + tavsiye |
| Akıllı hatırlatmalar | Tarih tabanlı + öncelik rozeti | ✅ Çalışıyor |

Ayrıca değerli metodolojik bulgular üretildi: veri sızıntısı (data leakage)
kanıtlandı, iki veri seti karşılaştırıldı, model boyutu–kalite ilişkisi ve
model boyutu–bellek/ortam uyumu gözlemlendi.

---

## 🚀 Planlanan AI Geliştirmeleri — İlerleme Takibi

> **Durum:** Çekirdek AI geliştirmelerinin tamamı (1–4. adımlar) tamamlandı. ✅
> Asistan artık kişiselleştirilmiş, anomali tespitiyle zincirli, hafızalı ve
> gerçek dökümanlardan besleniyor. 5. adım (sayım fine-tune) kapsamlı bir çalışma
> gerektirdiği için backend sonrasına planlandı; projenin gidişatına göre
> yapılabilir veya bir tez uzantısı olarak bırakılabilir.

---

### ☑ Adım 1 — Asistanı Hayvan Verisiyle Birleştirme (Kişiselleştirme) ✅
Asistan, belirli bir hayvanın gerçek verilerine (verim, ağırlık, anomali durumu)
bakarak kişiselleştirilmiş cevap veriyor. Sorunlu ve sağlıklı hayvanlar için farklı
cevaplar üretildiği test edildi.

### ☑ Adım 2 — Anomali + Asistan Zinciri ✅
Isolation Forest ile sapan hayvanlar model tarafından tespit ediliyor; asistan her
biri için "neden sapıyor ve ne yapmalı" yorumu üretiyor. İki yapay zeka bileşeni
tek akışta birleşti.

### ☑ Adım 3 — Asistana Konuşma Hafızası ✅
Asistan bir sınıf yapısına taşındı; önceki soru-cevapları hatırlıyor. "Peki ne
yapmalıyım?" gibi bağlamlı takip soruları doğru yanıtlanıyor.

### ☑ Adım 4 — Gerçek Veteriner Dökümanlarından Bilgi Tabanı ✅
66 sayfalık gerçek bir veteriner dökümanı okundu (pypdf), temiz parçalara ayrıldı
(chunking), embedding'e çevrildi. Dil modeli seçimi optimize edilerek asistan
gerçek dökümandan akıcı cevaplar üretiyor.

### ⏸️ Adım 5 — Sürü Sayımı Modelini Fine-Tune Etme (opsiyonel / ertelendi)
**Hedef:** Hazır YOLO yerine, üst üste binen hayvanları daha iyi ayıran, kendi
verimizle eğitilmiş bir sayım modeli.
**Durum:** Kapsamlı bir çalışma (veri toplama + etiketleme + eğitim) gerektirdiği
için backend sonrasına planlandı. Projenin önceliklerine göre yapılabilir ya da bir
tez uzantısı olarak ileriye bırakılabilir.

---

## 🗺️ Genel Yol

```
[✅ 1. Kişiselleştirme] → [✅ 2. Anomali zinciri] → [✅ 3. Hafıza] → [✅ 4. Gerçek dökümanlar] → [⏸️ 5. Sayım fine-tune]
                                                                                                    (backend sonrası / opsiyonel)
```

Çekirdek yapay zeka geliştirmeleri tamamlandı. Sıradaki büyük aşama, kurulan tüm
bu bileşenleri gerçek bir uygulamada birleştirmek: **backend, veritabanı ve
arayüz.**

---

*Bu yol haritası, proje ilerledikçe güncellenecektir.*

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
| Hava durumu danışmanı | API + kural + RAG | ✅ Entegre çalışıyor |
| Akıllı hatırlatmalar | Tarih tabanlı + öncelik rozeti | ✅ Çalışıyor |

Ayrıca değerli metodolojik bulgular üretildi: veri sızıntısı (data leakage)
kanıtlandı, iki veri seti karşılaştırıldı, model boyutu–kalite ilişkisi
gözlemlendi.

---

## 🚀 Planlanan AI Geliştirmeleri — İlerleme Takibi

> **Durum işaretleri:** ☐ Yapılacak &nbsp;|&nbsp; 🔨 Üzerinde çalışılıyor &nbsp;|&nbsp; ☑ Tamamlandı
>
> 👉 **Şu an sıradaki adım: 1. Adım (Kişiselleştirme)**

---

### ☐ Adım 1 — Asistanı Hayvan Verisiyle Birleştirme (Kişiselleştirme) ⭐
**Hedef:** Asistan, belirli bir hayvanın gerçek verilerine (verim, ağırlık,
anomali durumu) bakarak kişiselleştirilmiş cevap versin.
**Örnek:** "TR-002 ineğim neden az süt veriyor?" → o ineğin kendi verisiyle yanıt.
**Yapılacaklar:**
- [ ] Hayvan kaydını (küpe no ile) asistana bağlam olarak verme
- [ ] Verim/anomali model sonuçlarını cevaba dahil etme
- [ ] Kişiselleştirilmiş yanıtı test etme

### ☐ Adım 2 — Anomali + Asistan Zinciri
**Hedef:** Anomali modeli bir hayvanı "sapan" işaretlediğinde, asistan nedenini
ve önerisini açıklasın.
**Yapılacaklar:**
- [ ] Anomali çıktısını asistana bağlam olarak verme
- [ ] "Neden sapıyor + ne yapmalı" yorumu ürettirme

### ☐ Adım 3 — Asistana Konuşma Hafızası
**Hedef:** Asistan önceki soruları hatırlasın, gerçek sohbet akışı kursun.
**Yapılacaklar:**
- [ ] Konuşma geçmişini modele bağlam olarak iletme
- [ ] Bağlamlı takip sorularını test etme ("az önceki buzağı...")

### ☐ Adım 4 — Gerçek Veteriner Dökümanlarından Bilgi Tabanı
**Hedef:** Elle yazılan 24 konu yerine, gerçek dökümanlardan (PDF) otomatik ve
geniş bir bilgi tabanı.
**Yapılacaklar:**
- [ ] Döküman toplama
- [ ] Parçalara ayırma (chunking) + embedding
- [ ] Yeni bilgi tabanıyla asistanı test etme

### ☐ Adım 5 — Sürü Sayımı Modelini Fine-Tune Etme
**Hedef:** Hazır YOLO yerine, üst üste binen hayvanları daha iyi ayıran, kendi
verimizle eğitilmiş bir sayım modeli.
**Yapılacaklar:**
- [ ] Hayvan fotoğrafı toplama
- [ ] Etiketleme
- [ ] YOLO fine-tune + karşılaştırma

---

## 🗺️ Genel Yol

```
[ŞU AN] →  1. Kişiselleştirme  →  2. Anomali zinciri  →  3. Hafıza  →  4. Gerçek dökümanlar  →  5. Sayım fine-tune
             (temel)               (devam)                (katman)      (bağımsız)               (uzun vadeli)
```

Her geliştirme, bir öncekinin üzerine değer katacak şekilde tasarlanmıştır.
Sıralama; teknik bağımlılık ve kazanç/emek dengesine göre belirlenmiştir.
Bir adım tamamlandıkça başlığındaki ☐ işareti ☑ ile güncellenir.

---

*Bu yol haritası, proje ilerledikçe güncellenecektir.*

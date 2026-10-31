# Diğer 6 Fikrin Doğrulaması

Tarih: 31 Ekim 2026 · Yöntem: Madeni para fikrine uygulanan adımların aynısı (gelir tahminleri, şikâyet madenciliği, fiyat).
Rakamlar Sensor Tower, AppGoblin, Adapty ve benzeri üçüncü taraf **tahminleridir**. App Store'a doğrudan erişim bu ortamda kapalıydı.

**Ölçüt (2. adım):** Ayda $10–50K kazanan 3–5 rakip varsa talep kanıtlanmış sayılır. Para kazanan hiç rakip yoksa
bu "boşluk" değil, **ödeme isteği olmadığının işareti** olabilir.

---

## Özet sıralama (madeni para dahil 7 fikir)

| Sıra | Fikir | Ödeyen rakip kanıtı | Şikâyet boşluğu | Model | Karar |
|---|---|---|---|---|---|
| 1 | **Madeni/kâğıt para + portföy** | Güçlü ($10K – $1M/ay arası 5+ rakip) | Net (fatura, güven, tanıma) | B2C abonelik | ✅ Geçti |
| 2 | **Havuz bakım esnafı için rota + fatura** | Güçlü (Skimmer ~$74M yatırım; Joist ~$1M/ay) | Net (havuz başı fiyat artışı, SMS ücreti, mobilde fatura yok) | B2B, aylık sabit ücret | ✅ Geçti |
| 3 | DEHB alt kitlesi | Orta (Structured $10K+, Tiimo; Finch $1–2.5M/ay) | Var (fiyat, deneme ücreti, hatalar) ama pazar kalabalık | B2C | 🟡 Şartlı |
| 4 | Helal yatırım / Müslüman niş | Orta (Zoya 400K kullanıcı, $120/yıl; namaz uygulaması $200K/yıl) | Zayıf (Zoya memnuniyeti 4.7–4.8) | B2C | 🟡 Şartlı |
| 5 | Menopoz takibi | Zayıf (en çok gelir getirenler klinik, ör. Midi; uygulamalar ücretsiz veya düşük) | Var (düzensiz döngü takibi) | B2C | 🟠 Zayıf |
| 6 | Bakım veren aile uygulaması | Çok zayıf (büyükler ücretsiz: CaringBridge, Lotsa, ianacare) | Var | B2C (ödeme isteği düşük) | ❌ Kaldı |
| 7 | Kedi/egzotik hayvan sağlık günlüğü | Çok zayıf (çoğu <$10K/ay, bazıları $7–22/ay) | Var (senkron, veri kilidi) | B2C | ❌ Kaldı |

---

## 2. Havuz bakım esnafı için rota + fatura uygulaması ✅

**Pazar**
- ABD'de **78.817 havuz temizlik işletmesi** var (2025, +%4,4). Sektör geliri yaklaşık **$8,8 milyar**. İşletme başına ortalama **1,3 çalışan**, yani pazar neredeyse tamamen tek kişilik esnaftan oluşuyor (IBISWorld).
- Lider Skimmer: 35.000'den fazla kullanıcı (yaklaşık 7.000 ödeyen hesap), $500M+ yıllık ödeme hacmi ve **$74M büyüme yatırımı** (Mainsail, 2024).
- Genel esnaf faturalama uygulaması Joist: iOS'ta yaklaşık **$700K/ay** + Android'de yaklaşık **$300K/ay** (Sensor Tower). Esnafın fatura uygulamasına para ödediği kanıtlanmış.

**En sık şikâyetler (Skimmer ve Joist)**
1. **Havuz başına fiyat sürekli arttı:** $0,50 → $1 → $2. Eski müşteriler daha ucuz pakete geçince özellik kaybetti.
2. **SMS başına ücret:** "Telefonumdan bedavaya atabileceğim mesaja para ödüyorum."
3. **Mobil uygulamada fatura bölümü yok.** Ayrıca sabit fiyat kataloğu yok ve raporlama zayıf.
4. **Joist:** Ücretsiz özellikler ücretli pakete taşındı, ödeme işlem ücretlerinden şikâyet var, kesintiler yaşanıyor, takvim/planlama yok.
5. **Destek yavaş**, özellikle kesinti sırasında.

**Konumlandırma:** "Havuz sayısından bağımsız **sabit $39/ay**." Rota, kimyasal ölçüm kaydı (pH, klor, LSI), fotoğraflı
servis raporunun müşteriye otomatik gitmesi ve mobilde fatura ile tahsilat tek uygulamada. SMS'ler kullanıcının kendi telefon numarasından gider.

**Fiyat karşılaştırması**
| | 50 havuz | 100 havuz |
|---|---|---|
| Skimmer başlangıç paketi ($1/havuz, min. $49) | $50/ay | $100/ay |
| Skimmer büyüme paketi ($2/havuz, min. $98) | $100/ay | $200/ay |
| **Bizim sabit fiyat** | **$39/ay** | **$39/ay** (ya da 75 havuz üstü için $59) |

**Gelir hesabı:** 1.000 müşteri × $39 = **$39K aylık tekrarlayan gelir (MRR)**. Bu, pazardaki işletmelerin yalnızca yaklaşık %1,3'ü.
B2B iş aracı olduğu için abonelik iptali, tüketici uygulamalarına göre çok daha düşük.

**Risk:** App Store'da arama ile keşfedilmek zor. Müşteriler doğrudan satışla bulunmalı: Facebook'taki havuz
servis grupları, r/pools, havuz malzeme bayileri. Skimmer bu pazarda tanınıyor ve fiyatını düşürerek karşılık verebilir.
İlk yıl daha yavaş büyüme beklenmeli.

**3. adım:** `landing-havuz/index.html` sayfası ve aşağıdaki gönderi taslakları hazır.

---

## 3. DEHB alt kitlesi 🟡

- **Gelir:** Structured $10K+/ay (AppGoblin, 322K aylık aktif kullanıcı). Tiimo yaklaşık $200K/ay (ABD iOS tahmini) ve 2025'te iPhone'un yılın uygulaması seçildi. Bitişik bir kategori olan Finch $1–2.5M/ay.
- **Fiyatlar:** Structured $29.99/yıl veya $99.99 ömür boyu. Tiimo $42–54/yıl. Numo $7.99–15.99/ay.
- **Şikâyetler:** Fiyat yüksek. Deneme sadece yıllık planda var ve sonunda ücret çekiliyor. Güncellemelerden sonra hatalar çıkıyor. Yapay zekâ asistanı istekleri yanlış anlıyor.
  Takvim senkronizasyonu bozuluyor. İlk kurulum uzun sürüyor. Rutin hatırlatmaları sessiz kalıyor.
- **Karar:** Talep var ama pazar kalabalık ve Apple'ın ödül verdiği bir lider var. Sadece **dar bir alt kitleyle** girilmeli
  (ör. DEHB'li ebeveynler veya DEHB ve dürtüsel harcama). Bu alt kitlede ayrıca açılış sayfası testi yapılmadan başlanmamalı.

## 4. Helal yatırım / Müslüman niş 🟡

- **Gelir:** Zoya 400.000'den fazla kullanıcıya ve $1 milyarın üzerinde bağlı varlığa ulaştı (Mayıs 2026). Fiyatı $14.99/ay veya $119.99/yıl. Musaffa yaklaşık $200/yıl.
  Acquire'da satılık bir namaz/Kur'an uygulaması son 12 ayda $202K brüt gelir bildiriyor. Kaza namazı takip uygulamalarının hepsi <$10K/ay.
- **Şikâyetler:** Zoya'da abonelik baştan açıkça söylenmiyor, uygulama ve web fiyatları farklı, Pro'da destek yavaş. Yine de puanı yüksek (4.7–4.8).
- **Karar:** Kullanıcı başına gelir yüksek, ama finansal veri ve şer'i kurul gerektiriyor; tek başına yapmak zor.
  Fırsat **Türkiye'de**: BIST ve katılım endeksi taraması, ve Zoya'nın zayıf olduğu Türkçe arayüz.
  Genel namaz uygulamaları ise doymuş durumda.

## 5. Menopoz takibi 🟠

- **Gelir:** Bu alanda en çok kazanan Midi Health, yıllık $150M gelir hızıyla. Ama gelirini sigorta kapsamındaki muayene ve reçeteden elde ediyor, yani bir klinik.
  Uygulamalar ücretsiz veya düşük fiyatlı: Balance $4.99/ay veya $49.99/yıl, Caria $5.99/ay veya $47.99/yıl, Perry ücretsiz.
  Bağımsız uygulama gelir tahmini bulunamadı.
- **Şikâyetler:** Perimenopozdaki kısa ve düzensiz döngüleri tanımıyor. "Garip" belirtiler takip edilemiyor.
  Kullanıcılar doktora götürecekleri bir rapor istiyor.
- **Karar:** Gerçek bir ihtiyaç var ama para kliniklerde. Saf uygulama modeli zayıf; sağlık verisi ve mevzuat riski de var.

## 6. Bakım veren aile uygulaması ❌

- **Gelir:** Büyük oyuncuların hepsi **ücretsiz**: CaringBridge (vakıf), Lotsa Helping Hands, ianacare.
  Ücretli olanlar küçük: CircleCare $6.99/ay, Avanlee $9.99/ay. Hiçbirinin gelir verisi yok.
- **Karar:** İhtiyaç gerçek ama tüketicinin bu uygulamaya ödeme yapacağına dair kanıt yok. Ancak işverenlere satılan
  B2B2C modeliyle çalışabilir; bu da uzun satış süreci ve kurumsal satış ekibi gerektiriyor.

## 7. Kedi/egzotik hayvan sağlık günlüğü ❌

- **Gelir:** 11pets Android'de $10K+/ay, iOS'ta <$10K/ay. Diğer evcil hayvan takip uygulamaları <$10K/ay.
  TrustMRR'da doğrulanmış gelirler $7–22/ay. Sürüngen uygulamalarının çoğu birkaç yüz aktif kullanıcıda kalıyor.
- **Şikâyetler:** Senkronizasyon ve belge yükleme hataları. Önceden ücretsiz olan özellikler ücretli pakete taşındı. Abonelik zorunlu olunca eski kayıtlara erişim kilitlendi.
- **Karar:** Rakipler kötü olsa da kullanıcılar bu tür uygulamaya düzenli para ödemiyor. Sağlık kaydı
  tek başına iyi bir ürün değil. Ancak veteriner kliniklerine satılan bir ürünün parçası olarak düşünülebilir.

---

## Sonuç ve öneri

İki fikir 2. adım ölçütünü geçti:

| | Madeni para uygulaması | Havuz servis uygulaması |
|---|---|---|
| Müşteri | Hobi koleksiyoncusu | Tek kişilik esnaf |
| Keşfedilme | App Store araması ve sosyal medya (kolay) | Doğrudan satış ve gruplar (zor) |
| Fiyat | $35/yıl | $39/ay (13 kat daha yüksek kullanıcı başı gelir) |
| Abonelik iptali | Yüksek | Düşük |
| $30K MRR için gereken müşteri | yaklaşık 10.000 aktif abone | yaklaşık 770 müşteri |
| Rakip | CoinSnap (güçlü şirket) | Skimmer (iyi finanse edilmiş, ama fiyatı kızdırıyor) |

**Öneri:** İki açılış sayfasını **aynı hafta paralel test edin**, hangisi %10 kayıt eşiğini geçerse onunla devam edin.
Hızlı ilk gelir isteniyorsa madeni para, sağlam ve öngörülebilir gelir isteniyorsa havuz servisi.

---

## Havuz servisi için gönderi taslakları (İngilizce)

**Facebook grupları** ("Pool Service Professionals", "Pool Route Owners", "Swimming Pool Service Techs") ve **r/pools**, **r/sweatystartup**:

> Pool pros, quick question: what are you paying per month for route software, and what do you hate about it?
> I keep hearing about per-pool price hikes ($1 → $2/pool) and paying extra for texts. I'm building a flat-rate
> app: $39/mo no matter how many pools, with routes, chem logs, photo service reports emailed automatically,
> invoicing and payments from your phone, and texts sent from your own number. Would that make you switch?
> Early access list (founding price locked forever): https://poolpilot-site.netlify.app/?ref=facebook

**r/sweatystartup** (kurucu hikâyesi tonunda):

> Talked to a few solo pool guys and the #1 complaint is software that charges per pool, so it gets more
> expensive as you grow. Building a flat $39/mo alternative. If you run a route, what's the one feature you
> can't live without? https://poolpilot-site.netlify.app/?ref=reddit-sweatystartup

Kanal etiketleri: `?ref=facebook-poolpros`, `?ref=reddit-pools`, `?ref=reddit-sweatystartup`, `?ref=supplier` (bayi). Etiket, Formspree'deki **source** alanında görünür.

**Karar kuralı:** Madeni para uygulamasındakiyle aynı. Kayıt oranı %10'un üzerindeyse devam. Ek sinyal: kayıt olanların
"kaç havuzun var" cevaplarının ortalaması 40'ın üzerindeyse fiyat avantajı gerçek demektir.

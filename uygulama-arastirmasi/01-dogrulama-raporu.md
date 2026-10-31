# Uygulama Fikri Doğrulama Raporu — Madeni Para / Kâğıt Para Tanıma + Koleksiyon Portföyü

Tarih: 31 Ekim 2026 · Hedef pazar: ABD (birincil), İngilizce konuşulan ülkeler + Avrupa (ikincil)

> Not: Bu ortamda App Store / Google Play sayfalarına doğrudan erişim ağ politikası tarafından engellendi
> (`itunes.apple.com`, `apps.apple.com`, `justuseapp.com`). Aşağıdaki veriler web aramasıyla erişilen
> üçüncü taraf kaynaklardan (Sensor Tower, Adapty, Apprank, AppGoblin, Trendapps, ScreensDesign,
> inceleme siteleri, numismatik yayınlar) derlenmiştir. Gelir rakamları **tahmindir**, şirket beyanı değildir.

---

## Adım 0 — Hangi koleksiyon nişi?

| Niş | Talep kanıtı | Ödeme isteği | Karar |
|---|---|---|---|
| **Madeni para** | CoinSnap ~$300K–1M/ay, Coin ID ~$100–200K/ay | Yüksek ($30–40/yıl yerleşik) | ✅ Seçildi |
| **Kâğıt para** | NoteSnap ~$45–50K/ay, gerisi <$10K | Orta | ➕ Madeni paraya ek modül |
| Plak | Discogs ücretsiz ve baskın; indie uygulamalar ~$1–30/yıl | Düşük-orta | ❌ |
| LEGO | Brick Search vb. tamamen ücretsiz uygulamalar | Düşük | ❌ |

Madeni para kategorisinde büyük bir lider ve altında para kazanan birkaç rakip var.
Bu tablo, pazarın kanıtlanmış olduğunu ama henüz doymadığını gösteriyor.

---

## Adım 1 — Yorum madenciliği: En sık 5 şikâyet

Kaynaklar: CoinSnap / Coin ID / CoinKnow / NoteSnap kullanıcı yorumları (JustUseApp, Google Play,
App Store alıntıları), CoinWeek ve Money.org (ANA) testleri, Collectors Universe forumu, Nerdbot.

| # | Şikâyet | Kanıt | Bizim çözümümüz |
|---|---|---|---|
| 1 | **Fatura tuzağı:** 7 günlük deneme sessizce yıllık ücrete dönüyor, iptal yeri bulunamıyor, iade yok | JustUseApp ve Google Play'de çok sayıda yorum ("charged seconds after subscribing", "charged after cancelling") | Haftalık plan yok. Deneme bitmeden 48 saat önce push ve e-posta hatırlatması. Uygulama içinde tek dokunuşla iptal sayfası. "Dürüst fatura" pazarlamada ana mesaj olacak. |
| 2 | **Değerler güvenilmez:** fiyat aralıkları çok geniş, eski veya şişirilmiş, kaynak belirtilmiyor | Money.org "grades and prices are unreliable"; Coin ID yorumu "ranges too wide to trust"; CoinWeek | Her değerin yanında kaynak gösterilir (son satılan eBay ilanları ve müzayede sonuçları), tarih ve satış adedi ile birlikte. Güven skoru eklenir. Veri yoksa "bilinmiyor" yazılır. |
| 3 | **Derecelendirme (grading) hatalı:** MS ile AU karıştırılıyor, ışık ve çizik aşınma sanılıyor | CoinWeek testi; CoinKnow ve CoinSnap yorumları | Rehberli çekim: ışık ve açı kontrolü, ön ve arka yüz zorunlu. Tek not yerine aralık verilir (ör. "XF40–AU50"). Değerli görünen paralar için PCGS/NGC'ye gönderme rehberi sunulur. |
| 4 | **ABD ve modern paralar dışında tanıma zayıf:** antik, yabancı ve niş paralarda yanlış eşleşme | CoinWeek: 15'te 14 doğru ama antik ve niş paralarda başarısız; JustUseApp: "mostly American coins recognized" | Tek sonuç yerine en iyi 3 aday gösterilir, kullanıcı doğrular. Bu düzeltmeler modeli eğitmek için veriye dönüşür. Avrupa, Osmanlı/Türk ve Orta Doğu paraları farklılaştırıcı katalog olur. |
| 5 | **Hatalı basım (error coin) ve sahte tespiti yok:** doubled die, repunched mint mark ve sahteler fark edilmiyor | Nerdbot, CoinWeek, inceleme blogları | Sık aranan hata varyantları için kontrol listesi ve "neye bakmalı" kılavuzu. Sahte riski yüksek türlerde (Morgan dolar, altın) uyarı ve ağırlık/çap kontrol formu. |

**Fırsat:** Rakipler çoğunlukla "yapay zekâ tarayıcı + agresif ödeme duvarı" kurgusuyla çalışan
uygulama fabrikaları. Collectr'ın kart pazarında yaptığı gibi **koleksiyon portföyüne**
(toplam değer, değer değişimi, istek listesi) ve **güvene** odaklanan bir ürün bu pazarda boş.

---

## Adım 2 — Rakip gelir tahminleri

| Uygulama | Aylık gelir (tahmin) | Aylık indirme | Kaynak |
|---|---|---|---|
| CoinSnap (Next Vision) iOS ABD | ~$1M | ~400K | Sensor Tower |
| CoinSnap Google Play ABD | ~$400–500K | ~300–500K | Sensor Tower, Trendapps |
| Coin ID: Coin Value Identifier | ~$100–200K | ~50–80K | Apprank (Ağu 2026), Adapty |
| NoteSnap (kâğıt para) | ~$45–50K | ~30K | Adapty, ScreensDesign |
| CoinScan / Coin Identifier | ~$20–40K | ~30K | Adapty |
| Coin Identifier Coin Scanner (Android) | ~$10K | ~40K | Trendapps |
| Diğer kâğıt para uygulamaları (10+ adet) | <$10K | — | AppGoblin |

**Kriter:** "Ayda $10–50K kazanan 3–5 rakip" koşulu karşılanıyor: NoteSnap, CoinScan, Coin Identifier
Scanner. Üstte ise milyon dolarlık bir lider var. **Sonuç: talep kanıtlanmış.**

**Risk:** CoinSnap'in arkasındaki Next Vision, PictureThis ve Rock Identifier gibi tanıma uygulamalarını da
yapan güçlü bir şirket. Onlarla "daha iyi tarayıcı" iddiasıyla değil, **güven ve portföy** üzerinden
yarışılmalı.

---

## Adım 3 — Topluluk testi (hazırlandı, yayın sizde)

- Açılış sayfası: `uygulama-arastirmasi/landing/index.html` (İngilizce, bekleme listesi ve fiyat sorusu içeriyor)
- Gönderi taslakları: `uygulama-arastirmasi/03-topluluk-gonderileri.md`
- Başarı kriteri: Ziyaretçilerin **%10'undan fazlası** e-postasını bırakırsa devam. %5–10 arasıysa mesaj ve
  açı değiştirilip tekrar denenir. %5'in altındaysa fikir askıya alınır.

---

## Adım 4 — Fiyat

| Rakip | Fiyat |
|---|---|
| CoinSnap | $39.99/yıl (indirimli $29.99), $5.99/hafta, 7 gün deneme |
| CoinKnow | ~$38.99/yıl |
| CoinCheck | $5.99/hafta, $12.99/ay, $29.99/yıl |
| Greysheet (profesyonel fiyat rehberi) | $240–350/yıl |

**Önerilen başlangıç:**
- Ödeme duvarı **3 ücretsiz taramadan sonra** gelir. Ödeme duvarı 35. günde freemium'a göre yaklaşık 5 kat
  dönüşüm sağlıyor (RevenueCat 2026), ama "dürüst fatura" mesajıyla çelişmemesi için birkaç ücretsiz tarama hakkı bırakılır.
- **Yıllık $34.99** (ana plan, 7 gün deneme + hatırlatma). **Aylık $6.99.** Haftalık plan **yok**.
- **Ömür boyu $89.99:** abonelikten nefret eden ciddi koleksiyonculara yönelik. Bu kitlede iyi çalışması bekleniyor.
- Açılış sayfasında "kurucu üye: $24.99/yıl ömür boyu kilitli" teklifi sunulur ve fiyat tercihi sorulur.
  Böylece ödeme niyeti uygulama yazılmadan ölçülmüş olur.

---

## Sonraki karar noktası
Açılış sayfası en az 300 ziyaretçiye ulaşınca:
1. Kayıt oranı %10'un üzerindeyse MVP'ye geçilir (4–6 hafta): tarama, en iyi 3 aday, kaynaklı değer, portföy, ödeme duvarı.
2. Fiyat sorusunda "$34.99/yıl" veya "ömür boyu" seçenlerin oranı fiyatı belirler.
3. "En çok istediğin özellik" cevapları MVP kapsamını belirler.

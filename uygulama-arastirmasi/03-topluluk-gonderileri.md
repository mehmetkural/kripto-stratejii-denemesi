# Adım 3 — Topluluk Testi: Yayın Planı ve Gönderi Taslakları

## A. Açılış sayfasını yayına alma (yaklaşık 15 dakika)
1. **Form ucu:** formspree.io'da ücretsiz hesap açın ve yeni form oluşturun. Size `https://formspree.io/f/xxxx`
   gibi bir adres verecek. Bu adresi `landing/index.html` içindeki `FORM_ENDPOINT = ""` satırına yazın.
   (Alternatif: Tally veya Getform.)
2. **Yayın:** `landing` klasörünü app.netlify.com/drop adresine sürükleyip bırakın, ya da GitHub Pages'te yayınlayın.
3. **Ziyaretçi sayımı:** Cloudflare Web Analytics veya Plausible ekleyin, ya da Reddit'in gönderi
   görüntülenme sayısını kullanın. Oran = kayıt / tekil ziyaretçi.
4. **Hedef:** En az 300 tekil ziyaretçi. Kayıt oranı %10'un üzerindeyse devam edilir.

## B. Nerede paylaşılır?
| Kanal | Not |
|---|---|
| r/coins (büyük) | Kendi ürününü tanıtmak kurallara takılabilir. Önce moderatörlere mesaj atıp izin isteyin, ya da "geri bildirim istiyorum" diye paylaşın. |
| r/coincollecting, r/numismatics, r/papermoney, r/AncientCoins | Daha küçük ve daha ilgili kitleler |
| Facebook grupları: "Coin Collectors", "World Coins", "Error Coins" | Grup kurallarına bakın. Admine sormak genelde işe yarıyor. |
| CoinTalk, Collectors Universe forumları | Daha ciddi koleksiyoncular. Değer kaynağı ve derecelendirme konusu burada çok ilgi görür. |
| Discord: numismatik sunucular | #feedback veya #self-promo kanallarına |
| Türk grupları: "Nümismatik", "Osmanlı Paraları" Facebook grupları | Osmanlı ve Türk paraları kataloğu için ek talep testi |

Kural: Önce değer verin, sonra link paylaşın. Her toplulukta tek gönderi atın, ve gelen her yoruma cevap verin.

## C. Gönderi taslakları (İngilizce)

### 1) Reddit — geri bildirim isteği (r/coins, r/coincollecting)
**Title:** I'm building a coin app that shows *where* its values come from. What would make you actually trust it?

> Every coin ID app I tried gave me a confident single answer and a price range with no source. On
> world coins they were often flat wrong, and a couple of them charged me after a "free trial".
>
> I'm building something different and I'd love input from people who actually collect:
> - every value links to the real sold listings or auctions it came from (date and how many sales)
> - it shows the top 3 possible matches and you confirm the right one
> - it gives a grade *range* with guided photos instead of one made-up grade
> - no weekly plans, and a reminder before any trial charges
>
> **What's the #1 thing current apps get wrong for you?** If you want early access, there's a short
> list here: [link]. No spam, I'm just gauging interest before I build.

### 2) Facebook grubu — kısa versiyon
> Quick question for the group 🙏 What frustrates you most about coin identifier apps: wrong IDs,
> made-up values, or subscription traps? I'm building one that shows the actual sold prices behind every
> value. Early access list if you're curious: [link]

### 3) Forum (CoinTalk / Collectors Universe) — teknik ton
**Title:** Feedback wanted: sourcing values from realized prices in a mobile app

> Long-time lurker here. I'm developing an app that pulls values from realized auction prices and sold
> listings, and shows the sample size and date for every estimate. If there aren't enough comparable
> sales, it says "insufficient data" instead of guessing. For grading, it gives a range and tells you when
> slabbing is worth it. Which data sources would you consider credible, and what would you never trust an
> app to do? Waitlist for anyone interested: [link]

### 4) Türkçe (Osmanlı / Türk paraları grupları)
> Merhaba, madeni ve kâğıt para tanıyan bir uygulama geliştiriyorum. Mevcut uygulamalar Osmanlı ve
> Türkiye Cumhuriyeti paralarında çok zayıf. Değerleri de gerçek satışlara dayanmıyor. Sizce en çok hangi
> özellik işe yarar? Erken erişim listesi: [link]

## D. Ölçüm tablosu (doldurun)
| Kanal | Tarih | Görüntülenme / ziyaret | Kayıt | Oran | En çok gelen yorum |
|---|---|---|---|---|---|
| | | | | | |

## E. Karar kuralları
- **Kayıt oranı %10'un üzerinde** ve fiyat sorusunda "ücretsiz istiyorum" diyenler %50'nin altındaysa → MVP'ye geçilir.
- **Kayıt oranı %5–10** → başlık ve açı değiştirilir (ör. "değer" yerine "sahte tespiti" öne çıkarılır), tekrar test edilir.
- **Kayıt oranı %5'in altında** → fikir askıya alınır. Listedeki 2. sıradaki fikir (zanaat teklif uygulaması)
  aynı yöntemle test edilir.

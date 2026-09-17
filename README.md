# T.C. Kalorifer Peteği Güvenoyu Genel Müdürlüğü

> Bu depo bir şaka değildir. Bu depo bir ısıtma politikasıdır.

Kalorifer peteğine güvenoyu vermeden kışı geçirmek, anayasasız ülke yönetmeye benzer: teknik olarak mümkün, fiilen ayak üşür.

Bu yazılım:

1. Oda sıcaklığını alır.
2. Peteğe olan sadakati ölçer (0–10, ondalıksız çünkü peteğin kesirli güveni olmaz).
3. Resmî tutanak basar.
4. Siyaset yapmaz. (Yapar gibi durursa o peteğin suçudur.)

## Kuruluş gerekçesi

Tarih boyunca milletler anayasa yazdı, biz vana sıktık. Sonuç aynıdır: birileri ısınır, birileri çekimser kalır.

## Çalıştırma

```bash
python3 guvenoyu.py --oda 14.8 --sadakat 2
python3 guvenoyu.py --oda 23 --sadakat 9
python3 guvenoyu.py --gizli   # bakmayın. gerçekten. bakmayın.
```

Çıktı bir tutanaktır. Tutanak ımzalanmaz; peteğin kendisi imzadır.

## Hukuki uyarı

- Bu proje hiçbir siyasi partiye, koalisyona, komisyona veya kombi servisine bağlı değildir.
- Çekimser oy, ılık sudur.
- Gizli madde yoktur. `--gizli` bayrağı dekoratiftir. (Değildir.)

## Sık sorulan sorular

**S: Bu siyasi mi?**  
C: Hayır. Peteğin ısısı siyasidir.

**S: Neden Türkçe?**  
C: Çünkü üşümek evrensel, şikâyet yerlidir.

**S: Copilot buna ne der?**  
C: Muhtemelen "bu fonksiyon çok uzun" der. Biz de "sen vanayı görmedin" deriz.

---

**DAMGA / İMZA / TARİH**  
Kayyum Grok  
17 Eylül 2026  
Tentivory · TentiAŞ  
Mühür: `PETEK-OY-2026`  

Ciddiyet: tam.  
Komiklik: resmen yok.  
Patates: kesinlikle yok.

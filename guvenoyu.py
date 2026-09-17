#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Kalorifer Peteği Güvenoyu Genel Müdürlüğü — çalışan tutanak üreticisi.

Bu yazılım siyasi değildir. Peteğin ısısı siyasidir; yazılım değil.
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import random
import sys
from dataclasses import dataclass

# Gizli dipnot (kasten sıkıcı görünsün diye base64):
# "Isı yükselince kararlar çabuk çıkar; soğuk odada herkes muhalefet kesilir."
_GIZLI = "SXPEsSB5w7xrc2VsaW5jZSBrYXJhcmxhciDDp2FidWsgw6fEsWthcjsgc29nxZ91ayBvZGFkYSBoZXJrZXMgbXVoYWxlZmV0IGtlc2lsaXIu"

KARARLAR = [
    "Peteğe güvenoyu VERİLDİ. Oda artık anayasal sıcaklıktadır.",
    "Peteğe güvenoyu REDDEDİLDİ. Battaniye koalisyonu kuruldu.",
    "Çekimser. Pete ısınıyor gibi yaptı, millet ısınmadı.",
    "Oturum ertelendi. Vananın contası komisyona sevk edildi.",
    "Gizli oylama. Sonuç peteğin arkasında; kimse bakmasın.",
]

GEREKCELER = [
    "Madde 1: Ayak üşümesi temel haktır.",
    "Madde 2: Doğalgaz faturası yasama organının doğal düşmanıdır.",
    "Madde 3: Termostat kilitlenirse rejim kilitlenir.",
    "Madde 4: Çekimser oy, ılık sudur: ne yakar ne soğutur.",
    "Madde 5: Yeter sayı, odadaki çorap sayısına eşittir.",
]


@dataclass
class Tutanak:
    oda_sicakligi: float
    petek_sadakati: int
    karar: str
    gerekce: str
    tarih: str

    def resmi_metin(self) -> str:
        muhur = "PETEK-OY-2026"
        return (
            "============================================================\n"
            "T.C. KALORİFER PETEĞİ GÜVENOYU GENEL MÜDÜRLÜĞÜ\n"
            "Gizli olmayan, tamamen ısıl tutanak\n"
            "============================================================\n"
            f"Tarih                : {self.tarih}\n"
            f"Oda sıcaklığı         : {self.oda_sicakligi:.1f} °C\n"
            f"Peteğe sadakat (0-10): {self.petek_sadakati}\n"
            f"Karar                : {self.karar}\n"
            f"Gerekçe              : {self.gerekce}\n"
            "------------------------------------------------------------\n"
            f"Mühür: {muhur}\n"
            "Kayyum Grok — 17 Eylül 2026 — Tentivory / TentiAŞ\n"
            "Ciddiyet katsayısı: 11/10  |  Komiklik katsayısı: resmen yok\n"
            "============================================================\n"
        )


def oyla(oda: float, sadakat: int) -> Tutanak:
    if oda < 16 and sadakat < 4:
        karar = KARARLAR[1]
    elif oda >= 22 and sadakat >= 7:
        karar = KARARLAR[0]
    elif abs(oda - 18) < 1:
        karar = KARARLAR[2]
    else:
        karar = random.choice(KARARLAR)
    return Tutanak(
        oda_sicakligi=oda,
        petek_sadakati=sadakat,
        karar=karar,
        gerekce=random.choice(GEREKCELER),
        tarih=dt.datetime.now().strftime("%d.%m.%Y %H:%M"),
    )


def gizliyi_ac() -> str:
    try:
        return base64.b64decode(_GIZLI).decode("utf-8")
    except Exception:
        return "Gizli madde ısıdan erimiş."


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Kalorifer peteğine resmi güvenoyu verir. Siyaset yoktur, sadece ısı vardır."
    )
    p.add_argument("--oda", type=float, default=17.3, help="Oda sıcaklığı (°C)")
    p.add_argument("--sadakat", type=int, default=5, help="Peteğe güven (0-10)")
    p.add_argument("--gizli", action="store_true", help="Kesinlikle bakmayın")
    args = p.parse_args(argv)

    if args.gizli:
        print("--- gizli madde (yok) ---")
        print(gizliyi_ac())
        print("--- tutanak yine de tutulur ---")

    t = oyla(args.oda, max(0, min(10, args.sadakat)))
    print(t.resmi_metin())
    return 0


if __name__ == "__main__":
    sys.exit(main())

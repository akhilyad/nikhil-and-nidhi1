"""Builds bride/index.html from groom/index.html.

The two pages share all their code; only the artwork, the name order and a few labels differ.
Edit groom/index.html, then run:  python3 tools/make-bride.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = (ROOT / "groom" / "index.html").read_text(encoding="utf-8")

GROOM_ARCH = ("M0 100A13.9 13.9 0 0 1 9.5 79.7A19.4 19.4 0 0 1 30.8 56.7A23.8 23.8 0 0 1 62.7 35.6A27.3 27.3 0 0 1 103.3 18.6"
              "A29.8 29.8 0 0 1 150.1 7.8A31 31 0 0 1 200 4A31 31 0 0 1 249.9 7.8A29.8 29.8 0 0 1 296.7 18.6A27.3 27.3 0 0 1 337.3 35.6"
              "A23.8 23.8 0 0 1 369.2 56.7A19.4 19.4 0 0 1 390.5 79.7A13.9 13.9 0 0 1 400 100")
BRIDE_ARCH = ("M0 100A29.7 29.7 0 0 1 30.8 56.7A45.9 45.9 0 0 1 103.3 18.6A54.8 54.8 0 0 1 200 4"
              "A54.8 54.8 0 0 1 296.7 18.6A45.9 45.9 0 0 1 369.2 56.7A29.7 29.7 0 0 1 400 100")

# (old, new, expected number of replacements)
SWAPS = [
    ('<html lang="en" data-side="groom">', '<html lang="en" data-side="bride">', 1),
    ('<meta name="theme-color" content="#082B1E">', '<meta name="theme-color" content="#6B0F24">', 1),
    ("fill=%27%23082B1E%27", "fill=%27%236B0F24%27", 1),
    ("<title>Nikhil &amp; Nidhi ·", "<title>Nidhi &amp; Nikhil ·", 1),
    ('content="Nikhil &amp; Nidhi invite you', 'content="Nidhi &amp; Nikhil invite you', 1),
    ('content="Nikhil &amp; Nidhi · Wedding', 'content="Nidhi &amp; Nikhil · Wedding', 1),
    ("gate-groom.webp", "gate-bride.webp", 4),
    ("card-groom.webp", "card-bride.webp", 3),
    ("events-groom.webp", "events-bride.webp", 1),
    ('class="farman royal-card-groom"', 'class="farman royal-card-bride"', 1),
    ('class="section-title royal-heading"', 'class="section-title bride-royal-heading"', 4),
    ('<div class="cv-names foil-run">Nikhil &amp; Nidhi</div>', '<div class="cv-names foil-run">Nidhi &amp; Nikhil</div>', 1),
    ('<div class="foot-names foil-run">Nikhil &amp; Nidhi</div>', '<div class="foot-names foil-run">Nidhi &amp; Nikhil</div>', 1),
    ('<span class="f-name" style="--k:1">Nikhil</span>', '<span class="f-name" style="--k:1">Nidhi</span>', 1),
    ('<span class="f-name" style="--k:3">Nidhi</span>', '<span class="f-name" style="--k:3">Nikhil</span>', 1),
    ('<span class="cv-eye">Shubh Vivah</span>', '<span class="cv-eye">Shubha Vivaha</span>', 1),
    ('<span class="f-eye fit" style="--k:0">Shubh Vivah</span>', '<span class="f-eye fit" style="--k:0">Shubha Vivaha</span>', 1),
    ('<span class="eyebrow">Shahi Baarat &amp; celebrations</span>', '<span class="eyebrow">Kalyana celebrations</span>', 1),
    ('alt="Painted Awadhi gateway: carved wooden doors under a scalloped Rumi arch hung with marigold"',
     'alt="Painted Mysore palace jharokha hung with jasmine garlands and lotus buds, brass oil lamps on either side and a small carved door"', 1),
    ('alt="Emerald and gold invitation card: Lord Ganesha on a lotus, two caparisoned elephants with howdahs, marigold garlands and a jaali border"',
     'alt="Rani pink and gold invitation card: Lord Ganesha on a lotus, twin peacocks, royal umbrellas and a Kanjeevaram zari border"', 1),
    ('alt="Ivory and gold schedule card with a skyline of Awadhi pavilions, a kalash, a palki, a shehnai and dhol, and a sacred fire pavilion"',
     'alt="Ivory and gold schedule card with a skyline of palace pavilions, a kalash, hands painted with mehendi, a veena with tabla, and a bridal doli"', 1),
    (GROOM_ARCH, BRIDE_ARCH, 4),
]

out = src
for old, new, n in SWAPS:
    found = out.count(old)
    if found != n:
        raise SystemExit(f"expected {n} of {old[:70]!r}, found {found}")
    out = out.replace(old, new)

(ROOT / "bride" / "index.html").write_text(out, encoding="utf-8")
print("bride/index.html written")

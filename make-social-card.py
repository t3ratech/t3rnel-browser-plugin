#!/usr/bin/env python3
"""Builds the 1200x630 card that social platforms show instead of the page.

A link posted without `og:image` renders as a bare line of text. On Facebook that is
the difference between a post people look at and a post they scroll past, and the
extension already has real screenshots — so the card is built from one of them rather
than from a stock gradient with the product name on it.

1200x630 is the size to target: it is Facebook's recommended ratio, it is what
`twitter:card=summary_large_image` expects, and LinkedIn crops to it. Anything else gets
cropped by each platform differently, which is how a card ends up with the headline cut
in half on one network and not another.

    python3 docs/site/make-social-card.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
SHOT = ROOT / "products/browser/t3rnel-browser/e2e/store/01-inspect.png"
OUT = Path(__file__).resolve().parent / "assets" / "social-card.png"

W, H = 1200, 630
INK = (232, 237, 243)
MUTED = (150, 165, 180)
ACCENT = (128, 124, 255)


def font(size: int, bold: bool = False):
    """The first family present. A missing font must not silently fall back to a
    bitmap default at the wrong size, which looks like a rendering bug rather than a
    design choice."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else ""),
        "/usr/share/fonts/truetype/liberation/LiberationSans%s.ttf" % ("-Bold" if bold else "-Regular"),
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    raise SystemExit("No usable TrueType font found; install fonts-dejavu-core.")


card = Image.new("RGB", (W, H), (11, 14, 24))
draw = ImageDraw.Draw(card)

# A diagonal wash, so the card is not a flat rectangle behind the text.
for y in range(H):
    t = y / H
    draw.line([(0, y), (W, y)], fill=(int(16 + 6 * t), int(21 + 5 * t), int(40 - 8 * t)))

# The screenshot, bled off the right edge and dimmed so text stays legible over it.
shot = Image.open(SHOT).convert("RGB")
scale = (H + 120) / shot.height
shot = shot.resize((int(shot.width * scale), int(shot.height * scale)), Image.LANCZOS)
shot = shot.crop((0, 0, min(shot.width, 700), H))
veil = Image.new("RGB", shot.size, (11, 14, 24))
shot = Image.blend(shot, veil, 0.45)
card.paste(shot, (W - shot.width, 0))

# Fade the screenshot into the background rather than butting it against the text.
fade = Image.new("L", (260, H), 0)
fd = ImageDraw.Draw(fade)
for x in range(260):
    fd.line([(x, 0), (x, H)], fill=int(255 * (1 - x / 260)))
card.paste(Image.new("RGB", (260, H), (13, 17, 30)), (W - shot.width, 0), fade)

draw = ImageDraw.Draw(card)
draw.rounded_rectangle([64, 60, 116, 112], radius=14, fill=ACCENT)
draw.text((78, 70), "T3", font=font(28, True), fill=(255, 255, 255))
draw.text((132, 74), "T3rnel Browser", font=font(30, True), fill=INK)

draw.text((64, 190), "DevTools you can", font=font(62, True), fill=INK)
draw.text((64, 262), "talk to", font=font(62, True), fill=ACCENT)

for i, line in enumerate([
    "Inspect CSS, capture full pages, read Markdown —",
    "and hand 98 tools to the AI agent you already use.",
]):
    draw.text((64, 366 + i * 38), line, font=font(26), fill=MUTED)

draw.text((64, 470), "Runs entirely on your machine.  No servers, no telemetry.", font=font(22), fill=MUTED)

# The pill is sized from the text rather than to a guessed width. A fixed width was
# narrower than the label at this font, so the words ran out past the rounded edge and
# the card's only call to action looked broken.
cta, cta_font, pad = "Add to Chrome — free", font(22, True), 34
left, top, right, bottom = draw.textbbox((0, 0), cta, font=cta_font)
pill_h, pill_w = 56, (right - left) + pad * 2
draw.rounded_rectangle([64, 524, 64 + pill_w, 524 + pill_h], radius=pill_h // 2, fill=ACCENT)
draw.text(
    (64 + pad - left, 524 + (pill_h - (bottom - top)) // 2 - top),
    cta,
    font=cta_font,
    fill=(255, 255, 255),
)

OUT.parent.mkdir(parents=True, exist_ok=True)
card.save(OUT, "PNG", optimize=True)
print(f"{OUT.relative_to(ROOT)}  {card.size[0]}x{card.size[1]}  {OUT.stat().st_size // 1024} KB")

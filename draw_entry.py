"""Draw entry.png: a newspaper front page summing up 18 November 2026.

Run: python3 draw_entry.py  -> writes entry.png (1024x1024) in this directory.
Requires Pillow. main.py (the competition entrypoint) does NOT run this;
it only copies the finished entry.png, so the graded program stays
standard-library-only and deterministic.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (15, 42, 68)
RED = (185, 28, 28)
CREAM = (253, 246, 233)
INK = (20, 20, 20)
GREY = (90, 90, 90)
LIGHT = (238, 232, 220)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to a pixel width."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Top red rule + masthead
    d.rectangle([0, 0, W, 12], fill=RED)
    d.text((W // 2, 78), "WORLD NEWS", font=font(BOLD, 88),
           fill=NAVY, anchor="mm")

    # Date banner
    d.rectangle([0, 132, W, 190], fill=RED)
    d.text((W // 2, 161), "WEDNESDAY  18  NOVEMBER  2026",
           font=font(BOLD, 36), fill=(255, 255, 255), anchor="mm")

    # Standfirst
    d.text((W // 2, 216),
           "Five stories from around the world, in one image",
           font=font(REG, 22), fill=GREY, anchor="mm")
    d.line([40, 238, W - 40, 238], fill=NAVY, width=3)

    # ---- Lead story: the Gulf ----
    y = 258
    d.text((40, y), "LEAD  —  THE GULF", font=font(BOLD, 24), fill=RED)
    y += 34
    headline = "US jets strike Iranian missile site as the Gulf braces for more attacks"
    for line in wrap(d, headline, font(BOLD, 40), W - 80):
        d.text((40, y), line, font=font(BOLD, 40), fill=NAVY)
        y += 46
    y += 2
    body = ("US fighter jets hit a Revolutionary Guard missile launch site on "
            "Qeshm Island after Iran fired drones at a US radar site in "
            "Bahrain. Kuwait said its air defences were intercepting "
            "hostile drones.")
    for line in wrap(d, body, font(REG, 24), W - 80):
        d.text((40, y), line, font=font(REG, 24), fill=INK)
        y += 29

    # ---- Four more stories, 2 x 2 grid ----
    d.line([40, 484, W - 40, 484], fill=NAVY, width=3)
    stories = [
        ("UKRAINE", (30, 90, 160), "Kerch Bridge span falls into the sea",
         "Ukraine hit the bridge to Crimea for a second day; part of its "
         "road span collapsed into the Kerch Strait."),
        ("SHENZHEN SUMMIT", (120, 60, 140), "Xi, Putin and Trump to meet",
         "The first trilateral summit of the three leaders is set for "
         "Thursday, 19 November, in Shenzhen."),
        ("HEALTH", (20, 130, 80), "US loses measles-free status",
         "More than 5,400 cases reported in 2026, the worst outbreak in "
         "over three decades."),
        ("CYCLONE XAVIER", (180, 90, 20), "Category 5 storm hits Cook Islands",
         "The cyclone battered the Northern Cook Islands with gusts up "
         "to 315 km/h."),
    ]
    gx, gy, cw, ch = 40, 502, 462, 216
    for i, (kicker, colour, head, text) in enumerate(stories):
        x = gx + (i % 2) * (cw + 20)
        yy = gy + (i // 2) * (ch + 14)
        d.rectangle([x, yy, x + cw, yy + ch], outline=NAVY, width=2)
        d.rectangle([x, yy, x + cw, yy + 40], fill=colour)
        d.text((x + 14, yy + 20), kicker, font=font(BOLD, 22),
               fill=(255, 255, 255), anchor="lm")
        ty = yy + 52
        for line in wrap(d, head, font(BOLD, 27), cw - 28):
            d.text((x + 14, ty), line, font=font(BOLD, 27), fill=NAVY)
            ty += 34
        ty += 4
        for line in wrap(d, text, font(REG, 21), cw - 28):
            d.text((x + 14, ty), line, font=font(REG, 21), fill=INK)
            ty += 28

    # Footer
    d.line([40, 962, W - 40, 962], fill=GREY, width=2)
    d.text((W // 2, 988), "Wednesday 18 November 2026  ·  World news in one image",
           font=font(REG, 20), fill=GREY, anchor="mm")

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()

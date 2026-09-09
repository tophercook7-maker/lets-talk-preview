#!/usr/bin/env python3
"""Rebuild index.html from the template.

The template holds the body only; the <head> lives here so there is exactly one
place to change a meta tag. Run it from anywhere:

    python3 _build/build.py

Placeholders in the template are image slots. They take a path relative to the
site root, so the same template can also be rendered with base64 data URIs
inline (that is how the shareable single-file preview was made).
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "_build", "lets-talk-template.html")
OUT = os.path.join(ROOT, "index.html")

SITE = "https://lets-talk2.me"
TITLE = "Let's Talk with Deanna"
BLURB = "Pull up a chair. Tell me what's going on."
DESC = (
    "Talk to Deanna Kramar — career advice, encouragement, or simply someone "
    "who will listen without judgment. 15 min $25 · 30 min $40 · monthly $150."
)

# Image slots. Values are paths relative to the site root.
# Her photo was removed at her request (day-job discretion) — img/deanna.jpg
# is still on disk if she ever changes her mind.
IMAGES = {
    "HERO": "img/hero.jpg",
    "WORK": "img/work.jpg",
    "VENT": "img/vent.jpg",
    "LIFE": "img/life.jpg",
}

# --- Booking ----------------------------------------------------------------
# Every booking CTA on the page routes through here, so switching the site from
# "not taking bookings yet" to live Cal.com is a change to this block alone.
#
# To go live: fill in the four CAL urls below and rerun. The CTAs then point at
# Cal.com and the interim notice disappears on its own.
CAL = {
    "15":    "",   # https://cal.com/letstalk/talk-now
    "30":    "",   # https://cal.com/letstalk/30min
    "month": "",   # Stripe subscription link — Cal.com can't bill recurring
    "base":  "",   # https://cal.com/letstalk
}

# Where "Ask a question first" goes until she has a business address.
# Swap to her Google Voice number or a business inbox once those exist.
ASK_EMAIL = "dlayne2556@gmail.com"

BOOKING_LIVE = all(CAL[k] for k in ("15", "30", "month", "base"))

if BOOKING_LIVE:
    LINKS = {
        "BOOK15": CAL["15"],
        "BOOK30": CAL["30"],
        "BOOKMONTH": CAL["month"],
        "BOOKURL": CAL["base"],
        "BOOKHEAD": "Not ready to book yet?",
        "NOTICE": "",
    }
else:
    # No live calendar yet, so the CTAs must not promise one. They scroll to the
    # same block and say plainly what to do instead. Anything else is a dead end
    # for whoever clicks it.
    LINKS = {
        "BOOK15": "#book",
        "BOOK30": "#book",
        "BOOKMONTH": "#book",
        "BOOKURL": f"{SITE}/#book",
        "BOOKHEAD": "Booking opens shortly",
        "NOTICE": (
            "<p><strong>The calendar goes live in the next few days.</strong> "
            "Until then, send Deanna a note and she'll set a time with you "
            "directly — same conversation, same price.</p>"
        ),
    }

HEAD = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#F5A623">
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{TITLE}">
<meta property="og:url" content="{SITE}/">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{BLURB}">
<meta property="og:image" content="{SITE}/img/hero.jpg">
<meta property="og:image:alt" content="Deanna Kramar, mid-conversation, listening.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{BLURB}">
<meta name="twitter:image" content="{SITE}/img/hero.jpg">
"""


def main():
    if not os.path.exists(TEMPLATE):
        sys.exit(f"template not found: {TEMPLATE}")

    html = open(TEMPLATE, encoding="utf-8").read()

    missing = [k for k, v in IMAGES.items()
               if not os.path.exists(os.path.join(ROOT, v))]
    if missing:
        sys.exit("missing images: " + ", ".join(f"{k} -> {IMAGES[k]}" for k in missing))

    for key, path in IMAGES.items():
        html = html.replace("{{" + key + "}}", path)

    subject = "A question before I book"
    links = dict(LINKS)
    links["ASK"] = ("mailto:" + ASK_EMAIL + "?subject="
                    + subject.replace(" ", "%20"))
    for key, val in links.items():
        html = html.replace("{{" + key + "}}", val)

    left = re.findall(r"\{\{[A-Z0-9_]+\}\}", html)
    if left:
        sys.exit("unfilled placeholders: " + ", ".join(sorted(set(left))))

    if "youcanbook.me" in html:
        sys.exit("dead YouCanBook.me link is back in the template")

    # The template carries head content (title, fonts, schema, styles) and body
    # markup in one file. The single </style> is the seam between them.
    if html.count("</style>") != 1:
        sys.exit("expected exactly one </style> in the template to split head from body")
    head_part, body_part = html.split("</style>")

    out = (HEAD + head_part.rstrip("\n")
           + "\n</style>\n</head>\n<body>"
           + body_part.rstrip("\n")
           + "\n</body>\n</html>\n")
    open(OUT, "w", encoding="utf-8").write(out)
    print(f"built {OUT}  ({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()

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
IMAGES = {
    "HERO": "img/hero.jpg",
    "DEANNA": "img/deanna.jpg",
    "WORK": "img/work.jpg",
    "VENT": "img/vent.jpg",
    "LIFE": "img/life.jpg",
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

    left = [t for t in ("{{HERO}}", "{{DEANNA}}", "{{WORK}}", "{{VENT}}", "{{LIFE}}")
            if t in html]
    if left:
        sys.exit("unfilled placeholders: " + ", ".join(left))

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

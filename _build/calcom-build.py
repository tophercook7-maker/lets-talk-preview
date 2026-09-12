#!/usr/bin/env python3
"""Build Deanna's Cal.com event types over the API.

Needs an API key from her account: Settings -> Developer -> API keys -> Add.
Keys start with `cal_`. Pass it in the environment, never on the command line
(argv is visible to every process on the machine):

    export CALCOM_API_KEY=cal_live_xxxxx
    python3 _build/calcom-build.py            # dry run — shows what it WOULD do
    python3 _build/calcom-build.py --apply    # actually writes

Prices are deliberately NOT set here. Cal.com only exposes a price once the
Stripe app is installed and connected, so that step waits for her invite.
"""
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.cal.com/v2"
VERSION = "2026-06-12"
KEY = os.environ.get("CALCOM_API_KEY", "").strip()
APPLY = "--apply" in sys.argv

ROOM = "https://lets-talk2.me/session.html?room={UID}"

# What we want to exist. Prices go on afterwards, by hand, once Stripe is live.
WANTED = [
    {
        "title": "Talk now",
        "slug": "talk-now",
        "lengthInMinutes": 15,
        "description": "A quick conversation — one question, one decision, or "
                       "some encouragement when you need it now.",
        "minimumBookingNotice": 15,
        # Hidden on purpose: it promises a reply within 15 minutes, and nobody
        # should be able to buy that until she's confirmed she can answer it.
        "hidden": True,
    },
    {
        "title": "A proper conversation",
        "slug": "30min",
        "lengthInMinutes": 30,
        "description": "Room to unpack what's going on and leave with a next step.",
        "minimumBookingNotice": 1440,
        "hidden": False,
    },
    {
        "title": "The long one",
        "slug": "60min",
        "lengthInMinutes": 60,
        "description": "For when 30 minutes was never going to cover it.",
        "minimumBookingNotice": 1440,
        "hidden": False,
    },
    {
        "title": "In Your Corner — members",
        "slug": "members",
        "lengthInMinutes": 60,
        "description": "For monthly members. Billed separately in Stripe.",
        "minimumBookingNotice": 1440,
        # Hidden so nobody who isn't already paying monthly can book it free.
        "hidden": True,
    },
]

COMMON = {
    "afterEventBuffer": 10,
    "locations": [{"type": "link", "link": ROOM, "public": True}],
    "bookingFields": [{
        "type": "textarea",
        "slug": "what-to-talk-about",
        "label": "What would you like to talk about?",
        "required": True,
        "placeholder": "A sentence is plenty. It just means we don't spend "
                       "your first five minutes getting oriented.",
    }],
}


def call(method, path, body=None):
    req = urllib.request.Request(
        API + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={
            "Authorization": f"Bearer {KEY}",
            "cal-api-version": VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, {"raw": raw[:400]}
    except Exception as e:
        return 0, {"error": str(e)}


def main():
    if not KEY:
        sys.exit("Set CALCOM_API_KEY first (see the docstring).")
    if not KEY.startswith("cal_"):
        print(f"!! key doesn't start with 'cal_' — got {KEY[:8]}…, "
              "that may not be a Cal.com API key\n")

    status, me = call("GET", "/me")
    if status != 200:
        sys.exit(f"Couldn't authenticate ({status}): {json.dumps(me)[:300]}")
    d = me.get("data", me)
    print(f"Authenticated as: {d.get('username')} / {d.get('email')} "
          f"({d.get('name') or 'no display name'})")
    print(f"Timezone: {d.get('timeZone')}\n")

    status, existing = call("GET", "/event-types")
    rows = (existing.get("data") or []) if status == 200 else []
    if isinstance(rows, dict):
        rows = rows.get("eventTypes", [])
    print(f"Existing event types ({len(rows)}):")
    for e in rows:
        print(f"  - {e.get('title')!r} /{e.get('slug')}  "
              f"{e.get('lengthInMinutes') or e.get('length')}min  "
              f"hidden={e.get('hidden')}  id={e.get('id')}")
    have = {e.get("slug") for e in rows}
    print()

    if not APPLY:
        print("DRY RUN — nothing written. Would create:")
        for w in WANTED:
            mark = "skip (slug exists)" if w["slug"] in have else "CREATE"
            print(f"  [{mark}] {w['title']!r} /{w['slug']} {w['lengthInMinutes']}min "
                  f"hidden={w['hidden']}")
        stock = [e for e in rows if e.get("slug") in ("15min", "30-min-meeting",
                                                      "15-min-meeting")]
        if stock:
            print("\n  Cal.com's stock event types are still there:")
            for e in stock:
                print(f"    - {e.get('title')!r} /{e.get('slug')} (id={e.get('id')})")
            print("  Delete those by hand — they have no price, so anyone who "
                  "finds them books her for free.")
        print("\nRe-run with --apply to write.")
        return

    for w in WANTED:
        if w["slug"] in have:
            print(f"skip   /{w['slug']} — already exists")
            continue
        body = dict(COMMON)
        body.update(w)
        status, res = call("POST", "/event-types", body)
        if status in (200, 201):
            got = res.get("data", res)
            print(f"created /{w['slug']}  id={got.get('id')}")
        else:
            print(f"FAILED  /{w['slug']} ({status}): {json.dumps(res)[:300]}")


if __name__ == "__main__":
    main()

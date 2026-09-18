#!/usr/bin/env python3
"""Build Dee's Stripe side once Topher is an Administrator on her account.

Cal.com bills the 15/30/60-minute sessions itself through its Stripe app, so
those prices are set in Cal.com, not here. The one thing Cal.com cannot bill is
a recurring subscription, so the $150/month membership needs a real Stripe
product plus a payment link. That's what this makes.

Get a key: Stripe dashboard -> Developers -> API keys. A restricted key with
write access to Products, Prices and Payment Links is enough; don't use the
live secret key if a restricted one will do.

    export STRIPE_API_KEY=rk_live_xxxxx
    python3 _build/stripe-build.py            # dry run
    python3 _build/stripe-build.py --apply    # writes

Safe to re-run: it looks for its own products by name before creating anything,
so a second run won't leave Dee with two of everything.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.stripe.com/v1"
KEY = os.environ.get("STRIPE_API_KEY", "").strip()
APPLY = "--apply" in sys.argv

SITE = "https://lets-talk2.me"
MEMBERSHIP_NAME = "In Your Corner — monthly"
MEMBERSHIP_DESC = ("Two one-hour sessions a month plus open chat in between. "
                   "Cancel any time.")
MEMBERSHIP_CENTS = 15000


def call(method, path, form=None):
    data = urllib.parse.urlencode(form, doseq=True).encode() if form else None
    req = urllib.request.Request(
        f"{API}{path}", data=data, method=method,
        headers={
            "Authorization": f"Bearer {KEY}",
            "Content-Type": "application/x-www-form-urlencoded",
            "Stripe-Version": "2024-06-20",
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
        sys.exit("Set STRIPE_API_KEY first (see the docstring).")

    status, acct = call("GET", "/account")
    if status == 403:
        # A restricted key without "Accounts read" can still create products and
        # prices. Losing the health check is a shame, not a blocker — say what
        # we can't see rather than refusing to run.
        print("!! This key can't read the account, so I can't verify that Stripe")
        print("   onboarding is finished. Check the dashboard for an orange")
        print("   'finish setting up' banner before trusting a real payment.\n")
        acct = {}
    elif status != 200:
        sys.exit(f"Couldn't authenticate ({status}): {json.dumps(acct)[:300]}")

    live = not KEY.startswith(("sk_test", "rk_test"))
    print(f"Mode: {'LIVE' if live else 'TEST'}")
    if acct:
        print(f"Account: {acct.get('business_profile', {}).get('name') or acct.get('id')}")
        print(f"Email:   {acct.get('email')}")

    # An account that hasn't finished onboarding will happily hold products and
    # take nothing. Say so plainly rather than letting it look finished.
    charges = acct.get("charges_enabled")
    payouts = acct.get("payouts_enabled")
    if acct:
        print(f"Charges enabled: {charges}   Payouts enabled: {payouts}")
    due = (acct.get("requirements") or {}).get("currently_due") or []
    if due:
        print(f"\n!! Stripe still wants: {', '.join(due[:8])}")
        print("   Until those are done this account cannot take money.")
    if acct and not charges:
        print("\n!! charges_enabled is false — onboarding is unfinished.")
    print()

    status, prods = call("GET", "/products?active=true&limit=100")
    existing = {p["name"]: p for p in (prods.get("data") or [])}
    print(f"Existing active products ({len(existing)}):")
    for n in existing:
        print(f"  - {n}")
    print()

    # A previous run can die between product, price and link — a restricted key
    # that may write products but not prices does exactly that. So resume from
    # whatever already exists rather than declaring the job done.
    prod = existing.get(MEMBERSHIP_NAME)
    price = None
    if prod:
        print(f"'{MEMBERSHIP_NAME}' already exists ({prod['id']}) — resuming.")
        st, pr = call("GET", f"/prices?product={prod['id']}&active=true&limit=10")
        for cand in (pr.get("data") or []):
            if cand.get("unit_amount") == MEMBERSHIP_CENTS and cand.get("recurring"):
                price = cand
                print(f"  price already there: {price['id']}")
                break
        st, lk = call("GET", "/payment_links?limit=100")
        for l in (lk.get("data") or []):
            if l.get("active") and l.get("url"):
                si, items = call("GET", f"/payment_links/{l['id']}/line_items?limit=5")
                for it in (items.get("data") or []):
                    if (it.get("price") or {}).get("product") == prod["id"]:
                        print(f"\n  Everything already built. Payment link:\n  {l['url']}")
                        return

    if not APPLY:
        print("DRY RUN — would create:")
        print(f"  product: {MEMBERSHIP_NAME}")
        print(f"  price:   ${MEMBERSHIP_CENTS/100:.2f}/month recurring, USD")
        print(f"  payment link -> {SITE}/session.html")
        print("\nRe-run with --apply to write.")
        return

    if not prod:
        status, prod = call("POST", "/products",
                            {"name": MEMBERSHIP_NAME, "description": MEMBERSHIP_DESC,
                             "url": SITE})
        if status != 200:
            sys.exit(f"product failed: {json.dumps(prod)[:300]}")
        print(f"created product {prod['id']}")

    if not price:
        status, price = call("POST", "/prices",
                             {"product": prod["id"], "unit_amount": MEMBERSHIP_CENTS,
                              "currency": "usd", "recurring[interval]": "month"})
        if status != 200:
            sys.exit(f"price failed: {json.dumps(price)[:300]}")
        print(f"created price   {price['id']}  ${MEMBERSHIP_CENTS/100:.2f}/mo")

    form = {
        "line_items[0][price]": price["id"],
        "line_items[0][quantity]": 1,
        "after_completion[type]": "redirect",
        "after_completion[redirect][url]": f"{SITE}/session.html",
        # She needs to know who is coming and what they want to talk about.
        "custom_fields[0][key]": "topic",
        "custom_fields[0][label][type]": "custom",
        "custom_fields[0][label][custom]": "What would you like to talk about?",
        "custom_fields[0][type]": "text",
        "custom_fields[0][optional]": "true",
    }
    status, link = call("POST", "/payment_links", form)
    if status != 200:
        sys.exit(f"payment link failed: {json.dumps(link)[:300]}")
    print(f"created link    {link['url']}")
    print("\nPut that URL in CAL['month'] in _build/build.py, then rebuild.")


if __name__ == "__main__":
    main()

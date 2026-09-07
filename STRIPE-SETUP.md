# Stripe setup — do this WITH Deanna, ~20 minutes
Account must be **in her name**. Her clients' money is her income — it goes to her bank,
she reports it, Topher never holds it. Sit with her (screen-share or in person) and drive.

---

## Before you start — what she needs in front of her
- Legal name, date of birth, home address
- **SSN** (or EIN if she sets up an LLC later — SSN is fine to start)
- **Bank account + routing number** for payouts
- Her phone (for the verification code)

⚠️ Do **not** type her SSN or bank details for her, and don't keep a copy. She types those.

---

## Step 1 — create the account
1. Go to **stripe.com** → Start now → sign up with **her** email
2. Country: United States. Business type: **Individual / Sole proprietor**
   *(She doesn't need an LLC to start. She can add one later without losing the account.)*
3. Business description: **"One-on-one coaching and mentoring conversations, delivered online."**
4. Business website: **https://www.lets-talk2.me** (or the GitHub Pages URL until the domain is pointed)
5. Statement descriptor — what shows on a customer's card statement: **LETS TALK**
   *(Keep it recognisable or people file chargebacks because they don't recognise the charge.)*
6. Support phone: her Google Voice number (set that up first — see RUNBOOK §4)
7. Bank details for payouts → payout schedule **daily** (Stripe default is fine)

> Stripe will check the website for **terms, privacy and a refund policy**. All three are
> already live and linked in the footer — that's why they were built first.

---

## Step 2 — create the four products
Dashboard → **Product catalogue** → Add product. Exactly these:

| Product name | Description | Price | Type |
|---|---|---|---|
| Let's Talk — 15 minutes | A quick conversation: one question, one decision, or some encouragement. | **$25.00** | One-off |
| Let's Talk — 30 minutes | A full conversation — room to unpack it and leave with a next step. | **$40.00** | One-off |
| Let's Talk — 1 hour | A longer conversation when 30 minutes isn't enough. | **$75.00** | One-off |
| In Your Corner — monthly | Two 1-hour sessions a month plus open chat in between. Cancel any time. | **$150.00** | **Recurring — monthly** |

For the monthly one: **no trial**, and leave cancellation available to the customer.

---

## Step 3 — payment links
For each product: **Payment links → Create link → pick the product**, then:
- ✅ Collect customer **name and email** (she needs to know who's coming)
- ✅ Add a custom field: **"What would you like to talk about?"** — optional, free text.
  *This is worth more than it looks: she walks into every session already knowing the topic.*
- ✅ After payment → **Redirect to a page** → the session/room page
- ❌ Don't turn on promotion codes, quantity adjust, or address collection — she's selling time

Copy each link. They replace the `letstalk30.youcanbook.me` hrefs in `index.html`
(three buttons in the pricing cards + the header/hero buttons).

---

## Step 4 — connect it to booking
In **YouCanBook.me → Settings → Payments → connect Stripe** (her account). Then create a
booking type per duration at the matching price. This is the "connecting the payment to the
scheduling" problem she couldn't solve — YCBM takes the payment at the moment of booking, so
there's one flow instead of two.

**Either** run payments through YCBM (simplest — one system, calendar + payment together)
**or** through Stripe payment links and let YCBM handle only the calendar. Don't do both for
the same session or people get charged twice. **Recommendation: let YCBM take the payment.**

---

## Step 5 — turn on the money-safety basics
- **Radar** (fraud) is on by default — leave it on
- Email receipts: Settings → Customer emails → **turn on successful payments + refunds**
- Add her logo (the amber speech bubble) under Branding so receipts look like her
- Set the brand colour to **#F5A623**

---

## Step 6 — test before announcing
1. Use Stripe **test mode** first — card `4242 4242 4242 4242`, any future expiry, any CVC
2. Book a test session end-to-end: pay → redirect → does she get the email?
3. Then switch to **live mode** and do **one real $25 payment** with her own card
4. Refund it from the dashboard so she sees how refunds work — she'll need to do that herself
   one day, and it's better she's seen it once

---

## Her privacy / tax worry — answer it straight
She asked repeatedly about IRS monitoring and wanted to avoid it "as much as possible."
The honest answer, and Topher should give it plainly:

> **Any** money she earns is reportable — Stripe, Zelle, Chime, CashApp or cash. Stripe issues
> a **1099-K** over the federal threshold. The others simply don't send a form; the income is
> still taxable either way. Picking a processor to dodge a form isn't tax planning, it's
> exposure. Stripe also gives her clean records so she can **deduct her expenses** — which
> usually saves more than the worry costs.

⚠️ **Do not help her structure payments to avoid reporting.** If she wants real tax advice,
she needs an accountant — an hour with one is cheap and she'll likely come out ahead.

---

## ♻️ Reusable for the next client
Same six steps. The only things that change per client are the product names/prices, the
statement descriptor, the brand colour, and the website URL. Budget 20 minutes with the
client on a screen-share. **Never take their credentials — drive while they type the
sensitive fields.**

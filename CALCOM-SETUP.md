# Cal.com setup — replaces the locked YouCanBook.me page
**Why we moved:** her YCBM page returns `HTTP 423 Locked` — it was never activated (matches
"I couldn't get it live"). YCBM also charges ~$12/mo to take payments.
**Cal.com free plan includes Stripe payment acceptance**, unlimited event types, and 100+ app
integrations, at $0. Nothing is live on YCBM, so there is nothing to migrate.

---

## What only SHE can do (~10 min, screen-share)
1. **Create the account** at cal.com with **her** email → username **`letstalk`**
   (booking page becomes `cal.com/letstalk`)
2. **Connect her calendar** — Google (or Outlook). One click, but it needs her login.
   *This is the whole point: Cal.com then only ever offers times she is genuinely free.*
3. **Connect Stripe** — Apps → Stripe → Install → authorize. Needs her Stripe to exist first
   (see STRIPE-SETUP.md; also her own 5 minutes).

⚠️ Free plan is **1 user**, so there's no team seat to invite Topher into. Either she shares
access, or Topher drives the rest on a screen-share. Everything below he can do for her.

---

## Her answers, 2026-09-07 — what they lock in

| Asked | She said | What it changes |
|---|---|---|
| Would you ever meet in person? | **Yes** | Google Business Profile is now legitimate — see `GBP-SETUP.md`. Was ruled out before. |
| Do you want video? | **Yes** | Video stays the default in the room. All four event types keep the `session.html` link. |
| Book ahead, or catch you now? | **Both** | Keep *Talk now* **and** the scheduled types. Both modes ship. |

⚠️ **"Both" is the one to get right.** *Talk now* only works if it reflects real availability —
she has a full-time job she travels for. Set its availability to a **narrow, honest window**
(the evenings she's genuinely at a laptop), not her whole calendar. A "talk now" that nobody
answers is worse than not offering it: the customer has already paid.

---

## Event types to create (Topher builds these)

| Event type | Duration | Price | Notes |
|---|---|---|---|
| **Talk now — 15 minutes** | 15 min | **$25** | Short notice window (see below) |
| **A proper conversation — 30 minutes** | 30 min | **$40** | The default; feature this one |
| **The long one — 1 hour** | 60 min | **$75** | |
| **In Your Corner — monthly members** | 60 min | **$0** | Free to book; the $150/mo is billed in Stripe separately. Hide from the public page, share the link with members only. |

**Per event type:**
- Location → **Link meeting / custom** → the room page:
  `https://www.lets-talk2.me/session.html?room={UID}` *(Cal.com substitutes the booking UID,
  so every booking gets its own private room)*
- **Payment**: Apps → Stripe → set price → **require payment before the booking confirms**
- **Buffer**: 10 min after each session (she'll need it, and it prevents back-to-backs)
- **Minimum notice**: 2 hours for the 30/60-min types · **15 minutes** for "Talk now"
- **Booking questions**: name, email, and one required field —
  **"What would you like to talk about?"** (long text). She walks in already knowing the topic.
- **Confirmation + reminder emails**: on. Reminder 1 hour before.
- **Cancellation policy** text: link `refunds.html`

---

## Availability
- Set a weekly schedule around her day job — evenings and weekends to start
- ✅ Turn on **"Only show busy/free from calendar"** so her real commitments block automatically
- Timezone: **America/Chicago**, with "show times in the visitor's timezone" on
- She can change all of this from the Cal.com phone app while travelling — no need to ask Topher

---

## Wire it into the site (Topher, after the above)
Replace the `letstalk30.youcanbook.me` links in `index.html`:
- Header + hero "Talk to Deanna" → `https://cal.com/letstalk`
- 15-minute card → `https://cal.com/letstalk/talk-now`
- 30-minute card → `https://cal.com/letstalk/30min`
- Hour upsell line → `https://cal.com/letstalk/60min`
- Monthly card → Stripe subscription payment link (not Cal.com)

Optional: embed Cal.com inline on the site instead of linking out — one script tag, keeps
people on her page. Do this once the basics are proven working.

---

## Test before announcing
1. Book each event type as a customer, paying with Stripe **test card `4242 4242 4242 4242`**
2. Confirm: payment taken → booking appears on her calendar → confirmation email arrives →
   the room link works and opens `session.html`
3. Cancel one to check the refund path
4. Then switch Stripe to live and do one real $25 booking end-to-end

---

## ♻️ Reusable
Cal.com free + Stripe is the standard scheduling stack for the ready-made business package:
$0/month for the client, payment at booking, and the room link pattern above works for any
service where someone pays and then talks to someone.

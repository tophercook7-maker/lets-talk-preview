# Let's Talk — Launch Runbook
Everything needed to turn the site into a working business. Built as the template for
Topher's first **ready-made business** package — steps marked ♻️ are reusable for the next client.

---

## 0. Where it stands
| Piece | Status |
|---|---|
| Website (design, copy, her photo, custom photography) | ✅ live |
| Hosting (GitHub Pages, free, HTTPS) | ✅ live |
| Prices decided ($25 / $40 / $150, $75 hr upsell) | ✅ |
| Booking (YouCanBook.me) | ⚠️ exists, unpaid, not wired |
| Payments | ❌ not started |
| Private room (chat/voice/video) | ❌ not started |
| Legal pages | ✅ built (required by Stripe) |
| Business phone | ❌ not started |
| Domain pointed at the site | ⏳ needs her Squarespace access |

---

## 1. Stripe — must be in HER name
⚠️ **Not Topher's account.** Her clients' money is her income. Processing it through
MixedMakerShop's Stripe means Topher gets 1099'd for her revenue and is holding client funds.
Wrong on tax, wrong on liability.

**What she needs to hand over (15 min, screen-share or in person):**
- Legal name + address
- SSN or EIN (Stripe requires it — this is her earlier privacy worry; see §1a)
- Bank account + routing number for payouts
- The website URL (Stripe checks it — this is why the legal pages exist)

**Products to create** (exact — matches the site):
| Product | Price | Type |
|---|---|---|
| Let's Talk — 15 minutes | $25 | one-time |
| Let's Talk — 30 minutes | $40 | one-time |
| Let's Talk — 1 hour | $75 | one-time |
| In Your Corner — monthly | $150/mo | recurring, cancel anytime |

Then create a **Payment Link** per product, set each link's **success URL** to the private
room page (§3), and paste the links into `index.html` (they replace the YouCanBook.me hrefs).

### 1a. Her privacy/tax worry — the honest answer
She asked repeatedly about IRS monitoring and wanted to "wait on that as much as possible."
Be straight with her: **any** money she earns is reportable whether it arrives by Stripe,
Zelle, Chime, CashApp or cash. Stripe issues a 1099-K over the federal threshold; the others
just don't send the form — the income is still taxable. Choosing a processor to avoid a form
isn't tax planning, it's exposure. Stripe is the cleanest option and it lets her deduct
expenses properly. **Do not help her structure payments to avoid reporting.**

---

## 2. Booking — Cal.com (free) + Stripe ♻️
⚠️ **Her YouCanBook.me page returns HTTP 423 Locked** — it was never activated, which matches
"I couldn't get it live." YCBM also charges ~$12/mo for payments.
**Moved to Cal.com:** free plan includes Stripe payment acceptance, unlimited event types and
100+ integrations at $0. Nothing was live on YCBM, so nothing to migrate.
See **CALCOM-SETUP.md** for the exact event types, prices, buffers and room-link pattern.

---

## 3. The private room — one link, three ways ♻️
**Jitsi Meet** — free, unlimited, no account for either side, and it does **video + voice +
text chat in one room**. One thing for her to keep up with.
- Room URL pattern: `https://meet.jit.si/LetsTalk-<random>`
- After payment, the customer lands on `session.html`, which generates/holds the room link
- She joins the same link from laptop or phone
- Camera off = it's a phone call. Text only = it's a chat. Same room.

**Alternative if Jitsi feels rough:** Whereby free tier gives one permanent room
(`whereby.com/letstalk`) — simpler for her, one fixed link forever.

---

## 4. Business phone — Google Voice (free) ♻️
- Free US number, rings her **laptop and phone at once** (she wanted laptop calling)
- Keeps her personal number private
- Voicemail transcripts to email, and she can text from it
- Setup: voice.google.com → pick a number → link her mobile → done, ~10 min
- ❌ Skip a 1-800: $15–30/mo and it reads "call centre," which is the opposite of her brand

---

## 5. Google Business Profile — ⚠️ probably doesn't qualify
Google requires **a location customers visit** or **travel to the customer**. Deanna is
100% remote by choice. Purely-online businesses don't qualify and listings get suspended.
**Don't build the plan on GBP.** What actually works for a remote coach:
1. **LinkedIn** — the #1 channel for a business coach. Her 20 years of turnarounds is the content.
2. **Coaching directories** — Noomii, Coach.me, LifeCoachHub, Bark, Thumbtack
3. **The site's own SEO** — already has schema, meta, canonical; submit to Search Console
4. **Her own network + referrals** — fastest by far at this stage
5. Facebook/Instagram business pages (she asked for the social push)

*If she ever offers local in-person sessions in Hot Springs, GBP opens up legitimately.*

---

## 6. Reviews without meeting anyone ♻️
She has no in-person contact, so no tap cards. Instead:
- After a paid session, an automatic email: "how did that go?" + a review link
- Collect on **Google** only if a GBP exists (see §5) — otherwise **LinkedIn recommendations**
  and written testimonials for the site
- Add a testimonials section to the site once there are 3+. **Never invent them.**

---

## 7. Legal — required before Stripe approves live payments ♻️
Built and live: `terms.html`, `privacy.html`, `refunds.html`, linked in the footer.
⚠️ Templates, not legal advice — she should read them and confirm they match how she works,
especially the cancellation window and the "not therapy" clause.

---

## 8. Analytics
- Google Search Console (verify the domain, submit sitemap)
- GA4 or Plausible — light touch; what matters early is bookings, not pageviews

---

## ♻️ The reusable package — "business in a box"
What this becomes for the next client:
1. Website from this template (swap brand colour, copy, photos)
2. Custom photography generated locally with mflux — free, ~2 min per image
3. Stripe products + payment links **in the client's own name**
4. Booking wired to payment (YCBM or Cal.com)
5. One private room (Jitsi) for chat/voice/video
6. Google Voice business line
7. Legal pages
8. Directory + social presence (GBP only where it legitimately qualifies)
9. Review flow

**Price it as a package, not hours.** The build here was quoted at $400 — that is well under
what this is worth once it's a repeatable system. Suggested next-client pricing: setup fee
plus a small monthly for hosting/changes (see [[web-design-lane]] and the We Care $199/mo
model already floated).

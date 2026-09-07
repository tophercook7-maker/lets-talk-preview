# Do now — everything paste-ready

Ordered so nothing waits on anything else. The only steps needing Deanna are marked **[HER]**,
and each is under a minute.

⚠️ I can't create accounts or type passwords — those steps are yours. Everything else below is
written out so you're pasting, not deciding.

---

## 1. One Google account owns the business — make it first (5 min)

**Create a new Gmail for the business.** Not yours, not hers.

Suggested: `letstalkwithdeanna@gmail.com` (or `letstalk2me@gmail.com`)

Why a new one, and this matters more than it looks:
- **Google Voice numbers don't move between accounts.** Put the number on your account and
  she can never cleanly take it. Put it on hers and you can't set anything up while she
  travels. A business account solves both — you build it now, hand her the whole account
  later, she changes the password and owns everything in one move.
- The **Google Business Profile** lives in the same account.
- If she ever leaves, she takes one login and nothing breaks.

Set the recovery email to hers so she can always get back in.

---

## 2. Google Voice number — search these exact words (10 min)

**voice.google.com → For personal use → Choose a number → search by area code `501`**
(Hot Springs. It reads local, which is what the Google listing wants.)

Google Voice converts letters to keypad digits and filters its available pool, so you can
type a word into the search. Short words hit far more often — a 4-letter pattern has many
more matches than a 7-letter one.

**Search in this order and take the first decent hit:**

| Type this | Finds numbers containing | Odds |
|---|---|---|
| `TALK` | **8255** | best — try this first |
| `LETS` | **5387** | best |
| `CHAT` | **2428** | best |
| `HELP` | **4357** | good |
| `TALKS` | **82557** | decent |
| `COACH` | **26224** | decent |
| `TALKNOW` | **825-5669** | long shot, but perfect if it lands |
| `TALK2ME` | **825-5263** | the dream — matches lets-talk2.me exactly |

**The one to want: `501-825-5263` = 501-TALK2ME.** Almost certainly gone, but check — it costs
one search and it would match the domain perfectly.

Also worth knowing: **phone systems ignore anything past the 7th digit.** So a number ending
`538-7825` can be advertised as **LETS-TALK** even though "LETSTALK" is eight letters — the K
is never dialled. Same trick as 1-800-FLOWERS. If you see `5387825` anywhere in the list,
take it immediately; that's the best possible outcome.

If nothing good appears in 501, refresh the list a few times — the pool rotates. Only then
widen to a nearby Arkansas area code.

**[HER] — the verification code.** Google Voice has to link to a real US mobile. Use **her**
cell, `(815) 666-6813`, not yours:
- the line then rings *her* phone, which is what you want anyway
- your own cell may already be tied to a Google Voice account, which would block it

Text her: *"Setting up your business number — Google's about to text you a 6-digit code, send
it to me when it lands."* That's her entire involvement.

⚠️ If she already has a Google Voice account on that cell it'll conflict. Ask first if unsure.

**Then:** settings → forward calls and texts to her phone, voicemail transcripts on, and put
the number in `session.html` (`var PHONE = ""`) and on the Google listing.

---

## 3. Google Business Profile — paste-ready (15 min + verification wait)

Full walkthrough in `GBP-SETUP.md`. The content, ready to paste:

**Name:** `Let's Talk with Deanna`
⚠️ Exactly that. No "coach Hot Springs" added — keyword stuffing is the #1 suspension cause.

**Primary category:** search the picker for `Business management consultant`.
Closest alternatives if that's missing: *Business development service*, *Consultant*, *Life coach*.

**Location:** "Do you have a location customers can visit?" → **No** → service-area business.
Her address is collected but never shown.

**Service area:** Hot Springs. Add Hot Springs Village, Benton, Malvern only if she'd drive there.

**Phone:** the Google Voice number from step 2. **Website:** `https://lets-talk2.me`

**Description** (fits Google's 750-character limit):

```
Deanna Kramar has spent more than 20 years helping businesses — and the
people running them — get unstuck. Operational strategy, P&L, sales and
market share, cost control, leadership development, and turnarounds.

Let's Talk is her one-on-one coaching and mentoring practice: a straight
conversation with someone who has actually done the work, with no
judgment and no script. Book 15 minutes when you need a quick answer, 30
for a proper conversation, or an hour when 30 minutes won't cover it.
Ongoing monthly support is available.

Sessions are by video, voice or text from anywhere, or in person around
Hot Springs. Chicago-raised, Hot Springs-based.
```

**Services:**
| Service | Price |
|---|---|
| Talk now — 15 minutes | $25 |
| A proper conversation — 30 minutes | $40 |
| The long one — 1 hour | $75 |
| In Your Corner — monthly | $150/mo |

**[HER] Verification.** Google picks the method — usually a video for service-area businesses,
sometimes a postcard. Takes a few days. Then: **Users → Add → you as Manager.**

⚠️ Don't add photos that look AI-generated. Lead with her real photo (`img/deanna.jpg`).

---

## 4. Stripe and Cal.com — still hers

`STRIPE-SETUP.md` and `CALCOM-SETUP.md` have every field. The message is in
`DEANNA-SETUP-MSG.txt`. She keeps the Stripe login; you get the Cal.com one.

The moment Cal.com exists, fill the four `CAL` urls in `_build/build.py`, run
`python3 _build/build.py`, push — the site goes from "booking opens shortly" to live and
taking money in one step.

---

## ✅ Already done, needs nobody
- Domain live, HTTPS: **https://lets-talk2.me**
- Dead booking links fixed — every CTA now lands somewhere real
- Site says she meets people locally (hero, FAQ, structured data) so the Google listing matches
- Legal pages live — Stripe checks for these before approving
- Private room built — text, voice and video in one link

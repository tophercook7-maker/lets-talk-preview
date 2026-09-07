# Deann — lets-talk2.me — Build Brief
Source: Starbucks conversation, recorded 2026-09-06 09:09 AM (watch memo, first ~20 min).
Lead source: **she saw Topher's ad** ("I'm glad you ran that ad and I saw it").

## The deal
- **$450 total** = **$400 website** + **$50 promo video**
- ⚠️ She is **hesitant on the video** — wants to see if the business takes off first ("Let's talk on that. What I want to do is see if it even takes off"). **Treat the video as optional/later; the $400 site is the committed piece.**
- Timeline Topher quoted: **3–4 days max**
- Topher promised her a first look **"in the next four hours-ish"** from ~10:30 AM Sept 6.

## Who she is — ✅ CONFIRMED from her Google Sites draft
- **Deanna Kramar** — **business coach, mentor, and trusted advisor, 20+ years of experience.**
- Brand: **"LET'S TALK"** — remote coaching/advisory conversations.
- **Existing booking link (LIVE): https://letstalk30.youcanbook.me/** — YouCanBook.me, "30" = 30-minute sessions.
- Her draft site: Google Sites (unpublished) at `sites.google.com/u/0/d/12GIy0KfzzvVupN5tx2LPG5pVcCh2BvYo` — screenshots saved to `~/Desktop/00_Inbox - Review/deanna-current-site-*.png`.
- Has a **full-time job she travels for**; this is a side venture she's testing.

## ⭐ HER OWN COPY — verbatim, it's GOOD, keep her voice
> Brain feeling like 27 tabs are open… and you can't find where the music is coming from? 😅 Yeah, same.
>
> **Good news:** You don't have to figure it all out alone.
>
> Need advice? Got an issue you're stuck on? Or just need someone to talk to… **Let's Talk.**
>
> Sometimes talking to friends and family isn't enough—or comes with judgment, pressure, or the dreaded *"I told you so."* Here, you get **real conversation, honest guidance, and zero judgment.**
>
> And if you've ever wondered how successful people get there—and stay there… They don't do it alone. They work with **coaches and mentors** who help them align purpose, direction, and action.
>
> **You deserve that too!**
>
> With **20+ years of experience** as a business coach, mentor, and trusted advisor, I'm here to help you:
> ✨ Find clarity and direction · ✨ Work through challenges · ✨ Stay accountable and focused · ✨ Build the life and success you actually want
>
> ✔ Less stress · ✔ Better focus · ✔ Clearer path forward
>
> **The best part? It starts with a simple conversation.**
>
> Let's Talk… Set up your appointment today. **It's time to invest in YOU.**

⚠️ Bugs in her draft to fix: the footer link is mangled (`llets-talk2.meets-talk2.com`); hero image looks like stock/AI; no pricing anywhere; QR code present but unlabeled.

## 🎯 THE ACTUAL TECHNICAL GAP
Her "three dots" = **website → YouCanBook.me scheduling → payment.** YouCanBook.me *does* support paid bookings via **Stripe** — that's the connection she couldn't make. This is the single highest-value thing to solve for her.
⚠️ No pricing decided yet — she must set a session price before payment can be wired.
- **Remote only — "I'm not doing it in person."** No local/in-person service, no walk-ins.
- Travel: **leaves Tuesday, back the 26th.** Email + text only in between.
- Self-described not tech-savvy: *"I'm not the savviest in the world."*

## What she asked for
1. **Website** — she has lets-talk2.me on **Squarespace** (registered 2025-07-16, expires 2027-07-16, Google/Squarespace nameservers). Currently shows only *"We're under construction."*
2. **Booking / scheduling** — she got it partly set up on Squarespace but couldn't get it live.
3. **Payments wired to the booking** — *"connecting the payment to the scheduling is where it got stuck."* This is her core frustration: three dots she can't connect (site → scheduling → payment).
4. **QR code** — *"I do want like a QR code so I can throw that out there."*
5. **Google Business Profile** — she tried to set one up, couldn't. Topher: "I can do all that too."
6. **Social push** — Facebook + Instagram, like Topher's own posts.
7. Topher offered **tap cards** — she declined-ish (not doing in-person), but a **review link** was the point: she needs a way to collect reviews without meeting people.

## Payments — UNRESOLVED, needs a decision
- Topher recommended **Stripe** (knows it inside out, already set up for MMS).
- ⚠️ **She has privacy/tax concerns** — asked repeatedly about IRS/government monitoring, money laundering flags, whether every transaction is watched. Wants to "wait on that as much as possible."
- Alternatives discussed: **Zelle, Chime, CashApp**. She has used Chime before (VA payments for caring for her dad).
- Topher's stance: *"I don't really like handling people's accounts — it's safer not to."* He'll **build it with her live** (5 min, text him first), not take her credentials.
- **Decision still open.** Recommend Stripe for anything booked online; be straight with her that legitimate income is reportable regardless of processor.

## Her homework (the blocker)
Topher asked her to **email him a "story"**: a bio about herself + what she wants to achieve, written like she's talking to an editor. *"More information is better."* **Nothing can be finalized on content until this arrives.**
- Her email was given verbally but the recording is garbled — sounded like "…dr…megadon…". **Get the exact address from Topher's phone/card.** She handed him her card.

## Build decisions still to make
- **Hosting:** her domain is on Squarespace DNS. Either (a) point it at what we build (GitHub Pages like We Care, or Mac + Cloudflare Tunnel), or (b) she keeps paying Squarespace. Topher's call.
- **Stack:** match the We Care preview pattern (static site + booking + Stripe) — proven and fast.

## Notes
- She is testing viability, not scaling — keep it lean, cheap to run, easy for her to change.
- Do NOT invent credentials, certifications, or client results. She hasn't given any.

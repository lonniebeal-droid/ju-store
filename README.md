# JU Storefront (`ju-store`)

Public repository and GitHub Pages front door for the canonical **JU Storefront** — the unified commercial hub for JU audiobooks, music releases, books, AI platforms, and direct services.

---

## 🌐 Live Deployments

| Component | URL | Status | Description |
| :--- | :--- | :--- | :--- |
| **GitHub Pages Front Door** | [`https://lonniebeal-droid.github.io/ju-store/`](https://lonniebeal-droid.github.io/ju-store/) | 🟢 **HTTP 200** | Public redirect front door hosted on GitHub Pages |
| **Canonical Storefront** | [`https://ju-storefront-5hjkrj.v2.appdeploy.ai/`](https://ju-storefront-5hjkrj.v2.appdeploy.ai/) | 🟢 **HTTP 200** | Full-featured storefront with interactive audio preview, catalog, and checkout links |

---

## 🏛️ Architecture & Redirection

This repository implements a lightweight, zero-latency redirect architecture:
- **`index.html`**: A standards-compliant static entry point featuring:
  - `<meta http-equiv="refresh" content="0;url=https://ju-storefront-5hjkrj.v2.appdeploy.ai/">` for immediate browser redirection.
  - `<link rel="canonical" href="https://ju-storefront-5hjkrj.v2.appdeploy.ai/">` for SEO authority consolidation.
  - Plain-text fallback anchor link (`<a href="...">Enter store</a>`) ensuring accessibility across all browser modes.
- **Hosting**: GitHub Pages configured on branch `main` at root `/`.

---

## 📦 Storefront Catalog Breakdown

### 1. 🎧 JU Audiobooks (Payhip Digital Distribution)
- **No Map Given** — [Payhip Checkout](https://payhip.com/b/1z2xi)
- **Street-Level Survival Vol. 1** — [Payhip Checkout](https://payhip.com/b/AnDrk)
- **Black Law Vol. 1** — [Payhip Checkout](https://payhip.com/b/lBpzb)

### 2. 🎵 JU Music Store — Albums & Singles
Streaming and digital download availability across Spotify, Apple Music, and DistroKid:
- **LBB** (Single) — [Apple Music](https://music.apple.com/us/album/lbb-single/6772349111) · [DistroKid](https://distrokid.com/hyperfollow/juju65/lbb)
- **Still Standin in the A** — [Apple Music](https://music.apple.com/us/album/still-standin-in-the-a/6795197082)
- **Broken Halo Blues** — [Apple Music](https://music.apple.com/us/album/broken-halo-blues/6792440662) · [Spotify](https://open.spotify.com/album/1AVCwhHla9aVQPmaxZEHwy)
- **Sacrifice Sessions** — [Apple Music](https://music.apple.com/us/album/sacrifice-sessions/6795090605) · [Spotify](https://open.spotify.com/album/53CHSPtYsIwW1J09RWJaeY)
- **Credit Is Power** — [Apple Music](https://music.apple.com/us/album/credit-is-power/6797147825) · [Spotify](https://open.spotify.com/album/1X0VG8Imh2wzo0XzfLPHsc)
- **Kindergarten Early Learning** — [Apple Music](https://music.apple.com/us/album/kindergarten-early-learning/6794077989)

### 3. 📚 JU Books & Digital Library
- **Black Law Vol. 1** — [Gumroad Edition](https://atlantafinest.gumroad.com/l/BlackLawvol1)
- **Street Level Survival** — [Gumroad Edition](https://atlantafinest.gumroad.com/l/streetlevelsurvival)
- **Amazon Kindle & Paperback Editions**:
  - [ASIN B0H9HC4VSN](https://www.amazon.com/gp/product/B0H9HC4VSN)
  - [ASIN B0HB6MV6N8](https://www.amazon.com/gp/product/B0HB6MV6N8)
  - [ASIN B0HBQL8G68](https://www.amazon.com/gp/product/B0HBQL8G68)
  - [ASIN B0HBRF5K86](https://www.amazon.com/gp/product/B0HBRF5K86)
  - [ASIN B0HCKCX3R5](https://www.amazon.com/gp/product/B0HCKCX3R5)

### 4. 🤖 JU Projects & Platforms
- **Jessie AI Receptionist**:
  - Live 24/7 Voice Demo Line: [`+1 (770) 847-4325`](tel:+17708474325)
  - Four Verified Stripe Hosted Checkout Tiers:
    - Founding Partner: `$199` setup + `$299/mo` ([Stripe Checkout](https://buy.stripe.com/8x29AV63P83R5Wg56adIA00))
    - Essentials: `$1,500` setup + `$499/mo` ([Stripe Checkout](https://buy.stripe.com/00w9AVfEp83R70kPUdIA01))
    - Growth: `$2,500` setup + `$899/mo` ([Stripe Checkout](https://buy.stripe.com/bJefZjdwh83R4Sc1TYdIA02))
    - Pro: `$4,500` setup + `$1,499/mo` ([Stripe Checkout](https://buy.stripe.com/28E28tak5gAnfwQeGKdIA03))
- **CashRides Atlanta**:
  - Peer-to-peer rideshare and rental marketplace ([Live Web App](https://cashridesatlanta.netlify.app/))

### 5. 📞 Direct Inquiries & Social
- **Phone / SMS**: [`(706) 386-9010`](tel:7063869010)
- **Instagram**: [`@itsjujuatl`](https://www.instagram.com/itsjujuatl)
- **YouTube**: [`@itsjujuatl`](https://youtube.com/@itsjujuatl)

---

## 🧪 Automated Verification Suite

Run the automated verification suite to validate local file structure, remote GitHub Pages redirect response, canonical AppDeploy reachability, and catalog link invariants:

```bash
python3 test_storefront.py
```

### Test Coverage (24 Checks)
1. `index.html` file existence.
2. `meta http-equiv="refresh"` validity and target URL match.
3. `<link rel="canonical">` correctness.
4. Document title (`<title>JU Storefront</title>`).
5. Fallback anchor link presence and href validation.
6. GitHub Pages live HTTP status 200 check.
7. GitHub Pages response body contains canonical AppDeploy URL.
8. Canonical AppDeploy storefront live HTTP status 200 check.
9. Storefront page title verification (`JU | Music, Books, AI, Business`).
10–14. Required section headers presence (`JU Audiobooks`, `JU Music Store`, `JU Books & Digital Library`, `JU Projects`, `Contact JU`).
15–18. Live Stripe Checkout link integrity (4 tiers: Founding, Essentials, Growth, Pro).
19. Jessie AI Receptionist live telephony demo link (`tel:+17708474325`).
20–22. Payhip digital audiobook product link integrity (`1z2xi`, `AnDrk`, `lBpzb`).
23–24. Gumroad digital book product link integrity (`BlackLawvol1`, `streetlevelsurvival`).

**Last verified:** 2026-09-25 — **24/24 PASS** (Grok Portfolio Finisher). Essentials Stripe path aligned to live AppDeploy HTML.

---

## 🛡️ JU System Governance

Part of the **JU Ecosystem**.
All updates are tracked in the canonical **JU_SYSTEM Master Operations Dashboard** (`1gO_3FvISUQ7lktda8fSiOlWX7MizbGyJExcHoHrg-Qk`) and mirrored in `ju-command-center`.

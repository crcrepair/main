# CRC Repair – Facebook Ads landing page

A single-file landing page (`index.html`) with a quote request form that collects
**name, phone, email, device and notes**.

## Setup (2 values to fill in)

Open `index.html` and edit `window.LP_CONFIG` near the top:

| Setting | What to put there |
|---|---|
| `FORM_ENDPOINT` | Where submissions go. Easiest option: create a free form at [formspree.io](https://formspree.io), set it to email you, and paste its URL (e.g. `https://formspree.io/f/abcd1234`). |
| `FB_PIXEL_ID` | Your Meta Pixel ID from Events Manager. The page fires `PageView` on load and `Lead` on a successful submission, so you can optimise ads for leads. |

Until `FORM_ENDPOINT` is set, the form shows a "not connected yet" message instead of sending.

## What's included

- Mobile-first layout (most Facebook ad traffic is on phones)
- Field validation with inline error messages
- Spam honeypot field
- UTM parameters and `fbclid` from the ad link are sent along with each lead
- Thank-you message shown in place of the form after submitting
- `noindex` so the ad page doesn't show up in Google

## Hosting

It's a static file, so it can go anywhere: GitHub Pages, Netlify, Cloudflare Pages,
or uploaded to your existing site (e.g. `crcrepair.co.uk/quote/`).

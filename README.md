# CrC Repair – Facebook Ads landing page

A landing page (`index.html`, with the logo in `assets/`) with a quote request form that collects
**name, phone, email, device and notes**.

## Standalone page setup (2 values to fill in)

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

## Contact Form 7 (WordPress)

The `contact-form-7/` folder has the same form ready for Contact Form 7.

1. **Contact → Add New**, name it e.g. "Facebook Ads enquiry".
2. **Form tab:** delete the default content and paste in `contact-form-7/form.txt`.
3. **Mail tab:** fill in the fields from `contact-form-7/mail.txt`:
   - To: `support@crcrepair.co.uk`
   - Subject: `Facebook Ads enquire`
   - Additional headers: `Reply-To: [your-email]` (so hitting *Reply* answers the customer)
   - From: `[_site_title] <wordpress@crcrepair.co.uk>`. Keep this on your own domain:
     sending "from" the customer's address gets emails flagged as spam.
4. **Save**, then put the shortcode CF7 gives you on your landing page.
5. **Styling:** paste `contact-form-7/style.css` into Appearance → Customize → Additional CSS.
6. **Facebook Lead tracking:** add `contact-form-7/facebook-pixel-lead.html` to the page
   (Custom HTML block). It needs the Meta Pixel already installed on the site.

The hidden `utm_*` and `fbclid` fields pick up the values from your ad link automatically,
so each email shows which campaign/ad the enquiry came from.

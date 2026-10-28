# CrC Repair – Facebook Ads landing page

A landing page (`index.html`, with the logo in `assets/`) with a quote request form that collects
**name, phone, email, device and notes**.

## Standalone page setup (3 values to fill in)

Open `index.html` and edit `window.LP_CONFIG` near the top:

| Setting | What to put there |
|---|---|
| `FORM_ENDPOINT` | Where submissions go. Easiest option: create a free form at [formspree.io](https://formspree.io), set it to email you, and paste its URL (e.g. `https://formspree.io/f/abcd1234`). |
| `FB_PIXEL_ID` | Your Meta Pixel ID from Events Manager. The page fires `PageView` on load and `Lead` on a successful submission, so you can optimise ads for leads. |
| `GTM_ID` | Your Google Tag Manager container ID (`GTM-…`), for Google Analytics tracking. |

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

## WordPress version (Gutenberg blocks + Contact Form 7)

Files: `wordpress/` (page blocks + CSS) and `contact-form-7/` (form + mail settings).
All text uses the **Montserrat** font (loaded from Google Fonts by the CSS).

### 1. Create the form
1. **Contact → Add New**, name it e.g. "Facebook Ads enquiry".
2. **Form tab:** delete the default content and paste in `contact-form-7/form.txt`.
3. **Mail tab:** fill in the fields from `contact-form-7/mail.txt`:
   - To: `support@crcrepair.co.uk`
   - Subject: `Facebook Ads enquire`
   - Additional headers: `Reply-To: [your-email]` (so hitting *Reply* answers the customer)
   - From: `[_site_title] <wordpress@crcrepair.co.uk>`. Keep this on your own domain:
     sending "from" the customer's address gets emails flagged as spam.
4. **Messages tab (optional):** set the success message from the bottom of `mail.txt`.
5. **Save** and note the form ID in the shortcode CF7 shows (`[contact-form-7 id="…"]`).

### 2. Add the styles
Paste `wordpress/landing-page.css` into **Appearance → Customize → Additional CSS**
(block themes: **Appearance → Editor → Styles → ⋮ → Additional CSS**).

### 3. Build the page
1. Upload `assets/crc-repair-logo.webp` (or `.png`) to **Media**.
2. **Pages → Add New**. Open the ⋮ menu → **Code editor**, paste in
   `wordpress/landing-page-blocks.html`, then switch back to the **Visual editor**.
3. In the Shortcode block, replace `REPLACE_WITH_FORM_ID` with your form's ID
   (or replace the whole shortcode with the one CF7 gave you).
4. Click the logo image → **Replace** → pick the logo you uploaded.
5. Under Page settings → **Template**, choose a blank / full-width / "no header & footer"
   template if your theme has one, so the ad page has no menus to distract visitors.
6. Optional: if you use Yoast or Rank Math, set this page to **noindex** so the ad page stays out of Google.

The last block on the page (Custom HTML) does the tracking: Google Tag Manager events (see
below) and a Facebook **Lead** event each time the form is sent. It needs the Meta Pixel already installed on the site (e.g. the "Meta Pixel for
WordPress" plugin).

The hidden `utm_*` and `fbclid` form fields pick up the values from your ad link
automatically, so each email shows which campaign/ad the enquiry came from.

## Google Analytics tracking

Both versions push two events to Google Tag Manager: `quote_button_click` (button clicked)
and `generate_lead` (enquiry actually sent), each with the chosen `device`.
Step-by-step setup for Tag Manager and GA4: [`docs/google-analytics-setup.md`](docs/google-analytics-setup.md).

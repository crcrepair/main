# Tracking the "Get my free quote" button in Google Analytics (via Google Tag Manager)

The landing page already sends two events to Google Tag Manager. You only need to set up
Tag Manager and Analytics to receive them.

| Event | When it fires | Use it for |
|---|---|---|
| `quote_button_click` | Every click on **Get my free quote**, even if a field is missing | Seeing how many people *try* to send |
| `generate_lead` | Only when the enquiry is **actually sent** | Counting real leads (mark this one as a key event) |

Both events also carry:
- `device`: what they picked in the Device dropdown (e.g. `iPhone`)
- `form_name`: always `facebook_ads_quote`, so you can tell this form apart from others on your site

> Menu names in Google's tools move around now and then. If a button isn't exactly where
> described, the names in **bold** are what to look for.

---

## Step 1 – Get your Google Analytics 4 Measurement ID

Skip this if you already have GA4 for crcrepair.co.uk; just find the ID (step 4 below).

1. Go to <https://analytics.google.com> and sign in with your Google account.
2. **Admin** (cog icon, bottom left) → **Create** → **Property**.
3. Property name: `CrC Repair`, time zone: United Kingdom, currency: British Pound. Click through the business questions.
4. Choose platform **Web**, enter `crcrepair.co.uk`, stream name `CrC Repair website`, then **Create stream**.
5. Copy the **Measurement ID**. It looks like `G-ABC123XYZ`. You'll need it in Step 4.

## Step 2 – Create a Google Tag Manager container

1. Go to <https://tagmanager.google.com> → **Create account**.
2. Account name: `CrC Repair`, country: United Kingdom.
3. Container name: `crcrepair.co.uk`, target platform: **Web** → **Create** and accept the terms.
4. Copy the container ID at the top of the screen. It looks like `GTM-ABC1234`.

## Step 3 – Put Tag Manager on the website

**WordPress (recommended).** Pick one of these:
- **Site Kit by Google** plugin: connect it, then turn on **Tag Manager** and pick your container.
- **GTM4WP (Google Tag Manager for WordPress)** plugin: Settings → Google Tag Manager → paste `GTM-ABC1234` → Save.

**Standalone `index.html`.** Open the file and set `GTM_ID: "GTM-ABC1234"` in `window.LP_CONFIG` near the top.

> ⚠️ **Avoid double counting.** If Google Analytics is already on the site some other way
> (e.g. Site Kit's Analytics module adding a `G-` tag, or a theme setting), turn that off once
> Tag Manager is in charge. Otherwise every page view gets counted twice.

## Step 4 – Set up Tag Manager

Do all of this in your container at <https://tagmanager.google.com>.

### 4a. The Google tag (connects Tag Manager to Analytics)
1. **Tags** → **New** → name it `GA4 – Google tag`.
2. **Tag configuration** → **Google Tag** → Tag ID: your `G-ABC123XYZ`.
3. **Triggering** → **Initialization - All Pages**.
4. **Save**.

### 4b. Variables (to read the device and form name)
1. **Variables** → under *User-Defined Variables*, click **New**.
2. **Variable configuration** → **Data Layer Variable** → Data Layer Variable Name: `device`.
3. Name it `DLV – device` → **Save**.
4. Repeat for `form_name`, naming it `DLV – form_name`.

### 4c. Triggers (one per event)
1. **Triggers** → **New** → name it `Event – generate_lead`.
2. **Trigger configuration** → **Custom Event** → Event name: `generate_lead` → *All Custom Events* → **Save**.
3. Repeat with name `Event – quote_button_click` and event name `quote_button_click`.

The event names must match exactly, including lower case and underscores.

### 4d. Tags that send the events to Analytics
1. **Tags** → **New** → name it `GA4 – generate_lead`.
2. **Tag configuration** → **Google Analytics: GA4 Event**.
   - Measurement ID: `G-ABC123XYZ`
   - Event name: `generate_lead`
   - **Event parameters** → **Add parameter**:
     - `device` → value `{{DLV – device}}` (pick it with the brick icon)
     - `form_name` → value `{{DLV – form_name}}`
3. **Triggering** → `Event – generate_lead` → **Save**.
4. Repeat for the button: name `GA4 – quote_button_click`, event name `quote_button_click`,
   the same two parameters, and trigger `Event – quote_button_click`.

### 4e. Test before publishing
1. Click **Preview** (top right), enter your landing page URL and click **Connect**. Your page opens with a Tag Assistant badge.
2. Fill in the form with your own details and click **Get my free quote**.
3. In the Tag Assistant tab you should see `quote_button_click` and then `generate_lead` in the left column.
   Click each one and check that the matching **GA4 –** tag is listed under *Tags Fired*.
4. Click an empty-form submit too: you should only see `quote_button_click` (no lead).

### 4f. Publish
**Submit** (top right) → version name `Landing page lead tracking` → **Publish**.
Nothing goes live until you do this.

## Step 5 – Set up Google Analytics

### 5a. Check the data is arriving
**Reports** → **Realtime**, then submit a test enquiry. `generate_lead` should appear under
*Event count by Event name* within a minute or two. (**Admin** → **DebugView** shows events
from Tag Assistant preview sessions.)

### 5b. Mark the lead as a key event (conversion)
1. **Admin** → **Data display** → **Key events** → **New key event**.
2. Type `generate_lead` → **Save**.

GA4 then counts it as a conversion in reports, and Google Ads can import it later.
Leave `quote_button_click` as a normal event.

### 5c. Make "device" visible in reports
1. **Admin** → **Data display** → **Custom definitions** → **Create custom dimension**.
2. Dimension name: `Device`, scope: **Event**, event parameter: `device` → **Save**.
3. Optionally do the same for `form_name`.

Custom dimensions only collect data from the moment you create them, so set them up early.

### 5d. Where to look
- **Reports** → **Engagement** → **Events**: totals for `quote_button_click` and `generate_lead`.
  Lead count ÷ click count is roughly how many tries get through the form.
- **Reports** → **Acquisition** → **Traffic acquisition**: change the key-event column to
  `generate_lead` to see leads by source (Facebook vs. others).
- **Explore** → **Free form**: rows = `Device`, values = `Event count`, filter event name = `generate_lead`
  to see which devices bring in the most enquiries.

## Step 6 – Tag your Facebook ad links (so GA4 knows leads came from Facebook)

In Meta Ads Manager, edit the ad → **Tracking** → **URL parameters** and paste:

```
utm_source=facebook&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}
```

Facebook fills in the campaign and ad names automatically. GA4 then reports leads under
source `facebook` / medium `paid_social`. The same values also appear at the bottom of each
enquiry email.

## Cookie consent (UK)

Under UK GDPR/PECR, Google Analytics cookies need visitor consent. If you use a cookie banner
plugin (e.g. Complianz, CookieYes, Cookiebot), turn on its **Google Consent Mode** / Tag Manager
integration so Analytics respects the visitor's choice. In Tag Manager, **Admin** →
**Container Settings** → tick **Enable consent overview** to check each tag's consent settings.

## Troubleshooting

| Problem | Likely cause |
|---|---|
| Nothing in Tag Assistant | Tag Manager isn't on the page (Step 3), or the browser's ad blocker is blocking it. Try a private window with extensions off. |
| `generate_lead` shows in Tag Assistant but no **GA4 –** tag fired | Event name typo in the trigger (Step 4c); it must be exactly `generate_lead`. |
| Works in preview, not for real visitors | You haven't **Published** (Step 4f). |
| Page views doubled | Analytics is installed twice (see the warning in Step 3). |
| `Device` dimension is empty | It was created after the events were sent, or the variable name isn't exactly `device`. |

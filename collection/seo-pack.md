# Collection & drop-off page — SEO pack

Page: `https://www.crcrepair.co.uk/collection-booking/` · built 7 Nov 2026 · British English.
Files: `collection_page.html` (Gutenberg markup, paste via Code editor), `collection_schema.html` (JSON-LD),
`build_collection.py` (generator; the FAQ list feeds both page and schema), `preview-desktop.png`.

Facts used (from Gabor, 7 Nov 2026): fee £29.95 covers collection **and** return within 5 miles of the store, £1 per
additional mile; range agreed on the call; collections made by CrC's own fully insured staff; phones, tablets/iPads,
laptops/MacBooks/PCs and games consoles; available from Bournemouth, Farringdon, Surrey Quays, Romford and Whetstone only.

## 1. SEOPress fields (lengths counted by script)

| Field | Text | Length / aim |
|---|---|---|
| SEO title | `Repair Collection & Drop-off from £29.95 \| CrC Repair®` | 54 / <60 |
| Meta description | `We collect your phone, tablet, laptop or console, repair it in store and return it to you. From £29.95 within 5 miles of our London & Bournemouth stores.` | 153 / 150–155 |
| Facebook (OG) title | `We collect, repair and return your device – from £29.95` | 55 / <65 |
| Facebook (OG) description | `Fill in one form. We call to arrange collection, repair your device in store and return it to your door. From £29.95.` | 117 / 110–125 |
| X title | `Repair collection & drop-off from £29.95 \| CrC Repair®` | 54 / <70 |
| X description | `We collect your phone, tablet, laptop or console, fix it in store and bring it back. From £29.95 within 5 miles.` | 112 / <125 |

Canonical: `https://www.crcrepair.co.uk/collection-booking/`. Search Console still shows a few impressions for
`/book-a-collection/` — if that URL is live, 301 it to this page.

## 2. Page structure

```
H1  Book your collection and drop-off repair service   (+ one-line intro, then the Elfsight form 05e681ab, unchanged)
H2  How it works                → H3 × 4 numbered steps with icons (form · call · spanner · van)
    small print: "Our collection and drop-off service is only available from our Bournemouth, Farringdon,
                 Surrey Quays, Romford and Whetstone stores." (each store linked)
H2  What the collection service costs → H3 × 3 (£29.95 · £1 per mile · fixed repair quote)
H2  What we can collect and repair → H3 × 4 device cards with icons, linked to the repair pillars
H2  Why use our collection and drop-off service? → image + copy + H3 × 4 tiles
H2  Collection and drop-off: frequently asked questions → H3 × 10 (first open) — last section, as asked
H2  Ready to book your collection? (CTA: "Book a collection" jumps to the form, "Call 0330 133 1131")
```

Breadcrumb `Home › Collection & drop-off repair service` with BreadcrumbList schema. 1,100 words. 30 internal links
(five store pages, every device pillar, `/come-to-you/`, `/book-a-repair/`, `/store-locator/`, `/lifetime-warranty/`,
`/repair-portal`). Four empty paragraphs from the old page removed.

## 3. Image alt texts and captions

The page uses one existing image now; add the others when you have photos (recommended 1200 × 800, WebP).

| Image | File name suggestion | Alt text | Caption / media description |
|---|---|---|---|
| In page now (media id 27) | `main-page-pic1.webp` | Technician repairing a collected phone at a Pocket Geek Tech Repair store by CrC Repair® | Collected devices are repaired in your local store by our own technicians. |
| Hero / How-it-works | `collection-driver-doorstep.webp` | Pocket Geek Tech Repair driver collecting a customer's phone for repair at their front door | Our own insured drivers collect from your home or workplace. |
| Step 3 | `collection-booked-in-store.webp` | Collected devices being booked in at the Surrey Quays Pocket Geek Tech Repair store | Every device is booked into our system on arrival and tracked in the Repair Portal. |
| Why use us | `collection-screen-repair.webp` | CrC Repair® technician replacing a cracked iPhone screen on a collected device | Same technicians, same parts and the same lifetime warranty on phone screens. |
| Step 4 / CTA | `collection-return-handover.webp` | Repaired laptop handed back to a customer by a CrC Repair® driver | We return your device as soon as it's ready. |
| Open Graph image (1200 × 630) | `collection-og.webp` | Collection and drop-off repair service by CrC Repair® – from £29.95 | — |

To drop an image into the page, add a core Image block inside the relevant `block` group with the alt text above.

## 4. Keyword research and where each term is used

Sources: Search Console via Windsor.ai (12 months, queries landing on `/collection-booking/`, `/come-to-you/` and any
query containing collect / pick up / courier / deliver / door / mail-in / post), SE Ranking UK keyword database.

**Finding:** "collection"-worded searches have no measurable UK volume (SE Ranking returns no data for
`phone repair collection service`, `collect and return phone repair`, `laptop repair collection service` etc.) and
Search Console shows only brand queries landing on the page. The measurable demand around this service is:

| Term | UK vol/mo (SE Ranking) | Search Console (12 mo) | Used |
|---|---|---|---|
| doorstep repair | 90, rising | 77 impr. on `/`, pos 9.5 | "Prefer a repair on your doorstep…" → links `/come-to-you/` (keeps that page as the doorstep page) |
| mobile repair service / mobile phone repair service | 90 / 50 | 70 impr. spread over `/` and `/book-a-repair/` | intro, Why section |
| mobile phone repair service near me | 40 | — | FAQ "Which areas do you cover?" |
| doorstep phone repair (near me) | — | ~250 impr. across 12 pages, pos 9–14 | "from your door", "to your door" wording throughout |
| samsung doorstep repair | — | ~150 impr. | Samsung linked in the Phones card and FAQ |
| mail in phone repair / phone repair by post / postal phone repair | — | ~15 impr., 1 click | "the convenient alternative to a mail-in or postal repair" |
| phone repair come to you / we come to you phone repair | — | ~10 impr. | link to `/come-to-you/` |
| mobile phone repair van | 40 | 21 impr. on `/come-to-you/` | not used (you don't repair in a van) |

So the page is written to own the exact service phrase ("collection and drop-off repair service", "collect … repair …
return", "£29.95") and to pick up the doorstep / pick-up / mail-in long tail with natural wording, while linking the
genuinely searched "doorstep" intent to `/come-to-you/` rather than competing with it. Local signals: the five store
names appear in the small print, the FAQ, the CTA and the schema `areaServed`.

Also found: `/come-to-you/` collects 3,455 impressions for "pocket geek help" and 831 for "pocket geek site" — Assurant's
Pocket Geek app users, not repair customers. Worth a line on that page pointing them to Assurant so the bounce doesn't
drag the page down.

## 5. Schema (`collection_schema.html`)

`Service` (name, serviceType, provider → the homepage `Organization` @id, `areaServed` = the five areas,
`availableAtOrFrom` → the five `LocalBusiness` @ids from the homepage schema, `Offer` £29.95 GBP with the mileage rule in
the description), `WebPage`, `BreadcrumbList`, `HowTo` (the four steps) and `FAQPage` with the ten visible Q&As word for
word. Validated JSON; no HTML entities inside.

## 6. Please confirm before publishing

- FAQ "What happens if I don't want to go ahead with the quote?" says the device comes back unrepaired and **only the
  collection fee is payable** — change if you refund or waive it.
- FAQ "Is my phone safe?" says progress can be followed in the Repair Portal — remove if collection jobs aren't in it.
- FAQ "Do I need to do anything before you collect?" mentions asking for the passcode on the call when needed.
- "Businesses … arrange regular collections" — fine if you'll take B2B calls on 0330 133 1131.
- Meta description groups Romford under "London" (it's in Havering) to fit 155 characters.
- Payment method isn't mentioned anywhere (unknown) — tell me how customers pay and I'll add a FAQ.

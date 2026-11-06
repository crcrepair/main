# WooCommerce product description template: guide

Approved by Gabor on 2 Nov 2026. **The iPhone 15 Pro description is the template for every product description.**

Template files in Project knowledge:

| File | What it is |
|---|---|
| `claude/product-description-template-iphone-15-pro.html` | Long description (Product > Description). The approved page, exactly as live. |
| `claude/product-short-description-template-iphone-15-pro.html` | Short description (title, "Already have…?" line, two capsule buttons). |
| `claude/product-enquiry-cf7-form-setup.html` | Contact Form 7 "Product enquiry" form: Form, Mail and Messages tabs. Already created on the site. |

For a new product, copy the template, change only what's product-specific (below), and keep everything else identical: layout, CSS, order, widgets and wording patterns.

## Page structure (keep this order)

1. **Menu** (centred, 6 icon pills): Before you buy (info) · Specifications (chip) · Why buy from us (star) · Warranty (shield) · Book a repair (spanner) · Already own? (device icon).
2. **Overview + "Any questions?"** in a 50/50 row. On the left: H2 "<Product> — <short benefit line>" and a 2-paragraph `card lede`. On the right: a blue CF7 enquiry box, `[contact-form-7 id="7e17e9a" title="Product enquiry"]` (the same form on every product).
3. **Before you buy** (amber note card, info icon): 3 bold-led points on what the product doesn't include, or common mix-ups.
4. **Specifications** (chip icon): one white card containing a bulleted list of **Label:** value lines. The line "Figures are <manufacturer>'s." goes underneath.
5. **What makes the <product> stand out**: 6 feature cards (grid c3), no icon.
6. **Is the <product> right for you?**: 2-paragraph card, an honest who-it-suits and who-should-pick-something-else. No icon.
7. **Why buy your <product> from CrC Repair®** (star icon): 3 dark tiles: 60-point quality check · Verified, trusted stock · 15% off accessories.
8. **Two-year warranty and free Device MOT** (shield icon): 2 warranty cards (warranty for the device type, then the Device MOT every 6 months). The line under them reads "Warranty cover is subject to our terms and conditions" (link /terms/), then the line browsing /store/.
9. **Already own a <product>?** (device icon): 3 cards (main repair · other repairs · sell or trade in) with repair warranties per CrC rules.
10. **Book a repair / Sell** in a 50/50 row: a blue repair banner ("Book a repair" → /book-a-repair/, "Find a store" → /store-locator/) and a light-grey sell banner with the cash icon ("Check our trading price" → /we-buy/, "Get cash today" → /store-locator/).
11. **Would you like to collect today? Please contact any of our stores directly**: 10 store-name capsules (names only, each one calls that store), plus the opening-hours line linking /store-locator/.
12. **FAQ**: 6–7 product questions as accordions, the first one open.

## What to change per product

- The product name everywhere: headings, H2s, banner titles, the collect intro, FAQ.
- The overview text, Before you buy, the spec list, the 6 features, Is it for you?, the FAQ. **Check every spec and claim against the manufacturer's official spec page**, and correct marketing hype or wrong figures in the draft. List the corrections in the header comment.
- The **Already own?** icon: `phone` for phones. Console pages use `gamepad`. Add a new icon to the kit if a new device type needs one (tablet, laptop, watch).
- The device wording in the warranty card ("Phone warranty", "Console warranty") and in the Device MOT line.
- **Repair warranties** in the "Already own?" cards follow the CrC rules: phone screens = lifetime; other phone repairs = one year; tablets = one year on everything; consoles, laptops and computers = one year; soldering = three months. Devices sold = two years + a free Device MOT every 6 months.
- Parts wording: Samsung = genuine Samsung parts only; Google Pixel = genuine Google parts only; iPhone/iPad = premium or Genuine Apple part (link /genuine-apple-parts/).
- Internal links: the device's repair pillar (e.g. /iphone-repair/, /samsung-repair/, /playstation-repair/), /battery-replacement/ or /screen-repair/ where relevant, /we-buy/, /store/, /terms/, /book-a-repair/, /store-locator/. Never use a URL ending in "repairs".
- Suggested SEOPress meta in the header comment: title under 60 characters, description 150–155 characters, both counted by script.

## Short description template

- A bold product tagline as the title (e.g. "Titanium strength. Pro power. Next-level performance"), **left-aligned**, with a 16px gap under it.
- Below it, the line "Already have a/an <product>?" (left-aligned).
- Two equal capsules, 180px wide and 44px tall, left-aligned:
  - **Book your repair** (blue) → `https://www.crcrepair.co.uk/book-a-repair/?selected=repairs/<Brand>/<Model-with-hyphens>`. Get the exact `selected=` value from Gabor, e.g. `repairs/Apple/iPhone-15-Pro`.
  - **Sell my device** (light grey) → `https://www.crcrepair.co.uk/we-buy/`.
- Button styles use `!important` because the live theme overrides the booking link's shape. Keep that.
- Paste into the short description **Text** tab only.

### Black Friday variant (approved 6 Nov 2026 on the Galaxy S23 Ultra)

`templates/product-short-description-template-black-friday.html`: the same short description with a dark
"Black Friday Deal" banner between the tagline and the "Already have…?" line (gold "Deal", faint "BLACK FRIDAY"
watermark, one line of copy: "Sharper price on the <Product>. Shop with our 2 year warranty, express delivery or
collection from store."). Used only when Gabor says a product is a Black Friday deal. Per product, change only the
tagline, the product name in the banner copy, the "Already have…?" line and the booking link. The banner's CSS,
padding (10px top inside the box) and wording stay as approved. Deliver the normal short description too.

## SEO deliverables with every product (from 2 Nov 2026)

Deliver these alongside the long and short descriptions for every product, ready to paste into SEOPress and the media library:

1. **SEO title:** under 60 characters, product name first, counted by script.
2. **Meta description:** 150–155 characters, counted by script.
3. **Schema:** a separate `<product-slug>-schema.html` file (one Custom HTML block, JSON-LD, validated with a script). WooCommerce already outputs the Product schema with price and stock, so this file **adds to it rather than duplicating it**:
   - a Product node using the **same `@id` WooCommerce uses (`<product URL>#product`)**, so Google merges the two. It adds brand, model, colour/storage options and key specs (`additionalProperty`) but **no price or offers**, which stay with WooCommerce.
   - a FAQPage node with every visible FAQ, word for word.
   - Needs the product's live URL. No `&amp;`, straight quotes escaped.
4. **Facebook (Open Graph) title and description**, and **X (Twitter) title and description**, written for social: shorter and punchier than the meta. Counts reported.
5. **Product images:** alt text and a media-library description for each image. Alt text is specific (model, colour, angle), not stuffed with keywords; the description is one or two sentences.

6. **WooCommerce product tags** (from 3 Nov 2026), in the SEO pack with a copy-paste line. Use one controlled set, spelled identically on every product:
   - Brand (`Apple`, `Samsung`, `Google`, `Sony`…) · product line (`iPhone`, `Galaxy`, `Pixel`, `PlayStation`…) · model family (`iPhone 11 series`) · exact model (`iPhone 11 Pro`) · condition (`Pre-owned`, pending Gabor's choice of wording) · connectivity for phones (`4G` or `5G`).
   - Colours and storage are product **attributes** (variations), not tags.
   - Recommend `noindex` on tag archives in SEOPress (thin pages).

What to ask for with each product: the old description, the live product URL, the booking `?selected=` value, and the image filenames (or the images) with their colour and angle if it isn't obvious.

## Pasting and technical rules

- Long description: block editor → Code editor (Ctrl+Shift+Alt+M); classic editor → Text tab only, never Visual.
- The first style block is the shared `.crc-page` CSS, kept **verbatim**. The second style block holds the product-page additions (icon pills, centred menu, store capsules, heading icons, sell banner). The enquiry-box styles sit inside the overview row. Keep all three.
- Section heading icons are CSS classes on the heading block (`crc-ico-<name>`), so headings stay valid Gutenberg blocks.
- No Elfsight widgets, no `[Repair_Search_Box]`, no schema in product descriptions (WooCommerce/SEOPress output the Product schema).
- A "Delivery explained" section was trialled on 29 Oct 2026 and isn't part of the approved template.
- Open questions to settle per listing: network status (unlocked?), battery health shown on listings, box contents for pre-owned units.

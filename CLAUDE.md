# CrC Repair® website — page and product description builds

Owner: Gabor (CrC Repair®, crcrepair.co.uk). British English throughout.

## Standing rules
- Always deliver an HTML file (Gutenberg block markup, pasted via the WordPress Code editor
  or the classic editor TEXT tab).
- Never invent facts, prices, services or local details. Verify device specs against Apple or a
  UK carrier page before writing them. Correct errors in old copy and list every correction in
  the page's header comment.
- Count title / description lengths with a script, never by eye.
- When asked to change one thing, change only that thing, and diff to prove nothing else moved.
- No CrC URL ends in "repairs". Never use "click here" as link text.

## Reference docs (read the one that matches the job)
- Store location service pages (e.g. /glasgow/battery-repair): @docs/store-service-pages-instructions-v2.5.md
- Store facts and every Elfsight widget ID: @docs/store-information.md
- WooCommerce product descriptions: @templates/product-description-template-guide.md
- Progress and open items for store pages: docs/progress-log.md
- Duplicate-content corpus (large, read only when running the check): docs/delivered-pages-prose-corpus.md

## Product descriptions — how to build one
1. Approved template: `templates/product-description-template-iphone-15-pro.html`
   (short description: `templates/product-short-description-template-iphone-15-pro.html`,
   CF7 enquiry form id 7e17e9a: `templates/product-enquiry-cf7-form-setup.html`).
2. Copy the nearest existing builder in `kit/` (e.g. `kit/build_iphone16pro.py`) to
   `kit/build_<model>.py`, rewrite the content, keep the structure.
3. Run `python3 kit/build_<model>.py`. It writes four files to `output/products/`:
   `<slug>-product-description.html`, `-short-description.html`, `-schema.html`, `-seo-pack.html`,
   and prints structure/sentence-case problems. Known false positive: "plural repairs URL"
   (triggered by `?selected=repairs/` in the header comment).
4. Check: CSS identical to the template, group classes and heading icons identical to the
   previous product, FAQ schema questions == page `<summary>` texts, SEO lengths within aims
   (title <60, meta 150–155, FB title <65 / desc 110–125, X title <70 / desc <125).
5. Every product also gets: SEO title, meta description, schema, FB + X title/description,
   image alt texts + captions, and product tags (Brand, line, "<model> series", model,
   condition, 4G/5G — colours and storage go in attributes, not tags).

Open questions to keep flagging: condition tag wording (Pre-owned or Refurbished), and the
booking link pattern `?selected=repairs/Apple/<Model>`.

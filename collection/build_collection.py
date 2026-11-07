#!/usr/bin/env python3
"""CrC Repair® — Collection & drop-off page (/collection-booking/). Builds the Gutenberg markup + JSON-LD.

Run:  python3 collection/build_collection.py
Writes: collection/collection_page.html, collection/collection_schema.html
The FAQ list drives both the visible accordion and the FAQPage schema. The shared .crc-page CSS is read from
homepage/css.html (the WooCommerce product-kit block) so this page matches the homepage and product pages.
"""
import json, re, html, os

W = os.path.dirname(os.path.abspath(__file__))
B = "https://www.crcrepair.co.uk"
URL = f"{B}/collection-booking/"
CSS = open(os.path.join(W, "..", "homepage", "css.html"), encoding="utf-8").read().rstrip("\n")

FEE, FEE_MILES, EXTRA = "£29.95", "5 miles", "£1"
STORES5 = [("Bournemouth", "bournemouth"), ("Farringdon", "farringdon"), ("Surrey Quays", "surreyquays"),
           ("Romford", "romford"), ("Whetstone", "whetstone")]


# ---------------------------------------------------------------- Gutenberg helpers (same conventions as the homepage builder)
def L(path, text):
    href = path if path.startswith(("http", "tel:", "mailto:", "#")) else B + path
    return f'<a href="{href}">{text}</a>'


def para(text, cls=None, align=None):
    attrs = {}
    if align: attrs["align"] = align
    if cls: attrs["className"] = cls
    a = (" " + json.dumps(attrs, separators=(",", ":"))) if attrs else ""
    klass = ([f"has-text-align-{align}"] if align else []) + ([cls] if cls else [])
    c = f' class="{" ".join(klass)}"' if klass else ""
    return f"<!-- wp:paragraph{a} -->\n<p{c}>{text}</p>\n<!-- /wp:paragraph -->"


def head(level, text, cls=None):
    attrs = {}
    if level != 2: attrs["level"] = level
    if cls: attrs["className"] = cls
    a = (" " + json.dumps(attrs, separators=(",", ":"))) if attrs else ""
    c = f' class="wp-block-heading {cls}"' if cls else ' class="wp-block-heading"'
    return f"<!-- wp:heading{a} -->\n<h{level}{c}>{text}</h{level}>\n<!-- /wp:heading -->"


def group(cls, inner, anchor=None):
    attrs = {}
    if anchor: attrs["anchor"] = anchor
    attrs["className"] = cls
    idp = f' id="{anchor}"' if anchor else ""
    return (f"<!-- wp:group {json.dumps(attrs, separators=(',', ':'))} -->\n"
            f'<div class="wp-block-group {cls}"{idp}>\n{inner}\n</div>\n<!-- /wp:group -->')


def rawhtml(s):
    return f"<!-- wp:html -->\n{s}\n<!-- /wp:html -->"


def J(*parts):
    return "\n\n".join(p for p in parts if p)


ICONS = {  # 24px stroke icons; inherit currentColor
    "form": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3.5h6M9 9h6M9 13h6M9 17h3"/>',
    "call": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "van": '<path d="M1 6h13v10H1zM14 10h4l3 3v3h-7z"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="17.5" cy="18.5" r="2"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "tablet": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 17.5h.01"/>',
    "laptop": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/>',
    "gamepad": '<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 12h4M8 10v4M15 13h.01M18 11h.01"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "store": '<path d="M3 9l1.5-5h15L21 9M3 9v11h18V9M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M9 20v-6h6v6"/>',
    "home": '<path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    "calendar": '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M8 2v4M16 2v4M3 10h18"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M2 13h20"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- FAQ (drives the accordion AND the schema)
FAQ = [
    ("faq-same-day", "Is collection and drop-off a same-day service?",
     "It can be, depending on the repair. That's why we book collections in advance: when we call you we check the parts are in stock and plan the slot so the repair is completed in the shortest possible time. Simple repairs such as phone screens and batteries are often back with you the same day; laptop, console and board-level repairs can take longer, and we'll tell you the expected return date when we call."),
    ("faq-safe", "Is my phone safe?",
     f"Yes. Collections and returns are made by our own fully insured staff, not a third-party courier, and your device is covered by our insurance from the moment we collect it until it's back in your hands. In store it's booked into our system and handled only by our technicians, and you can follow its progress in the {L('/repair-portal', 'Repair Portal')}."),
    ("faq-cost", "How much does the collection and drop-off service cost?",
     f"The basic fee is {FEE}, which covers collection and return within {FEE_MILES} of the store. Beyond that we charge {EXTRA} for each additional mile. We confirm the exact fee on the call before anything is booked, and the repair itself is quoted separately."),
    ("faq-areas", "Which areas do you cover?",
     f"The service runs from our {L('/bournemouth/', 'Bournemouth')}, {L('/farringdon/', 'Farringdon')}, {L('/surreyquays/', 'Surrey Quays')}, {L('/romford/', 'Romford')} and {L('/whetstone/', 'Whetstone')} stores. There's no fixed cut-off: give us your postcode on the form and we'll confirm on the call whether we can reach you and what the mileage fee will be."),
    ("faq-devices", "Which devices can you collect?",
     f"{L('/phone-repair/', 'Phones')} (iPhone, Samsung, Google Pixel, Motorola and other Android), {L('/tablet-repair/', 'tablets and iPads')}, {L('/laptop-repair/', 'laptops')}, {L('/macbook-repair/', 'MacBooks')} and desktop PCs, and {L('/gaming-console-repair/', 'games consoles')} (PlayStation, Xbox and Nintendo Switch)."),
    ("faq-prepare", "Do I need to do anything before you collect?",
     "Back up your data if you can, and remove any case, SIM tray tools or accessories you want to keep. If we need your passcode to test the repair, we'll ask for it on the call and you can remove it again when the device is returned."),
    ("faq-warranty", "Is the warranty the same as an in-store repair?",
     f"Yes. Collected devices are repaired in our own stores by the same technicians, with the same {L('/lifetime-warranty/', 'lifetime warranty')} on phone screen repairs and a 12-month warranty on most other repairs."),
    ("faq-quote", "What happens if I don't want to go ahead with the quote?",
     "We always quote before any work starts. If you decide not to proceed, we'll bring your device back to you unrepaired; only the collection fee is payable."),
    ("faq-business", "Can businesses use the collection service?",
     f"Yes. It's ideal for offices and other organisations with several devices to repair: one collection, one return and a single point of contact. Call us on {L('tel:+443301331131', '0330 133 1131')} or email {L('mailto:info@crcrepair.co.uk', 'info@crcrepair.co.uk')} to arrange regular collections."),
    ("faq-workplace", "Can you collect from my workplace instead of my home?",
     "Yes. We can collect from and return to any address we can reach – home, office or elsewhere – and we agree the time slot with you on the call."),
]


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


# ---------------------------------------------------------------- page-specific CSS
EXTRA_CSS = """<!-- wp:html -->
<style>
  .crc-page .titlebox{text-align:center;padding:10px 0 16px}
  .crc-page .titlebox h1{font-size:clamp(26px,3.4vw,40px);font-weight:800}
  .crc-page .titlebox h1::after{margin:14px auto 0}
  .crc-page .titlebox .sectionintro{max-width:760px;margin:0 auto 10px}
  .crc-page .crumbs{font-size:13.5px;color:var(--ink-soft);margin:6px 0 10px}
  .crc-page .crumbs ol{list-style:none;margin:0;padding:0;display:flex;gap:8px}
  .crc-page .crumbs li+li::before{content:"›";margin-right:8px;color:var(--line)}
  .crc-page .crumbs a{text-decoration:none;font-weight:600}
  .crc-page .formbox{padding:6px 0 26px}
  .crc-page .grid.c4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
  /* numbered steps with icons */
  .crc-page .step{text-align:center;padding:26px 22px}
  .crc-page .step-ico{position:relative;width:66px;height:66px;border-radius:20px;background:#eaf1fb;color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 14px}
  .crc-page .step-ico svg{width:30px;height:30px}
  .crc-page .step-ico .n{position:absolute;top:-9px;right:-9px;width:26px;height:26px;border-radius:50%;background:var(--accent);color:#fff;font-size:13px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px #fff}
  .crc-page .step h3{font-size:16px;margin-bottom:8px}
  .crc-page .step p{color:var(--ink-soft);font-size:15px}
  .crc-page .smallprint{font-size:12px;line-height:1.5;color:var(--ink-soft);text-align:center;margin-top:16px}
  .crc-page .smallprint a{color:var(--ink-soft);text-decoration:underline}
  /* device cards & price cards */
  .crc-page .dev-ico{width:48px;height:48px;border-radius:14px;background:#eaf1fb;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:12px}
  .crc-page .dev-ico svg{width:24px;height:24px}
  .crc-page .rcard h3 a{color:inherit;text-decoration:none}
  .crc-page .rcard h3 a:hover{color:var(--accent)}
  .crc-page .why-tile h3::before{content:"✔"}
  .crc-page .btn.solid{background:var(--accent);color:#fff}
  .crc-page .btn.solid:hover{background:var(--accent-dark);color:#fff}
  .crc-page .about-row{gap:32px;align-items:center}
  .crc-page .about-row .about-img img{border-radius:var(--radius);box-shadow:0 2px 10px rgba(16,20,24,.08)}
  .crc-page .about-row h2{text-align:left;margin-bottom:16px}
  .crc-page .about-row h2::after{margin:12px 0 0}
  .crc-page .about-row p{color:var(--ink-soft);margin-bottom:14px}
</style>
<!-- /wp:html -->"""


# ---------------------------------------------------------------- sections
def title_and_form():
    crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><ol>'
              f'<li><a href="{B}/">Home</a></li><li aria-current="page">Collection &amp; drop-off repair service</li></ol></nav>')
    h1 = ('<!-- wp:heading {"level":1} -->\n'
          '<h1 class="wp-block-heading">Book your collection and drop-off repair service</h1>\n'
          '<!-- /wp:heading -->')
    form = ('<!-- Collection booking WALKIN -->\n'
            '<script src="https://elfsightcdn.com/platform.js" async></script>\n'
            '<div class="elfsight-app-05e681ab-d0c8-4fcb-acd1-1310369e895b" data-elfsight-app-lazy></div>')
    return J(
        rawhtml(crumbs),
        group("titlebox", J(h1, para(
            f"Can't get to a store? Fill in the form and we'll collect your phone, tablet, laptop or games console from your door, repair it in your local Pocket Geek Tech Repair store and bring it back. From {FEE} within {FEE_MILES} of the store.",
            cls="sectionintro"))),
        group("formbox", rawhtml(form), anchor="book"),
    )


def how_it_works():
    steps = [
        ("step-1", "form", "Fill in the form", "Tell us about the device, the fault and where to collect from. It takes about a minute."),
        ("step-2", "call", "We call you to arrange the collection", "We confirm the fee for your distance, check the parts are in stock and agree a collection slot that suits you."),
        ("step-3", "wrench", "We repair the device", "One of our own insured drivers brings it to your local store, where our technicians repair and test it."),
        ("step-4", "van", "We return the device", "As soon as it's ready we deliver it back to your door, with the same warranty as an in-store repair."),
    ]
    cards = []
    for i, (a, ico, h3, p) in enumerate(steps, 1):
        badge = rawhtml(f'<div class="step-ico"><span class="n">{i}</span>{icon(ico)}</div>')
        cards.append(group("card step", J(badge, head(3, h3), para(p)), anchor=a))
    links = ", ".join(L(f"/{slug}/", n) for n, slug in STORES5[:-1]) + " and " + L(f"/{STORES5[-1][1]}/", STORES5[-1][0])
    return group("block", J(
        head(2, "How it works"),
        para("Four steps from a broken device to a fixed one, without leaving the house.", cls="sectionintro"),
        group("grid c4", "\n\n".join(cards)),
        para(f"Our collection and drop-off service is only available from our {links} stores.", cls="smallprint"),
    ), anchor="how-it-works")


def pricing():
    cards = [
        ("price-basic", "Collection and return", FEE, f"Covers collection and delivery back to you within {FEE_MILES} of the store."),
        ("price-extra", "Further than 5 miles", f"{EXTRA} per mile", "Added for each additional mile, confirmed with you on the call before we book."),
        ("price-repair", "The repair itself", "Fixed quote", "Quoted before any work starts. Nothing is done without your go-ahead."),
    ]
    cs = [group("warranty card", J(head(3, h3), para(big, cls="big"), para(t)), anchor=a) for a, h3, big, t in cards]
    return group("block", J(
        head(2, "What the collection service costs"),
        para("Simple, upfront pricing. You'll know the full cost before anything is booked.", cls="sectionintro"),
        group("grid c3", "\n\n".join(cs)),
        para(f"Prefer to drop in? Repairs in store carry no collection fee – find your nearest store on the {L('/store-locator/', 'store locator')}.", cls="stores-after"),
    ), anchor="pricing")


def devices():
    items = [
        ("dev-phone", "phone", L("/phone-repair/", "Phones"),
         f"{L('/iphone-repair/', 'iPhone')}, {L('/samsung-repair/', 'Samsung')}, {L('/google-pixel-repair/', 'Google Pixel')}, Motorola and other Android phones – screens, batteries, charging ports, cameras and water damage."),
        ("dev-tablet", "tablet", L("/tablet-repair/", "Tablets &amp; iPads"),
         f"{L('/ipad-repair/', 'iPad')}, Samsung Galaxy Tab and other tablets – cracked screens, batteries and charging faults."),
        ("dev-laptop", "laptop", L("/laptop-repair/", "Laptops, MacBooks &amp; PCs"),
         f"Windows laptops, {L('/macbook-repair/', 'MacBooks')} and {L('/computer-repair/', 'desktop PCs')} – screens, keyboards, batteries, upgrades, virus removal and data recovery."),
        ("dev-console", "gamepad", L("/gaming-console-repair/", "Games consoles"),
         f"{L('/playstation-repair/', 'PlayStation')}, {L('/xbox-repair/', 'Xbox')} and {L('/nintendo-repair/', 'Nintendo Switch')} – HDMI ports, overheating, disc drives and controller faults."),
    ]
    cards = [group("card rcard", J(rawhtml(f'<div class="dev-ico">{icon(ico)}</div>'), head(3, h3), para(p)), anchor=a) for a, ico, h3, p in items]
    return group("block", J(
        head(2, "What we can collect and repair"),
        para("Anything we repair in store can be collected. Tap a device type for the repairs we offer.", cls="sectionintro"),
        group("grid c4", "\n\n".join(cards)),
    ), anchor="devices")


def why_us():
    img = ('<!-- wp:image {"id":27,"width":"560px","sizeSlug":"full","linkDestination":"none","className":"about-img"} -->\n'
           '<figure class="wp-block-image size-full is-resized about-img"><img src="https://www.crcrepair.co.uk/wp-content/uploads/2025/02/main-page-pic1.webp" '
           'alt="Technician repairing a collected phone at a Pocket Geek Tech Repair store by CrC Repair®" class="wp-image-27" style="width:560px" width="560" height="374"/></figure>\n'
           '<!-- /wp:image -->')
    text = J(
        head(2, "Why use our collection and drop-off service?"),
        para("It's the convenient alternative to a mail-in or postal repair: no packaging, no courier queues and no waiting for a returns label. Your device travels with our own staff, is repaired by our own technicians and comes back with the same warranty as if you'd walked into the store."),
        para(f"Prefer a repair on your doorstep while you wait? See our {L('/come-to-you/', 'come-to-you service')}. Happy to visit? {L('/book-a-repair/', 'Book an in-store repair')} at any of our 10 stores."),
    )
    cols = ('<!-- wp:columns {"verticalAlignment":"center","className":"about-row"} -->\n'
            '<div class="wp-block-columns are-vertically-aligned-center about-row"><!-- wp:column {"verticalAlignment":"center"} -->\n'
            f'<div class="wp-block-column is-vertically-aligned-center">{img}</div>\n'
            '<!-- /wp:column -->\n\n<!-- wp:column {"verticalAlignment":"center"} -->\n'
            f'<div class="wp-block-column is-vertically-aligned-center">{text}</div>\n'
            '<!-- /wp:column --></div>\n<!-- /wp:columns -->')
    tiles = [
        ("why-insured", "Our own insured drivers", "No third-party couriers. Your device is covered by our insurance from collection to return."),
        ("why-stores", "Repaired in our own stores", "Collected devices go to your local Pocket Geek Tech Repair store, not to a depot somewhere else in the country."),
        ("why-warranty", "Same warranty as in store", f"{L('/lifetime-warranty/', 'Lifetime warranty')} on phone screen repairs and 12 months on most other repairs."),
        ("why-business", "Built for busy people and businesses", "Collect from home or the office, several devices in one trip, and a single point of contact throughout."),
    ]
    ts = [group("why-tile", J(head(3, h3), para(t)), anchor=a) for a, h3, t in tiles]
    return group("block", J(cols, group("grid c4", "\n\n".join(ts))), anchor="why-us")


def faq():
    ds = []
    for i, (fid, q, a) in enumerate(FAQ):
        op = " open" if i == 0 else ""
        ds.append(f'<details{op} id="{fid}">\n  <summary><h3>{q}</h3></summary>\n  <div class="a">{a}</div>\n</details>')
    return group("block faq", J(
        head(2, "Collection and drop-off: frequently asked questions"),
        rawhtml("\n".join(ds)),
    ), anchor="faq")


def cta_banner():
    acts = ('<div class="actions">\n'
            '  <a class="btn light" href="#book">Book a collection</a>\n'
            '  <a class="btn ghost" href="tel:+443301331131">Call 0330 133 1131</a>\n'
            '</div>')
    return group("cta-banner", J(
        group("txt", J(head(2, "Ready to book your collection?"),
                       para(f"Fill in the form at the top of the page and we'll call you back to arrange it. From {FEE} within {FEE_MILES} of our Bournemouth, Farringdon, Surrey Quays, Romford and Whetstone stores."))),
        rawhtml(acts),
    ), anchor="cta")


HEADER = """<!-- CrC Repair® — Collection & drop-off repair service page (/collection-booking/). Built by collection/build_collection.py, 7 Nov 2026.
Paste: Pages > Collection booking > Code editor (Ctrl+Shift+Alt+M), replace everything. Schema: collection_schema.html.
SEO title, meta, Open Graph / X text and image alt texts: collection/seo-pack.md.
Kept from the old page: the Elfsight booking form 05e681ab (now directly under the H1). Removed: four empty paragraphs.
-->"""


def build():
    body = J(title_and_form(), how_it_works(), pricing(), devices(), why_us(), faq(), cta_banner())
    page = (f'<!-- wp:group {{"className":"crc-page crc-collection"}} -->\n<div class="wp-block-group crc-page crc-collection">\n\n'
            f'{body}\n\n</div>\n<!-- /wp:group -->')
    out = CSS + "\n\n" + EXTRA_CSS + "\n\n" + page + "\n"
    open(os.path.join(W, "collection_page.html"), "w", encoding="utf-8").write(out)
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<style>.*?</style>", " ", page, flags=re.S)).split())
    print("visible words:", words)


def schema():
    org = f"{B}/#organization"
    steps = [
        ("Fill in the form", "Tell us about the device, the fault and where to collect from."),
        ("We call you to arrange the collection", "We confirm the fee for your distance, check parts are in stock and agree a collection slot."),
        ("We repair the device", "One of our own insured drivers brings it to your local store, where our technicians repair and test it."),
        ("We return the device", "As soon as it's ready we deliver it back to your door, with the same warranty as an in-store repair."),
    ]
    service = {
        "@type": "Service", "@id": f"{URL}#service",
        "name": "Collection and drop-off repair service",
        "serviceType": "Device repair collection and return",
        "description": f"We collect your phone, tablet, laptop, MacBook, PC or games console from your home or workplace, repair it in your local Pocket Geek Tech Repair store and deliver it back. {FEE} covers collection and return within {FEE_MILES} of the store, plus {EXTRA} per additional mile.",
        "url": URL, "provider": {"@id": org}, "providerMobility": "dynamic",
        "areaServed": [
            {"@type": "City", "name": "Bournemouth"}, {"@type": "Place", "name": "Farringdon, London EC1"},
            {"@type": "Place", "name": "Surrey Quays, London SE16"}, {"@type": "City", "name": "Romford"},
            {"@type": "Place", "name": "Whetstone, London N20"},
        ],
        "availableAtOrFrom": [{"@id": f"{B}/{slug}/#store"} for _, slug in STORES5],
        "availableChannel": {"@type": "ServiceChannel", "serviceUrl": URL, "servicePhone": "+443301331131", "availableLanguage": "English"},
        "offers": {"@type": "Offer", "price": "29.95", "priceCurrency": "GBP", "url": URL,
                   "description": f"Collection and return within {FEE_MILES} of the store; {EXTRA} per additional mile, confirmed by phone before booking. The repair is quoted separately.",
                   "availability": "https://schema.org/InStock"},
        "termsOfService": f"{B}/terms/",
    }
    howto = {"@type": "HowTo", "@id": f"{URL}#howto", "name": "How the collection and drop-off repair service works",
             "step": [{"@type": "HowToStep", "position": i, "name": n, "text": t} for i, (n, t) in enumerate(steps, 1)]}
    crumbs = {"@type": "BreadcrumbList", "@id": f"{URL}#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{B}/"},
        {"@type": "ListItem", "position": 2, "name": "Collection & drop-off repair service", "item": URL}]}
    webpage = {"@type": "WebPage", "@id": f"{URL}#webpage", "url": URL,
               "name": f"Repair Collection & Drop-off from {FEE} | CrC Repair®",
               "description": f"We collect your phone, tablet, laptop or console, repair it in store and return it to you. From {FEE} within {FEE_MILES} of our London & Bournemouth stores.",
               "isPartOf": {"@id": f"{B}/#website"}, "about": {"@id": f"{URL}#service"}, "breadcrumb": {"@id": f"{URL}#breadcrumb"},
               "inLanguage": "en-GB", "mainEntity": {"@id": f"{URL}#service"}}
    faqpage = {"@type": "FAQPage", "@id": f"{URL}#faq", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for _, q, a in FAQ]}
    graph = {"@context": "https://schema.org", "@graph": [service, webpage, crumbs, howto, faqpage]}
    txt = json.dumps(graph, indent=2, ensure_ascii=False)
    json.loads(txt)
    assert "&amp;" not in txt
    open(os.path.join(W, "collection_schema.html"), "w", encoding="utf-8").write(f'<script type="application/ld+json">\n{txt}\n</script>\n')
    print("schema OK:", len(graph["@graph"]), "nodes;", len(FAQ), "FAQ pairs")


if __name__ == "__main__":
    build()
    schema()

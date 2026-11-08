#!/usr/bin/env python3
"""CrC Repair® — content for /book-a-repair/ (goes UNDER the RepairPlugin booking tool). Gutenberg markup + JSON-LD.

Run:  python3 booking/build_booking.py
Writes: booking/book-a-repair_content.html, booking/book-a-repair_schema.html
Starts at H2: the page's title ("Book a repair") is the H1. If the theme doesn't output one, change the first H2 to H1.
Shared .crc-page CSS comes from homepage/css.html so the page matches the homepage, product and collection pages.
"""
import json, re, html, os

W = os.path.dirname(os.path.abspath(__file__))
B = "https://www.crcrepair.co.uk"
URL = f"{B}/book-a-repair/"
CSS = open(os.path.join(W, "..", "homepage", "css.html"), encoding="utf-8").read().rstrip("\n")


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


def head(level, text):
    a = "" if level == 2 else f' {{"level":{level}}}'
    return f'<!-- wp:heading{a} -->\n<h{level} class="wp-block-heading">{text}</h{level}>\n<!-- /wp:heading -->'


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


ICONS = {
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "tablet": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M12 17.5h.01"/>',
    "laptop": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/>',
    "gamepad": '<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 12h4M8 10v4M15 13h.01M18 11h.01"/>',
    "watch": '<circle cx="12" cy="12" r="6"/><path d="M12 9.5V12l1.5 1.5M9 3h6l-.6 3H9.6zM9 21h6l-.6-3H9.6z"/>',
    "apple": '<path d="M16 3c-1.5.2-3 1.3-3.3 3 1.6.1 3.1-1.2 3.3-3z"/><path d="M17.5 12.4c0-2.2 1.8-3.2 1.9-3.3-1-1.5-2.6-1.7-3.2-1.7-1.4-.1-2.7.8-3.4.8-.7 0-1.8-.8-3-.8-1.5 0-2.9.9-3.7 2.3-1.6 2.8-.4 6.9 1.1 9.1.8 1.1 1.7 2.3 2.9 2.3 1.2 0 1.6-.8 3-.8 1.4 0 1.8.8 3 .7 1.3 0 2.1-1.1 2.8-2.2.9-1.3 1.3-2.5 1.3-2.6-.1 0-2.7-1-2.7-3.8z"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><path d="M7 7h.01"/>',
    "calendar": '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M8 2v4M16 2v4M3 10h18"/>',
    "store": '<path d="M3 9l1.5-5h15L21 9M3 9v11h18V9M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0"/><path d="M9 20v-6h6v6"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


STORES = [  # (name, slug, line)
    ("Bournemouth", "bournemouth", "Old Christchurch Road"), ("Colchester", "colchester", "Eld Lane"),
    ("Farringdon", "farringdon", "Long Lane, London EC1"), ("Glasgow", "glasgow", "St Enoch Centre"),
    ("Norwich", "norwich", "White Lion Street"), ("Romford", "romford", "Market Place"),
    ("Stoke-on-Trent", "stoke-on-trent", "Tunstall Trade Park"), ("Surrey Quays", "surreyquays", "Surrey Quays Shopping Centre"),
    ("Whetstone", "whetstone", "High Road, London N20"), ("Wolverhampton", "wolverhampton", "Mander Centre"),
]

# Deep links into the booking tool. Apple pattern confirmed by Gabor (3 Nov 2026): ?selected=repairs/Apple/<Model-with-hyphens>.
# The Samsung pattern (repairs/Samsung/Galaxy-S23-Ultra) is the one used in the product kit — confirm before relying on it.
POPULAR = [
    ("iPhone 16 Pro Max", "Apple/iPhone-16-Pro-Max"), ("iPhone 16 Pro", "Apple/iPhone-16-Pro"), ("iPhone 16", "Apple/iPhone-16"),
    ("iPhone 15 Pro Max", "Apple/iPhone-15-Pro-Max"), ("iPhone 15 Pro", "Apple/iPhone-15-Pro"), ("iPhone 15", "Apple/iPhone-15"),
    ("iPhone 14 Pro Max", "Apple/iPhone-14-Pro-Max"), ("iPhone 14", "Apple/iPhone-14"), ("iPhone 13", "Apple/iPhone-13"),
    ("iPhone 12", "Apple/iPhone-12"), ("iPhone 11", "Apple/iPhone-11"), ("iPhone XR", "Apple/iPhone-XR"),
    ("Galaxy S25 Ultra", "Samsung/Galaxy-S25-Ultra"), ("Galaxy S24 Ultra", "Samsung/Galaxy-S24-Ultra"), ("Galaxy S23 Ultra", "Samsung/Galaxy-S23-Ultra"),
]

FAQ = [
    ("faq-walk-in", "Do I have to book, or can I just walk in?",
     f"Walk-ins are welcome at all 10 stores. Booking online is better, though: it reserves the parts for your model, gives you a fixed time slot and usually means a faster turnaround. If you'd rather talk to someone, call {L('tel:+443301331131', '0330 133 1131')} or your {L('/store-locator/', 'local store')}."),
    ("faq-not-listed", "My device or fault isn't in the booking list. Can you still fix it?",
     f"Usually, yes. The booking tool covers the most common repairs, but our technicians work on older models, less common brands and faults that need a diagnosis first. Book the closest option and describe the problem in the notes, or {L('/contact/', 'contact us')} and we'll quote by phone or email."),
    ("faq-price", "Is the price shown online the final price?",
     "The price shown is the price for that repair on that model, with no hidden fees. If the technician finds a different or additional fault once the device is on the bench, we'll call you with a revised quote before doing any work – nothing is done without your go-ahead."),
    ("faq-how-long", "How long does a repair take?",
     "Most phone screen and battery replacements are finished the same day, often within 1–3 hours when the parts are in stock – and booking makes sure they are. Laptop, MacBook, console and board-level repairs can take longer; the store will give you an expected collection time when you drop the device off."),
    ("faq-change", "Can I change or cancel my booking?",
     f"Yes. Call the store you booked with and we'll move the slot or cancel it. You can also manage quotes and repairs in our {L('/repair-portal', 'Repair Portal')}."),
    ("faq-old-iphone", "Do you still repair older iPhones and Samsungs?",
     "In most cases, yes. Screens and batteries for older iPhone and Galaxy models are still available and often cheaper than you'd expect. If your model isn't listed online, call your nearest store and we'll check parts availability for you."),
    ("faq-parts", "What parts do you use?",
     f"Genuine and OEM-quality parts. {L('/genuine-apple-parts/', 'Genuine Apple parts')} are available for iPhone, Samsung repairs use genuine Samsung parts and Google Pixel repairs use genuine Google parts. Every device is tested before it's handed back."),
    ("faq-warranty", "What warranty do I get?",
     f"A {L('/lifetime-warranty/', 'lifetime warranty')} on phone screen repairs and a 12-month warranty on most other repairs, covering parts and labour. Board-level soldering repairs carry a three-month warranty."),
    ("faq-bring", "What should I bring to my appointment?",
     "Just the device. Back up your data first if you can, remove the case, and know your passcode in case we need it to test the repair. If the device is on an insurance claim, bring the claim reference."),
    ("faq-cant-travel", "What if I can't get to a store?",
     f"Choose our {L('/collection-booking/', 'collection and drop-off service')} (from £29.95, available from five stores) and we'll collect, repair and return the device, or book a {L('/come-to-you/', 'come-to-you repair')} at your home or workplace."),
]


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


EXTRA_CSS = """<!-- wp:html -->
<style>
  .crc-page .crumbs{font-size:13.5px;color:var(--ink-soft);margin:6px 0 10px}
  .crc-page .crumbs ol{list-style:none;margin:0;padding:0;display:flex;gap:8px}
  .crc-page .crumbs li+li::before{content:"›";margin-right:8px;color:var(--line)}
  .crc-page .crumbs a{text-decoration:none;font-weight:600}
  .crc-page .grid.c4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
  @media (min-width:900px){.crc-page .grid.devgrid{grid-template-columns:repeat(3,1fr)}}
  .crc-page .dev-ico{width:48px;height:48px;border-radius:14px;background:#eaf1fb;color:var(--accent);display:flex;align-items:center;justify-content:center;margin-bottom:12px}
  .crc-page .dev-ico svg{width:24px;height:24px}
  .crc-page .rcard h3 a{color:inherit;text-decoration:none}
  .crc-page .rcard h3 a:hover{color:var(--accent)}
  .crc-page .rcard .models{font-size:13.5px;color:var(--ink-soft);border-top:1px dashed var(--line);padding-top:10px;margin-top:12px}
  .crc-page .rcard .models b{color:var(--ink)}
  /* fault chips as links */
  .crc-page .chips a{background:var(--white);border:1px solid var(--line);border-left:5px solid var(--accent);padding:9px 15px;border-radius:10px;font-weight:600;font-size:14px;box-shadow:0 1px 4px rgba(16,20,24,.05);color:var(--ink);display:block;text-decoration:none;transition:background .15s,color .15s}
  .crc-page .chips a:hover{background:var(--accent);color:#fff}
  .crc-page .chips a b,.crc-page .chips span b{display:block;font-weight:700;font-size:13px;color:var(--accent-dark)}
  .crc-page .chips a:hover b{color:#eaf1fb}
  /* numbered steps */
  .crc-page .step{text-align:center;padding:26px 22px}
  .crc-page .step-ico{position:relative;width:66px;height:66px;border-radius:20px;background:#eaf1fb;color:var(--accent);display:flex;align-items:center;justify-content:center;margin:0 auto 14px}
  .crc-page .step-ico svg{width:30px;height:30px}
  .crc-page .step-ico .n{position:absolute;top:-9px;right:-9px;width:26px;height:26px;border-radius:50%;background:var(--accent);color:#fff;font-size:13px;font-weight:800;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 3px #fff}
  .crc-page .step h3{font-size:16px;margin-bottom:8px}
  .crc-page .step p{color:var(--ink-soft);font-size:15px}
  /* store capsules (same as homepage / product pages) and model capsules */
  .crc-page .storepills,.crc-page .modelpills{justify-items:stretch}
  .crc-page .storepills a,.crc-page .modelpills a{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;text-decoration:none;background:var(--white);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:14px 18px;box-shadow:0 2px 10px rgba(16,20,24,.05);transition:background .15s,border-color .15s,color .15s}
  .crc-page .storepills a strong,.crc-page .modelpills a strong{font-size:15px;font-weight:700;line-height:1.3}
  .crc-page .storepills a span{font-size:12.5px;font-weight:500;color:var(--ink-soft);line-height:1.3;margin-top:2px}
  .crc-page .storepills a:hover,.crc-page .storepills a:focus-visible,.crc-page .modelpills a:hover,.crc-page .modelpills a:focus-visible{background:var(--accent);border-color:var(--accent);color:#fff}
  .crc-page .storepills a:hover span{color:#eaf1fb}
  .crc-page .modelpills a{padding:11px 14px}
  .crc-page .modelpills a strong{font-size:14px}
  @media (max-width:560px){
    .crc-page .grid.c5.storepills,.crc-page .grid.c5.modelpills{grid-template-columns:repeat(2,1fr);gap:10px}
    .crc-page .storepills a,.crc-page .modelpills a{padding:10px 12px}
    .crc-page .storepills a span{display:none}
  }
  .crc-page .btn.solid{background:var(--accent);color:#fff}
  .crc-page .btn.solid:hover{background:var(--accent-dark);color:#fff}
  .crc-page .smallprint{font-size:12px;line-height:1.5;color:var(--ink-soft);text-align:center;margin-top:14px}
</style>
<!-- /wp:html -->"""


def intro():
    crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><ol>'
              f'<li><a href="{B}/">Home</a></li><li aria-current="page">Book a repair</li></ol></nav>')
    return J(
        rawhtml(crumbs),
        group("block", J(
            head(2, "Book a phone, tablet, laptop or games console repair online"),
            group("card lede", J(
                para("Use the booking tool above to pick your device, choose the fault and see the price, then select one of our 10 Pocket Geek Tech Repair stores and a time that suits you. Booking reserves the parts for your exact model, so most phone screen and battery replacements are finished the same day – often within 1–3 hours – with a lifetime warranty on phone screen repairs."),
                para(f"We repair iPhone, Samsung Galaxy, Google Pixel, Motorola and other Android phones, iPads and tablets, Windows laptops, MacBooks and PCs, PlayStation, Xbox and Nintendo Switch consoles, and smartwatches. Walk-ins are welcome too, and if you can't get to a store you can book a {L('/collection-booking/', 'collection and drop-off')} or a {L('/come-to-you/', 'come-to-you repair')} instead."),
            )),
        ), anchor="about-booking"),
    )


def devices():
    items = [
        ("dev-iphone", "apple", L("/iphone-repair/", "iPhone repair"),
         "Cracked screens, batteries, charging ports, cameras, back glass, speakers and microphones, water damage and Face ID faults.",
         "<b>Models:</b> iPhone 16 series (incl. 16e), 15, 14, 13, 12 and 11 series, iPhone XS Max and XR – and most older iPhones on request."),
        ("dev-samsung", "phone", L("/samsung-repair/", "Samsung Galaxy repair"),
         f"Screen and back glass replacement, batteries, charging ports and cameras with genuine Samsung parts. See the {L('/samsung-galaxy-s26-ultra-screen-repair/', 'Galaxy S26 Ultra screen repair')} and {L('/samsung-back-glass-replacement/', 'back glass replacement')} pages.",
         "<b>Models:</b> Galaxy S26, S25, S24 and S23 series, Z Fold and Z Flip, Galaxy A series and older Galaxy S models on request."),
        ("dev-android", "phone", L("/google-pixel-repair/", "Google Pixel, Motorola &amp; other Android"),
         f"{L('/google-pixel-repair/', 'Pixel')} screens, batteries and charging ports with genuine Google parts; {L('/motorola-repair/', 'Motorola')} Moto G, Edge and Razr repairs; OnePlus, Oppo, Sony, Nokia, Huawei and Xiaomi on request.",
         "<b>Not in the list?</b> Book the nearest option and tell us the model in the notes."),
        ("dev-tablet", "tablet", L("/tablet-repair/", "iPad &amp; tablet repair"),
         f"{L('/ipad-repair/', 'iPad')}, iPad mini, Air and Pro screens, batteries, charging ports and buttons, plus Samsung Galaxy Tab and other Android tablets.",
         "<b>Typical faults:</b> cracked glass, LCD lines, not charging, battery draining."),
        ("dev-laptop", "laptop", L("/laptop-repair/", "Laptop, MacBook &amp; PC repair"),
         f"Laptop screens, keyboards, batteries, hinges and charging ports; {L('/macbook-repair/', 'MacBook')} Air and Pro repairs; {L('/computer-repair/', 'desktop PC')} repairs, upgrades, virus removal and data recovery.",
         "<b>Brands:</b> Apple, HP, Lenovo, Dell, Acer, Asus, Microsoft Surface and custom gaming PCs."),
        ("dev-console", "gamepad", L("/gaming-console-repair/", "PlayStation, Xbox &amp; Nintendo repair"),
         f"{L('/playstation-repair/', 'PS5 and PS4')} HDMI ports, overheating and disc drives; {L('/xbox-repair/', 'Xbox Series X|S and One')}; {L('/nintendo-repair/', 'Nintendo Switch')} screens, charging and Joy-Con faults; {L('/ps5-controller-stick-drift/', 'controller stick drift')}.",
         "<b>Also:</b> smartwatches and fitness trackers (Apple Watch, Galaxy Watch) – screens, batteries and buttons."),
    ]
    cards = [group("card rcard", J(rawhtml(f'<div class="dev-ico">{icon(ico)}</div>'), head(3, h3), para(p), para(m, cls="models")), anchor=a)
             for a, ico, h3, p, m in items]
    return group("block", J(
        head(2, "What you can book"),
        para("Every repair we do in store can be booked here. Pick a device type for the repairs and models we cover.", cls="sectionintro"),
        group("grid c3 devgrid", "\n\n".join(cards)),
    ), anchor="devices")


def faults():
    items = [  # (href, label, detail)
        ("/screen-repair/", "Cracked screen replacement", "Phones, tablets, laptops – lifetime warranty on phone screens"),
        ("/battery-replacement/", "Battery replacement", "Draining fast, shutting down, swollen battery"),
        ("/phone-repair/", "Charging port repair", "Not charging, loose cable, only charges at an angle"),
        ("/samsung-back-glass-replacement/", "Back glass replacement", "Cracked rear glass on iPhone and Galaxy"),
        ("/phone-repair/", "Camera repair", "Blurry, black or shaking camera, cracked lens"),
        ("/phone-repair/", "Speaker &amp; microphone repair", "No sound on calls, crackling, people can't hear you"),
        ("/water-damaged-phone-what-to-do/", "Water damage repair", "Liquid-damage cleaning and board-level diagnostics"),
        ("/phone-repair/", "Buttons, Face ID &amp; sensors", "Power and volume buttons, proximity sensor, Face ID"),
        ("/computer-repair/", "Software, virus removal &amp; data recovery", "Slow devices, malware, lost files, SSD and RAM upgrades"),
        ("/laptop-repair/", "Laptop keyboard, hinge &amp; screen", "Broken keys, cracked hinges, flickering displays"),
        ("/gaming-console-repair/", "Console HDMI, overheating &amp; drift", "No signal, loud fan, disc not reading, stick drift"),
        ("/iphone-screen-repair-cost-uk-2026/", "Not sure what it costs?", "Read our iPhone screen repair cost guide"),
    ]
    chips = "\n".join(f'  <a href="{B}{h}"><b>{l}</b>{d}</a>' for h, l, d in items)
    return group("block", J(
        head(2, "Common faults you can book"),
        para("The booking tool lists the faults for your model. These are the ones we're asked for most.", cls="sectionintro"),
        rawhtml(f'<div class="chips">\n{chips}\n</div>'),
    ), anchor="faults")


def popular():
    pills = "\n".join(f'  <a href="{URL}?selected=repairs/{sel}"><strong>{n}</strong></a>' for n, sel in POPULAR)
    return group("block", J(
        head(2, "Popular repairs – start your booking"),
        para("Tap a model to open the booking tool with it already selected, then choose the fault, store and time.", cls="sectionintro"),
        rawhtml(f'<div class="grid c5 modelpills">\n{pills}\n</div>'),
        para(f"Looking for a different model? Scroll up and choose it in the booking tool, or {L('/contact/', 'ask us')}.", cls="stores-after"),
    ), anchor="popular")


def how_it_works():
    steps = [
        ("how-1", "search", "Choose your device", "Pick the make and model – iPhone, Galaxy, Pixel, iPad, MacBook, PS5 and more."),
        ("how-2", "tag", "Pick the fault and see the price", "Screen, battery, charging port, camera, water damage… The price is shown before you book."),
        ("how-3", "store", "Select a store and a time", "Any of our 10 stores. We reserve the parts for your model so the repair can start when you arrive."),
        ("how-4", "calendar", "Drop in – or let us come to you", "Bring the device at your slot and collect it later the same day for most phone repairs. Can't travel? Choose collection or come-to-you."),
    ]
    cards = []
    for i, (a, ico, h3, p) in enumerate(steps, 1):
        cards.append(group("card step", J(rawhtml(f'<div class="step-ico"><span class="n">{i}</span>{icon(ico)}</div>'), head(3, h3), para(p)), anchor=a))
    return group("block", J(
        head(2, "How online booking works"),
        group("grid c4", "\n\n".join(cards)),
    ), anchor="how-it-works")


def stores():
    pills = "\n".join(
        f'  <a href="{B}/{slug}/" aria-label="Phone repair {n} – Pocket Geek Tech Repair store page"><strong>{n}</strong><span>{line}</span></a>'
        for n, slug, line in STORES)
    return group("block", J(
        head(2, "Book a repair at any of our 10 stores"),
        para("Pocket Geek Tech Repair by CrC Repair® has stores in London, the South Coast, East Anglia, the Midlands and Scotland. Choose your store in the booking tool, or tap a store for its address, opening hours and local repair pages:", cls="sectionintro"),
        rawhtml(f'<div class="grid c5 storepills">\n{pills}\n</div>'),
        para(f"Opening hours differ from store to store – see the {L('/store-locator/', 'store locator')}. {L('/collection-booking/', 'Collection and drop-off')} is available from Bournemouth, Farringdon, Surrey Quays, Romford and Whetstone.", cls="stores-after"),
    ), anchor="stores")


def why_us():
    tiles = [
        ("why-warranty", L("/lifetime-warranty/", "Lifetime warranty on screen repairs"), "Every phone screen we fit is covered for life; most other repairs carry a 12-month warranty."),
        ("why-parts", "Genuine and OEM-quality parts", f"{L('/genuine-apple-parts/', 'Genuine Apple parts')} for iPhone, genuine Samsung and Google parts, tested OEM-quality parts elsewhere."),
        ("why-fast", "Same-day repairs", "Booking reserves your parts, so most screens and batteries are done in 1–3 hours."),
        ("why-price", "Upfront prices", f"The price you see is the price you pay, and we offer a {L('/price-match/', 'price match')} on like-for-like repairs (terms apply)."),
    ]
    ts = [group("why-tile", J(head(3, h3), para(t)), anchor=a) for a, h3, t in tiles]
    return group("block", J(
        head(2, "Why book with CrC Repair®?"),
        para("Award-winning, insurance-approved and repairing since 2004 – more than 20,000 repairs a year for households, businesses and insurers.", cls="sectionintro"),
        group("grid c4", "\n\n".join(ts)),
    ), anchor="why-us")


def faq():
    ds = []
    for i, (fid, q, a) in enumerate(FAQ):
        op = " open" if i == 0 else ""
        ds.append(f'<details{op} id="{fid}">\n  <summary><h3>{q}</h3></summary>\n  <div class="a">{a}</div>\n</details>')
    return group("block faq", J(head(2, "Booking a repair: frequently asked questions"), rawhtml("\n".join(ds))), anchor="faq")


def cta_banner():
    acts = ('<div class="actions">\n'
            f'  <a class="btn light" href="{URL}">Start your booking</a>\n'
            f'  <a class="btn ghost" href="{B}/store-locator/">Find a store</a>\n'
            '</div>')
    return group("cta-banner", J(
        group("txt", J(head(2, "Ready to book your repair?"),
                       para("Choose your device and fault in the booking tool at the top of the page, pick a store and a time, and we'll have the parts ready when you arrive."))),
        rawhtml(acts),
    ), anchor="cta")


HEADER = """<!-- CrC Repair® — /book-a-repair/ content. Paste BELOW the RepairPlugin booking tool (Code editor, Ctrl+Shift+Alt+M).
Built by booking/build_booking.py, 8 Nov 2026. Starts at H2 because the page title is the H1; if the theme doesn't
print one, change the first H2 to H1. Schema: book-a-repair_schema.html (FAQPage + BreadcrumbList).
Popular-repair capsules use ?selected=repairs/Apple/<Model> (confirmed) and repairs/Samsung/Galaxy-<Model> (the product-kit
pattern – confirm it opens the right model). Those URLs canonicalise to /book-a-repair/, which is intended.
-->"""


def build():
    body = J(intro(), devices(), faults(), popular(), how_it_works(), stores(), why_us(), faq(), cta_banner())
    page = (f'<!-- wp:group {{"className":"crc-page crc-booking"}} -->\n<div class="wp-block-group crc-page crc-booking">\n\n'
            f'{body}\n\n</div>\n<!-- /wp:group -->')
    out = HEADER + "\n" + CSS + "\n\n" + EXTRA_CSS + "\n\n" + page + "\n"
    open(os.path.join(W, "book-a-repair_content.html"), "w", encoding="utf-8").write(out)
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<style>.*?</style>", " ", page, flags=re.S)).split())
    hrefs = []
    for h in re.findall(r'href="(https://www\.crcrepair\.co\.uk/[^"#?]*)"', page):
        if h not in hrefs: hrefs.append(h)
    print("visible words:", words, "| distinct internal URLs:", len(hrefs))


def schema():
    crumbs = {"@type": "BreadcrumbList", "@id": f"{URL}#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{B}/"},
        {"@type": "ListItem", "position": 2, "name": "Book a repair", "item": URL}]}
    webpage = {"@type": "WebPage", "@id": f"{URL}#webpage", "url": URL,
               "name": "Book a Phone, Laptop or Console Repair Online | CrC Repair®",
               "description": "Book a same-day iPhone, Samsung, Pixel, iPad, laptop, MacBook or console repair at one of our 10 UK stores. See the price online and reserve your parts.",
               "isPartOf": {"@id": f"{B}/#website"}, "about": {"@id": f"{B}/#organization"},
               "breadcrumb": {"@id": f"{URL}#breadcrumb"}, "inLanguage": "en-GB",
               "potentialAction": {"@type": "ReserveAction", "name": "Book a repair", "target": URL}}
    faqpage = {"@type": "FAQPage", "@id": f"{URL}#faq", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for _, q, a in FAQ]}
    graph = {"@context": "https://schema.org", "@graph": [webpage, crumbs, faqpage]}
    txt = json.dumps(graph, indent=2, ensure_ascii=False)
    json.loads(txt)
    assert "&amp;" not in txt
    open(os.path.join(W, "book-a-repair_schema.html"), "w", encoding="utf-8").write(f'<script type="application/ld+json">\n{txt}\n</script>\n')
    print("schema OK:", len(graph["@graph"]), "nodes;", len(FAQ), "FAQ pairs")


if __name__ == "__main__":
    build()
    schema()

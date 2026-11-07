#!/usr/bin/env python3
"""CrC Repair® homepage v2.0 — builds the Gutenberg block markup and the JSON-LD schema.

Run:  python3 homepage/build_homepage.py
Writes: homepage/home_page_v2.html          (paste via WordPress Code editor, Ctrl+Shift+Alt+M)
        homepage/home_page_schema_v2.html   (replaces the old home-page JSON-LD block)

The FAQ list below drives BOTH the visible accordion and the FAQPage schema, so they can't drift.
Store facts live in STORES; the hero and Repair Portal banner are static parts in homepage/parts/.
"""
import json, re, html, os

W = os.path.dirname(os.path.abspath(__file__))
B = "https://www.crcrepair.co.uk"
CSS = open(os.path.join(W, "css.html"), encoding="utf-8").read().rstrip("\n")
HERO = open(os.path.join(W, "parts", "hero.html"), encoding="utf-8").read().rstrip("\n")
PORTAL = open(os.path.join(W, "parts", "portal.html"), encoding="utf-8").read().rstrip("\n")


# ---------------------------------------------------------------- Gutenberg helpers (same conventions as kit/product_kit.py)
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


ICONS = {  # stroke icons, inherit the pill's text colour
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- store facts (home_page_schema_original + GBP check 7 Nov 2026)
WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
STORES = [
    dict(slug="bournemouth", name="Bournemouth", line="Old Christchurch Road", tel="+441202776491",
         email="bournemouth@crcrepair.co.uk", street="70 Old Christchurch Road", town="Bournemouth", region=None,
         postcode="BH1 1LL", lat="50.7213482", lon="-1.8761133", hours=[(WEEK, "10:00", "18:00")],
         rating="5.0", reviews="142", image="bournemouth-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Bournemouth+by+CrC+Repair%C2%AE/@50.7213482,-1.8786882,17z/data=!3m1!4b1!4m6!3m5!1s0x4873a10bcdeb5037:0x1ea0fdde9868d33c!8m2!3d50.7213482!4d-1.8761133!16s%2Fg%2F11vrs0nlbm"),
    dict(slug="colchester", name="Colchester", line="Eld Lane", tel="+441206573500",
         email="colchester@crcrepair.co.uk", street="25 Eld Lane", town="Colchester", region=None,
         postcode="CO1 1LS", lat="51.8879355", lon="0.9020529", hours=[(WEEK, "10:00", "17:00")],
         rating="4.8", reviews="328", image="colchester-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Colchester+by+CrC+Repair%C2%AE/@51.8879355,0.899478,17z/data=!3m1!4b1!4m6!3m5!1s0x47d904f9cfa67b75:0xc729ab4c2d6fc7ec!8m2!3d51.8879355!4d0.9020529!16s%2Fg%2F1v3_1yv_"),
    dict(slug="farringdon", name="Farringdon", line="Long Lane, London EC1", tel="+447782796431",
         email="farringdon@crcrepair.co.uk", street="77 Long Lane", town="London", region="City of London",
         postcode="EC1A 9ET", lat="51.5195788", lon="-0.098842",
         hours=[(["Monday", "Wednesday", "Friday"], "09:00", "17:00"), (["Tuesday", "Thursday"], "09:00", "17:30")],
         rating="4.8", reviews="128", image="farringdon-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Farringdon+by+CrC+Repair%C2%AE/@51.5195788,-0.1014169,17z/data=!3m1!4b1!4m6!3m5!1s0x48761b7621392faf:0x45c03195b1cc85b1!8m2!3d51.5195788!4d-0.098842!16s%2Fg%2F11vz4bpndj"),
    dict(slug="glasgow", name="Glasgow", line="St Enoch Centre", tel="+441412219633",
         email="glasgow@crcrepair.co.uk", street="St. Enoch Centre (Level 1), St. Enoch Square", town="Glasgow", region=None,
         postcode="G1 4BW", lat="55.8576135", lon="-4.2543836",
         hours=[(WEEK, "10:00", "19:00"), (["Sunday"], "11:00", "18:00")],
         rating="5.0", reviews="1278", image="glasgow-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Glasgow+by+CrC+Repair%C2%AE/@55.8576135,-4.2569585,17z/data=!3m2!4b1!5s0x4888469f345a4fab:0x7edf0a3a184c8430!4m6!3m5!1s0x488847c4230a7b45:0x8b49c39d7c546ed7!8m2!3d55.8576135!4d-4.2543836!16s%2Fg%2F11sd_z_3tx"),
    dict(slug="norwich", name="Norwich", line="White Lion Street", tel="+441603853209",
         email="norwich@crcrepair.co.uk", street="22a White Lion Street", town="Norwich", region=None,
         postcode="NR2 1PX", lat="52.6273875", lon="1.2946649",
         hours=[(["Monday", "Tuesday", "Friday", "Saturday"], "10:30", "17:00")],
         rating="5.0", reviews="211", image="norwich-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Norwich+By+CrC+Repair%C2%AE/@52.6273875,1.29209,17z/data=!3m1!4b1!4m6!3m5!1s0x47d9e3862958344f:0xd1d8349724ddd477!8m2!3d52.6273875!4d1.2946649!16s%2Fg%2F11vdnzjw7g"),
    dict(slug="romford", name="Romford", line="Market Place", tel="+441708202461",
         email="romford@crcrepair.co.uk", street="Unit 2, Tollgate House, 96 Market Place", town="Romford", region=None,
         postcode="RM1 3ER", lat="51.5800004", lon="0.1836006",
         hours=[(["Monday", "Tuesday", "Thursday", "Friday"], "10:00", "18:00")],
         rating="4.8", reviews="222", image="romford-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Romford+by+CrC+Repair%C2%AE/@51.5800004,0.1810257,17z/data=!3m2!4b1!5s0x47d8a4b5cfc3ce4d:0x8d2c8243f035cb7e!4m6!3m5!1s0x47d8a5f4eb64204d:0x9f2b286bdfccf73e!8m2!3d51.5800004!4d0.1836006!16s%2Fg%2F11rvly2mts"),
    dict(slug="stoke-on-trent", name="Stoke-on-Trent", line="Tunstall Trade Park", tel="+447988300056",
         email="tunstall@crcrepair.co.uk", street="11a Tunstall Trade Park, Tunstall", town="Stoke-on-Trent", region=None,
         postcode="ST6 4SE", lat="53.0533283", lon="-2.2083108", hours=[(WEEK[:5], "09:30", "17:30")],
         rating="4.9", reviews="63", image="tunstall-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Stoke+on+Trent+by+CrC+Repair%C2%AE/@53.0533283,-2.2108857,17z/data=!3m1!4b1!4m6!3m5!1s0x487a432d1789550d:0xf030003d9ed647a4!8m2!3d53.0533283!4d-2.2083108!16s%2Fg%2F11vhrsgcfv"),
    dict(slug="surreyquays", name="Surrey Quays", line="Surrey Quays Shopping Centre", tel="+442073455323",
         email="surreyquays@crcrepair.co.uk", street="Unit 18 (Post 6) Surrey Quays Shopping Centre, Redriff Road", town="London", region=None,
         postcode="SE16 7LL", lat="51.4948767", lon="-0.0468703", hours=[(WEEK, "10:00", "18:00")],
         rating="4.8", reviews="780", image="surreyquays-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Surrey+Quays+by+CrC+Repair%C2%AE/@51.4948767,-0.0494452,17z/data=!3m2!4b1!5s0x487602df8ccfd399:0x7edf0a3a57616a8c!4m6!3m5!1s0x487602dffac3b383:0xe9dc5d65d75a5908!8m2!3d51.4948767!4d-0.0468703!16s%2Fg%2F11bzsxm1xw"),
    dict(slug="whetstone", name="Whetstone", line="High Road, London N20", tel="+442038415717",
         email="whetstone@crcrepair.co.uk", street="1346 High Road", town="London", region=None,
         postcode="N20 9HJ", lat="51.632496", lon="-0.175351", hours=[(WEEK, "10:00", "18:00")],
         rating="4.5", reviews="242", image="whetstone-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Whetstone+by+CrC+Repair%C2%AE/@51.632496,-0.1779259,17z/data=!3m1!4b1!4m6!3m5!1s0x48761791be04bd99:0xc7bcc50b6cdfd2d9!8m2!3d51.632496!4d-0.175351!16s%2Fg%2F11csrftxsm"),
    dict(slug="wolverhampton", name="Wolverhampton", line="Mander Centre", tel="+441902953971",
         email="wolverhampton@crcrepair.co.uk", street="54-55 Dudley Street, Mander Centre", town="Wolverhampton", region=None,
         postcode="WV1 3ER", lat="52.5853215", lon="-2.1272202", hours=[(WEEK, "10:00", "18:00")],
         rating="4.7", reviews="271", image="wolverhampton-store-outside.webp",
         maps="https://www.google.com/maps/place/Pocket+Geek+Tech+Repair+-+Wolverhampton+by+CrC+Repair%C2%AE/@52.5853215,-2.1297951,17z/data=!3m1!4b1!4m6!3m5!1s0x48709be29eb15d07:0xec9134ce5e47cc2!8m2!3d52.5853215!4d-2.1272202!16s%2Fg%2F11sgx2g1pw"),
]
STORE_DISPLAY_NAME = {s["slug"]: f'Pocket Geek Tech Repair - {s["name"].replace("-", " ") if s["slug"]=="stoke-on-trent" else s["name"]} by CrC Repair®' for s in STORES}
STORE_DISPLAY_NAME["norwich"] = "Pocket Geek Tech Repair - Norwich By CrC Repair®"  # as on Google

# ---------------------------------------------------------------- FAQ (drives the accordion AND the FAQPage schema)
FAQ = [
    ("faq-screen-cost", "How much does a phone screen replacement cost?",
     f"It depends on the model and the type of screen (OLED or LCD). Use the booking tool at the top of this page to get an instant price for your exact phone, or read our guide to {L('/iphone-screen-repair-cost-uk-2026/', 'iPhone screen repair costs in the UK')}. Prices are upfront with no hidden fees, and every phone screen we fit comes with a lifetime warranty."),
    ("faq-how-long", "How long does a phone repair take? Can I get it done the same day?",
     "Yes. Most phone screen repairs, battery replacements and common faults are completed the same day, often within 1–3 hours. More complex work such as motherboard or water-damage repair can take longer depending on diagnostics and parts availability."),
    ("faq-brands", "Do you repair all phone brands?",
     f"Yes. We repair {L('/iphone-repair/', 'Apple iPhone')}, {L('/samsung-repair/', 'Samsung Galaxy')}, {L('/google-pixel-repair/', 'Google Pixel')}, {L('/motorola-repair/', 'Motorola')}, OnePlus, Oppo, Sony, Huawei, Xiaomi and most other Android phones."),
    ("faq-other-devices", "Do you also repair tablets, laptops, MacBooks and games consoles?",
     f"We do. Our stores repair {L('/ipad-repair/', 'iPads')} and Android tablets, Windows {L('/laptop-repair/', 'laptops')} and desktop PCs, {L('/macbook-repair/', 'MacBooks')}, {L('/playstation-repair/', 'PlayStation')}, {L('/xbox-repair/', 'Xbox')} and {L('/nintendo-repair/', 'Nintendo Switch')} consoles, smartwatches and fitness trackers, drones and other electronics. We also build custom gaming PCs."),
    ("faq-wearables", "Do you repair smartwatches and other wearables?",
     f"Yes. We repair smartwatches and fitness trackers, including Apple Watch and Samsung Galaxy Watch, covering screens, batteries and buttons. {L('/book-a-repair/', 'Book online')} or ask your nearest store for a quote."),
    ("faq-warranty", "Do your repairs come with a warranty?",
     f"Yes. Phone screen repairs have a {L('/lifetime-warranty/', 'lifetime warranty')}, and most other repairs – batteries, charging ports, cameras, tablets, laptops and consoles – carry a 12-month warranty covering parts and labour. Board-level soldering repairs are covered for three months."),
    ("faq-parts", "What parts do you use – are they genuine?",
     f"We use genuine and OEM-quality replacement parts. {L('/genuine-apple-parts/', 'Genuine Apple parts')} are available for iPhone repairs, Samsung repairs use genuine Samsung parts and Google Pixel repairs use genuine Google parts. Every device is tested before it goes back to you."),
    ("faq-booking", "Do I need to book a repair in advance?",
     f"Walk-ins are welcome at all 10 stores. {L('/book-a-repair/', 'Booking online')} is recommended, though, because it reserves your parts and secures the fastest turnaround."),
    ("faq-options", "What if I can't get to a store?",
     f"Besides in-store repair we offer a mail-in service, {L('/collection-booking/', 'collection and drop-off')}, and a {L('/come-to-you/', 'come-to-you doorstep service')} from selected stores. Choose the option that suits you when you book, or contact your nearest store."),
    ("faq-water", "Can you fix a water-damaged phone?",
     f"Often, yes. Switch the phone off, don't charge it and bring it to us as soon as possible for liquid-damage cleaning and diagnostics. Read {L('/water-damaged-phone-what-to-do/', 'what to do with a water-damaged phone')} first – we'll tell you what can be saved before any work starts."),
    ("faq-stores", "Where are your repair stores?",
     f"Pocket Geek Tech Repair by CrC Repair® has 10 stores: {L('/bournemouth/', 'Bournemouth')}, {L('/colchester/', 'Colchester')}, {L('/farringdon/', 'Farringdon')} (London EC1), {L('/glasgow/', 'Glasgow')} (St Enoch Centre), {L('/norwich/', 'Norwich')}, {L('/romford/', 'Romford')}, {L('/stoke-on-trent/', 'Stoke-on-Trent')}, {L('/surreyquays/', 'Surrey Quays')} (London SE16), {L('/whetstone/', 'Whetstone')} (London N20) and {L('/wolverhampton/', 'Wolverhampton')}. Addresses, opening hours and phone numbers are on our {L('/store-locator/', 'store locator')}."),
    ("faq-we-buy", "Do you buy phones and other devices?",
     f"Yes. Bring your old phone, tablet, laptop or console into any store for a cash offer, or {L('/we-buy/', 'check our trading price online')}. We also sell checked, pre-owned devices with a two-year warranty in our {L('/store/', 'online store')}."),
]


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


# ---------------------------------------------------------------- page-specific CSS (the shared .crc-page block above it stays verbatim)
EXTRA_CSS = """<!-- wp:html -->
<style>
  /* hero (inside the Stackable banner) */
  .crc-hero-label{color:#fff;text-transform:uppercase;letter-spacing:.08em;font-size:13px;font-weight:700;text-align:center;margin:0 0 10px;opacity:.92}
  .crc-hero-h1{color:#fff !important;font-size:clamp(30px,4.6vw,58px) !important;line-height:1.08;font-weight:800;text-align:center;margin:0 0 14px}
  .crc-hero-sub{color:#fff;text-align:center;font-size:19px;line-height:1.5;margin:0 0 18px}
  .crc-hero-sub strong{font-size:24px;display:block;margin-bottom:4px}
  .stk-e17dd34 a{color:inherit;text-decoration:none}
  .stk-e17dd34 a:hover{text-decoration:underline}
  .crc-portal-text{color:#fff;font-size:17px;margin:0;padding:18px 22px}
  /* lock the 9 service cards and 6 why-tiles to three columns on desktop */
  @media (min-width:900px){
    .crc-page .grid.svcgrid,.crc-page .grid.whygrid{grid-template-columns:repeat(3,1fr)}
  }
  /* breadcrumb + jump navigation */
  .crc-page .crumbs{font-size:13.5px;color:var(--ink-soft);margin:6px 0 10px}
  .crc-page .crumbs ol{list-style:none;margin:0;padding:0;display:flex;gap:8px}
  .crc-page .crumbs li+li::before{content:"›";margin-right:8px;color:var(--line)}
  .crc-page .crumbs a{text-decoration:none;font-weight:600}
  .crc-page .jumpnav{justify-content:center!important}
  .crc-page .jumpnav a{display:inline-flex;align-items:center;gap:7px}
  .crc-page .jumpnav svg{width:16px;height:16px;flex-shrink:0;color:var(--accent)}
  .crc-page .jumpnav a:hover svg{color:#fff}
  /* service cards: linked headings */
  .crc-page .rcard h3 a{color:inherit;text-decoration:none}
  .crc-page .rcard h3 a:hover{color:var(--accent)}
  .crc-page .grid.c4{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
  /* brand chips as links */
  .crc-page .chips a{background:var(--white);border:1px solid var(--line);border-left:5px solid var(--accent);padding:9px 15px;border-radius:10px;font-weight:600;font-size:14px;box-shadow:0 1px 4px rgba(16,20,24,.05);color:var(--ink);display:block;text-decoration:none;transition:background .15s,color .15s}
  .crc-page .chips a:hover{background:var(--accent);color:#fff}
  .crc-page .chips a b,.crc-page .chips span b{display:block;font-weight:700;font-size:13px;color:var(--accent-dark)}
  .crc-page .chips a:hover b{color:#eaf1fb}
  /* about row */
  .crc-page .about-row{gap:32px;align-items:center}
  .crc-page .about-row .about-img img{border-radius:var(--radius);box-shadow:0 2px 10px rgba(16,20,24,.08)}
  .crc-page .about-row h2{text-align:left;margin-bottom:16px}
  .crc-page .about-row h2::after{margin:12px 0 0}
  .crc-page .about-row p{color:var(--ink-soft);margin-bottom:14px}
  .crc-page .about-row .btn{margin-top:4px}
  .crc-page .btn.solid{background:var(--accent);color:#fff}
  .crc-page .btn.solid:hover{background:var(--accent-dark);color:#fff}
  /* 10-store capsules (same style as the WooCommerce product pages) */
  .crc-page .storepills{justify-items:stretch}
  .crc-page .storepills a{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;text-decoration:none;background:var(--white);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:14px 18px;box-shadow:0 2px 10px rgba(16,20,24,.05);transition:background .15s,border-color .15s,color .15s}
  .crc-page .storepills a strong{font-size:15px;font-weight:700;line-height:1.3}
  .crc-page .storepills a span{font-size:12.5px;font-weight:500;color:var(--ink-soft);line-height:1.3;margin-top:2px}
  .crc-page .storepills a:hover,.crc-page .storepills a:focus-visible{background:var(--accent);border-color:var(--accent);color:#fff}
  .crc-page .storepills a:hover span,.crc-page .storepills a:focus-visible span{color:#eaf1fb}
  @media (max-width:560px){
    .crc-page .grid.c5.storepills{grid-template-columns:repeat(2,1fr);gap:10px}
    .crc-page .storepills a{padding:10px 12px}
    .crc-page .storepills a strong{font-size:14px}
    .crc-page .storepills a span{display:none}
  }
  /* repairs in detail */
  .crc-page .detail h3{font-size:17px;margin:26px 0 10px}
  .crc-page .detail h3:first-child{margin-top:0}
  .crc-page .detail p{color:var(--ink-soft);margin-bottom:12px}
  .crc-page .detail .card{padding:28px 32px}
  /* blog cards (Blocksy query) */
  .crc-page .bcard{overflow:hidden;padding:0}
  .crc-page .bcard img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover}
  .crc-page .bcard .bcard-date{font-size:13px;color:var(--ink-soft);margin:0 0 6px}
  .crc-page .bcard h3{font-size:17px;margin:0 0 8px}
  .crc-page .bcard h3 a{color:var(--ink);text-decoration:none}
  .crc-page .bcard h3 a:hover{color:var(--accent)}
  .crc-page .bcard p{color:var(--ink-soft);font-size:14.5px}
  .crc-page .blog-more{text-align:center;margin-top:24px}
  .crc-page .widget{padding:10px 0 28px}
  .crc-page .block.tight{padding-top:10px}
</style>
<!-- /wp:html -->"""

# ---------------------------------------------------------------- sections
def breadcrumbs_and_jumpnav():
    crumbs = ('<nav class="crumbs" aria-label="Breadcrumb"><ol>'
              f'<li><a href="{B}/">Home</a></li>'
              '<li aria-current="page">Phone, tablet, laptop &amp; console repair</li></ol></nav>')
    items = [("services", "What we repair", "wrench"), ("brands", "Brands", "phone"), ("why-us", "Why CrC Repair®", "star"),
             ("how-it-works", "How it works", "info"), ("stores", "Our 10 stores", "pin"),
             ("repairs-in-detail", "Repairs in detail", "cpu"), ("faq", "FAQ", "chat"), ("blog", "Blog", "book")]
    links = "\n".join(f'  <a href="#{a}">{icon(i)}{t}</a>' for a, t, i in items)
    return rawhtml(f'{crumbs}\n<nav class="jumpnav" aria-label="On this page">\n{links}\n</nav>')


def services():
    items = [
        ("svc-phone", L("/phone-repair/", "Mobile phone repair"),
         f"Cracked screens, dead batteries, charging ports, cameras, microphones and speakers on {L('/iphone-repair/', 'iPhone')}, {L('/samsung-repair/', 'Samsung')}, {L('/google-pixel-repair/', 'Google Pixel')}, {L('/motorola-repair/', 'Motorola')} and most Android phones. Most phone repairs are finished the same day."),
        ("svc-screen", L("/screen-repair/", "Screen replacement"),
         f"Original-quality OLED and LCD screens for phones, tablets and laptops, fitted in store while you wait, with a {L('/lifetime-warranty/', 'lifetime warranty')} on every phone screen repair."),
        ("svc-battery", L("/battery-replacement/", "Battery replacement"),
         "Phone, tablet, laptop and MacBook batteries replaced with new, tested cells, usually within the hour, and covered by a 12-month warranty."),
        ("svc-tablet", L("/tablet-repair/", "Tablet &amp; iPad repair"),
         f"{L('/ipad-repair/', 'iPad')}, Samsung Galaxy Tab and other Android tablet screens, batteries, charging ports and buttons, for every generation."),
        ("svc-laptop", L("/laptop-repair/", "Laptop &amp; computer repair"),
         f"Laptop screens, keyboards, batteries, hinges and charging ports, plus SSD and RAM upgrades, virus removal and data recovery on {L('/computer-repair/', 'desktop PCs')}. We also build custom gaming PCs."),
        ("svc-macbook", L("/macbook-repair/", "MacBook repair"),
         f"MacBook Air and MacBook Pro screens, batteries, keyboards, trackpads and logic-board repairs, with {L('/genuine-apple-parts/', 'Genuine Apple parts')} available."),
        ("svc-console", L("/gaming-console-repair/", "Games console repair"),
         f"{L('/playstation-repair/', 'PlayStation')} HDMI ports, overheating and disc-drive faults, {L('/xbox-repair/', 'Xbox')} Series X|S and One repairs, and {L('/nintendo-repair/', 'Nintendo Switch')} screens, charging ports and Joy-Con faults."),
        ("svc-wearable", L("/book-a-repair/", "Smartwatch &amp; wearable repair"),
         "Smartwatches and fitness trackers, including Apple Watch and Samsung Galaxy Watch: screen, battery and button repairs."),
        ("svc-water", L("/book-a-repair/", "Water damage &amp; board-level repair"),
         f"Liquid-damage cleaning, diagnostics and micro-soldering for phones, tablets and laptops that won't switch on. Start with {L('/water-damaged-phone-what-to-do/', 'what to do with a water-damaged phone')}."),
    ]
    cards = [group("card rcard", J(head(3, h3), para(body)), anchor=a) for a, h3, body in items]
    return group("block", J(
        head(2, "What we repair"),
        para("From a cracked phone screen to a PlayStation that won't read discs, CrC Repair® fixes the tech you rely on every day. Pick a service to see repairs, parts and warranties, or book straight away using the tool above.", cls="sectionintro"),
        group("grid c3 svcgrid", "\n\n".join(cards)),
        para(f"Can't see your device? Call us on {L('tel:+443301331131', '0330 133 1131')}, email {L('mailto:info@crcrepair.co.uk', 'info@crcrepair.co.uk')} or {L('/book-a-repair/', 'book a diagnostic')} and we'll take a look.", cls="stores-after"),
    ), anchor="services")


def brands():
    items = [  # (href or None, brand, what)
        ("/iphone-repair/", "Apple", "iPhone, iPad, MacBook, Apple Watch"),
        ("/samsung-repair/", "Samsung", "Galaxy S, Z Fold &amp; Flip, Galaxy Tab"),
        ("/google-pixel-repair/", "Google", "Pixel phones"),
        ("/motorola-repair/", "Motorola", "Moto G, Edge, Razr"),
        ("/we-repair-oneplus/", "OnePlus", "Phones"),
        ("/we-repair-oppo/", "Oppo", "Phones"),
        ("/we-repair-sony/", "Sony", "Xperia phones"),
        ("/we-repair-nokia/", "Nokia", "Phones"),
        (None, "Huawei &amp; Honor", "Phones &amp; tablets"),
        (None, "Xiaomi", "Phones &amp; tablets"),
        ("/we-repair-hp/", "HP", "Laptops &amp; desktops"),
        ("/we-repair-lenovo/", "Lenovo", "Laptops &amp; desktops"),
        ("/we-repair-acer/", "Acer", "Laptops &amp; desktops"),
        ("/we-repair-asus/", "Asus", "Laptops &amp; desktops"),
        ("/we-repair-microsoft/", "Microsoft", "Surface laptops &amp; tablets"),
        ("/playstation-repair/", "PlayStation", "PS5, PS4 &amp; controllers"),
        ("/xbox-repair/", "Xbox", "Series X|S &amp; One"),
        ("/nintendo-repair/", "Nintendo", "Switch &amp; Switch Lite"),
    ]
    chips = "\n".join(f'  <a href="{B}{h}"><b>{b}</b>{w}</a>' if h else f"  <span><b>{b}</b>{w}</span>" for h, b, w in items)
    return group("block tight", J(
        head(2, "Brands we repair"),
        para("We work on every major phone, tablet, laptop and console brand. Tap a brand for its repair page:", cls="sectionintro"),
        rawhtml(f'<div class="chips">\n{chips}\n</div>'),
    ), anchor="brands")


def why_us():
    img = ('<!-- wp:image {"id":27,"width":"560px","sizeSlug":"full","linkDestination":"none","className":"about-img"} -->\n'
           '<figure class="wp-block-image size-full is-resized about-img"><img src="https://www.crcrepair.co.uk/wp-content/uploads/2025/02/main-page-pic1.webp" '
           'alt="Phone repair at a Pocket Geek Tech Repair store by CrC Repair®" class="wp-image-27" style="width:560px" width="560" height="374"/></figure>\n'
           '<!-- /wp:image -->')
    text = J(
        head(2, "Why choose CrC Repair®?"),
        para("CrC Repair® has been repairing phones, tablets, laptops and games consoles since 2004. Today we run 10 Pocket Geek Tech Repair stores across England and Scotland and complete more than 20,000 repairs a year for households, businesses and insurers."),
        para("Stop searching for “phone repair near me” – pick your nearest store, book online in seconds and walk out with a working device, usually the same day."),
        rawhtml(f'<a class="btn solid" href="{B}/about/">More about CrC Repair®</a>'),
    )
    cols = ('<!-- wp:columns {"verticalAlignment":"center","className":"about-row"} -->\n'
            '<div class="wp-block-columns are-vertically-aligned-center about-row"><!-- wp:column {"verticalAlignment":"center"} -->\n'
            f'<div class="wp-block-column is-vertically-aligned-center">{img}</div>\n'
            '<!-- /wp:column -->\n\n<!-- wp:column {"verticalAlignment":"center"} -->\n'
            f'<div class="wp-block-column is-vertically-aligned-center">{text}</div>\n'
            '<!-- /wp:column --></div>\n<!-- /wp:columns -->')
    tiles = [
        ("why-warranty", L("/lifetime-warranty/", "Lifetime warranty on screen repairs"),
         "Every phone screen we fit is covered for life. Most other repairs carry a 12-month warranty on parts and labour."),
        ("why-parts", "Genuine and OEM-quality parts",
         f"{L('/genuine-apple-parts/', 'Genuine Apple parts')} available for iPhone, genuine Samsung and Google parts, and tested OEM-quality parts for everything else."),
        ("why-fast", "Same-day repairs",
         "Most screen and battery replacements are finished in 1–3 hours. Walk in, or book a slot so your parts are ready."),
        ("why-experience", "20+ years, 20,000+ repairs a year",
         "An award-winning, insurance-approved repair company trusted by households and businesses since 2004."),
        ("why-price", "Upfront prices and a price match",
         f"Clear quotes with no hidden fees before any work starts, and a {L('/price-match/', 'price match')} on like-for-like repairs (terms apply)."),
        ("why-reviews", "Rated by thousands of customers",
         "4.9 out of 5 on Trustpilot and up to 5.0 on Google across our stores. Read the latest reviews further down this page."),
    ]
    ts = [group("why-tile", J(head(3, h3), para(t)), anchor=a) for a, h3, t in tiles]
    return group("block", J(cols, group("grid c3 whygrid", "\n\n".join(ts))), anchor="why-us")


def how_it_works():
    items = [
        ("how-store", L("/store-locator/", "In store"),
         "Walk into any of our 10 stores – no appointment needed, although booking reserves your parts and the fastest turnaround."),
        ("how-online", L("/book-a-repair/", "Book online"),
         "Choose your device and repair, pick a store and a time, and get an instant quote before you arrive."),
        ("how-collection", L("/collection-booking/", "Collection &amp; drop-off"),
         "We collect your device, repair it and return it – ideal for businesses and multiple devices.*"),
        ("how-mail", L("/contact/", "Mail-in repair"),
         "Can't reach a store? Post your device to us and we'll repair it and send it back by tracked courier."),
        ("how-doorstep", L("/come-to-you/", "Come-to-you repair"),
         "A technician repairs your phone at your home or workplace while you carry on with your day.*"),
    ]
    cards = [group("card rcard", J(head(3, h3), para(body)), anchor=a) for a, h3, body in items]
    return group("block", J(
        head(2, "How to get your device repaired"),
        para("Five ways to get your repair done – choose whichever suits you.", cls="sectionintro"),
        group("grid c5", "\n\n".join(cards)),
        para("*Collection and come-to-you services are available from selected stores. Check with your local store when you book.", cls="stores-after"),
    ), anchor="how-it-works")


def quick_quote():
    return group("block widget", J(
        head(2, "Get a quick quote"),
        rawhtml('<!-- Quick quote -->\n<script src="https://elfsightcdn.com/platform.js" async></script>\n<div class="elfsight-app-da046425-90c9-49ea-8561-b5dc09300ce4" data-elfsight-app-lazy></div>'),
    ), anchor="quote")


def stores():
    pills = "\n".join(
        f'  <a href="{B}/{s["slug"]}/" aria-label="Phone repair {s["name"]} – Pocket Geek Tech Repair store page"><strong>{s["name"]}</strong><span>{s["line"]}</span></a>'
        for s in STORES)
    return group("block", J(
        head(2, "10 phone repair stores across the UK"),
        para("Pocket Geek Tech Repair by CrC Repair® has stores in London, the South Coast, East Anglia, the Midlands and Scotland. Tap your nearest store for its address, opening hours, local prices and the repairs it offers:", cls="sectionintro"),
        rawhtml(f'<div class="grid c5 storepills">\n{pills}\n</div>'),
        para(f"Opening hours differ from store to store. Full details, maps and directions are on our {L('/store-locator/', 'store locator')}, or call head office on {L('tel:+443301331131', '0330 133 1131')}.", cls="stores-after"),
    ), anchor="stores")


def repairs_in_detail():
    secs = [
        ("det-screen", "Screen replacement and cracked screen repair", [
            f"A cracked or smashed screen is the fault we see most, and screen replacement is what CrC Repair® is known for. We replace OLED and LCD displays on {L('/iphone-repair/', 'iPhone')}, {L('/samsung-repair/', 'Samsung Galaxy')}, {L('/google-pixel-repair/', 'Google Pixel')} and {L('/motorola-repair/', 'Motorola')} phones, on {L('/ipad-repair/', 'iPads')} and Android tablets, and on laptops and MacBooks.",
            f"Phone screen replacements are usually finished the same day, often within 1–3 hours, and every phone screen we fit is covered by our {L('/lifetime-warranty/', 'lifetime warranty')}. Not sure what a repair should cost? Read our guide to {L('/iphone-screen-repair-cost-uk-2026/', 'iPhone screen repair costs in the UK')} and the difference between {L('/screen-types/', 'OLED and LCD screens')}, then get an instant quote with the booking tool above.",
        ]),
        ("det-near-me", "Same-day phone repair near you", [
            f"Searching for “phone repair near me” or “phone repair shops near me”? With {L('#stores', '10 stores from Bournemouth to Glasgow')}, there's a good chance one is close by. Walk in with a broken phone and our technicians will diagnose it and quote before any work starts. Most screen, battery, charging-port, camera, microphone and speaker repairs are completed while you wait, and we repair every major brand – Apple, Samsung, Google Pixel, Motorola, OnePlus, Oppo, Sony, Huawei and Xiaomi.",
        ]),
        ("det-battery", "Battery replacement", [
            f"If your phone dies early, shuts down in the cold or charges slowly, a {L('/battery-replacement/', 'battery replacement')} is usually the quickest fix. We replace batteries in phones, tablets, laptops and MacBooks with new, tested cells, and every battery replacement comes with a 12-month warranty. Our guide to {L('/battery-repair-explained/', 'battery health and when to replace')} explains what the numbers in your settings mean.",
        ]),
        ("det-laptop", "Laptop, MacBook and computer repair", [
            f"Our {L('/laptop-repair/', 'laptop repair')} service covers cracked screens, failed keyboards and trackpads, worn batteries, broken hinges and charging ports on Windows laptops from HP, Lenovo, Acer, Asus and Microsoft Surface. {L('/macbook-repair/', 'MacBook repair')} includes MacBook Air and Pro screens, batteries, keyboards and logic-board work. For desktop PCs we offer {L('/computer-repair/', 'computer repair')}, virus and malware removal, data recovery, SSD and RAM upgrades, and custom gaming PC builds. Laptop and computer repairs carry a 12-month warranty.",
        ]),
        ("det-tablet", "Tablet and iPad repair", [
            f"We fix {L('/ipad-repair/', 'iPad')} screens, batteries and charging ports across every generation – iPad, iPad mini, iPad Air and iPad Pro – as well as Samsung Galaxy Tab and other Android {L('/tablet-repair/', 'tablets')}. Many tablet repairs are completed the same day; your store will confirm timing when you book.",
        ]),
        ("det-console", "Games console repair", [
            f"From {L('/playstation-repair/', 'PlayStation repair')} – PS5 and PS4 HDMI ports, overheating, disc drives and {L('/ps5-controller-stick-drift/', 'controller stick drift')} – to {L('/xbox-repair/', 'Xbox repair')} and {L('/nintendo-repair/', 'Nintendo Switch repair')}, our {L('/gaming-console-repair/', 'games console repair')} team gets you back in the game. We also build and upgrade custom gaming PCs in store.",
        ]),
        ("det-wearable", "Smartwatch and wearable repair", [
            f"We repair smartwatches and fitness trackers, including Apple Watch and Samsung Galaxy Watch screens, batteries and buttons. {L('/book-a-repair/', 'Book online')} or bring your watch into your nearest store for a quote.",
        ]),
        ("det-water", "Water damage, charging port, camera and speaker repairs", [
            f"Dropped your phone in water? Switch it off and read {L('/water-damaged-phone-what-to-do/', 'what to do with a water-damaged phone')}, then bring it to us for liquid-damage cleaning and board-level diagnostics. We also replace charging ports, cameras, microphones, speakers and {L('/samsung-back-glass-replacement/', 'back glass')} on all major phones.",
        ]),
        ("det-sell", "Sell your device or buy pre-owned", [
            f"Upgrading? {L('/we-buy/', 'We buy phones, tablets, laptops and consoles')} for cash in store, or you can put the value towards a device from our {L('/store/', 'online store')}. Every device we sell has passed a 60-point quality check and comes with a two-year warranty and a free Device MOT every six months.",
        ]),
    ]
    inner = []
    for a, h3, paras in secs:
        inner.append(group("detail-sec", J(head(3, h3), *[para(p) for p in paras]), anchor=a))
    return group("block detail", J(
        head(2, "Phone, tablet, laptop and console repairs in detail"),
        group("card", "\n\n".join(inner)),
    ), anchor="repairs-in-detail")


def instagram():
    return rawhtml('<!-- Instagram Feed | CrC Insta Feed -->\n<script src="https://elfsightcdn.com/platform.js" async></script>\n<div class="elfsight-app-a4e54e8d-9031-410d-8b7e-64b6b44dbd17" data-elfsight-app-lazy></div>')


# original lines 507-521: reusable block 861 on a full-width grey band, spacer, Elfsight reviews — kept verbatim
PARTNERS_AND_REVIEWS = """<!-- wp:stackable/columns {"uniqueId":"3978779","hasBackground":true,"blockBackgroundColor":"var(\\u002d\\u002dtheme-palette-color-7, #FAFBFC)","blockMargin":{"top":"","right":"","bottom":"","left":""},"blockPadding":{"top":"30","right":"","bottom":"30","left":""},"align":"full"} -->
<div class="wp-block-stackable-columns alignfull stk-block-columns stk-block stk-3978779 stk-block-background" data-block-id="3978779"><style>.stk-3978779 {background-color:var(--theme-palette-color-7, #FAFBFC) !important;padding-top:30px !important;padding-bottom:30px !important;}.stk-3978779:before{background-color:var(--theme-palette-color-7, #FAFBFC) !important;}</style><div class="stk-row stk-inner-blocks stk-block-content stk-content-align stk-3978779-column"><!-- wp:stackable/column {"uniqueId":"b243c29"} -->
<div class="wp-block-stackable-column stk-block-column stk-column stk-block stk-b243c29" data-v="4" data-block-id="b243c29"><div class="stk-column-wrapper stk-block-column__content stk-container stk-b243c29-container stk--no-background stk--no-padding"><div class="stk-block-content stk-inner-blocks stk-b243c29-inner-blocks"><!-- wp:block {"ref":861} /--></div></div></div>
<!-- /wp:stackable/column --></div></div>
<!-- /wp:stackable/columns -->

<!-- wp:spacer {"height":"30px"} -->
<div style="height:30px" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->

<!-- wp:html -->
<!-- Elfsight All-in-One Reviews | CrC AIO Review -->
<script src="https://static.elfsight.com/platform/platform.js" async></script>
<div class="elfsight-app-0f3fe05d-d52e-49b4-9b4e-368d9f7e25f5" data-elfsight-app-lazy></div>
<!-- /wp:html -->"""


def faq():
    ds = []
    for i, (fid, q, a) in enumerate(FAQ):
        op = " open" if i == 0 else ""
        ds.append(f'<details{op} id="{fid}">\n  <summary><h3>{q}</h3></summary>\n  <div class="a">{a}</div>\n</details>')
    return group("block faq", J(
        head(2, "Frequently asked questions"),
        para("Prices, turnaround times, warranties and parts – the questions our stores are asked most.", cls="sectionintro"),
        rawhtml("\n".join(ds)),
    ), anchor="faq")


def blog():
    q = """<!-- wp:blocksy/query {"uniqueId":"1445a193","limit":6} -->
<div class="wp-block-blocksy-query"><!-- wp:blocksy/post-template {"layout":{"type":"grid","columnCount":3}} -->
<!-- wp:group {"className":"card bcard","style":{"spacing":{"blockGap":"0"},"dimensions":{"minHeight":"100%"}},"layout":{"type":"flex","orientation":"vertical","justifyContent":"stretch","flexWrap":"nowrap"}} -->
<div class="wp-block-group card bcard" style="min-height:100%"><!-- wp:blocksy/dynamic-data {"field":"wp:featured_image","has_field_link":"yes","style":{"spacing":{"margin":{"bottom":"0"}}}} /-->

<!-- wp:group {"className":"bcard-body","style":{"dimensions":{"minHeight":"100%"},"layout":{"selfStretch":"fill","flexSize":null},"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30","left":"var:preset|spacing|30","right":"var:preset|spacing|30"}}},"backgroundColor":"palette-color-8","layout":{"type":"constrained"}} -->
<div class="wp-block-group bcard-body has-palette-color-8-background-color has-background" style="min-height:100%;padding-top:var(--wp--preset--spacing--30);padding-right:var(--wp--preset--spacing--30);padding-bottom:var(--wp--preset--spacing--30);padding-left:var(--wp--preset--spacing--30)"><!-- wp:blocksy/dynamic-data {"field":"wp:date","className":"bcard-date","style":{"typography":{"fontSize":"13px"}}} /-->

<!-- wp:blocksy/dynamic-data {"tagName":"h3","has_field_link":"yes","style":{"typography":{"fontSize":"17px"}}} /-->

<!-- wp:blocksy/dynamic-data {"field":"wp:excerpt","excerpt_length":20} /--></div>
<!-- /wp:group --></div>
<!-- /wp:group -->
<!-- /wp:blocksy/post-template --></div>
<!-- /wp:blocksy/query -->"""
    return group("block", J(
        head(2, "Latest from the CrC Repair® blog"),
        para("Repair guides, cost breakdowns and device news written by our technicians.", cls="sectionintro"),
        q,
        rawhtml(f'<p class="blog-more"><a class="btn solid" href="{B}/blog/">Read all articles</a></p>'),
    ), anchor="blog")


def cta_banner():
    acts = ('<div class="actions">\n'
            f'  <a class="btn light" href="{B}/book-a-repair/">Book a repair</a>\n'
            f'  <a class="btn ghost" href="{B}/store-locator/">Find a store</a>\n'
            '</div>')
    return group("cta-banner", J(
        group("txt", J(head(2, "Ready to get your device fixed?"),
                       para("Get an instant quote and book a same-day repair at your nearest Pocket Geek Tech Repair store, or sell your old device for cash."))),
        rawhtml(acts),
    ), anchor="book")


# ---------------------------------------------------------------- assemble
def crc_group(inner, suffix):
    return (f'<!-- wp:group {{"className":"crc-page crc-home-{suffix}"}} -->\n<div class="wp-block-group crc-page crc-home-{suffix}">\n\n'
            f'{inner}\n\n</div>\n<!-- /wp:group -->')


HEADER = """<!-- CrC Repair® homepage v2.0 — Gutenberg block markup. Built by homepage/build_homepage.py on 7 Nov 2026.
Paste: Pages > Home > Code editor (Ctrl+Shift+Alt+M), replace everything. Then paste home_page_schema_v2.html
into the page's schema/Custom HTML slot (replaces the old JSON-LD) and update the SEO title + meta (see homepage/README.md).

What changed vs the live page
- Headings: ONE H1 ("Phone, tablet, laptop & games console repair", in the banner). Old page had no H1 and
  13 H2s (incl. seven FAQ questions as H2). Now H2 = section titles only, H3 = cards / FAQ / blog titles.
- Banner kept (gradient, [Repair_Search_Box], USP text, 10-store list, phone image). Store list fixed
  ("Stroke on Trent" -> Stoke-on-Trent, alphabetical) and each store now links to its page.
- "We repair" / About block replaced by: What we repair (9 service cards), Brands we repair, Why CrC Repair®,
  How to get your device repaired (5 options), 10-store capsule grid (same style as the WooCommerce product
  pages), Repairs in detail (9 keyword sections), redesigned FAQ (12 questions), blog grid, closing CTA.
- Kept: reusable blocks ref 125 and ref 861, Elfsight quick quote / Instagram / reviews widgets.
- FAQ now uses native details/summary (H3) like the product pages. The Stackable accordions' built-in FAQ
  schema is gone, so the FAQPage node in home_page_schema_v2.html is the single source of FAQ schema.
- Corrections to old copy: "Lifetime warranty on screen repair" -> "screen repairs"; "10 store nationwide"
  -> "10 stores nationwide"; "Main-In service" -> "mail-in"; "XBox" -> "Xbox"; "Steam)" bracket typo removed.
Checks: see the PROBLEMS line printed by the builder (block balance, heading order, anchors, no "repairs" URLs).
-->"""


def build():
    body_a = J(
        breadcrumbs_and_jumpnav(),
        PORTAL,
        services(),
        brands(),
        why_us(),
        how_it_works(),
        quick_quote(),
        stores(),
        repairs_in_detail(),
        instagram(),
    )
    body_b = J(faq(), blog(), cta_banner())
    page = J(HERO, '<!-- wp:block {"ref":125} /-->', crc_group(body_a, "a"), PARTNERS_AND_REVIEWS, crc_group(body_b, "b"))
    out = HEADER + "\n" + CSS + "\n\n" + EXTRA_CSS + "\n\n" + page + "\n"
    open(os.path.join(W, "home_page_v2.html"), "w", encoding="utf-8").write(out)

    # ---- checks
    probs = []
    opens = len(re.findall(r"<!-- wp:(?!.*?/-->)", out))
    closes = out.count("<!-- /wp:")
    if opens != closes: probs.append(f"wp open/close mismatch {opens}/{closes}")
    if out.count("<!-- wp:group") != out.count("<!-- /wp:group"): probs.append("group mismatch")
    if len(re.findall(r"<div\b", out)) != out.count("</div>"): probs.append("div mismatch")
    if len(re.findall(r"<h1\b", out)) != 1: probs.append("H1 count != 1")
    levels = [int(x) for x in re.findall(r"<h(\d)", out)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1: probs.append(f"skipped heading {a}->{b}")
    ids = re.findall(r'\sid="([^"]+)"', out)
    for a in re.findall(r'href="#([^"]+)"', out):
        if a not in ids: probs.append(f"missing anchor #{a}")
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes: probs.append(f"duplicate ids {sorted(dupes)}")
    for h in re.findall(r'href="([^"]+)"', out):
        if h.rstrip("/").endswith("repairs"): probs.append(f"URL ends in repairs: {h}")
    if "click here" in out.lower(): probs.append("'click here' link text")
    if "-->" in HEADER[4:-3]: probs.append("comment close inside header")
    print("PROBLEMS:", probs or "none")
    print("headings:", "".join(f"h{l}" for l in levels))
    words = len(re.sub(r"<[^>]+>", " ", re.sub(r"<style>.*?</style>", " ", page, flags=re.S)).split())
    print("visible words (incl. menu/alt):", words)
    hrefs = []
    for h in re.findall(r'href="(https://www\.crcrepair\.co\.uk/[^"#]*)"', page):
        if h not in hrefs: hrefs.append(h)
    print(f"{len(hrefs)} distinct internal URLs")
    return hrefs


# ---------------------------------------------------------------- schema
def schema():
    org_id = f"{B}/#organization"
    services_catalog = [
        ("Mobile phone repair", "/phone-repair/"), ("iPhone repair", "/iphone-repair/"), ("Samsung repair", "/samsung-repair/"),
        ("Google Pixel repair", "/google-pixel-repair/"), ("Motorola repair", "/motorola-repair/"),
        ("Screen replacement", "/screen-repair/"), ("Battery replacement", "/battery-replacement/"),
        ("Tablet repair", "/tablet-repair/"), ("iPad repair", "/ipad-repair/"),
        ("Laptop repair", "/laptop-repair/"), ("MacBook repair", "/macbook-repair/"), ("Computer repair", "/computer-repair/"),
        ("Games console repair", "/gaming-console-repair/"), ("PlayStation repair", "/playstation-repair/"),
        ("Xbox repair", "/xbox-repair/"), ("Nintendo Switch repair", "/nintendo-repair/"),
        ("Smartwatch and wearable repair", "/book-a-repair/"), ("Water damage repair", "/book-a-repair/"),
        ("Collection and drop-off repair service", "/collection-booking/"), ("Come-to-you doorstep repair", "/come-to-you/"),
        ("We buy phones and devices", "/we-buy/"),
    ]
    org = {
        "@type": "Organization", "@id": org_id, "name": "CrC Repair®", "alternateName": ["CrC Repair", "Pocket Geek Tech Repair by CrC Repair®"],
        "legalName": "CrC (London) Limited", "foundingDate": "2004", "url": f"{B}/",
        "description": "CrC Repair® repairs phones, tablets, laptops, MacBooks, games consoles and wearables at 10 Pocket Geek Tech Repair stores across the UK. Same-day screen and battery replacements, board-level repairs and gaming PC builds, with a lifetime warranty on phone screen repairs and Genuine Apple parts available.",
        "logo": {"@type": "ImageObject", "@id": f"{B}/#logo", "url": f"{B}/pics/logo-schema.png", "contentUrl": f"{B}/pics/logo-schema.png", "caption": "CrC Repair®"},
        "image": {"@id": f"{B}/#logo"},
        "identifier": {"@type": "PropertyValue", "propertyID": "companyNumber", "name": "Company number", "value": "08040156"},
        "telephone": "+443301331131", "email": "info@crcrepair.co.uk",
        "address": {"@type": "PostalAddress", "streetAddress": "103 High Street", "addressLocality": "Waltham Cross", "addressRegion": "Hertfordshire", "postalCode": "EN8 7AN", "addressCountry": "GB"},
        "areaServed": {"@type": "Country", "name": "United Kingdom"},
        "knowsAbout": ["Phone repair", "iPhone repair", "Samsung repair", "Google Pixel repair", "Motorola repair", "Screen replacement", "Battery replacement",
                        "Laptop repair", "MacBook repair", "Computer repair", "Tablet repair", "iPad repair", "Games console repair", "PlayStation repair",
                        "Xbox repair", "Nintendo Switch repair", "Smartwatch repair", "Gaming PC building", "Water damage repair", "Data recovery", "Virus removal"],
        "contactPoint": [
            {"@type": "ContactPoint", "contactType": "customer service", "telephone": "+443301331131", "email": "info@crcrepair.co.uk", "areaServed": "GB", "availableLanguage": ["English"]},
            {"@type": "ContactPoint", "contactType": "customer support", "telephone": "+447713302330", "areaServed": "GB", "availableLanguage": ["English"]},
        ],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "116", "bestRating": "5", "worstRating": "1", "url": "https://www.trustpilot.com/review/crcrepair.co.uk"},
        "sameAs": ["https://www.trustpilot.com/review/crcrepair.co.uk", "https://www.facebook.com/crcrepair.uk", "https://www.instagram.com/crcrepair.uk", "https://www.tiktok.com/@crcrepair.uk", "https://www.youtube.com/@crcrepair-uk"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Repair services", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "url": f"{B}{u}", "provider": {"@id": org_id}, "areaServed": {"@type": "Country", "name": "United Kingdom"}}}
            for n, u in services_catalog]},
        "subOrganization": [{"@id": f"{B}/{s['slug']}/#store"} for s in STORES],
    }
    website = {"@type": "WebSite", "@id": f"{B}/#website", "url": f"{B}/", "name": "CrC Repair®",
               "description": "Phone, tablet, laptop, MacBook and games console repair at 10 UK stores.",
               "publisher": {"@id": org_id}, "inLanguage": "en-GB"}
    crumbs = {"@type": "BreadcrumbList", "@id": f"{B}/#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{B}/"}]}
    webpage = {"@type": "WebPage", "@id": f"{B}/#webpage", "url": f"{B}/",
               "name": "Phone, Tablet, Laptop & Games Console Repair | CrC Repair® – 10 UK Stores",
               "description": "Same-day phone screen replacement, battery replacement, tablet, laptop, MacBook and console repair at 10 Pocket Geek Tech Repair stores by CrC Repair®. Lifetime warranty on screen repairs. Book online.",
               "isPartOf": {"@id": f"{B}/#website"}, "about": {"@id": org_id}, "breadcrumb": {"@id": f"{B}/#breadcrumb"},
               "primaryImageOfPage": {"@id": f"{B}/#logo"}, "inLanguage": "en-GB",
               "potentialAction": {"@type": "ReserveAction", "name": "Book a repair", "target": f"{B}/book-a-repair/"}}
    faqpage = {"@type": "FAQPage", "@id": f"{B}/#faq", "mainEntity": [
        {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for _, q, a in FAQ]}
    stores_ld = []
    for s in STORES:
        addr = {"@type": "PostalAddress", "streetAddress": s["street"], "addressLocality": s["town"]}
        if s["region"]: addr["addressRegion"] = s["region"]
        addr.update({"postalCode": s["postcode"], "addressCountry": "GB"})
        stores_ld.append({
            "@type": "LocalBusiness", "@id": f"{B}/{s['slug']}/#store", "name": STORE_DISPLAY_NAME[s["slug"]],
            "url": f"{B}/{s['slug']}/", "image": f"{B}/pics/{s['image']}", "priceRange": "£25-£150",
            "telephone": s["tel"], "email": s["email"], "address": addr,
            "geo": {"@type": "GeoCoordinates", "latitude": s["lat"], "longitude": s["lon"]},
            "hasMap": s["maps"],
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c} for d, o, c in s["hours"]],
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": s["rating"], "reviewCount": s["reviews"], "bestRating": "5", "worstRating": "1"},
            "sameAs": [s["maps"], "https://www.facebook.com/crcrepair.uk", "https://www.instagram.com/crcrepair.uk", "https://www.tiktok.com/@crcrepair.uk", "https://www.youtube.com/@crcrepair-uk"],
            "parentOrganization": {"@id": org_id},
        })
    graph = {"@context": "https://schema.org", "@graph": [org, website, webpage, crumbs, faqpage] + stores_ld}
    txt = json.dumps(graph, indent=2, ensure_ascii=False)
    json.loads(txt)  # validity
    assert "&amp;" not in txt, "HTML entity inside JSON-LD"
    out = f'<script type="application/ld+json">\n{txt}\n</script>\n'
    open(os.path.join(W, "home_page_schema_v2.html"), "w", encoding="utf-8").write(out)
    # FAQ parity: every visible question/answer must be in the schema word for word
    page = open(os.path.join(W, "home_page_v2.html"), encoding="utf-8").read()
    for _, q, a in FAQ:
        assert f"<h3>{q}</h3>" in page and strip_tags(q) in txt
        assert strip_tags(a) in txt
    print("schema OK:", len(graph["@graph"]), "nodes;", len(FAQ), "FAQ pairs match the page")


if __name__ == "__main__":
    hrefs = build()
    schema()
    print("\n".join(hrefs))

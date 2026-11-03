"""Build the PS5 Pro WooCommerce product description in the .crc-page design system."""
import json, re, html, os, sys

W = os.path.dirname(os.path.abspath(__file__))
B = "https://www.crcrepair.co.uk"
CSS = open(os.path.join(W, "css.html")).read().rstrip("\n")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products", "") + "ps5-pro-product-description.html"


def L(path, text):
    href = path if path.startswith(("http", "tel:", "mailto:")) else B + path
    return f'<a href="{href}">{text}</a>'


def para(text, cls=None, align=None):
    attrs = {}
    if cls: attrs["className"] = cls
    if align: attrs["align"] = align
    a = (" " + json.dumps(attrs)) if attrs else ""
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
    return "\n".join(p for p in parts if p)


def jumpnav(items):
    links = "\n".join(f'  <a href="#{a}">{t}</a>' for a, t in items)
    return rawhtml(f'<nav class="jumpnav" aria-label="On this page">\n{links}\n</nav>')


def chips(anchor, h2, intro, items, after=None):
    sp = "\n".join(f"  <span><b>{b}</b>{t}</span>" for b, t in items)
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            rawhtml(f'<div class="chips">\n{sp}\n</div>'),
                            para(after, cls="stores-after") if after else ""), anchor=anchor)


def cards(anchor, h2, intro, items, after=None, cols="c3", extra=None):
    cs = [group("card rcard", J(head(3, h3), *[para(x) for x in (body if isinstance(body, list) else [body])]), anchor=a)
          for a, h3, body in items]
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            group(f"grid {cols}", "\n\n".join(cs)),
                            para(after, cls="stores-after") if after else "", extra or ""), anchor=anchor)


def note(anchor, h2, paras):
    return group("block", J(head(2, h2), group("note card", J(*[para(p) for p in paras]))), anchor=anchor)


def lede(anchor, h2, paras, after=None):
    return group("block", J(head(2, h2), group("card lede", J(*[para(p) for p in paras])),
                            para(after, cls="stores-after") if after else ""), anchor=anchor)


def warranty(anchor, h2, items, after):
    cs = [group("warranty card", J(head(3, h3), para(big, cls="big"), para(t)), anchor=a) for a, h3, big, t in items]
    return group("block", J(head(2, h2), group("grid c2", "\n".join(cs)), para(after, cls="stores-after")), anchor=anchor)


def whyus(anchor, h2, tiles, intro=None):
    ts = [group("why-tile", J(head(3, h3), para(t)), anchor=a) for a, h3, t in tiles]
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            group("grid c3", "\n".join(ts))), anchor=anchor)


def cta_banner(h2, text, btns):
    acts = '<div class="actions">\n' + "\n".join(
        f'  <a class="btn {cls}" href="{B + href if href.startswith("/") else href}">{label}</a>' for cls, href, label in btns) + "\n</div>"
    return group("cta-banner", J(group("txt", J(head(2, h2), para(text))), rawhtml(acts)))


def faq(h2, items):
    ds = []
    for i, (fid, q, a) in enumerate(items):
        op = " open" if i == 0 else ""
        ds.append(f'<details{op} id="{fid}">\n  <summary><h3>{q}</h3></summary>\n  <div class="a">{a}</div>\n</details>')
    return group("block faq", J(head(2, h2), rawhtml("\n".join(ds))), anchor="faq")


# ---------------------------------------------------------------- content

META_TITLE = "Buy PS5 Pro 2TB with 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy a PlayStation 5 Pro with 2TB SSD, PSSR upscaling and faster ray tracing. "
             "60-point checked, 2-year warranty and a free Device MOT every six months.")

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "gamepad")]

STORES = [  # (display name, tel digits, tel human) — store-information.md
    ("Bournemouth", "01202776491", "01202 776491"),
    ("Colchester", "01206573500", "01206 573500"),
    ("Farringdon", "02071015461", "020 7101 5461"),
    ("Glasgow", "01412219633", "0141 221 9633"),
    ("Norwich", "01603853209", "01603 853209"),
    ("Romford", "01708202461", "01708 202461"),
    ("Stoke-on-Trent", "07988300056", "07988 300056"),
    ("Surrey Quays", "02073455323", "020 7345 5323"),
    ("Whetstone", "02038415717", "020 3841 5717"),
    ("Wolverhampton", "01902953971", "01902 953971"),
]

# Product-page addition: capsule buttons for the 10-store block. Kept in its OWN style block so the
# shared .crc-page CSS block stays verbatim.
EXTRA_CSS = """<!-- wp:html -->
<style>
  .crc-page .storepills{justify-items:stretch}
  .crc-page .storepills a{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;text-decoration:none;background:var(--white);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:14px 18px;box-shadow:0 2px 10px rgba(16,20,24,.05);transition:background .15s,border-color .15s,color .15s}
  .crc-page .storepills a strong{font-size:15px;font-weight:700;line-height:1.3}
  .crc-page .storepills a:hover,.crc-page .storepills a:focus-visible{background:var(--accent);border-color:var(--accent);color:#fff}
  @media (max-width:560px){
    .crc-page .grid.c5.storepills{grid-template-columns:repeat(2,1fr);gap:10px}
    .crc-page .storepills a{padding:10px 12px}
    .crc-page .storepills a strong{font-size:14px}
  }
</style>
<!-- /wp:html -->"""


def storepills(anchor, h2, intro, after):
    pills = "\n".join(f'  <a href="tel:{d}" aria-label="Call Pocket Geek {n} on {h}"><strong>{n}</strong></a>'
                      for n, d, h in STORES)
    return group("block", J(head(2, h2), para(intro, cls="sectionintro"),
                            rawhtml(f'<div class="grid c5 storepills">\n{pills}\n</div>'),
                            para(after, cls="stores-after")), anchor=anchor)

FAQ = [
    ("faq-ps5pro-disc", "Does the PS5 Pro have a disc drive?",
     "No. The PS5 Pro is a digital console with no built-in drive. To play game discs or Blu-ray films you need "
     "Sony's add-on Disc Drive, which is sold separately and attaches to the side of the console. If you buy all "
     "your games digitally, you don't need it."),
    ("faq-ps5pro-games", "Will my PS5 and PS4 games work on the PS5 Pro?",
     "Yes. It plays PS5 games and over 8,500 PS4 games. Titles labelled PS5 Pro Enhanced get extra modes built for "
     "the Pro's hardware, and some other games can run more smoothly too, although results vary from game to game."),
    ("faq-ps5pro-tv", "Do I need a 4K TV for the PS5 Pro?",
     "It works with any HDMI TV, but it is designed for 4K. On a 4K TV you see the full benefit of PSSR upscaling "
     "and the extra graphics power. For 120Hz modes and variable refresh rate (VRR) you need a TV or monitor that "
     "supports HDMI 2.1. On a 1080p screen, the gains are mainly smoother frame rates."),
    ("faq-ps5pro-storage", "How much storage do I actually get?",
     "The console has a 2TB SSD, but part of it is reserved for system software, so the space for games is a little "
     "under 2TB. You can add more with a compatible M.2 SSD in the expansion slot or with USB external storage."),
    ("faq-ps5pro-warranty", "What warranty comes with a PS5 Pro from CrC Repair®?",
     "Every console we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-ps5pro-tradein", "Can I trade in my old console towards a PS5 Pro?",
     f"Yes. Bring your current console into one of our stores for an offer, and take cash or put the value towards "
     f"your next device. See {L('/we-buy/', 'how we buy consoles and devices')} for details."),
]

from product_kit import jumpnav, EXTRA_CSS, add_heading_icons, cta_pair  # icon nav pills + shared product-page CSS

sections = [
    jumpnav(NAV),

    group("block", J(
        head(2, "PlayStation 5 Pro — Sony's most powerful console"),
        group("card lede", J(
            para("The <strong>PlayStation 5 Pro</strong> is the upgraded PS5, built to get more out of a 4K TV. "
                 "Sony gave it a much larger graphics processor (67% more compute units than the standard PS5, and up to "
                 "45% faster rendering), memory that is 28% faster, and ray tracing that runs two to three times as fast. "
                 "On top of that sits PlayStation Spectral Super Resolution (PSSR), Sony's AI-driven upscaling."),
            para("In practice, you get sharper pictures and steadier frame rates, especially in games labelled "
                 "<strong>PS5 Pro Enhanced</strong>. Many of them let you keep ray tracing switched on without giving up "
                 "a smooth 60fps, so you no longer have to choose between detail and smoothness. A 2TB SSD, Wi-Fi 7 "
                 "and the DualSense controller complete the package, and it plays your existing PS5 games plus over "
                 "8,500 PS4 titles."),
        )),
    ), anchor="overview"),

    note("before-you-buy", "Before you buy — what the PS5 Pro doesn't include", [
        "<strong>No built-in disc drive.</strong> The PS5 Pro is a digital console. To play game discs or Blu-ray "
        "films, you need Sony's add-on Disc Drive, which is sold separately and attaches to the side of the console. "
        "If all your games are digital, you won't need it.",
        "<strong>No vertical stand.</strong> The console sits flat as standard. Sony sells the vertical stand separately.",
        "<strong>Your TV matters.</strong> For 120Hz modes and VRR you need a TV or monitor with HDMI 2.1. The Pro "
        "still runs games more smoothly on a 1080p TV, but most of the visual improvements are aimed at 4K screens.",
    ]),

    chips("specs", "PS5 Pro technical specifications", "The key hardware at a glance:", [
        ("Storage", "2TB ultra-high-speed SSD · M.2 expansion slot"),
        ("Processor (CPU)", "AMD Zen 2 · 8 cores / 16 threads · up to 3.85GHz"),
        ("Graphics (GPU)", "AMD Radeon-based · 67% more compute units than PS5"),
        ("Memory", "16GB GDDR6 (576GB/s) + 2GB DDR5"),
        ("Video output", "4K at 120Hz · 8K output · VRR (HDMI 2.1)"),
        ("Upscaling", "PlayStation Spectral Super Resolution (PSSR)"),
        ("Ray tracing", "2 to 3 times faster than PS5"),
        ("Audio", "Tempest 3D AudioTech"),
        ("Wireless", "Wi-Fi 7 · Bluetooth 5.1"),
        ("Ports", "HDMI 2.1 · Ethernet · USB"),
        ("Disc drive", "Not built in — add-on sold separately"),
    ], after="Figures are Sony's. Part of the 2TB SSD is reserved for system software."),

    cards("features", "What the PS5 Pro does better", None, [
        ("feat-pssr", "PSSR AI upscaling",
         "The console renders a game at a lower resolution, then uses AI to rebuild a sharp 4K image. You get close "
         "to native-4K detail without the frame-rate cost. A system setting can also improve PSSR image quality in "
         "supported games."),
        ("feat-rt", "Faster ray tracing",
         "Reflections, shadows and lighting are traced two to three times faster than on the standard PS5, so more "
         "games can offer ray tracing in their high frame-rate modes."),
        ("feat-fps", "Higher, steadier frame rates",
         "PS5 Pro Enhanced games add modes built for the Pro. Compatible games can run at 60fps, or up to 120fps on a "
         "120Hz display, often with ray tracing still enabled."),
        ("feat-ssd", "2TB SSD as standard",
         "Twice the storage of the original PS5, with the same very fast load times. There is room for more of your "
         "library before you need to delete anything, and you can expand it later."),
        ("feat-dualsense", "DualSense controller",
         "Haptic feedback and adaptive triggers let you feel the game: the tension of a bowstring, the kick of a "
         "weapon, or the surface under your feet."),
        ("feat-library", "Plays your existing library",
         "All your PS5 games work, along with over 8,500 PS4 titles. Tempest 3D AudioTech adds positional sound "
         "through compatible headphones and TV speakers."),
    ]),

    lede("who-for", "Is the PS5 Pro right for you?", [
        "The Pro makes most sense if you play on a 4K TV and image quality matters to you. Big open-world and action "
        "games, especially those labelled PS5 Pro Enhanced, show the clearest difference. If you were already short "
        "of storage, the 2TB drive is a genuine bonus.",
        "If you play on a 1080p screen, mostly play older or less demanding games, or need a disc drive anyway, a "
        "standard PS5 may be better value. Not sure which suits you? Ask in any of our stores and we'll talk you "
        "through it.",
    ]),

    whyus("why-us", "Why buy your PS5 Pro from CrC Repair®", [
        ("why-ps5pro-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-ps5pro-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-ps5pro-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-ps5pro-console", "Console warranty", "Two years",
         "A hassle-free two-year warranty covers your PS5 Pro from the day you buy it."),
        ("warranty-ps5pro-mot", "Free Device MOT", "Every 6 months",
         "Bring your console in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>" + "Looking for something else? Browse our " + L("/store/", "pre-owned consoles and devices") + "."),

    cards("own-one", "Already own a PS5 Pro?", "Whatever you need next, we can help:", [
        ("own-repair", "PS5 Pro repairs",
         "Our technicians fix HDMI port faults, the add-on disc drive, overheating and noisy fans, and DualSense "
         "stick drift. Repairs carry a one-year warranty. See our " + L("/playstation-repair/", "PlayStation repair") +
         " service."),
        ("own-sell", "Sell or trade in",
         "Upgrading, or finished with a console? We'll make you an offer. Take cash, or put the value towards your "
         "next device. Find out " + L("/we-buy/", "how we buy consoles") + "."),
        ("own-store", "Visit a store",
         "Pop into your nearest CrC Repair® store for repairs, trade-ins and advice. Use our " +
         L("/store-locator/", "store locator") + " to find the closest one."),
    ]),

    cta_pair((f"Need your PS5 Pro repaired?",
              "Book online for a quick estimate, or bring your console into your nearest store.",
              [("light", "/book-a-repair/", "Book a repair"), ("ghost", "/store-locator/", "Find a store")], None),
             (f"Would you like to sell your PS5 Pro?",
              "Check what we'd pay for it online, or bring it into your nearest store and walk out with cash the same day.",
              [("light", "/we-buy/", "Check our trading price"), ("ghost", "/store-locator/", "Get cash today")], "sell")),

    storepills("collect", "Would you like to collect today? Please contact any of our stores directly",
               "Call the store nearest you to check availability and arrange to collect your PS5 Pro in person. "
               "Tap a store to call it:",
               "Opening hours differ from store to store, so please call before you travel. Addresses and hours are "
               "on our " + L("/store-locator/", "store locator") + "."),

    faq("PS5 Pro — frequently asked questions", FAQ),
]

body = "\n\n".join(sections)
page = (f'<!-- wp:group {{"className":"crc-page"}} -->\n<div class="wp-block-group crc-page">\n\n{body}\n\n'
        f'</div>\n<!-- /wp:group -->')
page = add_heading_icons(page, {"before-you-buy": "info", "specs": "cpu", "why-us": "star", "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "gamepad"})

hrefs = []
for h_ in re.findall(r'href="([^"#][^"]*)"', page):
    if h_ not in hrefs:
        hrefs.append(h_)

hdr = f"""<!--
================================================================
PAGE:              WooCommerce product description — PlayStation 5 Pro (PS5 Pro)
WHERE IT GOES:     Product > Description (the long description, NOT the short description).
                   Block editor: paste into a Code editor view (Ctrl+Shift+Alt+M) or a Custom HTML block.
                   Classic editor: paste into the TEXT tab only and never switch to Visual.
                   The theme's product title is the H1, so this content starts at H2.
SUGGESTED META (SEOPress):
  Title:        {META_TITLE}   ({len(META_TITLE)} chars, script-counted)
  Description:  {META_DESC}   ({len(META_DESC)} chars, script-counted)

Design: scoped .crc-page CSS block copied verbatim from the delivered pages (accent #4180d5, Montserrat),
followed by a small SECOND style block (.storepills) for the 10-store capsule buttons. Keep both.
Store block: 10 capsules (alphabetical) above the FAQ. Each one calls that store's number from store-information.md.
No Elfsight widgets and no [Repair_Search_Box]: the product page already has its own add-to-cart area.
No schema in this file: WooCommerce/SEOPress output the Product schema.

SPEC CHANGES FROM THE DRAFT (checked against Sony's figures):
  - Ray tracing "2x to 4x" changed to "2 to 3 times" (Sony's figure).
  - "approx 33.5 TFLOPS" removed (an unofficial dual-issue number). Now "67% more compute units" (Sony's figure).
  - "RDNA 3-based" removed (not stated by Sony). Now "AMD Radeon-based".
  - "8K resolution in the future" (PSSR) removed. 8K output is listed as a spec only.
  - Added the missing points: no disc drive and no vertical stand (both sold separately).
  - Removed the stray Gemini <span class="math-inline"> markup.

QUESTIONS FOR GABOR:
  1. Is this listing pre-owned/refurbished or new? The two-year warranty rule applies to pre-owned consoles sold.
  2. What's in the box for this listing (DualSense, cables, stand, disc drive)? The copy says the DualSense
     is included, as your draft did.
  3. Is there a page for the free Device MOT or the 15% accessory offer that should be linked?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""
assert "-->" not in hdr[4:-5]
out = hdr + "\n" + CSS + "\n\n" + EXTRA_CSS + "\n\n" + page + "\n"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(out)

# ---------------------------------------------------------------- checks
probs = []
if len(re.findall(r"<!-- wp:(?!.*?/-->)", out)) != out.count("<!-- /wp:"): probs.append("wp open/close mismatch")
if out.count("<!-- wp:group") != out.count("<!-- /wp:group"): probs.append("group mismatch")
if len(re.findall(r"<div\b", page)) != page.count("</div>"): probs.append("div mismatch")
if re.search(r"<h1", page): probs.append("H1 present")
levels = [int(x) for x in re.findall(r"<h(\d)", page)]
if levels[0] != 2: probs.append("first heading not H2")
for a, b in zip(levels, levels[1:]):
    if b > a + 1: probs.append(f"skipped {a}->{b}")
ids = re.findall(r'id="([^"]+)"', page)
for a in re.findall(r'<a href="#([^"]+)"', page):
    if a not in ids: probs.append(f"missing anchor #{a}")
if len(ids) != len(set(ids)): probs.append("duplicate ids")
if "repairs/" in out: probs.append("plural repairs URL")
if "math-inline" in page or "data-math" in page: probs.append("math span residue")
OK_CAPS = set("""PlayStation PS5 PS4 Pro Sony's Sony CrC Repair® DualSense PSSR TV Device MOT FAQ""".split())
for hd in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", page):
    t = re.sub(r"<[^>]+>", "", html.unescape(hd))
    for w_ in re.findall(r"[A-Za-z][\w'®\-]*", t)[1:]:
        if w_[0].isupper() and w_ not in OK_CAPS: probs.append(f"sentence case? '{w_}' in: {t}")
print("PROBLEMS:", probs or "none")
print("title", len(META_TITLE), "desc", len(META_DESC))
print("links:", hrefs)
print(OUT, os.path.getsize(OUT), "bytes")

"""Samsung Galaxy S24+ — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s24-plus"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S24+"
FULL = "Samsung Galaxy S24+"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s24-plus/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S24-Plus"   # ❓ Samsung pattern still to confirm; "Plus" spelled out as in the URL
TAGLINE = "Bigger, smarter, and beautifully refined."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S24+ | 6.7-inch, Galaxy AI | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S24+ with a 6.7-inch QHD+ 120Hz screen, Galaxy AI, 50MP triple camera"
             " and 45W charging. 60-point checked, 2-year warranty, free MOT.")
OG_TITLE = "Galaxy S24+: 6.7-inch QHD+ screen, Galaxy AI, 2-year warranty"
OG_DESC = "The big-screen Galaxy S24, with Galaxy AI, a 50MP triple camera and a 4,900mAh battery. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S24+ with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch QHD+ 120Hz screen, Galaxy AI, 50MP triple camera and 45W charging. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S24 series", "Model family. Links the Galaxy S24, S24+, S24 FE and S24 Ultra listings."),
    ("Galaxy S24+", "Exact model, as Samsung writes it. If WooCommerce dislikes the + in a tag slug, use \"Galaxy S24 Plus\"."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s24p-box", "What comes with the Galaxy S24+?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s24p-vs-s23p", "What's the difference between the Galaxy S24+ and S23+?",
     "The S24+ has a sharper QHD+ screen in place of FHD+, brighter at 2,600 nits, with flat edges and a slightly "
     "larger 6.7-inch size. It has 12GB of RAM instead of 8GB, a bigger 4,900mAh battery, Galaxy AI and seven years "
     "of updates against four. In the UK the S24+ uses Samsung's Exynos 2400 chip where the S23+ used a Snapdragon; "
     "both are fast flagship chips. The cameras and 45W charging are the same."),
    ("faq-s24p-chip", "Does the UK Galaxy S24+ have a Snapdragon chip?",
     "No. In the UK and Europe the S24 and S24+ use Samsung's own Exynos 2400 chip; only the S24 Ultra has the "
     "Snapdragon 8 Gen 3 for Galaxy here. The Exynos 2400 is a fast 4nm flagship chip with a 10-core CPU that runs "
     "Galaxy AI on the phone, and it's what Samsung sold through every UK network."),
    ("faq-s24p-ai", "What can Galaxy AI do on the S24+?",
     "Circle to Search lets you circle anything on screen to search it. Live Translate translates phone calls in "
     "real time, Interpreter does the same face to face, Note Assist summarises and formats notes, Chat Assist "
     "adjusts the tone of messages, and Generative Edit moves or removes objects in photos. Most features run on "
     "the phone itself."),
    ("faq-s24p-updates", "Is the Galaxy S24+ still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2024 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2031."),
    ("faq-s24p-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s24p-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 12GB RAM on both"),
    ("Colours", "Onyx Black, Marble Grey, Cobalt Violet and Amber Yellow · Jade Green, Sapphire Blue and Sandstone Orange (Samsung online exclusives)"),
    ("Display", "6.7-inch Dynamic AMOLED 2X · QHD+ 3120 × 1440 · 513 ppi · flat"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Glass Victus 2, front and back"),
    ("Chip", "Samsung Exynos 2400 (UK and Europe) · 4nm · 10-core CPU"),
    ("Main camera", "50MP · ƒ/1.8 · optical image stabilisation"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120°"),
    ("Telephoto camera", "10MP · 3x optical zoom · ƒ/2.4 · stabilised"),
    ("Zoom range", "0.6x to 3x optical · Space Zoom up to 30x"),
    ("Photography", "ProVisual Engine · Nightography · Expert RAW · Generative Edit"),
    ("Video", "8K at 30fps · 4K at 60fps · Super HDR · Instant Slow-mo"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("Build", "Armor Aluminum frame · 196g · 7.7mm"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,900mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 6E · Bluetooth 5.3 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2031)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the big-screen Galaxy S24 with Galaxy AI", [
        f"The <strong>{FULL}</strong> pairs a 6.7-inch QHD+ screen, sharper than the standard S24's and bright enough "
        "for sunlight at 2,600 nits, with 12GB of RAM and a big 4,900mAh battery that charges at 45W. It was one of "
        "the first phones with <strong>Galaxy AI</strong>: Circle to Search, Live Translate on calls, Note Assist and "
        "Generative Edit for photos.",
        "The triple camera pairs a 50MP main sensor with a 3x telephoto and an Ultra Wide, with Nightography for low "
        "light and 8K video. The flat-edged Armor Aluminum body has Gorilla Glass Victus 2 front and back, and Samsung "
        "promises <strong>seven years of updates</strong>, so it stays current until 2031.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Exynos chip in the UK.</strong> UK and European S24+ phones use Samsung's Exynos 2400, not the "
        "Snapdragon 8 Gen 3 sold in the US. It's a fast flagship chip and runs Galaxy AI on the phone; the Snapdragon "
        "version is slightly quicker in games and more efficient. Only the S24 Ultra has the Snapdragon in the UK.",
        "<strong>Aluminium, not titanium.</strong> The S24+ has an Armor Aluminum frame. Titanium, the S Pen, the "
        "200MP camera and the 5x zoom are S24 Ultra features. No charger is included; it comes with a USB-C cable.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account. Samsung has said some AI features may become paid after 2025.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s24p-display", "6.7-inch QHD+ display",
         "A sharper screen than the standard S24's FHD+ and the S23+ before it, with 2,600 nits peak brightness for "
         "sunlight, an adaptive 1–120Hz refresh rate, flat edges and an Always-On display."),
        ("feat-s24p-ai", "Galaxy AI",
         "Circle to Search finds anything on screen, Live Translate turns your calls into another language in real "
         "time, Note Assist tidies and summarises notes, and Generative Edit moves or removes objects in photos."),
        ("feat-s24p-battery", "4,900mAh battery, 45W charging",
         "Comfortably lasts a full day, with 45W wired charging to around 65% in 30 minutes, 15W wireless charging "
         "and reverse wireless charging for earbuds or a watch."),
        ("feat-s24p-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and the ProVisual Engine for colour and detail."),
        ("feat-s24p-memory", "12GB of RAM, Exynos 2400",
         "Half as much memory again as the S23+, for smooth multitasking and on-device AI, on Samsung's 4nm Exynos "
         "2400 with a 10-core CPU and hardware ray tracing for games."),
        ("feat-s24p-updates", "Seven years of updates",
         "Samsung promised seven years of Android upgrades and security updates from 2024, so a pre-owned S24+ stays "
         "current until 2031, with IP68 water resistance and Gorilla Glass Victus 2 for the long haul."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a big, sharp screen, Galaxy AI, a strong battery and long update support "
        "without paying for the Ultra's stylus and camera extras, and at a lower price than the S25+. Coming from an "
        "S21+, S22+ or an A-series, you'll notice the brighter screen, the extra memory and the AI features.",
        "If you want the S Pen, the 200MP camera or the 5x zoom, the Galaxy S24 Ultra has them. For the newest chip and "
        "AI features, the Galaxy S25+ has the same screen and battery with the Snapdragon 8 Elite. If you'd prefer "
        "something smaller, the Galaxy S24 has the same chip and cameras in a 6.2-inch phone. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s24p-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s24p-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s24p-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s24p-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s24p-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s24p-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s24p-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s24p-sell", "Sell or trade in",
         "Upgrading, or finished with your phone? We'll make you an offer. Take cash, or put the value towards your "
         "next device. Find out " + L("/we-buy/", "how we buy phones") + "."),
    ]),

    cta_pair((f"Need your {P} repaired?",
              "Book online for a quick estimate, or bring your Galaxy into your nearest store.",
              [("light", "/book-a-repair/", "Book a repair"), ("ghost", "/store-locator/", "Find a store")], None),
             (f"Would you like to sell your {P}?",
              "Check what we'd pay for it online, or bring it into your nearest store and walk out with cash the same day.",
              [("light", "/we-buy/", "Check our trading price"), ("ghost", "/store-locator/", "Get cash today")], "sell")),

    storepills("collect", "Would you like to collect today? Please contact any of our stores directly",
               f"Call the store nearest you to check availability and arrange to collect your {P} in person. "
               "Tap a store to call it:",
               "Opening hours differ from store to store, so please call before you travel. Addresses and hours are "
               "on our " + L("/store-locator/", "store locator") + "."),

    faq(f"{P} — frequently asked questions", FAQ),
]


def header(hrefs):
    return f"""<!--
================================================================
PAGE:              WooCommerce product description — Samsung Galaxy S24+
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  - "Snapdragon 8 Gen 3 for Galaxy" was WRONG FOR THE UK: UK and European S24+ phones use Samsung's Exynos 2400.
    Only the S24 Ultra has the Snapdragon here. Corrected in the spec list, stated in "Before you buy" and
    explained in an FAQ, so nobody buys it expecting a Snapdragon. (If any of your stock is a US/Snapdragon
    import, tell me and the page needs a different line.)
  - "battery optimization" in the Galaxy AI list → not a Galaxy AI feature; dropped. "aluminum" → kept as part of
    Samsung's "Armor Aluminum" trade name, otherwise "aluminium".
  - "What's New vs S23 Plus" kept and made specific: QHD+ vs FHD+, 2,600 nits, 12GB vs 8GB, 4,900 vs 4,700mAh,
    Galaxy AI, seven vs four years of updates, and the UK chip change.
  - Name: Samsung writes "Galaxy S24+"; the old copy had "Plus". Page uses "S24+"; the URL and booking value keep
    "Plus" spelled out.
  - 6.7-inch QHD+ 120Hz LTPO, storage, colours (all seven, four shop plus three online exclusives) and the 50MP
    triple camera in the old copy were correct.
  - Added what the old copy left out: no charger in the box, cloud/paid AI caveat, update policy to 2031, S24+ vs
    Ultra and vs S25+ pointers, full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by GSMArena, Tech Advisor and UK retailers (Exynos 2400 in the UK, 12GB, 256/512GB, 6.7-inch QHD+
  3120 × 1440, 4,900mAh, 45W, 196g, 50MP + 12MP + 10MP). Wi-Fi 6E, 7.7mm and the colour names are Samsung's launch
  figures. Software line assumes One UI 8 / Android 16 in Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question; Plus vs +.
  2. Colours: trim the seven listed to what you stock.
  3. Chip: confirm your S24+ stock is UK/European (Exynos). If any are US imports, say so.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra FE S Pen Snapdragon Gen Elite Exynos Dynamic AMOLED QHD+ FHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Super HDR Instant Slow-mo Gorilla Glass Victus Armor Aluminum Always-On One UI Android Galaxy AI Circle Search Live Translate Interpreter Note Assist Chat Generative Edit Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S21 S22 S23 S24 S25 QHD W SIM Corning US Europe European UK A".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(T + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {FULL}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>", f"<strong>{TAGLINE}</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have a {FULL}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

if BLACK_FRIDAY:
    b = open(T + "product-short-description-template-black-friday.html", "rb").read()
    for o, n in [(b"CrC product SHORT description: Samsung Galaxy S23 Ultra.", f"CrC product SHORT description: {FULL}.".encode()),
                 (b"<strong>The ultimate Galaxy with 200MP pro-grade camera.</strong>", f"<strong>{TAGLINE}</strong>".encode()),
                 (b"Sharper price on the Galaxy S23 Ultra.", f"Sharper price on the {P}.".encode()),
                 (b"Already have a Samsung Galaxy S23 Ultra?", f"Already have a {FULL}?".encode()),
                 (b'?selected=repairs/Samsung/Galaxy-S23-Ultra"', f'?selected={BOOKING_SELECTED}"'.encode())]:
        assert b.count(o) == 1, o
        b = b.replace(o, n)
    open(O + f"{SLUG}-short-description-black-friday.html", "wb").write(b)

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S24+",
             "Samsung Galaxy S24+ with a 6.7-inch QHD+ 120Hz Dynamic AMOLED 2X display, Exynos 2400 chip, 12GB RAM, Galaxy "
             "AI, 50MP triple camera with 3x telephoto, 4,900mAh battery with 45W charging, 5G and seven years of updates. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Onyx Black", "Marble Grey", "Cobalt Violet", "Amber Yellow", "Jade Green", "Sapphire Blue", "Sandstone Orange"]
images = [(f"Main image: {c}", f"Samsung Galaxy S24+ in {c}, front and back view",
           f"The Galaxy S24+ in {c}, with a flat 6.7-inch QHD+ display, aluminium frame and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S24+ triple camera: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S24+ triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("Galaxy AI", "Samsung Galaxy S24+ showing Circle to Search on screen",
     "Galaxy AI on the Galaxy S24+: Circle to Search, Live Translate, Note Assist and Generative Edit."),
    ("Screen on, front", "Samsung Galaxy S24+ flat 6.7-inch Dynamic AMOLED 2X display switched on",
     "The flat 6.7-inch QHD+ 120Hz screen of the Galaxy S24+, up to 2,600 nits."),
    ("In the box", "Samsung Galaxy S24+ with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S24+ with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S24+ with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product. If WooCommerce mangles the + in \"Galaxy S24+\", use \"Galaxy S24 Plus\".",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern and Plus vs +.",
    "Chip: the page says Exynos 2400, correct for UK/European stock. If any units are US imports with the Snapdragon, say so.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

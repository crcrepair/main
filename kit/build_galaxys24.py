"""Samsung Galaxy S24 — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s24"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S24"
FULL = "Samsung Galaxy S24"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s24/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S24"   # ❓ Samsung pattern still to confirm
TAGLINE = "Compact flagship with smarter AI and sleek design."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S24 | Compact, Galaxy AI | CrC Repair®"
META_DESC = ("Buy a compact Samsung Galaxy S24 with a 6.2-inch 120Hz screen, Galaxy AI and a 50MP triple"
             " camera with 3x zoom. 60-point checked, 2-year warranty and MOT.")
OG_TITLE = "Galaxy S24: compact flagship with Galaxy AI, 2-year warranty"
OG_DESC = "The compact Galaxy S24: a 6.2-inch 120Hz screen, Galaxy AI and a 50MP triple camera at 167g. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S24 with a 2-year warranty | CrC Repair®"
X_DESC = "6.2-inch 120Hz screen, Galaxy AI and a 50MP triple camera with 3x zoom at 167g. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S24 series", "Model family. Links the Galaxy S24, S24+, S24 FE and S24 Ultra listings."),
    ("Galaxy S24", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s24-box", "What comes with the Galaxy S24?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s24-vs-s23", "What's the difference between the Galaxy S24 and S23?",
     "The S24 has a slightly larger 6.2-inch screen with slimmer bezels, much brighter at 2,600 nits against 1,750, "
     "flat edges, a bigger 4,000mAh battery against 3,900, Galaxy AI and seven years of updates against four. In the "
     "UK the S24 uses Samsung's Exynos 2400 chip where the S23 used a Snapdragon; both are fast flagship chips. The "
     "cameras and 25W charging are the same."),
    ("faq-s24-chip", "Does the UK Galaxy S24 have a Snapdragon chip?",
     "No. In the UK and Europe the S24 and S24+ use Samsung's own Exynos 2400 chip; only the S24 Ultra has the "
     "Snapdragon 8 Gen 3 for Galaxy here. The Exynos 2400 is a fast 4nm flagship chip with a 10-core CPU that runs "
     "Galaxy AI on the phone, and it's what Samsung sold through every UK network."),
    ("faq-s24-vs-plus", "Should I choose the Galaxy S24 or the S24+?",
     "They share the same chip, cameras, Galaxy AI and seven years of updates. The S24+ has a larger 6.7-inch QHD+ "
     "screen, 12GB of RAM against 8GB, a bigger 4,900mAh battery and faster 45W charging. The S24 is the one to pick "
     "if you want a phone that's easy to use one-handed: 6.2 inches and 167g against 196g, and it's cheaper."),
    ("faq-s24-updates", "Is the Galaxy S24 still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2024 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2031."),
    ("faq-s24-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s24-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "128GB · 256GB · 512GB · 8GB RAM"),
    ("Colours", "Onyx Black, Marble Grey, Cobalt Violet and Amber Yellow · Jade Green, Sapphire Blue and Sandstone Orange (Samsung online exclusives)"),
    ("Display", "6.2-inch Dynamic AMOLED 2X · FHD+ 2340 × 1080 · 416 ppi · flat"),
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
    ("Build", "Armor Aluminum frame · 167g · 7.6mm"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,000mAh"),
    ("Charging", "USB-C · 25W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 6E · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2031)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the compact Galaxy with Galaxy AI", [
        f"The <strong>{FULL}</strong> is the small one of the range: a 6.2-inch 120Hz screen in a flat-edged body "
        "that's 7.6mm thin and 167g, so it's easy to use one-handed and light in a pocket. It was one of the first "
        "phones with <strong>Galaxy AI</strong>: Circle to Search, Live Translate on calls, Note Assist and Generative "
        "Edit for photos, and Samsung promises <strong>seven years of updates</strong>.",
        "The triple camera pairs a 50MP main sensor with a 3x telephoto and an Ultra Wide, with Nightography for low "
        "light and 8K video. The screen is far brighter than the S23's at 2,600 nits, the 4,000mAh battery is bigger, "
        "and the Armor Aluminum body has Gorilla Glass Victus 2 front and back with IP68 water resistance.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Exynos chip in the UK.</strong> UK and European S24 phones use Samsung's Exynos 2400, not the "
        "Snapdragon 8 Gen 3 sold in the US. It's a fast flagship chip and runs Galaxy AI on the phone; the Snapdragon "
        "version is slightly quicker in games and more efficient. Only the S24 Ultra has the Snapdragon in the UK.",
        "<strong>Smaller battery, 25W charging.</strong> The 4,000mAh battery lasts a normal day but not as long as "
        "the S24+ (4,900mAh), wired charging is 25W rather than 45W, and RAM is 8GB rather than 12GB. No charger is "
        "included; it comes with a USB-C cable.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account. Samsung has said some AI features may become paid after 2025.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s24-size", "Compact and light",
         "At 6.2 inches, 7.6mm and 167g it's one of the few small flagships, comfortable one-handed and light in a "
         "pocket, with flat edges, an Armor Aluminum frame and Gorilla Glass Victus 2 front and back."),
        ("feat-s24-ai", "Galaxy AI",
         "Circle to Search finds anything on screen, Live Translate turns your calls into another language in real "
         "time, Note Assist tidies and summarises notes, and Generative Edit moves or removes objects in photos."),
        ("feat-s24-display", "6.2-inch 120Hz display at 2,600 nits",
         "A flat Dynamic AMOLED 2X screen that's far brighter than the S23's for sunlight, with an adaptive 1–120Hz "
         "refresh rate, slimmer bezels and an Always-On display."),
        ("feat-s24-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and the ProVisual Engine for colour and detail."),
        ("feat-s24-battery", "Bigger battery than the S23",
         "4,000mAh against 3,900mAh, with the Exynos 2400's efficiency for a full day, 25W wired charging, 15W wireless "
         "and reverse wireless charging for earbuds or a watch."),
        ("feat-s24-updates", "Seven years of updates",
         "Samsung promised seven years of Android upgrades and security updates from 2024, so a pre-owned S24 stays "
         "current until 2031, with IP68 water resistance for the long haul."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a genuinely compact phone with Galaxy AI, a proper telephoto camera and "
        "long update support, at the lowest price of the S24 range. Coming from an S21, S22 or an A-series, you'll "
        "notice the brighter screen, the lighter body and the AI features.",
        "If battery life matters most, the Galaxy S24+ has a bigger battery, faster charging and a larger, sharper "
        "screen. For the newest chip, the Galaxy S25 is the same size with the Snapdragon 8 Elite and 12GB of RAM. "
        "For the S Pen, the 200MP camera or the 5x zoom, look at the S24 Ultra. Not sure which suits you? Ask in any "
        "of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s24-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s24-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s24-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s24-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s24-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s24-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s24-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s24-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S24
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  - "Snapdragon 8 Gen 3 for Galaxy" was WRONG FOR THE UK: UK and European S24 phones use Samsung's Exynos 2400.
    Only the S24 Ultra has the Snapdragon here. Corrected in the spec list, stated in "Before you buy" and
    explained in an FAQ. (If any of your stock is a US/Snapdragon import, tell me.)
  - "Dual camera system" was WRONG: the S24 has a TRIPLE camera: 50MP main, 12MP Ultra Wide, 10MP 3x telephoto.
  - Colours: "Onyx Marble Grey" and "Sandstone Blue" aren't Samsung names. Corrected to Marble Grey and Sapphire
    Blue. Seven colours: four shop plus three online exclusives.
  - "adaptive battery usage" in the Galaxy AI list → not a Galaxy AI feature; dropped. "aluminum" kept only inside
    Samsung's "Armor Aluminum" trade name, otherwise "aluminium".
  - "What's New vs S23" kept and made specific: 2,600 vs 1,750 nits, 4,000 vs 3,900mAh, flat edges, Galaxy AI,
    seven vs four years of updates, and the UK chip change. "more efficient power management" dropped as vague.
  - 6.2-inch FHD+ 120Hz LTPO and storage in the old copy were correct.
  - Added what the old copy left out: 8GB RAM and 25W (less than the S24+), no charger in the box, cloud/paid AI
    caveat, update policy to 2031, S24 vs S24+ FAQ, full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by Tech Advisor, TechRadar, Expert Reviews and UK retailers (Exynos 2400 in the UK, 8GB, 128/256/512GB,
  6.2-inch FHD+ 2340 × 1080, 4,000mAh, 25W, 167g, 50MP + 12MP + 10MP 3x). Wi-Fi 6E, 7.6mm and the online-exclusive
  colour names are Samsung's launch figures. Software line assumes One UI 8 / Android 16 in Nov 2026: check
  against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  2. Colours: trim the seven listed to what you stock.
  3. Chip: confirm your S24 stock is UK/European (Exynos). If any are US imports, say so.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra FE S Pen Snapdragon Gen Elite Exynos Dynamic AMOLED QHD+ FHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Super HDR Instant Slow-mo Gorilla Glass Victus Armor Aluminum Always-On One UI Android Galaxy AI Circle Search Live Translate Interpreter Note Assist Chat Generative Edit Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi 5G G Hz 8K 4K S21 S22 S23 S24 S25 QHD W SIM Corning US Europe European UK A".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S24",
             "Samsung Galaxy S24 with a 6.2-inch 120Hz Dynamic AMOLED 2X display, Exynos 2400 chip, 8GB RAM, Galaxy AI, "
             "50MP triple camera with 3x telephoto, 4,000mAh battery, 5G and seven years of updates, at 167g. 60-point "
             "quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Onyx Black", "Marble Grey", "Cobalt Violet", "Amber Yellow", "Jade Green", "Sapphire Blue", "Sandstone Orange"]
images = [(f"Main image: {c}", f"Samsung Galaxy S24 in {c}, front and back view",
           f"The Galaxy S24 in {c}, with a flat 6.2-inch display, aluminium frame and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S24 triple camera: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S24 triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("In the hand", "Samsung Galaxy S24 held in one hand, showing its compact size",
     "The Galaxy S24 in the hand: a 6.2-inch screen in a 167g phone that's easy to use one-handed."),
    ("Galaxy AI", "Samsung Galaxy S24 showing Circle to Search on screen",
     "Galaxy AI on the Galaxy S24: Circle to Search, Live Translate, Note Assist and Generative Edit."),
    ("Screen on, front", "Samsung Galaxy S24 flat 6.2-inch Dynamic AMOLED 2X display switched on",
     "The flat 6.2-inch 120Hz screen of the Galaxy S24, up to 2,600 nits."),
    ("In the box", "Samsung Galaxy S24 with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S24 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S24 compact phone with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Chip: the page says Exynos 2400, correct for UK/European stock. If any units are US imports with the Snapdragon, say so.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

"""Samsung Galaxy S23+ — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s23-plus"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S23+"
FULL = "Samsung Galaxy S23+"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s23-plus/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S23-Plus"   # ❓ Samsung pattern still to confirm; "Plus" spelled out as in the URL
TAGLINE = "Big screen power with flagship performance."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S23+ | 6.6-inch, 120Hz | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S23+ with a 6.6-inch 120Hz screen, Snapdragon 8 Gen 2, 50MP triple ca"
             "mera and 45W charging. 60-point checked, 2-year warranty, MOT.")
OG_TITLE = "Galaxy S23+: 6.6-inch screen, Snapdragon 8 Gen 2, 2-year cover"
OG_DESC = "The big-screen Galaxy S23, with the Snapdragon 8 Gen 2, a 50MP triple camera and 45W charging. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S23+ with a 2-year warranty | CrC Repair®"
X_DESC = "6.6-inch 120Hz screen, Snapdragon 8 Gen 2, 50MP triple camera and 45W charging. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S23 series", "Model family. Links the Galaxy S23, S23+, S23 FE and S23 Ultra listings."),
    ("Galaxy S23+", "Exact model, as Samsung writes it. If WooCommerce dislikes the + in a tag slug, use \"Galaxy S23 Plus\"."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s23p-box", "What comes with the Galaxy S23+?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s23p-vs-s22p", "What's the difference between the Galaxy S23+ and S22+?",
     "The S23+ has the Snapdragon 8 Gen 2 for Galaxy chip in every region, where the UK S22+ used Samsung's Exynos "
     "2200, so it's faster and noticeably more efficient. The battery grew from 4,500 to 4,700mAh, storage starts at "
     "256GB instead of 128GB, the glass is tougher Gorilla Glass Victus 2 and the camera island is gone for a cleaner "
     "design. The 6.6-inch screen, cameras and 45W charging are the same."),
    ("faq-s23p-vs-s24p", "Should I choose the Galaxy S23+ or the S24+?",
     "The S24+ has a sharper QHD+ screen, 12GB of RAM against 8GB, a slightly bigger battery, Galaxy AI from launch "
     "and seven years of updates against four. But in the UK the S24+ uses Samsung's Exynos 2400, while the S23+ has "
     "the Snapdragon 8 Gen 2 for Galaxy, and the S23+ gained most Galaxy AI features in a 2024 update. The S23+ is "
     "the better-value choice if you don't need the sharper screen."),
    ("faq-s23p-ai", "Does the Galaxy S23+ have Galaxy AI?",
     "Yes, most of it. Galaxy AI launched on the S24 series and was added to the S23+ with One UI 6.1 in 2024: Circle "
     "to Search, Live Translate, Interpreter, Note Assist, Chat Assist and Generative Edit. Some newer AI features "
     "are limited to the S24 series and later."),
    ("faq-s23p-updates", "Is the Galaxy S23+ still supported by Samsung?",
     "Yes. Samsung promised four Android upgrades and five years of security updates from its 2023 launch, so it runs "
     "Android 16 with One UI 8, has Android 17 to come as its last major upgrade, and gets security updates into 2028."),
    ("faq-s23p-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s23p-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 8GB RAM"),
    ("Colours", "Phantom Black, Cream, Green and Lavender · Graphite and Lime (Samsung online exclusives)"),
    ("Display", "6.6-inch Dynamic AMOLED 2X · FHD+ 2340 × 1080 · 390 ppi · flat"),
    ("Refresh rate", "Adaptive 48Hz to 120Hz · Always-On display"),
    ("Brightness", "Up to 1,750 nits peak"),
    ("Glass", "Corning Gorilla Glass Victus 2, front and back"),
    ("Chip", "Snapdragon 8 Gen 2 for Galaxy · 4nm · octa-core"),
    ("Main camera", "50MP · ƒ/1.8 · optical image stabilisation"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120°"),
    ("Telephoto camera", "10MP · 3x optical zoom · ƒ/2.4 · stabilised"),
    ("Zoom range", "0.6x to 3x optical · Space Zoom up to 30x"),
    ("Photography", "Nightography · Expert RAW · Astrophoto · Galaxy AI Generative Edit (added 2024)"),
    ("Video", "8K at 30fps · 4K at 60fps · Super Steady"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("Build", "Armor Aluminum frame · 196g · 7.6mm"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,700mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 6E · Bluetooth 5.3 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · four Android upgrades and security updates to 2028 promised"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the big-screen Galaxy S23 with Snapdragon power", [
        f"The <strong>{FULL}</strong> gives you a 6.6-inch 120Hz screen and a big 4,700mAh battery with 45W "
        "charging, in a flat-edged Armor Aluminum body with Gorilla Glass Victus 2 front and back. It runs the "
        "<strong>Snapdragon 8 Gen 2 for Galaxy</strong>, the same chip as the S23 Ultra, which Samsung used in every "
        "region that year, UK included.",
        "The triple camera pairs a 50MP main sensor with a 3x telephoto and an Ultra Wide, with Nightography for low "
        "light and 8K video. <strong>Galaxy AI</strong> arrived in a 2024 update, bringing Circle to Search, Live "
        "Translate and Generative Edit, and Samsung's four Android upgrades keep it current into 2028.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>FHD+ screen, 48–120Hz.</strong> The screen is sharp and bright at 1,750 nits, but it's FHD+ rather "
        "than the QHD+ of the S23 Ultra and S24+, and its refresh rate adapts between 48Hz and 120Hz rather than down "
        "to 1Hz.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter; wireless charging is 15W.",
        "<strong>Galaxy AI arrived later, and updates end sooner.</strong> Galaxy AI came in 2024 with One UI 6.1, "
        "but some newer features are limited to the S24 series and later. Android 17 will be its last major upgrade, "
        "with security updates into 2028.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s23p-chip", "Snapdragon 8 Gen 2 for Galaxy",
         "A chip tuned for Samsung with higher clock speeds than the standard version, used in every region for the "
         "S23 series, for smooth gaming, 8K video and far better efficiency than the UK S22+'s Exynos."),
        ("feat-s23p-display", "6.6-inch 120Hz display",
         "A flat Dynamic AMOLED 2X screen with 1,750 nits peak brightness for sunlight, an adaptive 48–120Hz refresh "
         "rate and an Always-On display, in the same size as the S24+."),
        ("feat-s23p-battery", "4,700mAh battery, 45W charging",
         "Comfortably lasts a full day, 200mAh more than the S22+, with 45W wired charging to around 65% in 30 minutes, "
         "15W wireless charging and reverse wireless charging for earbuds or a watch."),
        ("feat-s23p-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and Astrophoto for the night sky."),
        ("feat-s23p-ai", "Galaxy AI, added in 2024",
         "Circle to Search finds anything on screen, Live Translate turns your calls into another language in real "
         "time, Note Assist tidies notes and Generative Edit moves or removes objects in photos."),
        ("feat-s23p-build", "Victus 2 and IP68",
         "Gorilla Glass Victus 2 front and back, an Armor Aluminum frame and IP68 water and dust resistance to 1.5 "
         "metres, in a cleaner design without the S22's camera island."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a big-screen Samsung flagship with a Snapdragon chip, a strong battery and "
        "Galaxy AI at a price well below the S24+ and S25+. Coming from an S20+, S21+ or S22+, you'll notice the "
        "efficiency, the brighter screen and the AI features.",
        "If you want a sharper QHD+ screen, 12GB of RAM and seven years of updates, the Galaxy S24+ has them, with the "
        "Exynos chip in the UK. For the S Pen, the 200MP camera and 10x zoom, look at the S23 Ultra. If you'd prefer "
        "something smaller, the Galaxy S23 has the same chip and cameras in a 6.1-inch phone. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s23p-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s23p-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s23p-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s23p-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s23p-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s23p-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s23p-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s23p-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S23+
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  - The old copy was correct (Snapdragon 8 Gen 2 for Galaxy, Armor Aluminum, Victus 2, 50MP triple camera,
    6.6-inch FHD+ 120Hz, storage, all six colours). Kept its facts and made them specific: 2340 × 1080, 1,750 nits,
    48–120Hz adaptive (not 1–120Hz LTPO, which is Ultra/S24+ only), 8GB RAM, 4,700mAh, 45W, 196g.
  - "All-day battery life with intelligent power management" → vague; replaced with the figures.
  - "What's New vs S22 Plus" kept and made specific, with the UK point that the S22+ used Exynos here, so the
    Snapdragon was a bigger upgrade for UK buyers than the old copy implied. 256GB base storage, 4,700 vs 4,500mAh.
  - Name: Samsung writes "Galaxy S23+"; the old copy had "Plus". Page uses "S23+"; the URL and booking value keep
    "Plus" spelled out.
  - Added what the old copy left out: Galaxy AI arrived in 2024 (honest about what's limited to S24+), update policy
    (four upgrades, security to 2028), no charger in the box, S23+ vs S24+ FAQ including the UK chip difference,
    full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by Tom's Guide, GSMArena and UK retailers (Snapdragon 8 Gen 2 for Galaxy, 8GB, 256/512GB, 6.6-inch FHD+
  2340 × 1080 at 48–120Hz, 4,700mAh, 45W, 196g, 50MP main). The 12MP Ultra Wide, 10MP 3x telephoto, Wi-Fi 6E and
  the Graphite/Lime online-exclusive colours are Samsung's launch figures. Software line assumes One UI 8 /
  Android 16 in Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question; Plus vs +.
  2. Colours: trim the six listed to what you stock.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra FE S Pen Snapdragon Gen Elite Exynos Dynamic AMOLED QHD+ FHD+ LTPO Nightography Expert RAW Astrophoto Space Zoom Super Steady Gorilla Glass Victus Armor Aluminum Always-On One UI Android Galaxy AI Circle Search Live Translate Interpreter Note Assist Chat Generative Edit Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S20 S21 S22 S23 S24 S25 QHD W SIM Corning UK A".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S23+",
             "Samsung Galaxy S23+ with a 6.6-inch 120Hz Dynamic AMOLED 2X display, Snapdragon 8 Gen 2 for Galaxy chip, 8GB "
             "RAM, 50MP triple camera with 3x telephoto, 4,700mAh battery with 45W charging, Galaxy AI and 5G. 60-point "
             "quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Phantom Black", "Cream", "Green", "Lavender", "Graphite", "Lime"]
images = [(f"Main image: {c}", f"Samsung Galaxy S23+ in {c}, front and back view",
           f"The Galaxy S23+ in {c}, with a flat 6.6-inch display, aluminium frame and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S23+ triple camera: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S23+ triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto, without a camera island."),
    ("Screen on, front", "Samsung Galaxy S23+ flat 6.6-inch Dynamic AMOLED 2X display switched on",
     "The flat 6.6-inch 120Hz screen of the Galaxy S23+, up to 1,750 nits."),
    ("Galaxy AI", "Samsung Galaxy S23+ showing Circle to Search on screen",
     "Galaxy AI on the Galaxy S23+, added in 2024: Circle to Search, Live Translate, Note Assist and Generative Edit."),
    ("In the box", "Samsung Galaxy S23+ with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S23+ with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S23+ with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Six colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product. If WooCommerce mangles the + in \"Galaxy S23+\", use \"Galaxy S23 Plus\".",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern and Plus vs +.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

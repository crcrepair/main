"""Samsung Galaxy S25+ — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s25-plus"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S25+"
FULL = "Samsung Galaxy S25+"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s25-plus/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S25-Plus"   # ❓ Samsung pattern still to confirm; "Plus" spelled out as in the URL
TAGLINE = "Bigger, smarter, and beautifully refined."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S25+ | 6.7-inch, Galaxy AI | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S25+ with a 6.7-inch QHD+ 120Hz screen, the Snapdragon 8 Elite, Galax"
             "y AI and a 50MP triple camera. 60-point checked, 2-year warranty.")
OG_TITLE = "Galaxy S25+: 6.7-inch screen, Snapdragon 8 Elite, 2-year cover"
OG_DESC = "The big-screen Galaxy S25: Snapdragon 8 Elite, Galaxy AI and a 50MP triple camera. Fully checked and covered for two years."
X_TITLE = "Samsung Galaxy S25+ with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch QHD+ 120Hz screen, Snapdragon 8 Elite, Galaxy AI and 50MP triple camera. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S25 series", "Model family. Links the Galaxy S25, S25+, S25 Edge and S25 Ultra listings."),
    ("Galaxy S25+", "Exact model, as Samsung writes it. If WooCommerce dislikes the + in a tag slug, use \"Galaxy S25 Plus\"."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s25p-box", "What comes with the Galaxy S25+?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s25p-vs-s24p", "What's the difference between the Galaxy S25+ and S24+?",
     "The S25+ has the much faster Snapdragon 8 Elite for Galaxy chip (the UK S24+ used Samsung's Exynos 2400), "
     "12GB of RAM, a thinner and lighter body at 7.3mm and 190g, and the newer Galaxy AI features such as Now Brief, "
     "the Now Bar and actions across apps. The 6.7-inch QHD+ screen, cameras, 4,900mAh battery and 45W charging are "
     "the same."),
    ("faq-s25p-vs-ultra", "Should I choose the Galaxy S25+ or the S25 Ultra?",
     "They share the same chip, 12GB of RAM, Galaxy AI and seven years of updates. The Ultra adds a 6.9-inch screen, "
     "a titanium frame, the built-in S Pen, a 200MP main camera, a 50MP Ultra Wide and a 5x telephoto. The S25+ is "
     "lighter at 190g against 218g, noticeably cheaper, and still has a 50MP main camera and 3x telephoto."),
    ("faq-s25p-ai", "What can Galaxy AI do on the S25+?",
     "Now Brief gives a morning, midday and evening summary of your day. The Now Bar on the lock screen shows live "
     "activities. You can ask Gemini to do things across several apps in one request, Audio Eraser removes background "
     "noise from videos, and Circle to Search, Live Translate, Note Assist and Generative Edit are all included. Most "
     "features run on the phone."),
    ("faq-s25p-updates", "Is the Galaxy S25+ still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2025 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2032."),
    ("faq-s25p-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s25p-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 12GB RAM on both"),
    ("Colours", "Navy, Icyblue, Silver Shadow and Mint · Blueblack, Coralred and Pinkgold (Samsung online exclusives)"),
    ("Display", "6.7-inch Dynamic AMOLED 2X · QHD+ 3120 × 1440 · 513 ppi · flat"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Glass Victus 2, front and back"),
    ("Chip", "Snapdragon 8 Elite for Galaxy · 3nm · octa-core"),
    ("Main camera", "50MP · ƒ/1.8 · optical image stabilisation"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120°"),
    ("Telephoto camera", "10MP · 3x optical zoom · ƒ/2.4 · stabilised"),
    ("Zoom range", "0.6x to 3x optical · Space Zoom up to 30x"),
    ("Photography", "ProVisual Engine · Nightography · Expert RAW · Generative Edit · Virtual Aperture"),
    ("Video", "8K at 30fps · 4K at 60fps · 10-bit HDR as standard · Log video · Audio Eraser"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("Build", "Armor Aluminum frame · 190g · 7.3mm thin"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,900mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.4 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2032)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the big-screen Galaxy S25, slim and light", [
        f"The <strong>{FULL}</strong> gives you the Galaxy S25's flagship chip and Galaxy AI with a larger 6.7-inch "
        "QHD+ screen, in a body that's just 7.3mm thin and 190g. Inside is the <strong>Snapdragon 8 Elite for "
        "Galaxy</strong> with 12GB of RAM, a big step up from the Exynos chip in the UK S24+.",
        "The triple camera pairs a 50MP main sensor with a 3x telephoto and an Ultra Wide, with Nightography for low "
        "light and 8K video. <strong>Galaxy AI</strong> adds Now Brief, the Now Bar, actions across apps and Audio "
        "Eraser, the 4,900mAh battery charges at 45W, and Samsung promises <strong>seven years of updates</strong>.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Aluminium, not titanium.</strong> The S25+ has an Armor Aluminum frame with Gorilla Glass Victus 2. "
        "Titanium, the S Pen, the 200MP camera and the 5x zoom are S25 Ultra features.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter; wireless charging is 15W.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account, and some Gemini features depend on Google's plans.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s25p-display", "6.7-inch QHD+ display",
         "A sharper screen than the standard S25's FHD+, with 2,600 nits peak brightness for sunlight, an adaptive "
         "1–120Hz refresh rate and an Always-On display."),
        ("feat-s25p-chip", "Snapdragon 8 Elite for Galaxy",
         "Qualcomm's 3nm flagship chip, tuned for Samsung and in every region this year, with a big jump in speed and "
         "efficiency over the Exynos in the UK S24+, and 12GB of RAM for on-device AI."),
        ("feat-s25p-ai", "Galaxy AI, now across apps",
         "Ask for several things at once across apps, get a Now Brief summary of your day, see live activities in the "
         "Now Bar, and remove background noise from videos with Audio Eraser. Circle to Search and Live Translate are included."),
        ("feat-s25p-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and the ProVisual Engine for colour and detail."),
        ("feat-s25p-design", "Slim and light",
         "At 7.3mm and 190g it's thinner and lighter than the S24+, with rounded corners, an Armor Aluminum frame and "
         "Gorilla Glass Victus 2 front and back, rated IP68."),
        ("feat-s25p-battery", "4,900mAh and seven years of updates",
         "Comfortably a full day, with 45W wired charging to around 65% in 30 minutes, 15W wireless and reverse "
         "wireless charging, on a phone Samsung will keep updating until 2032."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a big, sharp screen and the newest Samsung chip and Galaxy AI without "
        "paying for the Ultra's stylus and camera extras, in a phone that's lighter and easier to hold. Coming from an "
        "S22+, S21+ or an older A-series, you'll notice the brighter screen, the much faster chip and the AI features.",
        "If you want the S Pen, the 200MP camera or the 5x zoom, the Galaxy S25 Ultra has them. If you'd prefer "
        "something smaller, the Galaxy S25 has the same chip and cameras in a 6.2-inch phone. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s25p-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s25p-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s25p-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s25p-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s25p-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s25p-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s25p-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s25p-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S25+
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the S23/S24/S25 Ultra pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's
update policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  The old copy was written BEFORE LAUNCH and several claims are WRONG. All corrected:
  - "refined titanium frame" / "Titanium-infused frame" → the S25+ frame is ALUMINIUM (Armor Aluminum). Titanium
    is S25 Ultra only. Now stated plainly in "Before you buy" so nobody buys it expecting titanium.
  - "6.7\\" FHD+" → the S25+ screen is QHD+ (3120 × 1440). FHD+ is the standard S25.
  - "Snapdragon 8 Gen 4 for Galaxy" → Snapdragon 8 Elite for Galaxy.
  - "New AI-powered Pro Mode" and "Galaxy AI 2.0 Suite" → not Samsung names. Replaced with the real features:
    Now Brief, Now Bar, cross-app actions, Audio Eraser, ProVisual Engine. "adaptive battery management" dropped.
  - "What's New vs S24+" rewritten with the real differences: Snapdragon in place of the UK Exynos 2400, 12GB RAM,
    thinner and lighter; screen, cameras and battery unchanged.
  - Colours: "Blueback" was a typo for Blueblack. Samsung's seven colours kept (four shop, three online exclusives).
  - Name: Samsung writes "Galaxy S25+"; the old copy had "Plus". Page uses "S25+"; the URL and booking value keep
    "Plus" spelled out.
  - Storage, 120Hz LTPO and 50MP triple camera in the old copy were correct.
  - Added what the old copy left out: no charger in the box, cloud AI caveat, update policy to 2032, S25+ vs Ultra
    FAQ, full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by GSMArena and UK retailers (Snapdragon 8 Elite in all markets, 12GB, 6.7-inch QHD+ 3120 × 1440,
  4,900mAh, 50MP + 12MP + 10MP 3x, colours). 190g, 7.3mm and Armor Aluminum are Samsung's launch figures.
  Software line assumes One UI 8 / Android 16 in Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question; also whether your
     booking system uses "Plus" or "+".
  2. Colours: trim the seven listed to what you stock.
  3. Tag "Galaxy S25+": if WooCommerce mangles the + in the tag slug, use "Galaxy S25 Plus" instead.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra Edge S Pen Snapdragon Elite Exynos Dynamic AMOLED QHD+ FHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Virtual Aperture Audio Eraser Log HDR Gorilla Glass Victus Armor Aluminum Always-On One UI Android Galaxy AI Circle Search Live Translate Note Assist Generative Edit Now Brief Bar Gemini Google Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S22 S21 S24 S25 QHD W SIM Corning Qualcomm Wide A".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S25+",
             "Samsung Galaxy S25+ with a 6.7-inch QHD+ 120Hz Dynamic AMOLED 2X display, Snapdragon 8 Elite for Galaxy chip, "
             "12GB RAM, Galaxy AI, 50MP triple camera with 3x telephoto, 4,900mAh battery with 45W charging, 5G and seven "
             "years of updates. 60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT "
             "every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Navy", "Icyblue", "Silver Shadow", "Mint", "Blueblack", "Coralred", "Pinkgold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S25+ in {c}, front and back view",
           f"The Galaxy S25+ in {c}, with a 6.7-inch QHD+ display, slim aluminium frame and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S25+ triple camera: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S25+ triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("Galaxy AI", "Samsung Galaxy S25+ showing Now Brief on screen",
     "Galaxy AI on the Galaxy S25+: Now Brief, the Now Bar, cross-app actions and Audio Eraser."),
    ("Screen on, front", "Samsung Galaxy S25+ 6.7-inch Dynamic AMOLED 2X display switched on",
     "The 6.7-inch QHD+ 120Hz screen of the Galaxy S25+, up to 2,600 nits."),
    ("Side view", "Side of the Samsung Galaxy S25+ showing the 7.3mm aluminium frame",
     "The slim 7.3mm Armor Aluminum frame of the Galaxy S25+, at 190g."),
    ("In the box", "Samsung Galaxy S25+ with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S25+ with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S25+ with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product. If WooCommerce mangles the + in \"Galaxy S25+\", use \"Galaxy S25 Plus\".",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern and Plus vs +.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

"""Samsung Galaxy S25 — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s25"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S25"
FULL = "Samsung Galaxy S25"
# ❓ Gabor sent the S25+ URL for this product; this is the presumed S25 URL. CONFIRM before publishing: the schema @id uses it.
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s25/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S25"   # ❓ Samsung pattern still to confirm
TAGLINE = "Compact power with next-gen AI intelligence."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S25 | Compact, Galaxy AI | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S25 with a 6.2-inch 120Hz screen, the Snapdragon 8 Elite, Galaxy AI and a 50MP triple "
             "camera, at just 162g. 60-point checked, 2-year warranty and free MOT.")
OG_TITLE = "Galaxy S25: compact flagship with Snapdragon 8 Elite, 2-year warranty"
OG_DESC = "The compact Galaxy S25: Snapdragon 8 Elite, Galaxy AI and a 50MP triple camera at 162g. Fully checked and covered for two years."
X_TITLE = "Samsung Galaxy S25 with a 2-year warranty | CrC Repair®"
X_DESC = "6.2-inch 120Hz screen, Snapdragon 8 Elite, Galaxy AI and 50MP triple camera at 162g. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S25 series", "Model family. Links the Galaxy S25, S25+, S25 Edge and S25 Ultra listings."),
    ("Galaxy S25", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s25-box", "What comes with the Galaxy S25?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s25-vs-s24", "What's the difference between the Galaxy S25 and S24?",
     "The S25 has the much faster Snapdragon 8 Elite for Galaxy chip (the UK S24 used Samsung's Exynos 2400), 12GB of "
     "RAM in place of 8GB, a thinner and lighter body at 7.2mm and 162g, and the newer Galaxy AI features such as Now "
     "Brief, the Now Bar and actions across apps. The 6.2-inch screen, cameras, 4,000mAh battery and 25W charging are "
     "the same."),
    ("faq-s25-vs-plus", "Should I choose the Galaxy S25 or the S25+?",
     "They share the same chip, 12GB of RAM, cameras, Galaxy AI and seven years of updates. The S25+ has a larger "
     "6.7-inch QHD+ screen, a bigger 4,900mAh battery and faster 45W charging. The S25 is the one to pick if you want "
     "a phone that's easy to use one-handed: 6.2 inches and 162g against 190g, and it's cheaper."),
    ("faq-s25-ai", "What can Galaxy AI do on the S25?",
     "Now Brief gives a morning, midday and evening summary of your day. The Now Bar on the lock screen shows live "
     "activities. You can ask Gemini to do things across several apps in one request, Audio Eraser removes background "
     "noise from videos, and Circle to Search, Live Translate, Note Assist and Generative Edit are all included. Most "
     "features run on the phone."),
    ("faq-s25-updates", "Is the Galaxy S25 still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2025 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2032."),
    ("faq-s25-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s25-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "128GB · 256GB · 512GB · 12GB RAM on every model"),
    ("Colours", "Navy, Icyblue, Silver Shadow and Mint · Blueblack, Coralred and Pinkgold (Samsung online exclusives)"),
    ("Display", "6.2-inch Dynamic AMOLED 2X · FHD+ 2340 × 1080 · 416 ppi · flat"),
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
    ("Build", "Armor Aluminum frame · 162g · 7.2mm thin"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,000mAh"),
    ("Charging", "USB-C · 25W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.4 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2032)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the compact flagship with Galaxy AI", [
        f"The <strong>{FULL}</strong> is the small one of the range: a 6.2-inch 120Hz screen in a body that's 7.2mm "
        "thin and just 162g, so it's easy to use one-handed and light in a pocket. It runs the same "
        "<strong>Snapdragon 8 Elite for Galaxy</strong> chip and 12GB of RAM as the S25 Ultra, a big step up from "
        "the Exynos chip in the UK S24.",
        "The triple camera pairs a 50MP main sensor with a 3x telephoto and an Ultra Wide, with Nightography for low "
        "light and 8K video. <strong>Galaxy AI</strong> adds Now Brief, the Now Bar, actions across apps and Audio "
        "Eraser, and Samsung promises <strong>seven years of updates</strong>, so it stays current until 2032.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Aluminium, not titanium.</strong> The S25 has an Armor Aluminum frame with Gorilla Glass Victus 2. "
        "Titanium, the S Pen, the 200MP camera and the 5x zoom are S25 Ultra features.",
        "<strong>Smaller battery, 25W charging.</strong> The 4,000mAh battery lasts a normal day but not as long as "
        "the S25+ (4,900mAh), and wired charging is 25W rather than 45W. No charger is included; it comes with a "
        "USB-C cable.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account, and some Gemini features depend on Google's plans.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s25-size", "Compact and light",
         "At 6.2 inches, 7.2mm and 162g it's one of the few small flagships left, comfortable one-handed and light in "
         "a pocket, with rounded corners, an Armor Aluminum frame and Gorilla Glass Victus 2 front and back."),
        ("feat-s25-chip", "Snapdragon 8 Elite for Galaxy",
         "The same 3nm flagship chip as the S25 Ultra, in every region this year, with a big jump in speed and "
         "efficiency over the Exynos in the UK S24, and 12GB of RAM for on-device AI."),
        ("feat-s25-ai", "Galaxy AI, now across apps",
         "Ask for several things at once across apps, get a Now Brief summary of your day, see live activities in the "
         "Now Bar, and remove background noise from videos with Audio Eraser. Circle to Search and Live Translate are included."),
        ("feat-s25-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and the ProVisual Engine for colour and detail."),
        ("feat-s25-display", "6.2-inch 120Hz display",
         "A flat Dynamic AMOLED 2X screen with 2,600 nits peak brightness for sunlight, an adaptive 1–120Hz refresh "
         "rate and an Always-On display."),
        ("feat-s25-updates", "Seven years of updates",
         "Samsung promised seven years of Android upgrades and security updates from 2025, so a pre-owned S25 stays "
         "current until 2032, with IP68 water resistance and Wi-Fi 7 for the long haul."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a genuinely compact phone with the newest Samsung chip, Galaxy AI and a "
        "proper telephoto camera, at the lowest price of the S25 range. Coming from an S21, S22, S23 or an A-series, "
        "you'll notice the lighter body, the much faster chip and the AI features.",
        "If battery life matters most, the Galaxy S25+ has a bigger battery, faster charging and a larger, sharper "
        "screen. For the S Pen, the 200MP camera or the 5x zoom, look at the S25 Ultra. Not sure which suits you? Ask "
        "in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s25-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s25-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s25-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s25-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s25-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s25-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s25-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s25-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S25
PRODUCT URL:       {URL}
                   ❓ PRESUMED. Gabor sent the S25+ URL with this product. The schema @id uses this URL, so confirm
                   it matches the live product before pasting the schema.
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  The old copy was written BEFORE LAUNCH and most of its claims are WRONG. All corrected:
  - "refined titanium frame" / "Premium titanium build" → the S25 frame is ALUMINIUM (Armor Aluminum). Titanium is
    S25 Ultra only. Stated plainly in "Before you buy".
  - "6.3\\" FHD+" → the screen is 6.2-inch (FHD+ 2340 × 1080 is correct).
  - "Dual camera system" → the S25 has a TRIPLE camera: 50MP main, 12MP Ultra Wide, 10MP 3x telephoto.
  - "Titanium Gray, Titanium Black, Titanium Blue, Titanium Copper" → none of these are S25 colours. The S25 comes
    in Navy, Icyblue, Silver Shadow and Mint, plus Blueblack, Coralred and Pinkgold online.
  - "Snapdragon 8 Gen 4 for Galaxy" → Snapdragon 8 Elite for Galaxy.
  - "AI-driven Photo Assist", "Galaxy AI 2.0 Suite", "smart battery optimization" → not Samsung names. Replaced with
    the real features: Now Brief, Now Bar, cross-app actions, Audio Eraser, ProVisual Engine.
  - "What's New vs S24" rewritten with the real differences: Snapdragon in place of the UK Exynos 2400, 12GB RAM
    (was 8GB), thinner and lighter; screen, cameras and battery unchanged. The titanium claim removed.
  - "Already own an Samsung" → "a".
  - Storage options and 120Hz LTPO in the old copy were correct.
  - Added what the old copy left out: 4,000mAh and 25W (smaller and slower than the S25+), no charger in the box,
    cloud AI caveat, update policy to 2032, S25 vs S25+ FAQ, full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by O2 UK, GSMArena and reviews (6.2-inch 120Hz LTPO, Snapdragon 8 Elite, 12GB, 128/256/512GB, 50MP +
  12MP + 10MP 3x, 4,000mAh, 25W, 162g, colours). 7.2mm, 2340 × 1080 and Armor Aluminum are Samsung's launch
  figures. Software line assumes One UI 8 / Android 16 in Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. LIVE URL: confirm {URL}
  2. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  3. Colours: trim the seven listed to what you stock.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra Edge S Pen Snapdragon Elite Exynos Dynamic AMOLED QHD+ FHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Virtual Aperture Audio Eraser Log HDR Gorilla Glass Victus Armor Aluminum Always-On One UI Android Galaxy AI Circle Search Live Translate Note Assist Generative Edit Now Brief Bar Gemini Google Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S21 S22 S23 S24 S25 QHD W SIM Corning Qualcomm Wide A".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S25",
             "Samsung Galaxy S25 with a 6.2-inch 120Hz Dynamic AMOLED 2X display, Snapdragon 8 Elite for Galaxy chip, 12GB "
             "RAM, Galaxy AI, 50MP triple camera with 3x telephoto, 4,000mAh battery, 5G and seven years of updates, at "
             "162g. 60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Navy", "Icyblue", "Silver Shadow", "Mint", "Blueblack", "Coralred", "Pinkgold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S25 in {c}, front and back view",
           f"The Galaxy S25 in {c}, with a 6.2-inch display, slim aluminium frame and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S25 triple camera: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S25 triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("In the hand", "Samsung Galaxy S25 held in one hand, showing its compact size",
     "The Galaxy S25 in the hand: a 6.2-inch screen in a 162g phone that's easy to use one-handed."),
    ("Galaxy AI", "Samsung Galaxy S25 showing Now Brief on screen",
     "Galaxy AI on the Galaxy S25: Now Brief, the Now Bar, cross-app actions and Audio Eraser."),
    ("Screen on, front", "Samsung Galaxy S25 6.2-inch Dynamic AMOLED 2X display switched on",
     "The 6.2-inch 120Hz screen of the Galaxy S25, up to 2,600 nits."),
    ("In the box", "Samsung Galaxy S25 with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S25 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S25 compact phone with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "LIVE URL: the S25+ URL was supplied with this product, so the schema uses the presumed <code>…/samsung-galaxy-s25/</code>. Confirm before pasting the schema.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

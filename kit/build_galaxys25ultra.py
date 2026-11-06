"""Samsung Galaxy S25 Ultra — long + short description, schema, SEO pack and tags (normal short description, no Black Friday)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s25-ultra"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S25 Ultra"
FULL = "Samsung Galaxy S25 Ultra"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s25-ultra/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S25-Ultra"   # ❓ Samsung pattern still to confirm
TAGLINE = "The Ultra evolves: AI-powered mastery with next-gen titanium."
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S25 Ultra | 200MP, AI | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S25 Ultra with the Snapdragon 8 Elite, 6.9-inch 120Hz screen, 200MP camera and "
             "S Pen. 60-point checked, 2-year warranty and free MOT.")
OG_TITLE = "Galaxy S25 Ultra: Snapdragon 8 Elite, 200MP camera, 2-year cover"
OG_DESC = "The lightest Ultra yet: Snapdragon 8 Elite, Galaxy AI, 200MP camera and 50MP Ultra Wide. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S25 Ultra with a 2-year warranty | CrC Repair®"
X_DESC = "Snapdragon 8 Elite, 6.9-inch 120Hz screen, 200MP camera, Galaxy AI and built-in S Pen. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S25 series", "Model family. Links the Galaxy S25, S25+, S25 Edge and S25 Ultra listings."),
    ("Galaxy S25 Ultra", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s25u-box", "What comes with the Galaxy S25 Ultra?",
     "The phone comes with a charging cable as standard, and the S Pen is built into the phone. For a plug, screen "
     "protector, case or wireless charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount "
     "on selected accessories is applied automatically in the basket."),
    ("faq-s25u-vs-s24u", "What's the difference between the Galaxy S25 Ultra and S24 Ultra?",
     "The S25 Ultra is lighter at 218g against 232g, with rounded corners, a slightly larger 6.9-inch screen with "
     "slimmer bezels and tougher Gorilla Armor 2 glass. It has the much faster Snapdragon 8 Elite for Galaxy chip, a "
     "new 50MP Ultra Wide camera in place of 12MP, and newer Galaxy AI features such as Now Brief, the Now Bar and "
     "actions across apps. The main, 3x and 5x cameras, battery, charging and S Pen are otherwise the same, though "
     "the S Pen no longer has Bluetooth."),
    ("faq-s25u-spen", "Does the S Pen still come with the S25 Ultra?",
     "Yes, it's built in and works for notes, sketches, annotating and signing as before. Samsung removed its "
     "Bluetooth, so the Air actions gestures and the remote camera shutter from earlier Ultras aren't available."),
    ("faq-s25u-ai", "What can Galaxy AI do on the S25 Ultra?",
     "Now Brief gives a morning, midday and evening summary of your day. The Now Bar on the lock screen shows live "
     "activities. You can ask Gemini to do things across several apps in one request, Audio Eraser removes background "
     "noise from videos, and Circle to Search, Live Translate, Note Assist and Generative Edit carry over from the "
     "S24. Most features run on the phone."),
    ("faq-s25u-updates", "Is the Galaxy S25 Ultra still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2025 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2032."),
    ("faq-s25u-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s25u-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 1TB · 12GB RAM on every model"),
    ("Colours", "Titanium Silverblue, Titanium Black, Titanium Grey and Titanium Whitesilver · Titanium Jadegreen, Titanium Jetblack and Titanium Pinkgold (Samsung online exclusives)"),
    ("Display", "6.9-inch Dynamic AMOLED 2X · QHD+ 3120 × 1440 · 498 ppi · flat"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Armor 2, anti-reflective (front) · Gorilla Glass Victus 2 (back)"),
    ("Chip", "Snapdragon 8 Elite for Galaxy · 3nm · octa-core"),
    ("Main camera", "200MP · ƒ/1.7 · optical image stabilisation"),
    ("Ultra Wide camera", "50MP · ƒ/1.9 · 120° · macro"),
    ("Telephoto cameras", "10MP 3x optical (ƒ/2.4) · 50MP 5x optical (ƒ/3.4) · both stabilised"),
    ("Zoom range", "0.6x to 5x optical · optical-quality to 10x · Space Zoom up to 100x"),
    ("Photography", "ProVisual Engine · Nightography · Expert RAW · Generative Edit · Virtual Aperture"),
    ("Video", "8K at 30fps · 4K at 120fps · 10-bit HDR as standard · Log video · Audio Eraser"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("S Pen", "Built in · no Bluetooth (no Air actions or remote shutter)"),
    ("Build", "Titanium frame · rounded corners · 218g · 8.2mm thin"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "5,000mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.4 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2032)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — lighter titanium, Snapdragon 8 Elite, 200MP camera", [
        f"The <strong>{FULL}</strong> is the lightest Ultra yet at 218g, with rounded corners, a slimmer titanium "
        "frame and a slightly larger 6.9-inch QHD+ screen behind anti-reflective Gorilla Armor 2 glass. Inside is the "
        "<strong>Snapdragon 8 Elite for Galaxy</strong>, a big step up in speed and efficiency, with 12GB of RAM on "
        "every model.",
        "The camera keeps the 200MP main sensor and the 3x and 5x telephotos, and adds a new <strong>50MP Ultra "
        "Wide</strong> for sharper wide shots and macro. <strong>Galaxy AI</strong> grows with Now Brief, the Now Bar "
        "and actions across apps, the <strong>S Pen</strong> is still built in, and Samsung promises seven years of "
        "updates.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>The S Pen has lost Bluetooth.</strong> It still writes, sketches and annotates exactly as before, but "
        "the Air actions gestures and the remote camera shutter from the S24 Ultra and earlier are gone.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter; wireless charging is 15W, and the battery is the same 5,000mAh as the S24 Ultra.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account, and some Gemini features depend on Google's plans.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s25u-chip", "Snapdragon 8 Elite for Galaxy",
         "Qualcomm's 3nm flagship chip, tuned for Samsung, with a big jump in CPU and graphics speed over the S24 Ultra "
         "and better efficiency for all-day battery life and on-device AI."),
        ("feat-s25u-ultrawide", "New 50MP Ultra Wide",
         "The Ultra Wide camera moves from 12MP to 50MP, so wide landscapes and macro shots are far more detailed, "
         "alongside the 200MP main camera and the 3x and 50MP 5x telephoto lenses."),
        ("feat-s25u-ai", "Galaxy AI, now across apps",
         "Ask for several things at once across apps, get a Now Brief summary of your day, see live activities in the "
         "Now Bar, and remove background noise from videos with Audio Eraser. Circle to Search and Live Translate carry over."),
        ("feat-s25u-design", "Lighter, rounder titanium",
         "At 218g it's 14g lighter than the S24 Ultra, 0.4mm thinner, with rounded corners that are more comfortable "
         "to hold and Gorilla Armor 2 glass that cuts reflections and survives drops better."),
        ("feat-s25u-display", "6.9-inch QHD+ display at 2,600 nits",
         "Slimmer bezels make room for a slightly larger screen in a smaller body, with an adaptive 1–120Hz refresh "
         "rate, an Always-On display and anti-reflective glass for sunlight."),
        ("feat-s25u-video", "Pro video and seven years of updates",
         "10-bit HDR video as standard, Log recording for colour grading and 8K at 30fps, on a phone Samsung will keep "
         "updating until 2032."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want Samsung's most capable phone with the newest Galaxy AI, the lightest Ultra "
        "design and the longest update support, at a pre-owned price below new. Coming from an S23 Ultra or earlier, "
        "you'll notice the lighter body, the far faster chip, the sharper Ultra Wide and the AI features.",
        "If you have an S24 Ultra, the main camera, battery and screen size are close, so the upgrade is the chip, the "
        "Ultra Wide and the weight. If you need the S Pen's remote shutter, the S24 Ultra keeps it. If you don't need a "
        "stylus at all, the Galaxy S25+ is lighter still. Not sure which suits you? Ask in any of our stores and "
        "we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s25u-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s25u-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s25u-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s25u-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s25u-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s25u-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s25u-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port, camera and S Pen faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s25u-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S25 Ultra
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the S23/S24 Ultra pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's
update policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  The old copy was written BEFORE LAUNCH and several headline claims are WRONG. All corrected:
  - "Snapdragon 8 Gen 4 for Galaxy" → the chip is the Snapdragon 8 Elite for Galaxy (Qualcomm renamed it).
  - "upgraded 250MP main sensor" → the main camera is 200MP, the same as the S23 and S24 Ultra. The real camera
    upgrade is the new 50MP Ultra Wide (was 12MP).
  - "New 7x periscope telephoto lens" → there is no 7x lens. The telephotos are 10MP 3x and 50MP 5x, as on the S24 Ultra.
  - "Galaxy AI 2.0 Suite" → not a Samsung name. The new features are Now Brief, Now Bar, cross-app actions and
    Audio Eraser; "smarter battery optimisation" dropped as unverifiable.
  - "stronger, lighter, and more eco-friendly" titanium → kept what's verifiable: 218g vs 232g, 8.2mm, rounded corners.
  - 6.9-inch QHD+ 120Hz LTPO, storage and colours in the old copy were correct. Colours: "Gray" written "Grey" for
    the UK, as on the S24 Ultra page (Samsung's own spelling varies); four shop colours plus three online exclusives.
  - ADDED, as it affects buyers: the S Pen lost Bluetooth (no Air actions or remote shutter). Stated in "Before you
    buy", the spec list and an FAQ.
  - Added what the old copy left out: no charger in the box, cloud AI caveat, update policy to 2032, full spec list.
  - "Storage Options", "Key Features", "What's New" in sentence case; "choosen" spelling fixed; "click here" given
    descriptive anchor text; "optimization" → British spelling where kept.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by TechRadar and UK retailers (Snapdragon 8 Elite for Galaxy, 6.9-inch 3120 × 1440, 218g, 12GB, 200MP +
  50MP UW + 50MP 5x + 10MP 3x, 5,000mAh, 45W, Gorilla Armor front). Gorilla Armor 2, Bluetooth 5.4, 12MP front
  camera and the S Pen Bluetooth removal are Samsung's launch announcements. Software line assumes One UI 8 /
  Android 16 in Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question as the S23/S24 Ultra.
  2. Colours: trim the seven listed to what you stock.
  3. Tagline: kept the old copy's "{TAGLINE}". It's long for a tagline; say if you'd like a shorter one.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (6 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra Edge S Pen Snapdragon Elite Dynamic AMOLED QHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Virtual Aperture Audio Eraser Log HDR Gorilla Armor Glass Victus Always-On One UI Android Galaxy AI Circle Search Live Translate Note Assist Generative Edit Now Brief Bar Gemini Google Bluetooth Air Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S23 S24 S25 QHD W SIM Corning Qualcomm Wide".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S25 Ultra",
             "Samsung Galaxy S25 Ultra with a titanium frame, 6.9-inch QHD+ 120Hz Dynamic AMOLED 2X display with Gorilla "
             "Armor 2 glass, Snapdragon 8 Elite for Galaxy chip, Galaxy AI, 200MP main camera with 50MP Ultra Wide and 3x "
             "and 5x telephoto lenses, built-in S Pen, 5,000mAh battery with 45W charging, 5G and seven years of updates. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Titanium Silverblue", "Titanium Black", "Titanium Grey", "Titanium Whitesilver", "Titanium Jadegreen", "Titanium Jetblack", "Titanium Pinkgold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S25 Ultra in {c}, front and back view",
           f"The Galaxy S25 Ultra in {c}, with a flat 6.9-inch QHD+ display, rounded titanium frame, quad camera and built-in S Pen.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S25 Ultra quad camera: 200MP main, 50MP Ultra Wide, 3x and 5x telephoto",
     "The Galaxy S25 Ultra quad camera, with a 200MP main sensor, new 50MP Ultra Wide, 10MP 3x and 50MP 5x telephoto lenses."),
    ("S Pen", "Samsung Galaxy S25 Ultra with the S Pen pulled out from its slot",
     "The built-in S Pen of the Galaxy S25 Ultra, for notes, sketches and signatures."),
    ("Galaxy AI", "Samsung Galaxy S25 Ultra showing Now Brief on screen",
     "Galaxy AI on the Galaxy S25 Ultra: Now Brief, the Now Bar, cross-app actions and Audio Eraser."),
    ("Screen on, front", "Samsung Galaxy S25 Ultra flat 6.9-inch Dynamic AMOLED 2X display switched on",
     "The flat 6.9-inch QHD+ 120Hz screen of the Galaxy S25 Ultra, up to 2,600 nits with anti-reflective Gorilla Armor 2 glass."),
    ("In the box", "Samsung Galaxy S25 Ultra with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S25 Ultra with the S Pen built in and a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S25 Ultra in titanium with quad camera and S Pen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

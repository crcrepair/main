"""Samsung Galaxy S24 Ultra — long + short description, Black Friday short description, schema, SEO pack and tags."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s24-ultra"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S24 Ultra"
FULL = "Samsung Galaxy S24 Ultra"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s24-ultra/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S24-Ultra"   # ❓ Samsung pattern still to confirm (same as S23 Ultra)
TAGLINE = "The smartest Ultra ever, now with titanium."
BLACK_FRIDAY = True

META_TITLE = "Buy Samsung Galaxy S24 Ultra | Titanium, AI | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S24 Ultra with a titanium frame, Galaxy AI, 200MP camera, 5x telephoto and built-in "
             "S Pen. 60-point checked, 2-year warranty and MOT.")
OG_TITLE = "Galaxy S24 Ultra: titanium frame, Galaxy AI, 200MP, 2-year cover"
OG_DESC = "Samsung's titanium flagship with Galaxy AI, a 200MP camera, 5x telephoto and built-in S Pen. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S24 Ultra with a 2-year warranty | CrC Repair®"
X_DESC = "Titanium frame, Galaxy AI, 200MP camera, 5x telephoto and built-in S Pen. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S24 series", "Model family. Links the Galaxy S24, S24+ and S24 Ultra listings."),
    ("Galaxy S24 Ultra", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s24u-box", "What comes with the Galaxy S24 Ultra?",
     "The phone comes with a charging cable as standard, and the S Pen is built into the phone. For a plug, screen "
     "protector, case or wireless charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount "
     "on selected accessories is applied automatically in the basket."),
    ("faq-s24u-vs-s23u", "What's the difference between the Galaxy S24 Ultra and S23 Ultra?",
     "The S24 Ultra has a titanium frame in place of aluminium, a completely flat screen with anti-reflective Gorilla "
     "Armor glass that's brighter at 2,600 nits, the faster Snapdragon 8 Gen 3 for Galaxy chip, 12GB of RAM on every "
     "model, Wi-Fi 7 and seven years of updates against four. The 10x periscope lens is replaced by a 50MP 5x lens that "
     "gives sharper results from 5x to 10x. Galaxy AI launched on the S24 and was later added to the S23."),
    ("faq-s24u-ai", "What can Galaxy AI do on the S24 Ultra?",
     "Circle to Search lets you circle anything on screen to search it. Live Translate translates phone calls in "
     "real time, Interpreter does the same face to face, Note Assist summarises and formats notes, Chat Assist "
     "adjusts the tone of messages, and Generative Edit moves or removes objects in photos and fills in the "
     "background. Most features run on the phone itself."),
    ("faq-s24u-updates", "Is the Galaxy S24 Ultra still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2024 launch, so it runs "
     "Android 16 with One UI 8 now and will keep getting new versions and security updates until 2031, longer than "
     "any Galaxy before it."),
    ("faq-s24u-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-s24u-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s24u-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 1TB · 12GB RAM on every model"),
    ("Colours", "Titanium Grey, Titanium Black, Titanium Violet and Titanium Yellow · Titanium Blue, Green and Orange (Samsung online exclusives)"),
    ("Display", "6.8-inch Dynamic AMOLED 2X · QHD+ 3120 × 1440 · 505 ppi · flat"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Armor, anti-reflective, front and back"),
    ("Chip", "Snapdragon 8 Gen 3 for Galaxy · octa-core"),
    ("Main camera", "200MP · ƒ/1.7 · optical image stabilisation · Adaptive Pixel"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120°"),
    ("Telephoto cameras", "10MP 3x optical (ƒ/2.4) · 50MP 5x optical (ƒ/3.4) · both stabilised"),
    ("Zoom range", "0.6x to 5x optical · optical-quality to 10x · Space Zoom up to 100x"),
    ("Photography", "Galaxy AI Generative Edit · Nightography · Expert RAW · 50MP and 200MP modes"),
    ("Video", "8K at 30fps · 4K at 120fps · Super Steady · Instant Slow-mo"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("S Pen", "Built in · Bluetooth remote · Air actions"),
    ("Build", "Titanium frame · 232g"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "5,000mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.3 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · seven years of Android upgrades and security updates (to 2031)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — titanium, Galaxy AI and a 200MP camera", [
        f"The <strong>{FULL}</strong> is the first Galaxy with a <strong>titanium frame</strong> and the first with "
        "<strong>Galaxy AI</strong>: Circle to Search, Live Translate on calls, Note Assist and Generative Edit for "
        "photos, most of it running on the phone. The flat 6.8-inch QHD+ screen uses anti-reflective Gorilla Armor "
        "glass and reaches 2,600 nits, the brightest Galaxy at launch.",
        "The camera keeps the 200MP main sensor and adds a sharper <strong>50MP 5x telephoto</strong> that gives "
        "optical-quality shots all the way to 10x. The Snapdragon 8 Gen 3 for Galaxy chip, 12GB of RAM, a 5,000mAh "
        "battery with 45W charging and the built-in <strong>S Pen</strong> make it the complete flagship, with seven "
        "years of updates to come.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Big and heavy.</strong> At 232g and 162.3mm tall it's a large phone, only 2g lighter than the S23 "
        "Ultra despite the titanium. If you don't need a stylus, the Galaxy S24+ is lighter with the same Galaxy AI.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter; wireless charging is 15W.",
        "<strong>Some Galaxy AI features use the cloud.</strong> Most run on the phone, but a few need an internet "
        "connection and a Samsung account. Samsung has said some AI features may become paid after 2025.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s24u-ai", "Galaxy AI",
         "Circle to Search finds anything on screen, Live Translate turns your calls into another language in real "
         "time, Note Assist tidies and summarises notes, and Generative Edit moves or removes objects in photos."),
        ("feat-s24u-titanium", "Titanium frame, flat screen",
         "A titanium frame for strength and a premium feel, with a completely flat display and anti-reflective "
         "Gorilla Armor glass that cuts glare in sunlight and under office lights."),
        ("feat-s24u-camera", "200MP camera with 50MP 5x zoom",
         "The 200MP main sensor captures huge detail, and the new 50MP 5x telephoto gives sharp optical-quality shots "
         "from 5x to 10x, where the old 10x lens was weakest. Nightography handles low light."),
        ("feat-s24u-display", "6.8-inch QHD+ display at 2,600 nits",
         "The brightest Galaxy screen at launch, with an adaptive 1–120Hz refresh rate, flat edges for easier S Pen "
         "use and an Always-On display."),
        ("feat-s24u-spen", "Built-in S Pen",
         "The stylus slots into the phone, so it's always to hand for notes, sketches and signatures, and it works "
         "as a Bluetooth remote for the camera."),
        ("feat-s24u-updates", "Seven years of updates",
         "Samsung promised seven years of Android upgrades and security updates from 2024, so a pre-owned S24 Ultra "
         "stays current until 2031, longer than any phone before it."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the best Samsung camera, a built-in stylus, Galaxy AI and a phone that "
        "will keep getting updates for years, at a pre-owned price below the S25 Ultra. Coming from an S22 Ultra, S21 "
        "Ultra or a Note, you'll notice the brighter flat screen, the sharper zoom and the AI features.",
        "If you don't need the S Pen or the 5x zoom, the Galaxy S24+ has the same Galaxy AI in a lighter phone. For "
        "the S23 Ultra, you get the same 200MP camera and S Pen for less but shorter update support and no "
        "titanium. Not sure which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s24u-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s24u-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s24u-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s24u-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s24u-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s24u-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s24u-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port, camera and S Pen faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s24u-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S24 Ultra
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
BLACK FRIDAY DEAL: {SLUG}-short-description-black-friday.html (use during the sale; the normal short
description is delivered too, for afterwards).

Samsung rules as on the Galaxy S23 Ultra page: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's
update policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  - The old copy was correct (titanium, Snapdragon 8 Gen 3 for Galaxy, 200MP quad camera, 5x telephoto,
    Galaxy AI, QHD+ 120Hz LTPO). Kept its facts and made them specific: 3120 × 1440, 2,600 nits, Gorilla Armor,
    50MP 5x lens, 12GB RAM, Wi-Fi 7, 232g, seven years of updates.
  - "Lighter titanium body" was OVERSTATED: 232g against the S23 Ultra's 234g, so 2g lighter. Now says so.
  - "Difference vs S23 Ultra" kept and expanded in the FAQ: the 10x lens was replaced by the 50MP 5x (sharper
    5x–10x, but no longer true 10x optical), Galaxy AI later came to the S23 too, seven vs four years of updates.
  - Colours: Samsung UK spells it "Titanium Grey" (the old copy had the US "Gray"). Four shop colours plus three
    Samsung online exclusives (Blue, Green, Orange) listed; trim to what you stock.
  - "Catchy line:" label dropped; the line itself is the tagline. "Screen Size", "Special Features" in sentence case.
  - Added what the old copy left out: no charger in the box, weight, cloud/paid AI caveat, update policy, a
    Galaxy AI FAQ, full spec list.
  - "choosen" spelling fixed; "click here" given descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by UK carriers and reviews (232g, 2,600 nits, 50MP 5x, seven upgrades, QHD+, £1,249 launch). 3120 ×
  1440, Gorilla Armor and Wi-Fi 7 are Samsung's launch figures. Software line assumes One UI 8 / Android 16 in
  Nov 2026: check against a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question as the S23 Ultra.
  2. Colours: trim the seven listed to what you stock.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov); Black Friday short description template (6 Nov).
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra S Pen Snapdragon Gen Dynamic AMOLED QHD+ LTPO Nightography Expert RAW Space Zoom Super Steady Instant Slow-mo Gorilla Armor Always-On Adaptive Pixel One UI Android Galaxy AI Circle Search Live Translate Interpreter Note Assist Chat Generative Edit Bluetooth Air Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S23 S24 S25 S22 S21 QHD W SIM Corning".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

# Standard short description (for after the sale)
t = open(T + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {FULL}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>", f"<strong>{TAGLINE}</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have a {FULL}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

# Black Friday short description (approved template, Galaxy S23 Ultra values replaced)
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S24 Ultra",
             "Samsung Galaxy S24 Ultra with a titanium frame, 6.8-inch QHD+ 120Hz Dynamic AMOLED 2X display with Gorilla "
             "Armor glass, Snapdragon 8 Gen 3 for Galaxy chip, Galaxy AI, 200MP main camera with 3x and 50MP 5x "
             "telephoto lenses, built-in S Pen, 5,000mAh battery with 45W charging, 5G and seven years of updates. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Titanium Grey", "Titanium Black", "Titanium Violet", "Titanium Yellow", "Titanium Blue", "Titanium Green", "Titanium Orange"]
images = [(f"Main image: {c}", f"Samsung Galaxy S24 Ultra in {c}, front and back view",
           f"The Galaxy S24 Ultra in {c}, with a flat 6.8-inch QHD+ display, titanium frame, quad camera and built-in S Pen.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S24 Ultra quad camera: 200MP main, Ultra Wide, 3x and 50MP 5x telephoto",
     "The Galaxy S24 Ultra quad camera, with a 200MP main sensor, 12MP Ultra Wide, 10MP 3x and 50MP 5x telephoto lenses."),
    ("S Pen", "Samsung Galaxy S24 Ultra with the S Pen pulled out from its slot",
     "The built-in S Pen of the Galaxy S24 Ultra, for notes, sketches and remote camera control."),
    ("Galaxy AI", "Samsung Galaxy S24 Ultra showing Circle to Search on screen",
     "Galaxy AI on the Galaxy S24 Ultra: Circle to Search, Live Translate, Note Assist and Generative Edit."),
    ("Screen on, front", "Samsung Galaxy S24 Ultra flat 6.8-inch Dynamic AMOLED 2X display switched on",
     "The flat 6.8-inch QHD+ 120Hz screen of the Galaxy S24 Ultra, up to 2,600 nits with anti-reflective Gorilla Armor glass."),
    ("In the box", "Samsung Galaxy S24 Ultra with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S24 Ultra with the S Pen built in and a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S24 Ultra in titanium with quad camera and S Pen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "BLACK FRIDAY DEAL: paste <code>" + SLUG + "-short-description-black-friday.html</code> into the short description during the sale, and the normal short description afterwards.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Seven colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says Android 16 / One UI 8. Check against a handset before publishing.",
], tags=TAGS)
print("built")

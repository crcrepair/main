"""Samsung Galaxy S23 Ultra — long + short description, schema, SEO pack and tags, from the approved template.
First Samsung product: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update policy, "a" not "an"."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s23-ultra"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "Galaxy S23 Ultra"
FULL = "Samsung Galaxy S23 Ultra"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s23-ultra/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S23-Ultra"   # ❓ first Samsung: confirm the exact value in the booking system
TAGLINE = "The ultimate Galaxy with 200MP pro-grade camera."

META_TITLE = "Buy Samsung Galaxy S23 Ultra | 200MP, S Pen | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S23 Ultra with a 200MP camera, 10x optical zoom, built-in S Pen and 6.8-inch 120Hz "
             "screen. 60-point checked, 2-year warranty and MOT.")
OG_TITLE = "Galaxy S23 Ultra: 200MP camera, 10x zoom, S Pen, 2-year warranty"
OG_DESC = "Samsung's flagship: 200MP camera, 10x optical zoom, built-in S Pen and a 6.8-inch 120Hz screen. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S23 Ultra with a 2-year warranty | CrC Repair®"
X_DESC = "200MP camera, 10x optical zoom, built-in S Pen and a 6.8-inch 120Hz screen. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S23 series", "Model family. Links the Galaxy S23, S23+ and S23 Ultra listings."),
    ("Galaxy S23 Ultra", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s23u-box", "What comes with the Galaxy S23 Ultra?",
     "The phone comes with a charging cable as standard, and the S Pen is built into the phone. For a plug, screen "
     "protector, case or wireless charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount "
     "on selected accessories is applied automatically in the basket."),
    ("faq-s23u-vs-s22u", "What's the difference between the Galaxy S23 Ultra and S22 Ultra?",
     "The S23 Ultra has a 200MP main camera in place of 108MP, the faster and more efficient Snapdragon 8 Gen 2 for "
     "Galaxy chip in every region (the UK S22 Ultra used Samsung's Exynos chip), tougher Gorilla Glass Victus 2, "
     "flatter screen edges and noticeably longer battery life from the same 5,000mAh cell. The screen, S Pen, zoom "
     "lenses and design are otherwise much the same."),
    ("faq-s23u-updates", "Is the Galaxy S23 Ultra still supported by Samsung?",
     "Yes. Samsung promised four Android upgrades and five years of security updates from its 2023 launch, so it runs "
     "Android 16 with One UI 8, has Android 17 to come as its last major upgrade, and gets security updates into "
     "2028. Galaxy AI features such as Circle to Search and Live Translate were added in 2024."),
    ("faq-s23u-spen", "Does the S Pen come with the phone?",
     "Yes. The S Pen slots into the bottom of the phone, so it's always with you. Pull it out to take notes on the "
     "lock screen, annotate screenshots, sign documents or use it as a remote shutter for the camera."),
    ("faq-s23u-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-s23u-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s23u-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB with 8GB RAM · 512GB or 1TB with 12GB RAM"),
    ("Colours", "Phantom Black, Cream, Green and Lavender · Graphite, Lime, Sky Blue and Red (Samsung online exclusives)"),
    ("Display", "6.8-inch Dynamic AMOLED 2X · QHD+ 3088 × 1440 · 500 ppi"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 1,750 nits peak"),
    ("Chip", "Snapdragon 8 Gen 2 for Galaxy · octa-core"),
    ("Main camera", "200MP · ƒ/1.7 · optical image stabilisation · Adaptive Pixel"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120°"),
    ("Telephoto cameras", "10MP 3x optical (ƒ/2.4) · 10MP 10x optical periscope (ƒ/4.9) · both stabilised"),
    ("Zoom range", "0.6x to 10x optical · Space Zoom up to 100x"),
    ("Photography", "Nightography · Expert RAW · Astrophoto · 50MP and 200MP modes"),
    ("Video", "8K at 30fps · 4K at 60fps · Super Steady · Pro video"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("S Pen", "Built in · Bluetooth remote · Air actions"),
    ("Build", "Armor Aluminum frame · Gorilla Glass Victus 2 front and back · 234g"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "5,000mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 6E · Bluetooth 5.3 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Android 16 with One UI 8 · four Android upgrades and security updates to 2028 promised"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — 200MP camera, 10x zoom and the built-in S Pen", [
        f"The <strong>{FULL}</strong> is the flagship of the S23 range and the first Galaxy with a "
        "<strong>200MP main camera</strong>. Alongside it sit a 12MP Ultra Wide and two telephoto lenses, a 3x and a "
        "10x periscope, so you can shoot everything from wide landscapes to distant detail at optical quality, with "
        "Nightography for low light and 8K video.",
        "The 6.8-inch QHD+ Dynamic AMOLED 2X screen runs at an adaptive 1–120Hz and reaches 1,750 nits, the "
        "<strong>Snapdragon 8 Gen 2 for Galaxy</strong> chip handles anything, and the <strong>S Pen</strong> is built "
        "into the phone for notes, sketches and signatures. A 5,000mAh battery with 45W charging, Gorilla Glass Victus 2 "
        "and IP68 water resistance complete a phone built for creators, gamers and heavy users.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Big and heavy.</strong> At 234g and 163.4mm tall it's one of the largest phones you can buy. The S Pen "
        "is part of the reason, so if you don't need a stylus, the Galaxy S23+ is lighter with the same chip.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter; wireless charging is 15W.",
        "<strong>Galaxy AI arrived later.</strong> The S23 Ultra gained Galaxy AI features with One UI 6.1 in 2024, "
        "but some newer AI features are limited to the S24 series and later. Android 17 will be its last major "
        "upgrade.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s23u-200mp", "200MP main camera",
         "The Adaptive Pixel sensor combines pixels for bright, detailed 12MP shots by default, or captures at 50MP or "
         "the full 200MP when you want to crop in. Nightography pulls detail out of low light."),
        ("feat-s23u-zoom", "3x and 10x optical zoom",
         "Two telephoto lenses give true optical zoom at 3x and 10x, the periscope lens reaching 230mm-equivalent. "
         "Space Zoom goes to 100x, and both lenses are optically stabilised for sharper handheld shots."),
        ("feat-s23u-spen", "Built-in S Pen",
         "The stylus slots into the phone, so it's always to hand for notes, sketches, annotating screenshots and "
         "signing documents, and it works as a Bluetooth remote for the camera."),
        ("feat-s23u-display", "6.8-inch QHD+ 120Hz display",
         "A Dynamic AMOLED 2X panel with 1,750 nits peak brightness for sunlight, an adaptive 1–120Hz refresh rate to "
         "save power, and flatter edges than the S22 Ultra for easier S Pen use."),
        ("feat-s23u-chip", "Snapdragon 8 Gen 2 for Galaxy",
         "A chip tuned for Samsung with higher clock speeds than the standard version, for smooth gaming, 8K video "
         "and all-day efficiency. Samsung DeX turns the phone into a desktop with a monitor."),
        ("feat-s23u-battery", "5,000mAh battery, 45W charging",
         "Comfortably lasts a full day of heavy use, with 45W wired charging to around 65% in 30 minutes, 15W wireless "
         "charging and reverse wireless charging for earbuds or a watch."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the most capable Android phone of its year: the best zoom camera, a "
        "built-in stylus, a huge bright screen and a battery that lasts, at a pre-owned price well below the S24 and "
        "S25 Ultra. Coming from an S21 Ultra, S20 Ultra or a Note, you'll notice the 200MP camera, the brighter screen "
        "and the longer battery.",
        "If you don't need the S Pen or the 10x zoom, the Galaxy S23+ has the same chip in a lighter phone. If you "
        "want titanium, a 5x telephoto and the newest Galaxy AI features, look at the Galaxy S24 Ultra or S25 Ultra. "
        "Not sure which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s23u-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s23u-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s23u-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s23u-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s23u-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s23u-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s23u-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port, camera and S Pen faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s23u-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S23 Ultra
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

FIRST SAMSUNG PRODUCT. Differences from the iPhone pages, per the template guide:
  - Parts wording: genuine Samsung parts only (no "premium or Genuine Apple part" choice).
  - Repair pillar link: /samsung-repair/ in place of /iphone-repair/.
  - Software: Samsung's update policy (four Android upgrades, five years of security) in place of iOS 27.
  - "a Galaxy" not "an iPhone" in the headings, FAQ and short description.
  - Everything else (layout, CSS, icons, sections, store capsules, warranty rules) is identical.

CHANGES FROM THE OLD DESCRIPTION (checked against Samsung's published specs):
  - The old copy was correct (200MP, 10x periscope, Snapdragon 8 Gen 2 for Galaxy, Victus 2, S Pen, 6.8-inch QHD+
    120Hz LTPO). Kept its facts and made them specific: 3088 × 1440, 1,750 nits, 3x and 10x lenses, 5,000mAh, 45W,
    234g, IP68 to 1.5 m.
  - "What's New vs S22 Ultra" was correct and is kept in the FAQ, with the UK-specific point that the S22 Ultra
    used Exynos here, so the Snapdragon chip was a bigger upgrade for UK buyers than the old copy implied.
  - Colours: old copy listed six. Samsung sold four in shops and four online exclusives (adding Sky Blue and Red).
    All eight listed, marked; trim to the colours you actually stock.
  - "Storage Options", "Key Features", "What's New" written in sentence case; "Storage" label kept.
  - "Armor Aluminum" kept with Samsung's spelling, as it's their trade name.
  - Added what the old copy left out: no charger in the box, weight warning, Galaxy AI position, update policy,
    RAM by storage size, full spec list, S Pen FAQ.
  - "choosen" spelling fixed; "click here" given descriptive anchor text.

SOURCES: samsung.com was not fetched (session network). Figures were checked against Samsung's spec sheet as
  reported by UK retailers and reviews (6.8-inch 3088 × 1440 at 1–120Hz, 1,750 nits, 5,000mAh, IP68, four OS
  upgrades to One UI 8). 234g, 45W and Victus 2 are Samsung's launch figures. Software line assumes One UI 8 /
  Android 16 is current for the S23 Ultra in Nov 2026, with Android 17 still to come: please check against
  a handset before publishing.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. First Samsung product: what does the booking system
     use for Samsung models (Galaxy-S23-Ultra, Samsung-Galaxy-S23-Ultra, S23-Ultra)?
  2. Colours: trim the eight listed to what you stock.
  3. Software line: confirm which One UI version your handsets are on.

CONFIRMED BY GABOR (3 Nov 2026): condition tag "Pre-owned". Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra S Pen Snapdragon Gen Dynamic AMOLED QHD+ LTPO Nightography Expert RAW Astrophoto Space Zoom Super Steady Pro Armor Aluminum Gorilla Glass Victus Always-On Adaptive Pixel One UI Android Galaxy AI Circle Search Live Translate DeX Bluetooth Air Exynos Note Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband RAW 5G G Hz 8K 4K Note S23 S22 S24 S25 S21 S20 QHD W SIM".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "") + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {FULL}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>", f"<strong>{TAGLINE}</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have a {FULL}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S23 Ultra",
             "Samsung Galaxy S23 Ultra with a 6.8-inch QHD+ 120Hz Dynamic AMOLED 2X display, Snapdragon 8 Gen 2 for Galaxy "
             "chip, 200MP main camera with 3x and 10x optical telephoto lenses, built-in S Pen, 5,000mAh battery with 45W "
             "charging and 5G. 60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT "
             "every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Phantom Black", "Cream", "Green", "Lavender", "Graphite", "Lime", "Sky Blue", "Red"]
images = [(f"Main image: {c}", f"Samsung Galaxy S23 Ultra in {c}, front and back view",
           f"The Galaxy S23 Ultra in {c}, with a 6.8-inch QHD+ display, quad camera and built-in S Pen.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S23 Ultra quad camera: 200MP main, Ultra Wide, 3x and 10x telephoto",
     "The Galaxy S23 Ultra quad camera, with a 200MP main sensor, 12MP Ultra Wide and 3x and 10x optical telephoto lenses."),
    ("S Pen", "Samsung Galaxy S23 Ultra with the S Pen pulled out from its slot",
     "The built-in S Pen of the Galaxy S23 Ultra, for notes, sketches and remote camera control."),
    ("Screen on, front", "Samsung Galaxy S23 Ultra 6.8-inch Dynamic AMOLED 2X display switched on",
     "The 6.8-inch QHD+ 120Hz screen of the Galaxy S23 Ultra, up to 1,750 nits for sunlight."),
    ("In the box", "Samsung Galaxy S23 Ultra with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S23 Ultra with the S Pen built in and a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S23 Ultra with quad camera and S Pen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Eight colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product. Samsung set: Samsung · Galaxy · Galaxy S23 series · Galaxy S23 Ultra · Pre-owned · 5G.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. First Samsung product: please confirm the value your booking system uses for Samsung models.",
    "Software line says Android 16 / One UI 8 with Android 17 to come. Check against a handset before publishing.",
], tags=TAGS)
print("built")

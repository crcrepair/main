"""Samsung Galaxy S26 — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's basic spec sheet plus verified sources; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s26"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S26"
FULL = "Samsung Galaxy S26"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s26/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S26"   # ❓ Samsung pattern still to confirm
TAGLINE = "The compact Galaxy, sharper in every way."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S26 | Compact, Galaxy AI | CrC Repair®"
META_DESC = ("Buy a compact Samsung Galaxy S26 with a 6.3-inch 120Hz screen, Exynos 2600, Galaxy AI and "
             "a 50MP triple camera. 60-point checked, 2-year warranty and MOT.")
OG_TITLE = "Galaxy S26: the compact 2026 Galaxy with Galaxy AI, 2-year cover"
OG_DESC = "The compact Galaxy S26: 6.3-inch 120Hz screen, Galaxy AI, 50MP triple camera and 4,300mAh battery at 167g. 2-year cover."
X_TITLE = "Samsung Galaxy S26 with a 2-year warranty | CrC Repair®"
X_DESC = "6.3-inch 120Hz screen, Galaxy AI, 50MP triple camera and 4,300mAh battery at 167g. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S26 series", "Model family. Links the Galaxy S26, S26+ and S26 Ultra listings."),
    ("Galaxy S26", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s26-box", "What comes with the Galaxy S26?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s26-vs-s25", "What's the difference between the Galaxy S26 and S25?",
     "The S26 has a slightly larger 6.3-inch screen with slimmer bezels, anti-reflective Gorilla Armor 2 glass, a "
     "bigger 4,300mAh battery against 4,000mAh, Samsung's new Exynos 2600 chip in the UK in place of the S25's "
     "Snapdragon, the new mobile DNIe engine for colour accuracy, a redesigned translucent camera island and newer "
     "Galaxy AI features such as Now Nudge. The cameras and 25W charging are the same."),
    ("faq-s26-chip", "Does the UK Galaxy S26 have a Snapdragon chip?",
     "No. In the UK and Europe the S26 and S26+ use Samsung's own Exynos 2600, a 10-core chip built on a 2nm process; "
     "only the S26 Ultra has the Snapdragon 8 Elite Gen 5 for Galaxy here. The Exynos 2600 is a fast flagship chip "
     "that runs Galaxy AI on the phone, and it's what Samsung sells through every UK network."),
    ("faq-s26-vs-plus", "Should I choose the Galaxy S26 or the S26+?",
     "They share the same chip, cameras, Galaxy AI and seven years of updates. The S26+ has a larger 6.7-inch QHD+ "
     "screen, a bigger battery and faster charging. The S26 is the one to pick if you want a phone that's easy to use "
     "one-handed: 6.3 inches and 167g, and it's cheaper."),
    ("faq-s26-updates", "Is the Galaxy S26 still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2026 launch, so it launched "
     "on Android 16 with One UI 8.5, has since moved to Android 17 with One UI 9, and will keep getting new versions "
     "and security updates until 2033."),
    ("faq-s26-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s26-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "128GB · 256GB · 512GB · 12GB RAM"),
    ("Colours", "Black, White, Sky Blue and Cobalt Violet · Silver Shadow and Pink Gold (Samsung online exclusives)"),
    ("Display", "6.3-inch Dynamic AMOLED 2X · FHD+ · flat · mobile DNIe colour engine"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Armor 2, anti-reflective (front)"),
    ("Chip", "Samsung Exynos 2600 (UK and Europe) · 2nm · 10-core CPU"),
    ("Main camera", "50MP · optical image stabilisation"),
    ("Ultra Wide camera", "12MP · 120°"),
    ("Telephoto camera", "10MP · 3x optical zoom · stabilised"),
    ("Zoom range", "0.6x to 3x optical · Space Zoom up to 30x"),
    ("Photography", "ProVisual Engine · Nightography · Expert RAW · Photo Assist · Generative Edit"),
    ("Video", "8K at 30fps · 4K at 60fps · 10-bit HDR · Log video · Audio Eraser"),
    ("Front camera", "12MP · autofocus"),
    ("Build", "Armor Aluminum frame · 149.6 × 71.7 × 7.2mm · 167g · translucent camera island"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,300mAh"),
    ("Charging", "USB-C 3.2 · 25W wired fast charging (adapter sold separately) · wireless charging · reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.4 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Security", "Ultrasonic in-display fingerprint reader · face recognition · Knox Matrix"),
    ("Software", "Launched on Android 16 with One UI 8.5, now Android 17 with One UI 9 · seven years of updates (to 2033)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the compact 2026 Galaxy", [
        f"The <strong>{FULL}</strong> is the small one of the 2026 range: a 6.3-inch 120Hz screen in a body that's "
        "7.2mm thin and 167g, so it's easy to use one-handed. The screen sits behind anti-reflective <strong>Gorilla "
        "Armor 2</strong> glass and reaches 2,600 nits, with Samsung's new mobile DNIe engine for more accurate colour, "
        "and the redesigned translucent camera island gives the whole S26 range one look.",
        "Inside is Samsung's <strong>Exynos 2600</strong>, a 2nm flagship chip with 12GB of RAM, a bigger 4,300mAh "
        "battery than the S25's, and a 50MP triple camera with a 3x telephoto. <strong>Galaxy AI</strong> adds Now "
        "Nudge, Photo Assist and Circle to Search, and Samsung promises <strong>seven years of updates</strong>.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Exynos chip in the UK.</strong> UK and European S26 phones use Samsung's Exynos 2600, not the "
        "Snapdragon 8 Elite Gen 5 sold in the US. It's a fast 2nm flagship chip and runs Galaxy AI on the phone; only "
        "the S26 Ultra has the Snapdragon in the UK.",
        "<strong>25W charging, no charger in the box.</strong> The 4,300mAh battery is bigger than the S25's, but wired "
        "charging stays at 25W rather than the S26+'s faster rate. It comes with a USB-C cable; no adapter.",
        "<strong>No Privacy Display.</strong> The S26 Ultra's built-in Privacy Display, 200MP camera and S Pen aren't "
        "on the S26. Some Galaxy AI features use the cloud and need a Samsung account.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s26-size", "Compact and light",
         "At 6.3 inches, 7.2mm and 167g it's one of the few small flagships, comfortable one-handed and light in a "
         "pocket, with an Armor Aluminum frame and IP68 water resistance."),
        ("feat-s26-display", "6.3-inch display with Gorilla Armor 2",
         "Anti-reflective glass that cuts glare, 2,600 nits peak brightness, an adaptive 1–120Hz refresh rate and "
         "Samsung's mobile DNIe engine for more accurate colour."),
        ("feat-s26-chip", "Exynos 2600 and 12GB of RAM",
         "Samsung's 2nm flagship chip with a 10-core CPU, a big step up from the S25's chip in graphics and AI "
         "efficiency, with 12GB of RAM for on-device Galaxy AI and multitasking."),
        ("feat-s26-ai", "Galaxy AI",
         "Photo Assist edits pictures from a typed description, Now Nudge suggests shortcuts from what's on screen, "
         "and Circle to Search, Live Translate and Now Brief carry over from the S25."),
        ("feat-s26-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low light and the ProVisual Engine for colour and detail."),
        ("feat-s26-battery", "Bigger battery, seven years of updates",
         "A 4,300mAh battery, up from 4,000mAh in the S25, with 25W wired and wireless charging, on a phone Samsung "
         "will keep updating until 2033."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a genuinely compact phone with the newest Galaxy AI, a proper telephoto "
        "camera and the longest update support, at the lowest price of the S26 range. Coming from an S22, S23 or S24, "
        "you'll notice the brighter anti-reflective screen, the bigger battery and the AI features.",
        "If battery life matters most, the Galaxy S26+ has a bigger battery, faster charging and a larger, sharper "
        "screen. For the Privacy Display, the 200MP camera or the S Pen, look at the S26 Ultra. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s26-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s26-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s26-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s26-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s26-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s26-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s26-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s26-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S26
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

SOURCE: no old marketing copy, only Gabor's basic spec sheet (6.3-inch, 12GB, 10-core 3.8/3.26/2.76GHz chip = Exynos
  2600, 50MP + 10MP + 12MP, 12MP front, Android 16, Wi-Fi 7, Bluetooth 5.4, USB 3.2, colours Black / Pink Gold /
  Silver Shadow / Cobalt Violet / Sky Blue / White, 128/256/512GB, Galaxy AI photo editing, Now Nudge, Circle to
  Search, Bixby, Knox Matrix, mobile DNIe engine, translucent camera island). All used as given; "Sivler" corrected
  to Silver. The rest comes from UK reviews and launch coverage: Exynos 2600 in the UK, 2,600 nits LTPO, Gorilla
  Armor 2, 4,300mAh (up from 4,000), 25W wired, 167g, 149.6 × 71.7 × 7.2mm, IP68, announced 25 Feb 2026, UK price
  £879 (256GB) / £1,049 (512GB), One UI 8.5 on Android 16 at launch, seven years of updates. samsung.com and review
  sites could not be fetched directly from this session (network); search results only.

NOTES:
  - 128GB: the sheet lists it, but UK reviews say Samsung dropped the 128GB model in the UK (256GB is the base).
    Listed as on the sheet; ❓ trim if you don't stock it.
  - Chip ❓: Exynos 2600 for UK/European stock. If any units are US imports with the Snapdragon, tell me.
  - Wireless charging wattage and exact screen resolution not confirmed; stated without figures.
  - Software: launched on One UI 8.5 / Android 16; One UI 9 / Android 17 has since rolled out to the S26 range.
    The page says both. ❓ Check a handset.

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  2. 128GB, chip and software (above). Colours: trim the six listed to what you stock. Tagline (above).

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (12 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra S Pen Snapdragon Elite Gen Exynos Dynamic AMOLED FHD+ QHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Audio Eraser Log HDR Gorilla Armor Always-On One UI Android Galaxy AI Circle Search Live Translate Now Brief Nudge Photo Assist Generative Edit Privacy Display Knox Matrix Bixby DNIe Armor Aluminum Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi 5G G Hz 8K 4K S22 S23 S24 S25 S26 W SIM Corning UK Europe US Wide GB".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S26",
             "Samsung Galaxy S26 with a 6.3-inch 120Hz Dynamic AMOLED 2X display with Gorilla Armor 2 glass, Exynos 2600 "
             "chip, 12GB RAM, Galaxy AI, 50MP triple camera with 3x telephoto, 4,300mAh battery, 5G and seven years of "
             "updates, at 167g. 60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT "
             "every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Sky Blue", "Cobalt Violet", "Silver Shadow", "Pink Gold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S26 in {c}, front and back view",
           f"The Galaxy S26 in {c}, with a flat 6.3-inch display, translucent camera island and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S26 triple camera in its translucent island: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S26 triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("In the hand", "Samsung Galaxy S26 held in one hand, showing its compact size",
     "The Galaxy S26 in the hand: a 6.3-inch screen in a 167g phone that's easy to use one-handed."),
    ("Galaxy AI", "Samsung Galaxy S26 showing Photo Assist editing a photo from a typed prompt",
     "Galaxy AI on the Galaxy S26: Photo Assist, Now Nudge, Circle to Search and Live Translate."),
    ("Screen on, front", "Samsung Galaxy S26 6.3-inch Dynamic AMOLED 2X display switched on",
     "The 6.3-inch 120Hz screen of the Galaxy S26, up to 2,600 nits behind anti-reflective Gorilla Armor 2 glass."),
    ("In the box", "Samsung Galaxy S26 with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S26 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S26 compact phone with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and UK launch coverage. The tagline is new: please approve or replace.",
    "Chip: the page says Exynos 2600, correct for UK/European stock. If any units are US imports with the Snapdragon, say so.",
    "128GB is listed as on the sheet, but UK reviews say the 128GB model wasn't sold in the UK. Trim if you don't stock it.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Six colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says launched on One UI 8.5, now One UI 9. Check against a handset before publishing.",
], tags=TAGS)
print("built")

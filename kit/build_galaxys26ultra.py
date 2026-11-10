"""Samsung Galaxy S26 Ultra — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's basic spec sheet plus verified sources; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s26-ultra"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S26 Ultra"
FULL = "Samsung Galaxy S26 Ultra"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s26-ultra/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S26-Ultra"   # ❓ Samsung pattern still to confirm
TAGLINE = "The Ultra with a Privacy Display and 60W charging."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S26 Ultra | 200MP, S Pen | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy S26 Ultra with the Privacy Display, Snapdragon 8 Elite Gen 5, 200MP c"
             "amera, 60W charging and S Pen. 60-point checked, 2-year warranty.")
OG_TITLE = "Galaxy S26 Ultra: Privacy Display, 200MP camera, 2-year warranty"
OG_DESC = "Samsung's 2026 flagship: Privacy Display, 200MP camera, 60W charging and built-in S Pen. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy S26 Ultra with a 2-year warranty | CrC Repair®"
X_DESC = "Privacy Display, Snapdragon 8 Elite Gen 5, 200MP camera, 60W charging and built-in S Pen. 60-point checked, free Device MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S26 series", "Model family. Links the Galaxy S26, S26+ and S26 Ultra listings."),
    ("Galaxy S26 Ultra", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s26u-box", "What comes with the Galaxy S26 Ultra?",
     "The phone comes with a charging cable as standard, and the S Pen is built into the phone. For a plug, screen "
     "protector, case or wireless charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount "
     "on selected accessories is applied automatically in the basket."),
    ("faq-s26u-privacy", "What is the Privacy Display?",
     "A setting that narrows the screen's viewing angle, so the person next to you on the train or in a meeting "
     "sees a dark screen while you see it normally. It's built into the panel rather than a stick-on filter, you "
     "switch it on and off as you like, and you can limit it to certain apps. With it on, the screen is a little "
     "dimmer and less colour-accurate, which is why it's optional."),
    ("faq-s26u-vs-s25u", "What's the difference between the Galaxy S26 Ultra and S25 Ultra?",
     "The S26 Ultra adds the Privacy Display, a brighter main camera lens at ƒ/1.4, faster 60W wired and 25W Qi2 "
     "wireless charging, the newer Snapdragon 8 Elite Gen 5 for Galaxy chip and Gorilla Armor 2 glass. The camera "
     "island is now flush with the back, the phone is slightly thinner and lighter at 7.9mm and 214g, and Galaxy AI "
     "gains Photo Assist, Creative Studio and Now Nudge. The screen size, 200MP sensor, zoom lenses, 5,000mAh "
     "battery and S Pen are otherwise much the same."),
    ("faq-s26u-spen", "Does the S Pen come with the phone, and does it have Bluetooth?",
     "Yes, it's built in and slots into the phone for notes, sketches, annotating and signing. Like the S25 Ultra, "
     "it has no Bluetooth, so the Air actions gestures and remote camera shutter from older Ultras aren't available."),
    ("faq-s26u-updates", "Is the Galaxy S26 Ultra still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2026 launch, so it launched "
     "on Android 16 with One UI 8.5, has since moved to Android 17 with One UI 9, and will keep getting new versions "
     "and security updates until 2033."),
    ("faq-s26u-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s26u-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 1TB · 12GB RAM"),
    ("Colours", "Black, White, Sky Blue and Cobalt Violet · Silver Shadow and Pink Gold (Samsung online exclusives)"),
    ("Display", "6.9-inch Dynamic AMOLED 2X · QHD+ 3120 × 1440 · flat · Privacy Display built in"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Armor 2, anti-reflective (front)"),
    ("Chip", "Snapdragon 8 Elite Gen 5 for Galaxy · octa-core"),
    ("Main camera", "200MP · ƒ/1.4 · optical image stabilisation"),
    ("Ultra Wide camera", "50MP · ƒ/1.9 · macro"),
    ("Telephoto cameras", "10MP 3x optical (ƒ/2.4) · 50MP 5x optical (ƒ/2.9) · both stabilised"),
    ("Zoom range", "3x and 5x optical · optical-quality 2x and 10x · Space Zoom up to 100x"),
    ("Photography", "Photo Assist · ProVisual Engine · Nightography · Expert RAW · Generative Edit"),
    ("Video", "8K at 30fps · 4K at 120fps · 10-bit HDR · Log video · Audio Eraser"),
    ("Front camera", "12MP · ƒ/2.2 · autofocus"),
    ("S Pen", "Built in · no Bluetooth (no Air actions or remote shutter)"),
    ("Build", "Rounded corners · flush camera island · 214g · 7.9mm thin · 163.6 × 78.1mm"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "5,000mAh · up to 31 hours of video playback"),
    ("Charging", "USB-C 3.2 · 60W wired fast charging (adapter sold separately) · 25W Qi2 wireless · reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 6.0 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Ultrasonic in-display fingerprint reader · face recognition"),
    ("Software", "Launched on Android 16 with One UI 8.5, now Android 17 with One UI 9 · seven years of updates (to 2033)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — Privacy Display, 200MP camera and 60W charging", [
        f"The <strong>{FULL}</strong> is Samsung's 2026 flagship, and its headline is new: a <strong>Privacy "
        "Display</strong> built into the 6.9-inch QHD+ screen, which hides what you're reading from anyone looking "
        "from the side. The <strong>Snapdragon 8 Elite Gen 5 for Galaxy</strong> chip and 12GB of RAM drive it, "
        "behind anti-reflective Gorilla Armor 2 glass, in a slimmer 7.9mm body with a flush camera island.",
        "The quad camera keeps the 200MP main sensor with a brighter ƒ/1.4 lens, a 50MP Ultra Wide and 3x and 5x "
        "telephotos. Charging finally gets faster: <strong>60W wired</strong> and 25W Qi2 wireless. Galaxy AI adds "
        "Photo Assist, Creative Studio and Now Nudge, the <strong>S Pen</strong> is still built in, and Samsung "
        "promises seven years of updates.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Privacy Display is optional, and has a cost.</strong> With it on, the screen is dimmer and colours "
        "are slightly muted. Most people leave it off and switch it on for banking, email or on the train.",
        "<strong>No charger, and Qi2 needs a case for magnets.</strong> It comes with a USB-C cable; 60W charging "
        "needs a 60W USB-C PD adapter. Qi2 wireless charging is 25W, but the magnets aren't in the phone, so a Qi2 "
        "case is needed for magnetic chargers to snap on.",
        "<strong>The S Pen has no Bluetooth.</strong> It writes and sketches as before, but the Air actions gestures "
        "and remote camera shutter from the S24 Ultra and earlier are gone, as on the S25 Ultra.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s26u-privacy", "Privacy Display",
         "A viewing-angle control built into the panel: switch it on and people beside you see a dark screen while "
         "you see it normally. Set it per app for banking, messages or work email."),
        ("feat-s26u-camera", "200MP camera with a brighter lens",
         "The main camera's new ƒ/1.4 aperture lets in more light for sharper night shots, alongside a 50MP Ultra "
         "Wide and 3x and 5x telephotos for optical-quality zoom from 2x to 10x."),
        ("feat-s26u-charging", "60W wired, 25W Qi2 wireless",
         "The fastest charging on a Galaxy S yet, up from 45W, with 25W Qi2 wireless charging and reverse wireless "
         "charging for earbuds or a watch, on a 5,000mAh battery rated for up to 31 hours of video."),
        ("feat-s26u-chip", "Snapdragon 8 Elite Gen 5 for Galaxy",
         "Qualcomm's latest flagship chip, tuned for Samsung and used in every region, with faster graphics and more "
         "efficient on-device AI than the S25 Ultra."),
        ("feat-s26u-ai", "Galaxy AI: Photo Assist, Creative Studio, Now Nudge",
         "Edit photos by describing the change, turn photos or sketches into sticker sets, and get shortcuts suggested "
         "from what's on screen, alongside Circle to Search, Live Translate and Now Brief."),
        ("feat-s26u-design", "Slimmer, with a flush camera",
         "At 7.9mm and 214g it's thinner and lighter than the S25 Ultra, with rounded corners, a camera island that "
         "sits flush with the back, Gorilla Armor 2 glass and IP68 water resistance."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want Samsung's newest flagship with the best camera, the built-in S Pen, the "
        "fastest charging and the longest update support, at a pre-owned price below new. Coming from an S23 Ultra or "
        "S24 Ultra, you'll notice the Privacy Display, the brighter main camera, 60W charging and the slimmer body.",
        "If you have an S25 Ultra, the screen, battery, zoom lenses and S Pen are much the same, so the upgrade is "
        "the Privacy Display, the ƒ/1.4 lens, faster charging and the chip. If you don't need a stylus, the Galaxy "
        "S26+ is lighter with the same Galaxy AI. Not sure which suits you? Ask in any of our stores and we'll talk "
        "you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s26u-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s26u-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s26u-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s26u-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s26u-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s26u-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s26u-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port, camera and S Pen faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s26u-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy S26 Ultra
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

SOURCE: no old marketing copy this time, only Gabor's basic spec sheet (6.9-inch, 12GB, Snapdragon 8 Elite Gen 5
  for Galaxy, 200MP ƒ/1.4 + 50MP ƒ/1.9 + 50MP ƒ/2.9 5x + 10MP ƒ/2.4 3x, 12MP front, Android 16, Wi-Fi 7, Bluetooth
  6.0, UWB, Privacy Display, Photo Assist, Creative Studio, Now Nudge, Circle to Search). All of it is used as given.
  The rest comes from Samsung UK's page as reported, GSMArena's review and launch coverage: 214g, 7.9mm, 163.6 × 78.1,
  5,000mAh, 31 h video, 60W wired, 25W Qi2 without built-in magnets, Gorilla Armor 2, 2,600 nits, 1–120Hz, IP68,
  One UI 8.5 at launch, seven years of updates, colours Black / White / Sky Blue / Cobalt Violet plus Silver Shadow
  and Pink Gold online, S Pen without Bluetooth, UK launch price £1,279 (256GB).
  samsung.com and review sites could not be fetched directly from this session (network); search results only.

THINGS LEFT OUT ON PURPOSE (sources conflict; not invented):
  - FRAME METAL. GSMArena's review says Armor Aluminum 2; other listings say titanium. The page describes the build
    without naming the metal. ❓ Check a handset or the box and tell me; one line to add.
  - Exact ppi and the resolution of the 5x lens's zoom modes.
  - Whether the 1TB model has 16GB RAM: the sheet says 12GB, so 12GB is used throughout.

SOFTWARE NOTE: launched on Android 16 / One UI 8.5; coverage says it has since moved to Android 17 / One UI 9.
  The page says both. ❓ Check a handset. (The S23/S24/S25 pages say One UI 8; some may now be on One UI 9 too.)

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. Frame metal (above).
  2. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  3. Colours: trim the six listed to what you stock.
  4. Tagline (above).

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (10 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra S Pen Snapdragon Elite Gen Dynamic AMOLED QHD+ LTPO Nightography Expert RAW Space Zoom ProVisual Engine Audio Eraser Log HDR Gorilla Armor Glass Always-On One UI Android Galaxy AI Circle Search Live Translate Now Brief Nudge Photo Assist Creative Studio Generative Edit Privacy Display Qi2 Bluetooth Air Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S23 S24 S25 S26 QHD W SIM Corning Qualcomm Wide".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S26 Ultra",
             "Samsung Galaxy S26 Ultra with a 6.9-inch QHD+ 120Hz display with built-in Privacy Display, Snapdragon 8 Elite "
             "Gen 5 for Galaxy chip, 12GB RAM, 200MP main camera with 50MP Ultra Wide and 3x and 5x telephoto lenses, "
             "built-in S Pen, 5,000mAh battery with 60W charging, 5G and seven years of updates. 60-point quality checked "
             "by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Sky Blue", "Cobalt Violet", "Silver Shadow", "Pink Gold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S26 Ultra in {c}, front and back view",
           f"The Galaxy S26 Ultra in {c}, with a flat 6.9-inch display, flush camera island and built-in S Pen.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S26 Ultra quad camera: 200MP main, 50MP Ultra Wide, 3x and 5x telephoto",
     "The Galaxy S26 Ultra quad camera, flush with the back, with a 200MP ƒ/1.4 main sensor, 50MP Ultra Wide and 3x and 5x telephotos."),
    ("Privacy Display", "Samsung Galaxy S26 Ultra viewed from the side with the Privacy Display switched on",
     "The Privacy Display on the Galaxy S26 Ultra: the screen looks dark from the side while staying clear to the user."),
    ("S Pen", "Samsung Galaxy S26 Ultra with the S Pen pulled out from its slot",
     "The built-in S Pen of the Galaxy S26 Ultra, for notes, sketches and signatures."),
    ("Screen on, front", "Samsung Galaxy S26 Ultra 6.9-inch Dynamic AMOLED 2X display switched on",
     "The 6.9-inch QHD+ 120Hz screen of the Galaxy S26 Ultra, up to 2,600 nits behind anti-reflective Gorilla Armor 2 glass."),
    ("In the box", "Samsung Galaxy S26 Ultra with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S26 Ultra with the S Pen built in and a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S26 Ultra with quad camera and S Pen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and verified sources. The tagline is new: please approve or replace.",
    "Frame metal is deliberately not stated (sources conflict between aluminium and titanium). Tell me which and I'll add it.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Six colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says launched on One UI 8.5, now One UI 9. Check against a handset before publishing.",
], tags=TAGS)
print("built")

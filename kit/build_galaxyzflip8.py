"""Samsung Galaxy Z Flip8 — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's full spec sheet plus verified launch details; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-z-flip8"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy Z Flip8"
FULL = "Samsung Galaxy Z Flip8"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/f-series/samsung-galaxy-z-flip8/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-Z-Flip8"   # ❓ Samsung pattern still to confirm
TAGLINE = "The pocket-sized flip with a 4.1-inch cover screen."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy Z Flip8 | 6.9-inch Flip | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy Z Flip8 with a 6.9-inch folding screen, 4.1-inch cover screen, 50MP c"
             "amera and 4,300mAh battery. 60-point checked, 2-year warranty.")
OG_TITLE = "Galaxy Z Flip8: 6.9-inch flip phone with a 4.1-inch cover screen"
OG_DESC = "The pocket-sized Galaxy flip: 6.9-inch folding screen, 4.1-inch cover screen and 50MP camera. Fully checked, 2-year cover."
X_TITLE = "Samsung Galaxy Z Flip8 with a 2-year warranty | CrC Repair®"
X_DESC = "6.9-inch folding screen, 4.1-inch cover screen, 50MP camera and 4,300mAh battery in a pocket-sized flip. 60-point checked."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy Z Flip series", "Model family. Links the Z Flip6, Z Flip7 and Z Flip8 listings."),
    ("Galaxy Z Flip8", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-flip8-box", "What comes with the Galaxy Z Flip8?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-flip8-cover", "What can you do on the Galaxy Z Flip8's cover screen?",
     "The 4.1-inch cover screen fills most of the front of the closed phone. Without opening it you can read and "
     "reply to messages, check notifications, control music, use widgets for weather, calendar and timers, pay with "
     "Samsung Wallet, and take selfies with the main 50MP camera using the cover screen as a viewfinder. You can also "
     "run full apps on it."),
    ("faq-flip8-vs-flip7", "What's the difference between the Galaxy Z Flip8 and Z Flip7?",
     "The Flip8 has a bigger 6.9-inch inner screen with a shallower crease, a brighter 4.1-inch cover screen, the "
     "newer Exynos 2600 chip built on a 2nm process, a larger 4,300mAh silicon-carbon battery, Bluetooth 5.4 and Wi-Fi "
     "7, and launched on Android 17 with One UI 9. The cameras and 25W charging are much the same."),
    ("faq-flip8-chip", "Does the UK Galaxy Z Flip8 have a Snapdragon chip?",
     "No. UK and European Flip8 phones use Samsung's own Exynos 2600, a 10-core chip built on a 2nm process; the "
     "Snapdragon 8 Elite Gen 5 version is sold in the US, Canada and China. The Exynos 2600 is a fast flagship chip "
     "that runs Galaxy AI on the phone, and it's what Samsung sells through every UK network."),
    ("faq-flip8-durability", "Is the Galaxy Z Flip8 waterproof?",
     "It's rated IP48: water-resistant to 1.5 metres for 30 minutes, and protected against solid objects over 1mm, "
     "but not fully dust-sealed, so keep it out of sand and pockets full of grit. The frame is Armor Aluminum and the "
     "cover screen and back are Gorilla Glass Victus 2."),
    ("faq-flip8-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-flip8-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 12GB RAM"),
    ("Colours", "Graphite, Cream and Pink · Mint (Samsung online exclusive)"),
    ("Main screen", "6.9-inch Dynamic AMOLED 2X, folding · 2520 × 1080 · 21:9 · adaptive 1Hz to 120Hz · up to 3,000 nits"),
    ("Cover screen", "4.1-inch Super AMOLED · 1048 × 948 · 120Hz · up to 3,000 nits · Gorilla Glass Victus 2"),
    ("Chip", "Samsung Exynos 2600 (UK and Europe) · 2nm · 10-core CPU"),
    ("Rear cameras", "50MP Wide (ƒ/1.8) with optical stabilisation · 12MP Ultra Wide (ƒ/2.2, 123°)"),
    ("Front camera", "10MP (ƒ/2.2) on the main screen · cover screen doubles as a viewfinder for the 50MP camera"),
    ("Video", "4K at 60fps"),
    ("Galaxy AI", "Now Brief · Now Bar on the cover screen · Circle to Search · Live Translate · Photo Assist"),
    ("Build", "Armor Aluminum frame · Gorilla Glass Victus 2 cover screen and back · 85.7 × 75.4 × 13.1mm folded · 166.9 × 75.4 × 6.1mm unfolded · 180g"),
    ("Water and dust", "IP48 (water to 1.5 metres for 30 minutes; not dust-sealed)"),
    ("Battery", "4,300mAh silicon-carbon"),
    ("Charging", "USB-C 3.2 · 25W wired, about 55% in 30 minutes (adapter sold separately) · 15W wireless · 4.5W reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.4 · NFC"),
    ("SIM", "Nano-SIM and eSIM (two active at once)"),
    ("Audio", "Stereo speakers · no headphone jack"),
    ("Biometrics", "Side fingerprint reader in the power button · face recognition"),
    ("Software", "Android 17 with One UI 9 · seven years of Android upgrades and security updates (to 2033) · Samsung DeX"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — a full-size phone that folds in half", [
        f"The <strong>{FULL}</strong> gives you a 6.9-inch 120Hz screen that folds to the size of a compact, 13mm "
        "thick and 180g, so it fits a small pocket or bag. Closed, the <strong>4.1-inch cover screen</strong> covers "
        "most of the front: read and reply to messages, check widgets, pay, and take selfies with the main camera "
        "without opening the phone.",
        "Inside is Samsung's <strong>Exynos 2600</strong>, a 2nm flagship chip with 12GB of RAM, a 4,300mAh "
        "silicon-carbon battery, a 50MP main camera with optical stabilisation and a 12MP Ultra Wide. "
        "<strong>Galaxy AI</strong> runs on the cover screen too, with Now Brief and the Now Bar, and Samsung promises "
        "seven years of updates.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>25W charging, 4,300mAh.</strong> The battery is bigger than the Flip7's but still smaller than a "
        "Galaxy S, and wired charging is 25W rather than 45W, so a full charge takes a while. Wireless charging is 15W.",
        "<strong>IP48, not IP68.</strong> It's water-resistant to 1.5 metres, but only protected against particles "
        "over 1mm, so sand and fine dust are a risk for any folding phone. Treat it with a little more care than a "
        "normal phone.",
        "<strong>Exynos chip in the UK, two cameras.</strong> UK and European Flip8s use Samsung's Exynos 2600, not "
        "the Snapdragon sold in the US. There's no telephoto camera; zoom is digital, cropped from the 50MP sensor.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-flip8-cover", "4.1-inch cover screen",
         "Almost the whole front of the closed phone is screen: messages, widgets, music, Samsung Wallet, full apps "
         "and the Now Bar, all without flipping it open, at up to 3,000 nits for sunlight."),
        ("feat-flip8-selfies", "Selfies with the main camera",
         "Close the phone and use the cover screen as a viewfinder, so selfies and vlogs come from the 50MP main camera "
         "with optical stabilisation rather than a small front camera. Flex Mode stands it half-open for hands-free shots."),
        ("feat-flip8-screen", "6.9-inch 120Hz folding screen",
         "Open, it's a full-size phone with a tall 21:9 screen, an adaptive 1–120Hz refresh rate, up to 3,000 nits "
         "and a shallower crease than earlier Flips."),
        ("feat-flip8-chip", "Exynos 2600 and 12GB of RAM",
         "Samsung's 2nm flagship chip with a 10-core CPU and 12GB of RAM, for smooth multitasking, gaming and "
         "on-device Galaxy AI, with Samsung DeX for a desktop on a monitor."),
        ("feat-flip8-battery", "Bigger silicon-carbon battery",
         "A 4,300mAh silicon-carbon cell, bigger than the Flip7's in the same slim body, with 25W wired charging to "
         "around 55% in 30 minutes, 15W wireless and reverse wireless charging for earbuds."),
        ("feat-flip8-updates", "Seven years of updates",
         "Launched on Android 17 with One UI 9, with Android upgrades and security updates promised until 2033, so a "
         "pre-owned Flip8 stays current for years."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a big-screen phone that disappears into a small pocket or bag, a cover "
        "screen that handles most quick tasks closed, and the best selfie camera of any Samsung thanks to the flip "
        "design. Coming from a Flip4, Flip5 or Flip6, you'll notice the bigger screens, the slimmer body and the "
        "battery.",
        "If you'd rather have a tablet-size screen when open, the Galaxy Z Fold8 is the one to look at. If you want "
        "the best camera and longest battery in a normal phone, the Galaxy S26 Ultra beats it on both. Not sure which "
        "suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-flip8-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-flip8-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-flip8-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-flip8-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-flip8-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-flip8-screen", "Screen repair",
         f"Cracked cover screen or a damaged folding screen? We replace {P} screens with genuine Samsung parts only, "
         "with a lifetime warranty on the screen repair."),
        ("own-flip8-repairs", "Battery, hinge and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to hinge, charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-flip8-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy Z Flip8
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

SOURCE: no old marketing copy; Gabor supplied a full spec sheet this time, used as given: 6.9-inch 2520 × 1080
  21:9 LTPO 120Hz main screen at 3,000 nits, 4.1-inch 1048 × 948 120Hz cover screen with Victus 2, Exynos 2600
  (2nm, 10-core) for the UK with the Snapdragon 8 Elite Gen 5 only in the US/Canada/China, 12GB, 256/512GB,
  50MP ƒ/1.8 OIS + 12MP ƒ/2.2 123° cameras, 10MP front, 4K60, 4,300mAh silicon-carbon, 25W (55% in 30 min),
  15W wireless, 4.5W reverse, IP48, Armor Aluminum, 180g, 166.9 × 75.4 × 6.1 / 85.7 × 75.4 × 13.1mm, Wi-Fi 7,
  Bluetooth 5.4, USB-C 3.2, side fingerprint, DeX, stereo speakers, no 3.5mm, colours Graphite / Cream / Pink / Mint.
  Launch details from UK coverage: announced 22 Jul 2026, on sale 7 Aug 2026, £1,149 (256GB), Mint online-only,
  seven years of updates. Software line (Android 17 / One UI 9) follows the Fold8, launched the same day: ❓ check
  a handset. samsung.com and review sites could not be fetched directly from this session (network).

CHIP ❓: the page says Exynos 2600, correct for UK/European stock. If any units are US imports with the Snapdragon,
  tell me. (Sources online mix the two; the sheet's regional note is clear.)

REPAIR WARRANTY ❓: as on the Fold pages, the template rule "phone screens = lifetime" is applied, including the
  folding inner screen. Confirm that's what CrC offers on foldables.

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  2. Chip (above), foldable screen repair warranty (above), tagline (above).
  3. Colours: trim the four listed to what you stock.

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (11 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Z Flip Flip4 Flip5 Flip6 Flip7 Flip8 Fold8 Ultra Exynos Snapdragon Elite Gen Dynamic AMOLED Super Gorilla Glass Victus Armor Aluminum Flex Mode One UI Android Galaxy AI Circle Search Live Translate Now Brief Bar Photo Assist Wallet DeX Bluetooth Please MP IP48 IP68 RAM USB-C Wi-Fi 5G G Hz 4K S26 W SIM Wide GB UK Flip8's".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy Z Flip8",
             "Samsung Galaxy Z Flip8 folding phone with a 6.9-inch 120Hz main screen, 4.1-inch cover screen, Exynos 2600 "
             "chip, 12GB RAM, 50MP main camera with optical stabilisation, Galaxy AI, 4,300mAh battery, 5G and seven years "
             "of updates, at 180g. 60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT "
             "every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Graphite", "Cream", "Pink", "Mint"]
images = [(f"Main image: {c}", f"Samsung Galaxy Z Flip8 in {c}, half-open, showing the 6.9-inch screen",
           f"The Galaxy Z Flip8 in {c}, open to its 6.9-inch 120Hz screen.") for c in colours]
images += [
    ("Closed, cover screen", "Samsung Galaxy Z Flip8 closed, showing the 4.1-inch cover screen with widgets",
     "The Galaxy Z Flip8 closed: the 4.1-inch cover screen fills most of the front, with widgets and the Now Bar."),
    ("Cover-screen selfie", "Samsung Galaxy Z Flip8 closed, taking a selfie with the main camera using the cover screen",
     "Selfies on the Galaxy Z Flip8 with the 50MP main camera, using the cover screen as a viewfinder."),
    ("Folded in hand", "Samsung Galaxy Z Flip8 folded in the palm of a hand",
     "The Galaxy Z Flip8 folded: 85.7 × 75.4 × 13.1mm and 180g, small enough for any pocket."),
    ("Flex Mode", "Samsung Galaxy Z Flip8 standing half-open in Flex Mode on a table",
     "Flex Mode on the Galaxy Z Flip8: the phone stands half-open for hands-free video calls and photos."),
    ("In the box", "Samsung Galaxy Z Flip8 with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy Z Flip8 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy Z Flip8 folding phone half-open, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and UK launch coverage. The tagline is new: please approve or replace.",
    "Chip: the page says Exynos 2600, correct for UK/European stock. If any units are US imports with the Snapdragon, say so.",
    "Screen repair warranty: the page applies the lifetime screen rule to the folding inner screen too. Confirm, or tell me the Fold/Flip rule.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Four colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
    "Software line says Android 17 / One UI 9. Check against a handset before publishing.",
], tags=TAGS)
print("built")

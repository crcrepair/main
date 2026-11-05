"""iPhone 12 mini — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-12-mini"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 12 mini"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-12-mini/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-12-mini"   # pattern confirmed; capitalisation of "mini" still to confirm
TAGLINE = "Small size. Huge power."

META_TITLE = "Buy iPhone 12 mini | 5G, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy a compact iPhone 12 mini with 5G, a 5.4-inch OLED screen, the A14 Bionic and MagSafe. 60-point "
             "checked, with a 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 12 mini: the smallest 5G iPhone, 2-year warranty"
OG_DESC = "A14 Bionic, 5G, a dual 12MP camera with Night mode and MagSafe in a 133g phone. Fully checked and covered for two years."
X_TITLE = "iPhone 12 mini with a 2-year warranty | CrC Repair®"
X_DESC = "Pocket-sized 5G iPhone with the A14 Bionic, OLED screen and MagSafe. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 12 series", "Model family. Links the iPhone 12 mini, 12, 12 Pro and 12 Pro Max listings."),
    ("iPhone 12 mini", "Exact model, matching how people search. Apple writes \"mini\" in lower case."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-12mini-box", "What comes with the iPhone 12 mini?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-12mini-vs-se", "What's the difference between the iPhone 12 mini and iPhone SE (2020)?",
     "The 12 mini has 5G, an edge-to-edge 5.4-inch OLED screen with Face ID (the SE has a 4.7-inch LCD with a Home "
     "button and Touch ID), the faster A14 Bionic chip, a second Ultra Wide camera with Night mode, MagSafe and "
     "better water resistance. Despite the bigger screen, it's slightly smaller than the SE."),
    ("faq-12mini-vs-13mini", "Should I choose the iPhone 12 mini or the iPhone 13 mini?",
     "They're the same size. The 13 mini has the newer A15 chip, longer battery life of up to 17 hours of video "
     "against 15, Cinematic mode and sensor-shift stabilisation on the main camera, and it starts at 128GB. The "
     "12 mini is the cheaper way to get a small 5G iPhone with the same screen size and MagSafe."),
    ("faq-12mini-ios", "Is the iPhone 12 mini still supported by Apple?",
     "Yes. Apple supports the iPhone 12 mini with iOS 27. Apple Intelligence isn't available on it, though, as it "
     "needs an iPhone 15 Pro or later."),
    ("faq-12mini-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-12mini-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-12mini-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 128GB · 256GB"),
    ("Colours", "Black, White, Blue, Green, Purple and (PRODUCT)RED"),
    ("Display", "5.4-inch Super Retina XDR (OLED) · 2340 × 1080 · 476 ppi"),
    ("Brightness", "625 nits typical · 1,200 nits HDR"),
    ("Chip", "A14 Bionic · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Dual 12MP: Wide (ƒ/1.6, optical image stabilisation) and Ultra Wide (ƒ/2.4, 120°)"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Night mode on both cameras · Deep Fusion · Smart HDR 3 · Portrait mode"),
    ("Video", "4K up to 60fps · Dolby Vision HDR up to 30fps · Night mode Time-lapse"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Aluminium frame · Ceramic Shield front · 133g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 15 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe and Qi wireless charging"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the smallest 5G iPhone", [
        f"The <strong>{P}</strong> fits a 5.4-inch Super Retina XDR screen into a phone that weighs just 133g and is "
        "smaller than an iPhone SE, so it sits comfortably in one hand and slips into any pocket. Inside is the same "
        "<strong>A14 Bionic</strong> chip as the full-size iPhone 12, and Apple supports it with iOS 27.",
        "You get the same dual 12MP camera as the iPhone 12 too, with Night mode on both lenses and Dolby Vision HDR "
        "video. It was the first mini with 5G, <strong>MagSafe</strong> and a Ceramic Shield front, and it's the most "
        "affordable way into a small, modern iPhone.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Smaller battery.</strong> Up to 15 hours of video playback is fine for a normal day, but it's the "
        "shortest of the iPhone 12 range. If you watch a lot of video or play games, the iPhone 12 or 13 mini last "
        "longer.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 12 mini charges through Apple's Lightning port; USB-C "
        "arrived with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>No Apple Intelligence or Crash Detection.</strong> Apple supports it with iOS 27, but Apple "
        "Intelligence needs an iPhone 15 Pro or later, and Crash Detection arrived with the iPhone 14.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-12mini-size", "Smaller than an iPhone SE",
         "At 131.5mm tall and 133g, it's easy to use with one thumb and disappears into a pocket, while the edge-to-edge "
         "OLED screen still gives you a 5.4-inch display."),
        ("feat-12mini-a14", "A14 Bionic",
         "The same chip as the full-size iPhone 12, so apps, games and photo editing run just as quickly on the mini. "
         "Apple supports it with iOS 27."),
        ("feat-12mini-5g", "5G and MagSafe",
         "The first small iPhone with 5G for fast downloads, and MagSafe chargers, cases and wallets that snap into "
         "place magnetically."),
        ("feat-12mini-camera", "Dual 12MP camera with Night mode",
         "A Wide camera with a bright ƒ/1.6 lens and an Ultra Wide for landscapes, with Night mode on both, Deep Fusion "
         "for detail and Dolby Vision HDR video."),
        ("feat-12mini-display", "Super Retina XDR OLED",
         "A sharp 476 ppi OLED screen with true blacks and HDR up to 1,200 nits, in place of the SE's LCD, with Face ID "
         "instead of a Home button."),
        ("feat-12mini-tough", "Ceramic Shield and IP68",
         "A Ceramic Shield front with four times better drop performance than the iPhone 11, and IP68 water and dust "
         "resistance to 6 metres."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a genuinely small iPhone with a modern edge-to-edge screen, Face ID and 5G, "
        "at the lowest price for a mini. Coming from an iPhone SE, 8 or older, you'll notice the bigger, sharper screen "
        "in a smaller body, the faster chip and the much better camera.",
        "If battery life matters most, the iPhone 12 has a bigger battery, and the iPhone 13 mini lasts two hours "
        "longer in the same size. For USB-C you'll need an iPhone 15 or later, and for Apple Intelligence an iPhone "
        "15 Pro or later. Not sure which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-12mini-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-12mini-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-12mini-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-12mini-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-12mini-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-12mini-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-12mini-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-12mini-sell", "Sell or trade in",
         "Upgrading, or finished with your phone? We'll make you an offer. Take cash, or put the value towards your "
         "next device. Find out " + L("/we-buy/", "how we buy phones") + "."),
    ]),

    cta_pair((f"Need your {P} repaired?",
              "Book online for a quick estimate, or bring your iPhone into your nearest store.",
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
PAGE:              WooCommerce product description — Apple iPhone 12 mini
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - "iPhone 12 Mini" written as Apple names it: "iPhone 12 mini" (lower-case m), including the tag.
  - "vs SE (2020): 5G, edge-to-edge screen, MagSafe support" was correct and is kept, made specific in the FAQ:
    OLED and Face ID vs LCD and Touch ID, A14 vs A13, Ultra Wide camera with Night mode, and it's smaller than the SE.
  - The old copy had no description paragraph at all. Written fresh from Apple's specs.
  - Added what the old copy left out: 15-hour battery (shortest of the 12 range), Lightning (not USB-C), iOS 27
    support, no Apple Intelligence or Crash Detection, full spec list, a 12 mini vs 13 mini FAQ.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct (Purple was added in April 2021).

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (5.4-inch, 2340 × 1080 at 476 ppi, 15 h video, A14, Bluetooth 5.0) and the iOS 27
  compatibility list (iPhone 11 and later). Weight: Apple lists 133g for UK/EU models and 135g for the US model;
  133g used. MagSafe wattage is left out on purpose: Apple's spec sheet says up to 15W, but the mini models are
  limited to 12W, so no figure is safer (same approach as the iPhone 13 mini).

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Is "mini" lower case in your booking system,
     or "iPhone-12-Mini"? (Same question as the iPhone 13 mini.)

CONFIRMED BY GABOR (3 Nov 2026): condition tag "Pre-owned"; booking link pattern repairs/Apple/<Model>.
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Cinematic Deep Fusion Dolby Vision Face ID Home Touch SE SIM Please MP IP68 OLED 5G G Night Retina XDR Shield".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "") + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {P}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>", f"<strong>{TAGLINE}</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have an {P}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 12 mini", "Apple", "iPhone 12 mini",
             "Apple iPhone 12 mini with 5G, a 5.4-inch Super Retina XDR display, the A14 Bionic chip, a dual 12MP camera "
             "with Night mode, MagSafe and a Ceramic Shield front, in a 133g body. 60-point quality checked by CrC Repair® "
             "with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Blue", "Green", "Purple", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone 12 mini in {c}, front and back view",
           f"The iPhone 12 mini in {c}, with a 5.4-inch Super Retina XDR display and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 12 mini dual camera with Wide and Ultra Wide lenses",
     "The dual 12MP camera on the iPhone 12 mini, with Night mode on both lenses and Dolby Vision HDR video."),
    ("In the hand", "iPhone 12 mini held in one hand, showing its compact size",
     "The iPhone 12 mini in the hand: a 5.4-inch screen in a 133g phone that's smaller than an iPhone SE."),
    ("MagSafe", "iPhone 12 mini with a MagSafe charger attached to the back",
     "MagSafe charging on the iPhone 12 mini, with magnetic alignment for chargers, cases and wallets."),
    ("In the box", "Apple iPhone 12 mini with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 12 mini with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 12 mini", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 12 mini with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm whether \"mini\" is lower case in the booking system.",
], tags=TAGS)
print("built")

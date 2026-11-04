"""iPhone 13 — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-13"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 13"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-13/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-13"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "A perfect balance of power and size."

META_TITLE = "Buy iPhone 13 | 5G, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 13 with 5G, a 6.1-inch OLED screen, the A15 Bionic and Cinematic mode. 60-point checked, "
             "2-year warranty and free Device MOT every 6 months.")
OG_TITLE = "iPhone 13: 5G, Cinematic mode, all-day battery, 2-year warranty"
OG_DESC = "A15 Bionic, a brighter 6.1-inch OLED screen, dual 12MP camera and up to 19 hours of video. Fully checked, two-year cover."
X_TITLE = "iPhone 13 with a 2-year warranty | CrC Repair®"
X_DESC = "5G, a 6.1-inch OLED screen, the A15 Bionic and Cinematic mode. 60-point checked, free Device MOT every 6 months."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 13 series", "Model family. Links the iPhone 13 mini, 13, 13 Pro and 13 Pro Max listings."),
    ("iPhone 13", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-13-box", "What comes with the iPhone 13?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-13-vs-12", "What's the difference between the iPhone 13 and iPhone 12?",
     "The iPhone 13 has the faster A15 Bionic chip (the 12 has the A14), a brighter screen, a smaller notch and much "
     "longer battery life: up to 19 hours of video against 17. Its diagonal dual camera adds sensor-shift "
     "stabilisation, Cinematic mode and Photographic Styles, and storage starts at 128GB instead of 64GB."),
    ("faq-13-vs-13pro", "What's the difference between the iPhone 13 and iPhone 13 Pro?",
     "The 13 Pro adds a 120Hz ProMotion screen, a third telephoto camera, macro photography, ProRes video, a 5-core "
     "GPU and a stainless steel frame. The iPhone 13 has the same A15 chip, the same main and Ultra Wide cameras, "
     "Cinematic mode and a 60Hz screen, and it's lighter at 173g against 203g."),
    ("faq-13-ios", "Is the iPhone 13 still supported by Apple?",
     "Yes. Apple supports the iPhone 13 with iOS 27. Apple Intelligence isn't available on it, though, as it needs "
     "an iPhone 15 Pro or later."),
    ("faq-13-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-13-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-13-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Pink, Blue, Midnight, Starlight, Green and (PRODUCT)RED"),
    ("Display", "6.1-inch Super Retina XDR (OLED) · 2532 × 1170 · 460 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A15 Bionic · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Dual 12MP: Main (ƒ/1.6, sensor-shift stabilisation) and Ultra Wide (ƒ/2.4, 120°)"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Photographic Styles · Night mode · Smart HDR 4 · Portrait mode"),
    ("Video", "4K up to 60fps · Cinematic mode (1080p at 30fps) · Dolby Vision HDR"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Aluminium frame · Ceramic Shield front · 173g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 19 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the balanced choice: power, size and battery", [
        f"The <strong>{P}</strong> is the sweet spot of the range: a 6.1-inch Super Retina XDR screen that's brighter "
        "than the iPhone 12's, the <strong>A15 Bionic</strong> chip, and a battery that lasts up to 19 hours of video, "
        "a big jump on the model before it. Apple supports it with iOS 27.",
        "The diagonal dual 12MP camera has sensor-shift stabilisation for steadier shots, Photographic Styles to set the "
        "look you like, and <strong>Cinematic mode</strong> for film-style focus effects in video. Add 5G, MagSafe, a "
        "Ceramic Shield front and IP68 water resistance, and it's an easy phone to live with every day.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>60Hz screen, dual camera.</strong> The 120Hz ProMotion display, telephoto camera, macro photography "
        "and ProRes video are iPhone 13 Pro features. The iPhone 13 has a 60Hz screen and two cameras.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 13 charges through Apple's Lightning port; USB-C arrived "
        "with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>No Apple Intelligence or Crash Detection.</strong> Apple supports it with iOS 27, but Apple "
        "Intelligence needs an iPhone 15 Pro or later, and Crash Detection arrived with the iPhone 14.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-13-battery", "All-day battery",
         "Up to 19 hours of video playback, two and a half hours more than the iPhone 12, with fast charging to around "
         "50% in 30 minutes using a 20W adapter."),
        ("feat-13-a15", "A15 Bionic",
         "Fast enough for gaming, photo editing and 4K video at 60fps, and Apple supports it with iOS 27 for the "
         "latest features and security updates."),
        ("feat-13-cinematic", "Cinematic mode",
         "Record video with a shallow depth of field that shifts focus automatically between people, and change the "
         "focus after you've filmed."),
        ("feat-13-camera", "Diagonal dual 12MP camera",
         "The main camera has a larger sensor and sensor-shift stabilisation for steadier photos and video, Night mode "
         "works on both cameras, and Photographic Styles let you set the look you like."),
        ("feat-13-display", "Brighter 6.1-inch display",
         "The Super Retina XDR OLED screen reaches 800 nits in daylight, 28% brighter than the iPhone 12, with a "
         "20% smaller notch."),
        ("feat-13-tough", "5G, MagSafe and IP68",
         "5G for fast downloads, MagSafe chargers and accessories that snap into place, and a Ceramic Shield front with "
         "IP68 water and dust resistance."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a modern 5G iPhone with a really good camera, a bright screen and battery "
        "life that lasts a full day, without paying for Pro features you may not use. Coming from an iPhone 11, 12 or "
        "older, you'll notice the faster chip, longer battery and Cinematic mode.",
        "If you want a 120Hz screen or a telephoto camera, look at the iPhone 13 Pro. If you'd like something smaller, "
        "the iPhone 13 mini has the same chip and cameras in a 5.4-inch phone. For USB-C you'll need an iPhone 15 or "
        "later, and for Apple Intelligence an iPhone 15 Pro or later. Not sure which suits you? Ask in any of our "
        "stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-13-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-13-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-13-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-13-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-13-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-13-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-13-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-13-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 13
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old description paragraph was WRONG: it described the iPhone 13 PRO ("120Hz refresh with ProMotion",
    "5-core GPU", "Triple cameras", "macro photography", "ProRes"). None of that applies to the iPhone 13, which
    has a 60Hz screen, a 4-core GPU and two cameras. Rewritten for the iPhone 13, and the Pro-only features are
    listed in "Before you buy" so nobody buys it expecting them.
  - "vs iPhone 12: Diagonal dual cameras, brighter screen, Cinematic Mode" was correct and is kept, made specific:
    A15 vs A14, 19 vs 17 hours of video, sensor-shift stabilisation, Photographic Styles, 128GB base storage.
  - Added what the old copy left out: Lightning (not USB-C), iOS 27 support, no Apple Intelligence or
    Crash Detection, full spec list.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct (Green was added in March 2022).

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.1-inch, 2532 × 1170 at 460 ppi, 173g, 19 h video, MagSafe 15W, Qi 7.5W,
  Bluetooth 5.0) and the iOS 27 compatibility list (iPhone 11 and later). The 4-core GPU matches the approved
  iPhone 14 page ("the iPhone 13's has 4").

CONFIRMED BY GABOR (3 Nov 2026):
  1. Booking link value: ?selected={BOOKING_SELECTED}
  2. Condition tag: Pre-owned
  3. Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Cinematic Photographic Styles SIM Please MP IP68 Pro".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 13", "Apple", "iPhone 13",
             "Apple iPhone 13 with 5G, a 6.1-inch Super Retina XDR display, the A15 Bionic chip, a dual 12MP camera "
             "with sensor-shift stabilisation and Cinematic mode, MagSafe and up to 19 hours of video playback. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Pink", "Blue", "Midnight", "Starlight", "Green", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone 13 in {c}, front and back view",
           f"The iPhone 13 in {c}, with a 6.1-inch Super Retina XDR display and diagonal dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 13 diagonal dual camera with Main and Ultra Wide lenses",
     "The diagonal dual 12MP camera on the iPhone 13, with sensor-shift stabilisation and Cinematic mode."),
    ("Screen on, front", "iPhone 13 6.1-inch Super Retina XDR display switched on",
     "The 6.1-inch OLED Super Retina XDR screen of the iPhone 13, 800 nits in daylight and 1,200 nits for HDR."),
    ("MagSafe", "iPhone 13 with a MagSafe charger attached to the back",
     "MagSafe charging on the iPhone 13, at up to 15W with magnetic alignment."),
    ("In the box", "Apple iPhone 13 with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 13 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 13", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 13 with diagonal dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
], tags=TAGS)
print("built")

"""iPhone 12 Pro — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-12-pro"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 12 Pro"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-12-pro/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-12-Pro"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "Precision in every pixel."

META_TITLE = "Buy iPhone 12 Pro | 5G, Triple Camera | CrC Repair®"
META_DESC = ("Buy an iPhone 12 Pro with a 6.1-inch OLED screen, 2x telephoto, LiDAR, 5G and a stainless steel frame. "
             "60-point checked, 2-year warranty, free Device MOT.")
OG_TITLE = "iPhone 12 Pro: triple camera, LiDAR, 5G, 2-year warranty"
OG_DESC = "A14 Bionic, 6.1-inch OLED screen, 2x telephoto, LiDAR and Dolby Vision video in stainless steel. Fully checked, 2-year cover."
X_TITLE = "iPhone 12 Pro with a 2-year warranty | CrC Repair®"
X_DESC = "6.1-inch OLED screen, triple camera with LiDAR, 5G and MagSafe in stainless steel. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 12 series", "Model family. Links the iPhone 12 mini, 12, 12 Pro and 12 Pro Max listings."),
    ("iPhone 12 Pro", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-12pro-box", "What comes with the iPhone 12 Pro?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-12pro-vs-11pro", "What's the difference between the iPhone 12 Pro and iPhone 11 Pro?",
     "The 12 Pro adds 5G, a larger 6.1-inch screen (the 11 Pro is 5.8-inch) in a flat-edged stainless steel body "
     "that's lighter at 189g against 188g for a bigger phone, the faster A14 Bionic chip, a LiDAR scanner for Night "
     "mode portraits, Apple ProRAW, Dolby Vision video, MagSafe and a Ceramic Shield front. Battery life is similar, "
     "up to 17 hours of video against 18."),
    ("faq-12pro-vs-12", "Is the iPhone 12 Pro worth it over the iPhone 12?",
     "Choose the Pro if you want the 2x telephoto camera, the LiDAR scanner, Apple ProRAW, a brighter screen, a "
     "stainless steel frame and 128GB as the starting storage. The iPhone 12 shares the A14 chip, the 6.1-inch OLED "
     "screen, 5G, MagSafe and the main and Ultra Wide cameras, and it's lighter at 162g."),
    ("faq-12pro-ios", "Is the iPhone 12 Pro still supported by Apple?",
     "Yes. Apple supports the iPhone 12 Pro with iOS 27. Apple Intelligence isn't available on it, though, as it "
     "needs an iPhone 15 Pro or later."),
    ("faq-12pro-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-12pro-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-12pro-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Silver, Graphite, Gold and Pacific Blue"),
    ("Display", "6.1-inch Super Retina XDR (OLED) · 2532 × 1170 · 460 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A14 Bionic · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Triple 12MP: Wide (ƒ/1.6), Ultra Wide (ƒ/2.4, 120°) and Telephoto (ƒ/2.0) · optical stabilisation on Wide and Telephoto"),
    ("Zoom", "2x optical zoom in · 2x optical zoom out · 4x optical zoom range · up to 10x digital"),
    ("Photography", "LiDAR scanner · Night mode on all cameras and Night mode portraits · Deep Fusion · Smart HDR 3 · Apple ProRAW"),
    ("Video", "4K up to 60fps · Dolby Vision HDR up to 60fps · Night mode Time-lapse"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Stainless steel frame · Ceramic Shield front · 189g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 17 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — Pro cameras and stainless steel in a 6.1-inch phone", [
        f"The <strong>{P}</strong> brought the Pro range to a flat-edged <strong>stainless steel</strong> design with a "
        "6.1-inch Super Retina XDR screen, larger than the iPhone 11 Pro's yet almost the same weight. It runs on the "
        "<strong>A14 Bionic</strong>, the first 5-nanometre phone chip, and Apple supports it with iOS 27. 5G, MagSafe "
        "and a Ceramic Shield front all arrived with this generation.",
        "The triple camera adds a <strong>LiDAR scanner</strong> for sharper Night mode portraits and faster autofocus "
        "in the dark, alongside a 2x telephoto and an Ultra Wide. Apple ProRAW gives full editing control over photos, "
        "and it was the first phone to record Dolby Vision HDR video. Battery life is up to 17 hours of video.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Same main camera as the iPhone 12.</strong> The Pro's extras are the 2x telephoto, LiDAR scanner, "
        "ProRAW and the steel frame. Sensor-shift stabilisation and the 2.5x telephoto are iPhone 12 Pro Max only.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 12 Pro charges through Apple's Lightning port; USB-C "
        "arrived with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>60Hz screen, no Apple Intelligence.</strong> The 120Hz ProMotion display arrived with the iPhone 13 "
        "Pro. Apple supports the phone with iOS 27, but Apple Intelligence needs an iPhone 15 Pro or later, and "
        "Crash Detection arrived with the iPhone 14.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-12pro-lidar", "LiDAR scanner",
         "The LiDAR scanner measures depth with light, so Night mode works in Portrait mode, autofocus in low light is "
         "up to six times faster, and augmented reality apps place objects more accurately."),
        ("feat-12pro-telephoto", "2x telephoto camera",
         "A 52mm-equivalent telephoto gets you closer for portraits and detail without digital zoom, giving a 4x "
         "optical zoom range from Ultra Wide to Telephoto, with optical stabilisation on both Wide and Telephoto."),
        ("feat-12pro-proraw", "Apple ProRAW and Dolby Vision",
         "Shoot ProRAW for full editing control over colour and detail, and record Dolby Vision HDR video at up to "
         "4K 60fps, a first for any phone."),
        ("feat-12pro-steel", "Stainless steel and Ceramic Shield",
         "A polished stainless steel frame, flat edges and a Ceramic Shield front with four times better drop "
         "performance than the iPhone 11 Pro, with IP68 water resistance to 6 metres."),
        ("feat-12pro-display", "6.1-inch Super Retina XDR display",
         "Bigger than the iPhone 11 Pro's 5.8-inch screen in almost the same body, with true blacks, HDR up to 1,200 "
         "nits and 460 ppi."),
        ("feat-12pro-a14", "A14 Bionic, 5G and MagSafe",
         "Fast enough for gaming and 4K editing, with 5G for quick downloads and MagSafe chargers and accessories that "
         "snap into place. Apple supports the phone with iOS 27."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a Pro iPhone with a telephoto camera, LiDAR and a stainless steel build in a "
        "size that's comfortable to hold, at a pre-owned price. Coming from an iPhone X, XS or 11 Pro, you'll notice "
        "5G, the bigger screen, the better Night mode and MagSafe.",
        "If you don't need the telephoto or LiDAR, the iPhone 12 has the same chip, screen size and main camera for "
        "less. For the biggest screen, longest battery and sensor-shift stabilisation, look at the iPhone 12 Pro Max, "
        "and for a 120Hz screen and macro photography, the iPhone 13 Pro. For USB-C you'll need an iPhone 15 or later, "
        "and for Apple Intelligence an iPhone 15 Pro or later. Not sure which suits you? Ask in any of our stores and "
        "we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-12pro-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-12pro-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-12pro-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-12pro-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-12pro-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-12pro-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-12pro-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-12pro-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 12 Pro
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - "vs iPhone 11 Pro: LiDAR scanner, Dolby Vision video, stainless steel frame, 5G-ready" was correct and is
    kept, made specific in the FAQ. "5G-ready" changed to "5G": the phone has 5G, it's not waiting for it.
    (The 11 Pro also had a stainless steel frame; the 12 Pro's is the flat-edged design.)
  - The old copy had no description paragraph at all. Written fresh from Apple's specs.
  - Added what the old copy left out: 2x telephoto and 4x zoom range, ProRAW, 17-hour battery, what the Pro
    adds over the iPhone 12 and what the Pro Max adds over the Pro, Lightning (not USB-C), 60Hz (no ProMotion),
    iOS 27 support, no Apple Intelligence or Crash Detection, full spec list.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct.

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.1-inch, 2532 × 1170 at 460 ppi, 189g, 17 h video, ƒ/2.0 telephoto, dual
  optical stabilisation) and the iOS 27 compatibility list (iPhone 11 and later).

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
      ok_caps="iPhone Pro Max Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Deep Fusion Dolby Vision ProRAW LiDAR Night Retina XDR Shield Ceramic Face ID GPU SIM Please MP IP68 OLED 5G G Hz Super".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 12 Pro", "Apple", "iPhone 12 Pro",
             "Apple iPhone 12 Pro with a 6.1-inch Super Retina XDR display, the A14 Bionic chip, 5G, a triple 12MP camera "
             "with 2x telephoto and LiDAR scanner, Apple ProRAW, Dolby Vision video and MagSafe, in stainless steel. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Silver", "Graphite", "Gold", "Pacific Blue"]
images = [(f"Main image: {c}", f"Apple iPhone 12 Pro in {c}, front and back view",
           f"The iPhone 12 Pro in {c}, with a 6.1-inch Super Retina XDR display and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 12 Pro triple camera with Wide, Ultra Wide and Telephoto lenses and LiDAR scanner",
     "The triple 12MP camera on the iPhone 12 Pro, with 2x telephoto and LiDAR scanner for Night mode portraits."),
    ("Screen on, front", "iPhone 12 Pro 6.1-inch Super Retina XDR display switched on",
     "The 6.1-inch OLED Super Retina XDR screen of the iPhone 12 Pro, up to 1,200 nits for HDR."),
    ("MagSafe", "iPhone 12 Pro with a MagSafe charger attached to the back",
     "MagSafe charging on the iPhone 12 Pro, at up to 15W with magnetic alignment."),
    ("In the box", "Apple iPhone 12 Pro with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 12 Pro with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 12 Pro", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 12 Pro in stainless steel with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
], tags=TAGS)
print("built")

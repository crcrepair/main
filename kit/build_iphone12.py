"""iPhone 12 — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-12"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 12"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-12/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-12"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "Fast, sleek and 5G."

META_TITLE = "Buy iPhone 12 | 5G, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 12 with 5G, a 6.1-inch OLED screen, the A14 Bionic, MagSafe and Night mode camera. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 12: 5G, OLED screen and MagSafe, 2-year warranty"
OG_DESC = "A14 Bionic, a 6.1-inch OLED screen, dual 12MP camera with Night mode and MagSafe. Fully checked and covered for two years."
X_TITLE = "iPhone 12 with a 2-year warranty | CrC Repair®"
X_DESC = "5G, a 6.1-inch OLED screen, the A14 Bionic and MagSafe. 60-point checked, free Device MOT every 6 months."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 12 series", "Model family. Links the iPhone 12 mini, 12, 12 Pro and 12 Pro Max listings."),
    ("iPhone 12", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-12-box", "What comes with the iPhone 12?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-12-vs-11", "What's the difference between the iPhone 12 and iPhone 11?",
     "The iPhone 12 has 5G, an OLED screen in place of the 11's LCD, with twice the resolution and HDR, a flat-edged "
     "design that's thinner and lighter, the faster A14 Bionic chip, MagSafe, a Ceramic Shield front and better water "
     "resistance. The camera adds Night mode on the Ultra Wide and front cameras, and Dolby Vision video."),
    ("faq-12-vs-13", "Should I choose the iPhone 12 or the iPhone 13?",
     "They look almost identical. The 13 has the newer A15 chip, a longer battery of up to 19 hours of video against "
     "17, a brighter screen, Cinematic mode, sensor-shift stabilisation on the main camera, a smaller notch and "
     "128GB as the starting storage. The 12 is the cheaper way to get a 5G iPhone with the same screen size, MagSafe "
     "and the same Ultra Wide camera."),
    ("faq-12-ios", "Is the iPhone 12 still supported by Apple?",
     "Yes. Apple supports the iPhone 12 with iOS 27. Apple Intelligence isn't available on it, though, as it needs "
     "an iPhone 15 Pro or later."),
    ("faq-12-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-12-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-12-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 128GB · 256GB"),
    ("Colours", "Black, White, Blue, Green, Purple and (PRODUCT)RED"),
    ("Display", "6.1-inch Super Retina XDR (OLED) · 2532 × 1170 · 460 ppi · HDR10 and Dolby Vision"),
    ("Brightness", "625 nits typical · 1,200 nits HDR"),
    ("Chip", "A14 Bionic · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Dual 12MP: Wide (ƒ/1.6, optical image stabilisation) and Ultra Wide (ƒ/2.4, 120°)"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Night mode on both cameras · Deep Fusion · Smart HDR 3 · Portrait mode"),
    ("Video", "4K up to 60fps · Dolby Vision HDR up to 30fps · Night mode Time-lapse"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Aluminium frame · Ceramic Shield front · 162g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 17 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — 5G, OLED and MagSafe in a flat-edged design", [
        f"The <strong>{P}</strong> was a big step from the iPhone 11: a 6.1-inch Super Retina XDR OLED screen with HDR "
        "in place of the LCD, a thinner and lighter flat-edged body with a <strong>Ceramic Shield</strong> front, and "
        "the <strong>A14 Bionic</strong> chip, the first 5-nanometre chip in a phone. Apple supports it with iOS 27.",
        "It was also the first iPhone with <strong>5G</strong> and <strong>MagSafe</strong>, so chargers, cases and "
        "wallets snap into place magnetically. The dual 12MP camera has a brighter ƒ/1.6 lens, Night mode on both "
        "lenses and Deep Fusion for detail, and it records Dolby Vision HDR video. Battery life is up to 17 hours of "
        "video playback.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Lightning, not USB-C.</strong> The iPhone 12 charges through Apple's Lightning port; USB-C arrived "
        "with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>60Hz screen, dual camera.</strong> The display is sharp with true blacks, but the 120Hz ProMotion "
        "screen arrived with the iPhone 13 Pro, and the telephoto camera and LiDAR scanner are iPhone 12 Pro features.",
        "<strong>No Apple Intelligence or Crash Detection.</strong> Apple supports it with iOS 27, but Apple "
        "Intelligence needs an iPhone 15 Pro or later, and Crash Detection arrived with the iPhone 14.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-12-display", "Super Retina XDR OLED",
         "A 6.1-inch OLED screen with 460 ppi, true blacks, HDR10 and Dolby Vision up to 1,200 nits, more than twice "
         "the resolution of the iPhone 11's LCD."),
        ("feat-12-design", "Flat-edged, thinner and lighter",
         "The flat aluminium edges and 162g weight make it 11% thinner and 16% lighter than the iPhone 11, with a "
         "Ceramic Shield front that has four times better drop performance."),
        ("feat-12-5g", "5G and MagSafe",
         "The first iPhone with 5G for fast downloads, and MagSafe chargers, cases and wallets that snap into place "
         "magnetically and charge at up to 15W."),
        ("feat-12-camera", "Dual 12MP camera with Night mode",
         "A Wide camera with a bright ƒ/1.6 lens and an Ultra Wide for landscapes, with Night mode on both, Deep Fusion "
         "for detail and Dolby Vision HDR video."),
        ("feat-12-a14", "A14 Bionic",
         "Fast enough for gaming, photo editing and 4K video at 60fps, and Apple supports it with iOS 27 for the "
         "latest features and security updates."),
        ("feat-12-battery", "Battery and fast charging",
         "Up to 17 hours of video playback, with fast charging to around 50% in 30 minutes using a 20W adapter, and "
         "IP68 water resistance to 6 metres."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a modern-looking 5G iPhone with an OLED screen, MagSafe and a good camera at "
        "one of the lowest prices for the flat-edged design. Coming from an iPhone 8, X, XR or 11, you'll notice the "
        "sharper screen, the lighter body, 5G and the better Night mode.",
        "If you want a longer battery and Cinematic mode, the iPhone 13 looks the same and costs a little more. For a "
        "telephoto camera and LiDAR, look at the iPhone 12 Pro, and for something smaller, the iPhone 12 mini has the "
        "same chip and cameras in a 5.4-inch phone. For USB-C you'll need an iPhone 15 or later, and for Apple "
        "Intelligence an iPhone 15 Pro or later. Not sure which suits you? Ask in any of our stores and we'll talk you "
        "through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-12-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-12-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-12-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-12-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-12-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-12-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-12-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-12-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 12
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was correct (OLED with Dolby Vision and HDR10, A14, flat edges, Ceramic Shield, aluminium,
    dual 12MP with Night mode and Deep Fusion, MagSafe). Kept its facts and made them specific: 460 ppi, ƒ/1.6,
    Night mode on both cameras, 17-hour battery, 15W MagSafe, 11% thinner and 16% lighter than the 11.
  - "5G-ready" changed to "5G" in the tagline and the comparison: the phone has 5G, it's not waiting for it.
  - "Night Mode", "ceramic shield" written as Apple does: "Night mode", "Ceramic Shield".
  - Added what the old copy left out: Lightning (not USB-C), 60Hz (no ProMotion), no telephoto or LiDAR (12 Pro),
    iOS 27 support, no Apple Intelligence or Crash Detection, a 12 vs 13 FAQ, full spec list.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct (Purple was added in April 2021).

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.1-inch, 2532 × 1170 at 460 ppi, 17 h video, MagSafe 15W, Qi 7.5W) and the
  iOS 27 compatibility list (iPhone 11 and later). Weight: Apple's UK page lists 162g; the 164g seen on many
  third-party sites is the US model. 162g used, and the iPhone 12 Pro FAQ updated to match.

CONFIRMED BY GABOR (3 Nov 2026):
  1. Booking link value: ?selected={BOOKING_SELECTED}
  2. Condition tag: Pre-owned
  3. Tagline from the old copy, with "5G-ready" changed to "5G": "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Cinematic Deep Fusion Dolby Vision ProMotion LiDAR Night Retina XDR Shield Ceramic Face ID SIM Please MP IP68 OLED 5G G Hz Super".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 12", "Apple", "iPhone 12",
             "Apple iPhone 12 with 5G, a 6.1-inch Super Retina XDR OLED display, the A14 Bionic chip, a dual 12MP camera "
             "with Night mode and Dolby Vision video, MagSafe and a Ceramic Shield front. 60-point quality checked by "
             "CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Blue", "Green", "Purple", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone 12 in {c}, front and back view",
           f"The iPhone 12 in {c}, with a 6.1-inch Super Retina XDR display and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 12 dual camera with Wide and Ultra Wide lenses",
     "The dual 12MP camera on the iPhone 12, with Night mode on both lenses and Dolby Vision HDR video."),
    ("Screen on, front", "iPhone 12 6.1-inch Super Retina XDR display switched on",
     "The 6.1-inch OLED Super Retina XDR screen of the iPhone 12, up to 1,200 nits for HDR."),
    ("MagSafe", "iPhone 12 with a MagSafe charger attached to the back",
     "MagSafe charging on the iPhone 12, at up to 15W with magnetic alignment."),
    ("In the box", "Apple iPhone 12 with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 12 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 12", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 12 with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
], tags=TAGS)
print("built")

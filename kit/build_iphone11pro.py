"""iPhone 11 Pro — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-11-pro"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 11 Pro"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-11-pro/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-11-Pro"   # ❓ pattern from the iPhone 15 Pro link; confirm

META_TITLE = "Buy iPhone 11 Pro | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 11 Pro: compact 5.8-inch Super Retina XDR screen, triple camera with Night mode and A13 "
             "Bionic. 60-point checked with a 2-year warranty.")
OG_TITLE = "iPhone 11 Pro: Pro cameras in a compact size, 2-year warranty"
OG_DESC = "Triple camera with Night mode, a 5.8-inch Super Retina XDR screen and A13 Bionic. Fully checked and covered for two years."
X_TITLE = "iPhone 11 Pro with a 2-year warranty | CrC Repair®"
X_DESC = "Compact 5.8-inch Pro iPhone with a triple camera and Night mode. 60-point checked, free Device MOT every 6 months."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 11 series", "Model family. Links the iPhone 11, 11 Pro and 11 Pro Max listings."),
    ("iPhone 11 Pro", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("4G", "Connectivity. Lets shoppers separate 4G phones from 5G ones; use 5G on iPhone 12 and later."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-11pro-box", "What comes with the iPhone 11 Pro?",
     "The phone comes with a charging cable as standard. Need a plug, screen protector, case or wireless charger? "
     "Have a look at our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount is taken off automatically "
     "in the basket on selected accessories."),
    ("faq-11pro-size", "How big is the iPhone 11 Pro?",
     "It has a 5.8-inch screen and weighs 188g, so it fits comfortably in one hand and most pockets. If you'd like a "
     "bigger screen and longer battery life, the iPhone 11 Pro Max has the same cameras and chip on a 6.5-inch display."),
    ("faq-11pro-ios", "Is the iPhone 11 Pro still supported by Apple?",
     "Yes. Apple supports the iPhone 11 Pro with iOS 27. Some of the newest iOS features need more recent hardware, "
     "and Apple Intelligence is only available on the iPhone 15 Pro and later."),
    ("faq-11pro-5g", "Is the iPhone 11 Pro 5G?",
     "No. It uses 4G LTE, which works on every UK network, plus Wi-Fi 6 at home and work. 5G came in with the "
     "iPhone 12."),
    ("faq-11pro-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can run two numbers. Ask us if you'd like to "
     "confirm the network status of a specific handset."),
    ("faq-11pro-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-11pro-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 256GB · 512GB"),
    ("Colours", "Midnight Green, Space Grey, Silver and Gold"),
    ("Display", "5.8-inch Super Retina XDR (OLED) · 2436 × 1125 · 458 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A13 Bionic · third-generation Neural Engine"),
    ("Rear cameras", "Triple 12MP: Wide, Ultra Wide and Telephoto"),
    ("Zoom", "2x optical zoom in and out (4x optical range) · up to 10x digital zoom"),
    ("Photography", "Night mode · Deep Fusion · Smart HDR · Portrait mode"),
    ("Video", "4K up to 60fps · extended dynamic range · slo-mo"),
    ("Front camera", "12MP TrueDepth · 4K video · Face ID"),
    ("Build", "Stainless steel frame · textured matte glass back · 188g"),
    ("Water and dust", "IP68 (up to 4 metres for 30 minutes)"),
    ("Battery", "Up to 18 hours video playback (up to 4 hours longer than iPhone XS)"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (18W adapter) · Qi wireless"),
    ("Connectivity", "4G LTE · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — Pro cameras, compact size", [
        f"The <strong>{P}</strong> puts Apple's first triple-camera system into a phone that fits easily in one hand. "
        "Its 5.8-inch Super Retina XDR screen is bright and sharp, the A13 Bionic chip handles demanding apps and "
        "games without fuss, and Apple still supports it with iOS 27.",
        "Next to the iPhone XS it gains the ultra-wide lens, Night mode for low-light shots, a faster chip and up to "
        "four hours more battery life. A stainless steel frame and textured matte glass back give it a premium "
        "finish, and it arrives with a <strong>charging cable</strong> as standard.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Lightning, not USB-C.</strong> It charges through the Lightning port, so older Lightning cables and "
        "accessories still fit. Qi wireless chargers work too, but it has no MagSafe magnets.",
        "<strong>4G, not 5G.</strong> Fast 4G LTE and Wi-Fi 6 cover everyday use on any UK network. Apple added 5G "
        "with the iPhone 12.",
        "<strong>No Apple Intelligence.</strong> The phone is still supported by iOS 27, but Apple Intelligence "
        "needs an iPhone 15 Pro or later, and a few of the newest iOS features are limited on older models.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-11pro-triple", "Triple camera system",
         "Three 12MP cameras (Wide, Ultra Wide and Telephoto) cover a 4x optical zoom range, from group shots in "
         "tight spaces to portraits with natural background blur."),
        ("feat-11pro-night", "Night mode and Deep Fusion",
         "Night mode kicks in automatically when the light drops, so evening photos come out brighter without the "
         "flash. Deep Fusion sharpens detail and texture indoors."),
        ("feat-11pro-compact", "Pro features, pocket size",
         "At 5.8 inches and 188g it's one of the most compact Pro iPhones, yet it keeps the full triple camera and "
         "Super Retina XDR screen of its bigger sibling."),
        ("feat-11pro-display", "Super Retina XDR display",
         "The OLED screen reaches 800 nits for everyday use and 1,200 nits for HDR video, with deep blacks and accurate "
         "colour for photos, films and games."),
        ("feat-11pro-a13", "A13 Bionic chip",
         "Fast enough for gaming, editing photos and 4K video at 60fps, and still supported by iOS 27 for security "
         "updates and new features."),
        ("feat-11pro-battery", "All-day battery",
         "Up to 18 hours of video playback, up to four hours more than the iPhone XS. An 18W or higher adapter "
         "fast-charges it to about 50% in around 30 minutes."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's a great fit if you want a proper Pro camera in a small, easy-to-hold phone without paying new-model "
        "prices. Coming from an iPhone X, XS or 8, you'll notice the better camera, the extra battery life and Night "
        "mode straight away.",
        "If you'd like a larger screen and the longest battery life of the iPhone 11 range, look at the iPhone 11 Pro "
        "Max. For 5G, USB-C or Apple Intelligence, you'll need a newer model. Not sure which suits you? Ask in any of "
        "our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-11pro-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-11pro-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-11pro-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-11pro-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-11pro-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-11pro-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-11pro-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-11pro-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 11 Pro
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's iPhone 11 Pro tech specs):
  - "Memory: 64GB, 256GB, 512GB" relabelled "Storage".
  - "It also introduced a fast 18W charger included in the box" removed. Apple's original box had it, but your
    listing includes a charging cable only, so the line could mislead. Fast charging is still explained (18W adapter).
  - "Faster GPU/CPU" made specific (A13 Bionic vs the XS's A12); "Night Mode" lower-cased to Apple's "Night mode".
  - "Click here" accessories link given descriptive anchor text; links normalised to https://www.crcrepair.co.uk.
  - Added: iOS 27 support, no Apple Intelligence, 4G not 5G, Lightning/Qi (no MagSafe), full spec list, size FAQ.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Night Deep Fusion Super Retina XDR Bionic".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "") + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {P}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>",
              "<strong>Pro power in your palm.</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have an {P}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 11 Pro", "Apple", "iPhone 11 Pro",
             "Apple iPhone 11 Pro with a compact 5.8-inch Super Retina XDR display, triple 12MP camera with Night mode "
             "and the A13 Bionic chip. 60-point quality checked by CrC Repair® with a two-year warranty and a free "
             "Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 11 Pro", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 11 Pro with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], [
    ("Main image: Midnight Green", "Apple iPhone 11 Pro in Midnight Green, front and back view",
     "The iPhone 11 Pro in Midnight Green, with its 5.8-inch display and triple camera on a matte glass back."),
    ("Main image: Space Grey", "Apple iPhone 11 Pro in Space Grey, front and back view",
     "The iPhone 11 Pro in Space Grey, with a stainless steel frame and textured matte glass back."),
    ("Main image: Silver", "Apple iPhone 11 Pro in Silver, front and back view",
     "The iPhone 11 Pro in Silver, quality checked by CrC Repair® before sale."),
    ("Main image: Gold", "Apple iPhone 11 Pro in Gold, front and back view",
     "The iPhone 11 Pro in Gold, with a Super Retina XDR display and A13 Bionic chip."),
    ("Camera close-up", "Close-up of the iPhone 11 Pro triple camera with Wide, Ultra Wide and Telephoto lenses",
     "The triple 12MP camera on the iPhone 11 Pro, with a 4x optical zoom range and Night mode."),
    ("Screen on, front", "iPhone 11 Pro 5.8-inch Super Retina XDR display switched on",
     "The compact 5.8-inch OLED screen of the iPhone 11 Pro, up to 800 nits typical and 1,200 nits HDR."),
    ("In the hand", "iPhone 11 Pro held in one hand, showing its compact size",
     "The 5.8-inch iPhone 11 Pro is small enough to use comfortably with one hand."),
    ("Bottom and Lightning port", "Bottom edge of the iPhone 11 Pro with Lightning port and speakers",
     "The Lightning charging port and speaker grilles on the bottom edge of the iPhone 11 Pro."),
    ("In the box", "Apple iPhone 11 Pro with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 11 Pro with a charging cable included as standard."),
], notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product, so each tag page groups the right listings.",
    "Tag archive pages (/product-tag/…) have no unique content of their own. Set them to <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies, so they don't compete with your product and category pages in Google.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

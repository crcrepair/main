"""iPhone 11 — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-11"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 11"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-11/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-11"   # ❓ pattern from the iPhone 15 Pro link; confirm

META_TITLE = "Buy iPhone 11 | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 11 with a 6.1-inch Liquid Retina screen, dual camera with Night mode and A13 Bionic. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 11: dual camera, all-day battery, 2-year warranty"
OG_DESC = "Night mode dual camera, a 6.1-inch Liquid Retina screen and A13 Bionic speed, in six colours. Fully checked, two-year cover."
X_TITLE = "iPhone 11 with a 2-year warranty | CrC Repair®"
X_DESC = "Dual camera with Night mode, 6.1-inch screen and up to 17 hours of video. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 11 series", "Model family. Links the iPhone 11, 11 Pro and 11 Pro Max listings."),
    ("iPhone 11", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("4G", "Connectivity. Separates 4G phones from 5G ones; use 5G on iPhone 12 and later."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-11-box", "What comes with the iPhone 11?",
     "Your iPhone 11 comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, "
     "see our " + L(ACCESSORIES, "phone accessories") + ". The 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-11-vs-pro", "What's the difference between the iPhone 11 and iPhone 11 Pro?",
     "The iPhone 11 has a 6.1-inch LCD Liquid Retina screen, a dual camera (Wide and Ultra Wide) and an aluminium "
     "frame. The 11 Pro adds an OLED Super Retina XDR screen, a third telephoto camera for 2x optical zoom, and a "
     "stainless steel frame. Both use the same A13 Bionic chip, so everyday speed is the same."),
    ("faq-11-ios", "Is the iPhone 11 still supported by Apple?",
     "Yes. Apple supports the iPhone 11 with iOS 27. Some of the newest iOS features need more recent hardware, and "
     "Apple Intelligence is only available on the iPhone 15 Pro and later."),
    ("faq-11-5g", "Does the iPhone 11 work with 5G?",
     "No. It uses 4G LTE, which works on every UK network, and Wi-Fi 6 for fast home broadband. Apple introduced "
     "5G with the iPhone 12."),
    ("faq-11-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers. Ask us if you'd like to "
     "confirm the network status of a specific handset."),
    ("faq-11-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-11-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 128GB · 256GB"),
    ("Colours", "Black, White, Green, Yellow, Purple and (PRODUCT)RED"),
    ("Display", "6.1-inch Liquid Retina HD (LCD) · 1792 × 828 · 326 ppi · True Tone"),
    ("Brightness", "625 nits typical"),
    ("Chip", "A13 Bionic · third-generation Neural Engine"),
    ("Rear cameras", "Dual 12MP: Wide and Ultra Wide"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Night mode · Deep Fusion · Smart HDR · Portrait mode"),
    ("Video", "4K up to 60fps · extended dynamic range · slo-mo"),
    ("Front camera", "12MP TrueDepth · 4K video · Face ID"),
    ("Audio", "Spatial audio · Dolby Atmos playback"),
    ("Build", "Aluminium frame · glass front and back · 194g"),
    ("Water and dust", "IP68 (up to 2 metres for 30 minutes)"),
    ("Battery", "Up to 17 hours video playback (up to 1 hour longer than iPhone XR)"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (18W adapter) · Qi wireless"),
    ("Connectivity", "4G LTE · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — dual camera, all-day battery", [
        f"The <strong>{P}</strong> gave Apple's everyday iPhone a second camera: Wide and Ultra Wide lenses that "
        "switch with a tap. Night mode handles low light, the 6.1-inch Liquid Retina screen is bright and clear, and the "
        "A13 Bionic chip keeps everything quick. Apple still supports it with iOS 27.",
        "Next to the iPhone XR it adds the ultra-wide lens and Night mode, a faster chip, and better water resistance "
        "(IP68 to 2 metres). Face ID is quicker and works from more angles, and stereo speakers with Dolby Atmos "
        "make films and music sound fuller. It comes in six colours, with a <strong>charging cable</strong> as "
        "standard.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>LCD, not OLED.</strong> The iPhone 11 uses a Liquid Retina LCD, which is sharp and colour-accurate "
        "but lacks the deeper blacks of the OLED screens on the 11 Pro models.",
        "<strong>Lightning and 4G.</strong> It charges through the Lightning port (Qi wireless works too, without "
        "MagSafe magnets) and connects over 4G LTE rather than 5G.",
        "<strong>No Apple Intelligence.</strong> Apple still supports the iPhone 11 with iOS 27, but Apple "
        "Intelligence needs an iPhone 15 Pro or later, and a few of the newest features are limited on older models.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-11-dual", "Dual camera system",
         "The 12MP Wide and Ultra Wide cameras let you switch between a standard shot and a 120° view that fits in "
         "far more of the scene, ideal for landscapes, buildings and group photos."),
        ("feat-11-night", "Night mode",
         "In dim light, Night mode turns on by itself and brightens the picture while keeping colours natural, with "
         "no flash needed. Deep Fusion adds fine detail in medium light."),
        ("feat-11-video", "4K video, front and back",
         "Both the rear and front cameras record 4K video at up to 60fps, and QuickTake lets you start filming "
         "without leaving photo mode."),
        ("feat-11-a13", "A13 Bionic chip",
         "The same chip as the iPhone 11 Pro runs apps, games and photo editing smoothly, and Apple still supports "
         "the phone with iOS 27."),
        ("feat-11-battery", "All-day battery",
         "Up to 17 hours of video playback, an hour more than the iPhone XR. With an 18W or higher adapter it "
         "fast-charges to about 50% in around 30 minutes."),
        ("feat-11-colours", "Six colours, tough build",
         "Choose from Black, White, Green, Yellow, Purple or (PRODUCT)RED. The aluminium frame and glass front and "
         "back are rated IP68 for water and dust, to depths of 2 metres."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's a great choice if you want a reliable, good-looking iPhone with a capable camera and strong battery "
        "life at a sensible price, or a first iPhone for a family member. Upgrading from an iPhone XR, 8 or older, "
        "you'll notice the better camera, Night mode and speed.",
        "If you want an OLED screen and a telephoto lens, the iPhone 11 Pro and 11 Pro Max are the step up. For 5G, "
        "USB-C or Apple Intelligence you'll need a newer model. Not sure which suits you? Ask in any of our stores "
        "and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-11-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-11-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-11-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-11-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-11-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-11-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-11-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-11-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 11
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's iPhone 11 tech specs):
  - "Memory: 64GB, 128GB, 256GB" relabelled "Storage".
  - Screen name made consistent: Apple calls it "Liquid Retina HD" (LCD); the old copy used two names.
  - "Improved water resistance" made specific: IP68 to 2 metres (the XR was IP67 to 1 metre).
  - "Strong battery life" made specific: up to 17 hours video, 1 hour more than the XR.
  - "Tougher glass" kept as "glass front and back"; Apple's 2019 "toughest glass" claim is dated, so not repeated.
  - "Night Mode" lower-cased to Apple's "Night mode"; "click here" link given descriptive anchor text.
  - Added: iOS 27 support, LCD vs OLED, no Apple Intelligence, 4G not 5G, Lightning/Qi, full spec list.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Night Liquid Retina Bionic Apple LCD OLED".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "") + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {P}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>",
              "<strong>Dual camera magic and all-day battery.</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have an {P}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 11", "Apple", "iPhone 11",
             "Apple iPhone 11 with a 6.1-inch Liquid Retina HD display, dual 12MP camera with Night mode and the A13 "
             "Bionic chip, in six colours. 60-point quality checked by CrC Repair® with a two-year warranty and a free "
             "Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = [("Black", "black"), ("White", "white"), ("Green", "green"), ("Yellow", "yellow"),
           ("Purple", "purple"), ("(PRODUCT)RED", "(PRODUCT)RED")]
images = [(f"Main image: {c}", f"Apple iPhone 11 in {c}, front and back view",
           f"The iPhone 11 in {c}, with a 6.1-inch Liquid Retina display and dual camera.") for c, _ in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 11 dual camera with Wide and Ultra Wide lenses",
     "The dual 12MP camera on the iPhone 11, with Night mode and a 120° Ultra Wide lens."),
    ("Screen on, front", "iPhone 11 6.1-inch Liquid Retina display switched on",
     "The 6.1-inch Liquid Retina HD screen of the iPhone 11, with True Tone."),
    ("Bottom and Lightning port", "Bottom edge of the iPhone 11 with Lightning port and speakers",
     "The Lightning charging port and stereo speaker grilles on the bottom of the iPhone 11."),
    ("In the box", "Apple iPhone 11 with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 11 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 11", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 11 with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

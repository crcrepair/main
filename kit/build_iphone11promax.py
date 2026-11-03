"""iPhone 11 Pro Max — long + short description, schema and SEO pack, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-11-pro-max"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 11 Pro Max"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-11-pro-max/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-11-Pro-Max"   # ❓ pattern from the iPhone 15 Pro link; confirm

META_TITLE = "Buy iPhone 11 Pro Max | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 11 Pro Max with a 6.5-inch Super Retina XDR screen, triple camera and A13 Bionic. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 11 Pro Max: big screen, triple camera, 2-year warranty"
OG_DESC = "6.5-inch Super Retina XDR screen, Night mode triple camera, up to 20 hours of video. Fully checked and covered for two years."
X_TITLE = "iPhone 11 Pro Max with a 2-year warranty | CrC Repair®"
X_DESC = "Triple camera, 6.5-inch XDR screen, up to 20 hours of video. 60-point checked, free Device MOT every 6 months."

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-11promax-box", "What comes with the iPhone 11 Pro Max?",
     "The phone comes with a charging cable as standard. If you need a plug, screen protector, case or wireless "
     "charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount is applied automatically "
     "in the basket on selected accessories."),
    ("faq-11promax-ios", "Does the iPhone 11 Pro Max still get iOS updates?",
     "Yes. Apple supports the iPhone 11 Pro Max with iOS 27. Some newer iOS features need more recent hardware, and "
     "Apple Intelligence is only available on the iPhone 15 Pro and later."),
    ("faq-11promax-5g", "Does the iPhone 11 Pro Max support 5G?",
     "No. It uses fast 4G LTE, which works on every UK network, and Wi-Fi 6 for quick home and office "
     "connections. For 5G you would need an iPhone 12 or later."),
    ("faq-11promax-wireless", "Can I charge it wirelessly?",
     "Yes. It works with standard Qi wireless chargers. It has no MagSafe magnets, so magnetic MagSafe accessories "
     "won't attach. With the cable and an 18W or higher adapter it fast-charges to about 50% in around 30 minutes."),
    ("faq-11promax-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers on one phone. Ask us if "
     "you'd like to confirm the network status of a specific handset."),
    ("faq-11promax-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-11promax-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 256GB · 512GB"),
    ("Colours", "Midnight Green, Space Grey, Silver and Gold"),
    ("Display", "6.5-inch Super Retina XDR (OLED) · 2688 × 1242 · 458 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A13 Bionic · third-generation Neural Engine"),
    ("Rear cameras", "Triple 12MP: Wide, Ultra Wide and Telephoto"),
    ("Zoom", "2x optical zoom in and out (4x optical range) · up to 10x digital zoom"),
    ("Photography", "Night mode · Deep Fusion · Smart HDR · Portrait mode"),
    ("Video", "4K up to 60fps · extended dynamic range · slo-mo"),
    ("Front camera", "12MP TrueDepth · 4K video · Face ID"),
    ("Build", "Stainless steel frame · textured matte glass back · 226g"),
    ("Water and dust", "IP68 (up to 4 metres for 30 minutes)"),
    ("Battery", "Up to 20 hours video playback (up to 5 hours longer than iPhone XS Max)"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (18W adapter) · Qi wireless"),
    ("Connectivity", "4G LTE · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — big screen, triple camera", [
        f"Together with the iPhone 11 Pro, the <strong>{P}</strong> was the first iPhone with a triple-camera system "
        "and Apple's Super Retina XDR display, here on a big 6.5-inch screen. Inside is the A13 Bionic chip, and Apple still "
        "supports it with iOS 27.",
        "Compared with the iPhone XS Max it lasts up to five hours longer on a charge, its screen is noticeably "
        "brighter, and it adds an ultra-wide camera and Night mode for low-light photos. The stainless steel frame, "
        "textured matte glass back and IP68 rating make it a tough, premium phone, and it comes with a "
        "<strong>charging cable</strong> as standard.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Lightning, not USB-C.</strong> It charges through Apple's Lightning port, so your existing Lightning "
        "cables and accessories fit. Standard Qi wireless chargers work, but there are no MagSafe magnets.",
        "<strong>4G, not 5G.</strong> It runs on fast 4G LTE and Wi-Fi 6, which covers everyday use on every UK network. "
        "5G arrived with the iPhone 12.",
        "<strong>No Apple Intelligence.</strong> The phone is supported by iOS 27, but Apple Intelligence needs an "
        "iPhone 15 Pro or later, and some of the newest iOS features are limited on older models.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-11promax-triple", "Triple camera system",
         "Wide, Ultra Wide and Telephoto lenses, all 12MP, give you a 4x optical zoom range. Step back for a sweeping "
         "landscape or zoom in for a portrait without moving."),
        ("feat-11promax-night", "Night mode and Deep Fusion",
         "Night mode switches on automatically in low light for brighter, cleaner photos without a flash. Deep Fusion "
         "brings out fine texture and detail in indoor and mid-light shots."),
        ("feat-11promax-display", "6.5-inch Super Retina XDR",
         "A large OLED screen with deep blacks and up to 800 nits of brightness, rising to 1,200 nits for HDR video. "
         "It's easy to read outdoors and great for films and games."),
        ("feat-11promax-battery", "Battery that lasts",
         "Up to 20 hours of video playback, up to five hours more than the iPhone XS Max. Fast charging takes it to "
         "about 50% in around half an hour with an 18W adapter."),
        ("feat-11promax-a13", "A13 Bionic chip",
         "Apple's A13 Bionic keeps apps, photos and games running smoothly, and the phone is still supported by "
         "iOS 27 for security updates and new features."),
        ("feat-11promax-build", "Built to last",
         "A surgical-grade stainless steel frame and textured matte glass back give it a premium feel. "
         "IP68 water resistance covers depths of up to 4 metres for 30 minutes."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It suits you if you want a big, bright screen and a genuinely good triple camera without paying for a "
        "newer model. It's a clear step up from an iPhone XS Max, X or 8 Plus, with better battery life, Night mode "
        "and the ultra-wide lens.",
        "If you need 5G, USB-C or Apple Intelligence, or want the longest possible run of future iOS updates, a newer "
        "model such as the iPhone 15 Pro Max is the better fit. Not sure which suits you? Ask in any of our stores and "
        "we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-11promax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-11promax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-11promax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-11promax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-11promax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-11promax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-11promax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-11promax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 11 Pro Max
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's iPhone 11 Pro Max tech specs):
  - "Memory: 64GB, 256GB, 512GB" relabelled "Storage" (storage options, not memory).
  - "Click here" accessories link given descriptive anchor text; links normalised to https://www.crcrepair.co.uk.
  - "Enhanced screen brightness" made specific: 800 nits typical, 1,200 nits HDR.
  - Added: iOS 27 support, no Apple Intelligence, 4G not 5G, Lightning/Qi (no MagSafe), full spec list.
  - Kept from the old copy: charging cable included as standard; 15% accessory discount applied in the basket.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Network status: are these handsets unlocked? The copy doesn't claim they are.
  3. Battery health: show a minimum (or the actual %) on listings? Older phones get asked about this most.

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Night Deep Fusion Super Retina XDR".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

# ---- short description (from the approved template)
t = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "") + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {P}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>",
              "<strong>Max power. Max display. Max Pro.</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have an {P}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

# ---- schema
build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 11 Pro Max", "Apple", "iPhone 11 Pro Max",
             "Apple iPhone 11 Pro Max with a 6.5-inch Super Retina XDR display, triple 12MP camera with Night "
             "mode and the A13 Bionic chip. 60-point quality checked by CrC Repair® with a two-year warranty and a free "
             "Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

# ---- SEO pack
seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 11 Pro Max", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 11 Pro Max with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], [
    ("Main image: Midnight Green", "Apple iPhone 11 Pro Max in Midnight Green, front and back view",
     "The iPhone 11 Pro Max in Midnight Green, showing the 6.5-inch display and the triple camera on the matte glass back."),
    ("Main image: Space Grey", "Apple iPhone 11 Pro Max in Space Grey, front and back view",
     "The iPhone 11 Pro Max in Space Grey, with its stainless steel frame and textured matte glass back."),
    ("Main image: Silver", "Apple iPhone 11 Pro Max in Silver, front and back view",
     "The iPhone 11 Pro Max in Silver, a pre-owned phone checked by CrC Repair® before sale."),
    ("Main image: Gold", "Apple iPhone 11 Pro Max in Gold, front and back view",
     "The iPhone 11 Pro Max in Gold, with a 6.5-inch Super Retina XDR display and A13 Bionic chip."),
    ("Camera close-up", "Close-up of the iPhone 11 Pro Max triple camera: Wide, Ultra Wide and Telephoto lenses",
     "The triple 12MP camera system on the iPhone 11 Pro Max, with a 4x optical zoom range and Night mode."),
    ("Screen on, front", "iPhone 11 Pro Max 6.5-inch Super Retina XDR display switched on",
     "The 6.5-inch OLED Super Retina XDR screen, up to 800 nits typical and 1,200 nits for HDR."),
    ("Side and buttons", "Side view of the iPhone 11 Pro Max showing the stainless steel frame and buttons",
     "The stainless steel frame of the iPhone 11 Pro Max, with the side button and volume controls."),
    ("Bottom and Lightning port", "Bottom edge of the iPhone 11 Pro Max with Lightning port and speakers",
     "The Lightning charging port and speaker grilles on the bottom edge of the iPhone 11 Pro Max."),
    ("In the box", "Apple iPhone 11 Pro Max with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 11 Pro Max with a charging cable included as standard."),
], notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the row that matches each photo's colour and angle, and delete the rest.",
    "SEOPress: SEO title and meta description go in Titles &amp; metas; the Facebook and X fields go in the Social tab.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm it matches your booking system.",
])
print("built all four files")

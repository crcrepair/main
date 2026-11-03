"""iPhone 14 — long + short description, schema, SEO pack and tags, from the approved template.
No old description supplied: copy written fresh from Apple's specs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-14"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 14"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-14/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-14"   # ❓ pattern from the iPhone 15 Pro link; confirm
TAGLINE = "Brilliant camera. All-day battery. Safety built in."   # ❓ written by Claude (no old copy supplied)

META_TITLE = "Buy iPhone 14 | 5G, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 14 with 5G, a 6.1-inch Super Retina XDR screen, Crash Detection and the A15 Bionic. 60-point "
             "checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 14: 5G, great camera and Crash Detection, 2-year warranty"
OG_DESC = "Low-light camera with Action mode, 5G, MagSafe and Emergency SOS via satellite. Fully checked and covered for two years."
X_TITLE = "iPhone 14 with a 2-year warranty | CrC Repair®"
X_DESC = "5G, a 6.1-inch OLED screen and up to 20 hours of video. 60-point checked, free Device MOT every 6 months."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 14 series", "Model family. Links the iPhone 14, 14 Plus, 14 Pro and 14 Pro Max listings."),
    ("iPhone 14", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("5G", "Connectivity. The iPhone 14 is 5G; older iPhone 11 listings carry 4G."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-14-box", "What comes with the iPhone 14?",
     "It comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, see our "
     + L(ACCESSORIES, "phone accessories") + ". The 15% discount on selected accessories is applied automatically "
     "in the basket."),
    ("faq-14-vs-13", "What's the difference between the iPhone 14 and iPhone 13?",
     "The iPhone 14 has a bigger main camera sensor with a brighter f/1.5 lens, autofocus on the front camera, "
     "Action mode for steady video, Crash Detection and Emergency SOS via satellite. Its A15 Bionic has a 5-core GPU "
     "(the iPhone 13's has 4), and battery life is slightly longer."),
    ("faq-14-ios", "Is the iPhone 14 still supported by Apple?",
     "Yes. Apple supports the iPhone 14 with iOS 27. Apple Intelligence isn't available on it, though, as it needs "
     "an iPhone 15 Pro or later."),
    ("faq-14-magsafe", "Does the iPhone 14 work with MagSafe?",
     "Yes. MagSafe chargers attach magnetically and charge at up to 15W, and MagSafe cases and wallets snap on. "
     "Standard Qi wireless chargers work too, at up to 7.5W."),
    ("faq-14-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-14-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-14-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Midnight, Starlight, Blue, Purple, Yellow and (PRODUCT)RED"),
    ("Display", "6.1-inch Super Retina XDR (OLED) · 2532 × 1170 · 460 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A15 Bionic · 6-core CPU · 5-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Dual 12MP: Main (ƒ/1.5, sensor-shift stabilisation) and Ultra Wide"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Photonic Engine · Night mode · Smart HDR 4 · Portrait mode"),
    ("Video", "4K up to 60fps · Cinematic mode in 4K · Action mode · Dolby Vision HDR"),
    ("Front camera", "12MP TrueDepth with autofocus · Face ID"),
    ("Build", "Aluminium frame · Ceramic Shield front · 172g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 20 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Crash Detection · Emergency SOS via satellite"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — 5G, a sharper camera and safety features", [
        f"The <strong>{P}</strong> pairs a bright 6.1-inch Super Retina XDR screen with a much-improved camera: a "
        "larger main sensor and Apple's Photonic Engine make low-light photos clearer, and Action mode keeps handheld "
        "video smooth even when you're running. The A15 Bionic chip keeps everything fast, and Apple supports it "
        "with iOS 27.",
        "It's also the iPhone that introduced <strong>Crash Detection</strong> and <strong>Emergency SOS via "
        "satellite</strong>, which can contact help after a serious car crash or when you've no signal. Add 5G, "
        "MagSafe and up to 20 hours of video playback, and it's an easy phone to live with every day.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Lightning, not USB-C.</strong> The iPhone 14 charges through Apple's Lightning port; USB-C arrived "
        "with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>60Hz screen, no Always-On.</strong> The display is sharp and bright, but the faster 120Hz ProMotion "
        "and Always-On features are only on the iPhone 14 Pro models.",
        "<strong>No Apple Intelligence.</strong> Apple supports the iPhone 14 with iOS 27, but Apple Intelligence "
        "needs an iPhone 15 Pro or later.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-14-camera", "Better low-light camera",
         "The 12MP main camera has a larger sensor and a bright ƒ/1.5 lens, and the Photonic Engine processes "
         "photos earlier for more detail and truer colour, especially indoors and at night."),
        ("feat-14-action", "Action mode video",
         "Action mode smooths out shake and bumps, so walking, running or cycling footage looks steady without a "
         "gimbal. Cinematic mode adds film-style focus effects in 4K."),
        ("feat-14-safety", "Crash Detection and satellite SOS",
         "If you're in a severe car crash, the iPhone 14 can detect it and call the emergency services. Where there's "
         "no mobile or Wi-Fi signal, Emergency SOS via satellite can still send a message for help."),
        ("feat-14-selfie", "Autofocus front camera",
         "The TrueDepth camera gains autofocus, so selfies and video calls stay sharp, including group shots and "
         "low-light selfies."),
        ("feat-14-a15", "A15 Bionic with 5-core GPU",
         "The same A15 Bionic chip as the iPhone 13 Pro, with a 5-core GPU for smooth gaming and editing. Apple "
         "supports the iPhone 14 with iOS 27."),
        ("feat-14-battery", "Battery and MagSafe",
         "Up to 20 hours of video playback, with fast charging to around 50% in 30 minutes using a 20W adapter. "
         "MagSafe chargers and accessories snap neatly into place."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It suits you if you want a modern 5G iPhone with a really good camera, strong battery life and peace-of-mind "
        "safety features, without paying for the latest model. Coming from an iPhone 11 or older, the jump in photo "
        "quality, 5G and Crash Detection is easy to notice.",
        "If you want a 120Hz ProMotion screen, a telephoto camera or USB-C, look at the iPhone 14 Pro or iPhone 15 "
        "models. For Apple Intelligence you'll need an iPhone 15 Pro or later. Not sure which suits you? Ask in any "
        "of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-14-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-14-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-14-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-14-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-14-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-14-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-14-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, "
         "our technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-14-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 14
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

SOURCE: no old description was supplied and the live page couldn't be read, so this copy is written fresh from
Apple's iPhone 14 specifications. The short-description tagline is new: "{TAGLINE}"

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Box contents: copy says "a charging cable as standard", as on your iPhone 11 listings. Confirm for the 14.
  3. Tagline: keep "{TAGLINE}" or use your own?
  4. Colours: lists all six Apple colours, including Yellow. Trim to the colours you actually stock.
  5. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Crash Detection SOS Action GPU Bionic Apple MagSafe".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 14", "Apple", "iPhone 14",
             "Apple iPhone 14 with 5G, a 6.1-inch Super Retina XDR display, dual 12MP camera with Photonic Engine and "
             "Action mode, Crash Detection and the A15 Bionic chip. 60-point quality checked by CrC Repair® with a "
             "two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Midnight", "Starlight", "Blue", "Purple", "Yellow", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone 14 in {c}, front and back view",
           f"The iPhone 14 in {c}, with a 6.1-inch Super Retina XDR display and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 14 dual camera with Main and Ultra Wide lenses",
     "The dual 12MP camera on the iPhone 14, with a large ƒ/1.5 main sensor, Photonic Engine and Action mode."),
    ("Screen on, front", "iPhone 14 6.1-inch Super Retina XDR display switched on",
     "The 6.1-inch OLED Super Retina XDR screen of the iPhone 14, up to 1,200 nits for HDR."),
    ("MagSafe", "iPhone 14 with a MagSafe charger attached to the back",
     "MagSafe charging on the iPhone 14, at up to 15W with magnetic alignment."),
    ("In the box", "Apple iPhone 14 with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 14 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 14", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 14 with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old description was supplied, so all copy is new. The short-description tagline is mine: please approve or replace it.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

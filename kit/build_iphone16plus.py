"""iPhone 16 Plus — long + short description, schema, SEO pack and tags, from the approved template.
No old description supplied: copy written fresh from Apple's UK specs."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-16-plus"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 16 Plus"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-16-plus/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-16-Plus"   # ❓ pattern from the iPhone 15 Pro link; confirm
TAGLINE = "Big screen. Bigger battery. Apple Intelligence."   # ❓ written by Claude (no old copy supplied)

META_TITLE = "Buy iPhone 16 Plus | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 16 Plus: 6.7-inch screen, up to 27 hours of video, A18 chip and Apple Intelligence. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 16 Plus: big screen, 27-hour battery, 2-year warranty"
OG_DESC = "A 6.7-inch screen, Apple Intelligence, Camera Control and up to 27 hours of video. Fully checked and covered for two years."
X_TITLE = "iPhone 16 Plus with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch screen, 27-hour battery and Apple Intelligence. 60-point checked, free Device MOT every 6 months."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 16 series", "Model family. Links the iPhone 16e, 16, 16 Plus, 16 Pro and 16 Pro Max listings."),
    ("iPhone 16 Plus", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-16plus-box", "What comes with the iPhone 16?",
     "It comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, take a look "
     "at our " + L(ACCESSORIES, "phone accessories") + ". The 15% discount on selected accessories comes off "
     "automatically in the basket."),
    ("faq-16plus-camera-control", "What is Camera Control?",
     "Camera Control is a touch-sensitive button on the side of the iPhone 16 Plus. Press it to open the camera, press "
     "again to take a photo, and slide your finger along it to zoom or change settings. It also opens Visual "
     "Intelligence, which tells you about whatever you point the camera at."),
    ("faq-16plus-vs-16", "What's the difference between the iPhone 16 Plus and iPhone 16?",
     "They share the same A18 chip, cameras, Camera Control and Apple Intelligence. The 16 Plus has a larger "
     "6.7-inch screen (the iPhone 16 is 6.1-inch) and a bigger battery, with up to 27 hours of video playback "
     "against 22. It's heavier, at 199g against 170g."),
    ("faq-16plus-vs-15plus", "What's the difference between the iPhone 16 Plus and iPhone 15 Plus?",
     "The 16 Plus has the faster A18 chip and supports Apple Intelligence, which the 15 Plus doesn't. It adds Camera "
     "Control, the Action button, macro photos and spatial video, faster 25W MagSafe charging and Wi-Fi 7, and its "
     "battery lasts a little longer: up to 27 hours of video against 26."),
    ("faq-16plus-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-16plus-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-16plus-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Black, White, Pink, Teal and Ultramarine"),
    ("Display", "6.7-inch Super Retina XDR (OLED) · 2796 × 1290 · 460 ppi · Dynamic Island"),
    ("Brightness", "1,000 nits typical · 1,600 nits HDR · 2,000 nits outdoors"),
    ("Chip", "A18 · 6-core CPU · 5-core GPU · 16-core Neural Engine"),
    ("Apple Intelligence", "Supported"),
    ("Main camera", "48MP Fusion · ƒ/1.6 · sensor-shift stabilisation · 2x optical-quality telephoto"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120° · autofocus with macro photography"),
    ("Photography", "Spatial photos · Photonic Engine · Night mode · up to 10x digital zoom"),
    ("Video", "4K Dolby Vision up to 60fps · Cinematic mode · Action mode · spatial video · Audio Mix"),
    ("Front camera", "12MP TrueDepth with autofocus · Face ID"),
    ("Buttons", "Camera Control · Action button"),
    ("Build", "Aluminium frame · Ceramic Shield front · 199g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 27 hours video playback"),
    ("Charging", "USB-C (USB 2) · fast charging with a 20W or higher adapter · MagSafe and Qi2 up to 25W"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Emergency SOS via satellite · Crash Detection"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — big screen, longest battery", [
        f"The <strong>{P}</strong> gives you everything in the iPhone 16 on a larger 6.7-inch Super Retina XDR "
        "screen, with a bigger battery to match: up to 27 hours of video playback. It's built for "
        "<strong>Apple Intelligence</strong>, with the A18 chip running Apple's AI features for writing, photo "
        "editing, image creation and a more helpful Siri.",
        "<strong>Camera Control</strong> puts shooting, zooming and settings under your thumb, the 48MP Fusion "
        "camera adds a 2x telephoto option, and the Ultra Wide focuses close enough for macro shots. You also get the "
        "Dynamic Island, the Action button, 25W MagSafe charging and Wi-Fi 7.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>It's a big phone.</strong> The 6.7-inch screen and 199g weight are great for films, games and "
        "reading, but it's best used with two hands. The iPhone 16 has the same features in a 6.1-inch size.",
        "<strong>60Hz screen, no Always-On.</strong> 120Hz ProMotion and the Always-On display are only on the iPhone "
        "16 Pro models.",
        "<strong>2x zoom, no telephoto lens.</strong> The 2x option comes from the 48MP main sensor; 5x optical zoom "
        "is on the iPhone 16 Pro Max. Wired USB-C transfers also run at USB 2 speed.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-16plus-ai", "Apple Intelligence",
         "Writing Tools rewrite and summarise your text, Clean Up removes distractions from photos, Image Playground "
         "and Genmoji create images, and Siri understands more. New features arrive with iOS updates."),
        ("feat-16plus-camera-control", "Camera Control",
         "A touch-sensitive button that opens the camera, takes the shot and lets you slide to zoom or adjust exposure. "
         "It also launches Visual Intelligence to look things up through the camera."),
        ("feat-16plus-cameras", "48MP Fusion and macro",
         "The main camera shoots 24MP or 48MP photos and a 2x telephoto crop. The Ultra Wide adds autofocus, so you "
         "can get crisp close-ups of flowers, food and fine detail."),
        ("feat-16plus-screen", "6.7-inch Super Retina XDR",
         "A big, bright OLED screen with the Dynamic Island, up to 2,000 nits outdoors and 1,600 nits for HDR. Ideal "
         "for films, games, maps and split-screen-style multitasking."),
        ("feat-16plus-a18", "A18 chip",
         "Faster than the iPhone 15's chip, with a 5-core GPU for smooth gaming and plenty of headroom for Apple "
         "Intelligence. Apple supports the phone with iOS 27."),
        ("feat-16plus-battery", "27-hour battery",
         "Up to 27 hours of video playback, five more than the iPhone 16. MagSafe and Qi2 chargers charge at up to "
         "25W, and USB-C fast-charges with a 20W or higher adapter."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It suits you if you want a large screen and the longest battery life of the standard iPhone 16 models, plus "
        "Apple Intelligence and Camera Control. It's a natural upgrade from an older Plus or Max model, or from any "
        "iPhone that struggles to last the day.",
        "If you'd prefer something easier to use one-handed, the iPhone 16 has the same features in a 6.1-inch size. "
        "For a 120Hz screen or a 5x telephoto, look at the iPhone 16 Pro Max. Not sure which suits you? Ask in any of "
        "our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-16plus-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-16plus-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-16plus-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-16plus-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-16plus-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-16plus-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-16plus-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-16plus-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 16 Plus
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

SOURCE: no old description was supplied, so this copy is written fresh from Apple's iPhone 16 specs
and UK carrier specs for the Plus (6.7-inch, 199g, up to 27 hours video).
Storage lists the launch options (128/256/512GB); Apple now sells new units in 128GB only.
The short-description tagline is new: "{TAGLINE}"

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Box contents: copy says "a charging cable as standard", as on your other iPhone listings. Confirm.
  3. Tagline: keep "{TAGLINE}" or use your own?
  4. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence Camera Control Fusion MagSafe Dynamic Island Spatial Audio Mix".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 16 Plus", "Apple", "iPhone 16 Plus",
             "Apple iPhone 16 Plus with a 6.7-inch Super Retina XDR display, up to 27 hours of video playback, the A18 chip, "
             "Apple Intelligence, Camera Control and a 48MP Fusion camera with macro-capable Ultra Wide. 60-point quality checked by "
             "CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Pink", "Teal", "Ultramarine"]
images = [(f"Main image: {c}", f"Apple iPhone 16 Plus in {c}, front and back view",
           f"The iPhone 16 Plus in {c}, with a 6.7-inch display, Dynamic Island and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 16 Plus vertical dual camera with 48MP Fusion and Ultra Wide lenses",
     "The vertically stacked 48MP Fusion and 12MP Ultra Wide cameras on the iPhone 16 Plus, with macro photography."),
    ("Camera Control", "Side of the iPhone 16 Plus showing the Camera Control button",
     "Camera Control on the iPhone 16 Plus: press to take a photo, slide to zoom or adjust settings."),
    ("Screen on, front", "iPhone 16 Plus 6.7-inch Super Retina XDR display with Dynamic Island switched on",
     "The large 6.7-inch OLED screen of the iPhone 16 Plus, up to 2,000 nits outdoors, with the Dynamic Island."),
    ("Apple Intelligence on screen", "iPhone 16 Plus showing Apple Intelligence Writing Tools on screen",
     "Apple Intelligence on the iPhone 16 Plus, with Writing Tools helping to rewrite and summarise text."),
    ("In the box", "Apple iPhone 16 Plus with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 16 Plus with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 16 Plus", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 16 Plus with Apple Intelligence, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old description was supplied, so all copy is new. The short-description tagline is mine: please approve or replace it.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

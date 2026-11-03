"""iPhone 16 Pro — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-16-pro"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 16 Pro"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-16-pro/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-16-Pro"   # ❓ pattern from the iPhone 15 Pro link; confirm
TAGLINE = "Larger screen, smarter camera, smarter you."

META_TITLE = "Buy iPhone 16 Pro | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 16 Pro with A18 Pro, Apple Intelligence, 5x telephoto, 4K 120fps video and a 6.3-inch "
             "ProMotion screen. 60-point checked, 2-year warranty.")
OG_TITLE = "iPhone 16 Pro: 5x zoom, 4K 120fps video, 2-year warranty"
OG_DESC = "A18 Pro, Apple Intelligence, Camera Control and a 48MP triple camera in titanium. Fully checked and covered for two years."
X_TITLE = "iPhone 16 Pro with a 2-year warranty | CrC Repair®"
X_DESC = "A18 Pro, 5x telephoto, 4K 120fps Dolby Vision and Apple Intelligence. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 16 series", "Model family. Links the iPhone 16e, 16, 16 Plus, 16 Pro and 16 Pro Max listings."),
    ("iPhone 16 Pro", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-16pro-box", "What comes with the iPhone 16 Pro?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-16pro-vs-15pro", "What's the difference between the iPhone 16 Pro and iPhone 15 Pro?",
     "The 16 Pro has a slightly larger 6.3-inch screen (the 15 Pro is 6.1-inch), the faster A18 Pro chip, Camera "
     "Control, a 5x telephoto camera instead of 3x, a 48MP Ultra Wide, 4K video at 120fps, four studio-quality "
     "microphones and longer battery life: up to 27 hours of video against 23. Both support Apple Intelligence."),
    ("faq-16pro-vs-16", "Is the iPhone 16 Pro worth it over the iPhone 16?",
     "Choose the Pro if you want a 120Hz ProMotion screen with Always-On, the 5x telephoto camera, 4K 120fps and "
     "ProRes video, USB 3 transfers and a titanium build. The iPhone 16 shares Apple Intelligence and Camera "
     "Control but has a 60Hz screen and two cameras."),
    ("faq-16pro-camera-control", "What is Camera Control?",
     "Camera Control is a touch-sensitive button on the side of the iPhone 16 Pro. Press to open the camera and take "
     "photos, slide to zoom or adjust exposure, and use it to open Visual Intelligence for information about what's "
     "in front of you."),
    ("faq-16pro-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-16pro-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-16pro-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB · 1TB"),
    ("Colours", "Black, White, Natural and Desert Titanium"),
    ("Display", "6.3-inch Super Retina XDR (OLED) · 2622 × 1206 · 460 ppi · Dynamic Island"),
    ("Refresh rate", "ProMotion up to 120Hz · Always-On display"),
    ("Brightness", "1,000 nits typical · 1,600 nits HDR · 2,000 nits outdoors"),
    ("Chip", "A18 Pro · 6-core CPU · 6-core GPU · 16-core Neural Engine"),
    ("Apple Intelligence", "Supported"),
    ("Main camera", "48MP Fusion · ƒ/1.78 · second-generation sensor-shift stabilisation · 2x option"),
    ("Ultra Wide camera", "48MP · ƒ/2.2 · 120° · 48MP macro photography"),
    ("Telephoto camera", "12MP · 5x optical zoom (120mm) · tetraprism · 3D sensor-shift stabilisation"),
    ("Zoom range", "0.5x, 1x, 2x and 5x optical-quality · up to 25x digital"),
    ("Video", "4K Dolby Vision up to 120fps · ProRes and Log · spatial video · Audio Mix · four studio-quality mics"),
    ("Front camera", "12MP TrueDepth with autofocus · Face ID"),
    ("Buttons", "Camera Control · Action button"),
    ("Build", "Titanium frame · latest-generation Ceramic Shield front · 199g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 27 hours video playback"),
    ("Charging", "USB-C · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe and Qi2 up to 25W"),
    ("Data transfer", "USB 3 up to 10Gb/s (with a USB 3 cable)"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Emergency SOS via satellite · Crash Detection"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — bigger screen, 5x zoom, 4K 120fps", [
        f"The <strong>{P}</strong> grows the Pro screen to 6.3 inches with slimmer borders, and runs on the "
        "<strong>A18 Pro</strong> chip with full support for <strong>Apple Intelligence</strong>. The titanium frame "
        "keeps it strong, and the ProMotion display is smooth at up to 120Hz with an Always-On option.",
        "Its camera system is a real step up: a 48MP Fusion main camera, a new 48MP Ultra Wide for detailed macro "
        "shots, and a 5x telephoto. Video reaches 4K at 120fps in Dolby Vision, and four studio-quality microphones "
        "capture clear sound. <strong>Camera Control</strong>, the Action button, Wi-Fi 7 and up to 27 hours of video "
        "playback complete the package.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>4K, not 8K.</strong> Video tops out at 4K, at up to 120fps in Dolby Vision, which is smoother than "
        "most phones manage, but it doesn't record 8K.",
        "<strong>A little heavier.</strong> At 199g it's 12g heavier than the iPhone 15 Pro, because of the larger "
        "screen and battery.",
        "<strong>No power adapter.</strong> It comes with a charging cable. For 25W MagSafe charging you'll need a "
        "MagSafe charger and a 30W adapter.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-16pro-cameras", "48MP triple camera with 5x zoom",
         "Fusion, Ultra Wide and Telephoto lenses cover 0.5x to 5x. The 48MP Ultra Wide captures detailed macro shots, "
         "and the 5x tetraprism telephoto, previously Pro Max only, gets you close from far away."),
        ("feat-16pro-video", "4K 120fps Dolby Vision",
         "Record 4K at 120 frames per second for smooth slow motion you can adjust after filming. ProRes and Log "
         "recording, spatial video and Audio Mix suit creators and pros."),
        ("feat-16pro-ai", "Apple Intelligence on A18 Pro",
         "Writing Tools, Clean Up, Image Playground, Genmoji and a smarter Siri run on the A18 Pro, which also handles "
         "demanding games with hardware ray tracing."),
        ("feat-16pro-control", "Camera Control",
         "Press to launch the camera and capture, slide to zoom or change exposure, and open Visual Intelligence to "
         "identify places, plants and more."),
        ("feat-16pro-display", "6.3-inch ProMotion display",
         "A larger screen with the thinnest borders on any iPhone at launch, refresh rates up to 120Hz, an Always-On "
         "mode and brightness that drops to 1 nit for night-time reading."),
        ("feat-16pro-battery", "Longer battery and fast USB 3",
         "Up to 27 hours of video playback, four more than the iPhone 15 Pro. MagSafe charges at up to 25W, and USB-C "
         "moves files at up to 10Gb/s with a USB 3 cable."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a Pro camera with 5x zoom and pro video in a size that's still comfortable "
        "to hold, plus Apple Intelligence and a smooth 120Hz screen. Coming from an iPhone 13 Pro, 14 Pro or older, "
        "you'll see a big jump in zoom, video and battery life.",
        "If you want the largest screen and longest battery, the iPhone 16 Pro Max is the one to look at. If you don't "
        "need ProMotion or the telephoto, the iPhone 16 offers Apple Intelligence and Camera Control for less. Not sure "
        "which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-16pro-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-16pro-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-16pro-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-16pro-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-16pro-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-16pro-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-16pro-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-16pro-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 16 Pro
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple and UK carrier specs):
  - "cinematic 8K video" was WRONG: the iPhone 16 Pro records up to 4K at 120fps (Dolby Vision). Fixed.
  - "lighter and tougher than ever" was WRONG: at 199g it's 12g HEAVIER than the 15 Pro (187g). Now states the weight.
  - "dedicated Capture button" renamed to Apple's name, "Camera Control".
  - Screen size made consistent at 6.3-inch (the old copy said both 6.27" and 6.3").
  - "Better improved AI-powered camera" made specific: 48MP Ultra Wide, 5x telephoto (15 Pro had 3x), 4K 120fps.
  - "Memory" relabelled "Storage"; "customizable" to British spelling; "click here" given descriptive anchor text.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence Camera Control Fusion MagSafe Dynamic Island ProMotion Dolby Vision A18 USB 4K SIM Please".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 16 Pro", "Apple", "iPhone 16 Pro",
             "Apple iPhone 16 Pro with a 6.3-inch ProMotion Super Retina XDR display, A18 Pro chip, Apple Intelligence, "
             "Camera Control and a 48MP triple camera with 5x telephoto and 4K 120fps Dolby Vision video, in titanium. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black Titanium", "White Titanium", "Natural Titanium", "Desert Titanium"]
images = [(f"Main image: {c}", f"Apple iPhone 16 Pro in {c}, front and back view",
           f"The iPhone 16 Pro in {c}, with a 6.3-inch ProMotion display and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 16 Pro triple camera: 48MP Fusion, 48MP Ultra Wide and 5x Telephoto",
     "The iPhone 16 Pro triple camera, with a 48MP Fusion main camera, 48MP Ultra Wide and 5x tetraprism telephoto."),
    ("Camera Control", "Side of the iPhone 16 Pro showing the Camera Control button",
     "Camera Control on the iPhone 16 Pro: press to capture, slide to zoom or adjust exposure."),
    ("Screen on, front", "iPhone 16 Pro 6.3-inch Super Retina XDR display with Dynamic Island switched on",
     "The 6.3-inch ProMotion OLED screen of the iPhone 16 Pro, with Always-On and up to 2,000 nits outdoors."),
    ("Apple Intelligence on screen", "iPhone 16 Pro showing Apple Intelligence Writing Tools on screen",
     "Apple Intelligence on the iPhone 16 Pro, with Writing Tools helping to rewrite and summarise text."),
    ("In the box", "Apple iPhone 16 Pro with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 16 Pro with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 16 Pro", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 16 Pro in titanium with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

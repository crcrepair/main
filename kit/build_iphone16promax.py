"""iPhone 16 Pro Max — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-16-pro-max"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 16 Pro Max"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-16-pro-max/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-16-Pro-Max"   # ❓ pattern from the iPhone 15 Pro link; confirm
TAGLINE = "A new era of intelligence and interaction."

META_TITLE = "Buy iPhone 16 Pro Max | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 16 Pro Max with A18 Pro, Apple Intelligence, a 6.9-inch 120Hz screen, 5x zoom and "
             "up to 33 hours of video. 60-point checked, 2-year warranty.")
OG_TITLE = "iPhone 16 Pro Max: 6.9-inch screen, 33-hour battery"
OG_DESC = "The biggest iPhone screen, A18 Pro, Apple Intelligence and a 5x telephoto. Fully checked and covered for two years."
X_TITLE = "iPhone 16 Pro Max with a 2-year warranty | CrC Repair®"
X_DESC = "6.9-inch ProMotion screen, 5x zoom, 4K 120fps video and up to 33 hours of video playback. Free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 16 series", "Model family. Links the iPhone 16e, 16, 16 Plus, 16 Pro and 16 Pro Max listings."),
    ("iPhone 16 Pro Max", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-16promax-box", "What comes with the iPhone 16 Pro Max?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-16promax-vs-15promax", "What's the difference between the iPhone 16 Pro Max and iPhone 15 Pro Max?",
     "The 16 Pro Max has a larger 6.9-inch screen (the 15 Pro Max is 6.7-inch), the faster A18 Pro chip, Camera "
     "Control, a 48MP Ultra Wide (up from 12MP), 4K video at 120fps, four studio-quality microphones and longer "
     "battery life: up to 33 hours of video against 29. Both have a 5x telephoto camera and support Apple "
     "Intelligence."),
    ("faq-16promax-vs-16pro", "Should I choose the iPhone 16 Pro Max or the iPhone 16 Pro?",
     "They share the same chip, cameras, Camera Control and video features. The Pro Max adds a larger 6.9-inch "
     "screen and the longest battery life of the two, up to 33 hours of video against 27, but it's bigger and "
     "heavier at 227g against 199g. Storage on the Pro Max starts at 256GB."),
    ("faq-16promax-camera-control", "What is Camera Control?",
     "Camera Control is a touch-sensitive button on the side of the iPhone 16 Pro Max. Press to open the camera and "
     "take photos, slide to zoom or adjust exposure, and use it to open Visual Intelligence for information about "
     "what's in front of you."),
    ("faq-16promax-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-16promax-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-16promax-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "256GB · 512GB · 1TB"),
    ("Colours", "Black, White, Natural and Desert Titanium"),
    ("Display", "6.9-inch Super Retina XDR (OLED) · 2868 × 1320 · 460 ppi · Dynamic Island"),
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
    ("Build", "Titanium frame · latest-generation Ceramic Shield front · 227g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 33 hours video playback"),
    ("Charging", "USB-C · fast charge to 50% in about 35 minutes (20W adapter) · MagSafe and Qi2 up to 25W"),
    ("Data transfer", "USB 3 up to 10Gb/s (with a USB 3 cable)"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Emergency SOS via satellite · Crash Detection"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — biggest screen, longest battery", [
        f"The <strong>{P}</strong> has the largest display Apple had put on an iPhone at launch: 6.9 inches, with "
        "slimmer borders so the phone itself grows only a little. It runs on the <strong>A18 Pro</strong> chip with "
        "full support for <strong>Apple Intelligence</strong>, and its titanium frame and 120Hz ProMotion display "
        "with Always-On make it the flagship of the iPhone 16 range.",
        "Battery life is its headline: up to 33 hours of video playback, the longest of any iPhone at launch. The "
        "camera system pairs a 48MP Fusion main camera with a new 48MP Ultra Wide for macro shots and a 5x telephoto. "
        "Video reaches 4K at 120fps in Dolby Vision, and <strong>Camera Control</strong>, the Action button and Wi-Fi 7 "
        "complete the package.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Big and heavy.</strong> At 227g and 163mm tall it's the largest iPhone 16. If you'd rather have "
        "the same cameras in a smaller phone, the iPhone 16 Pro is 199g.",
        "<strong>Same 5x zoom as the 15 Pro Max.</strong> The 5x telephoto isn't new on the Pro Max. Coming from a 15 "
        "Pro Max, the upgrades are the larger screen, Camera Control, the 48MP Ultra Wide, 4K 120fps video and battery "
        "life.",
        "<strong>No power adapter.</strong> It comes with a charging cable. For 25W MagSafe charging you'll need a "
        "MagSafe charger and a 30W adapter.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-16promax-display", "6.9-inch ProMotion display",
         "The biggest iPhone screen at launch, with the thinnest borders, refresh rates up to 120Hz, an Always-On mode "
         "and brightness that drops to 1 nit for night-time reading."),
        ("feat-16promax-battery", "Up to 33 hours of video",
         "The longest battery life of any iPhone at launch, four hours more than the iPhone 15 Pro Max. MagSafe charges "
         "at up to 25W, and USB-C moves files at up to 10Gb/s with a USB 3 cable."),
        ("feat-16promax-cameras", "48MP triple camera with 5x zoom",
         "Fusion, Ultra Wide and Telephoto lenses cover 0.5x to 5x. The new 48MP Ultra Wide captures detailed macro "
         "shots, and the 5x tetraprism telephoto gets you close from far away."),
        ("feat-16promax-video", "4K 120fps Dolby Vision",
         "Record 4K at 120 frames per second for smooth slow motion you can adjust after filming. ProRes and Log "
         "recording, spatial video and Audio Mix suit creators and pros."),
        ("feat-16promax-ai", "Apple Intelligence on A18 Pro",
         "Writing Tools, Clean Up, Image Playground, Genmoji and a smarter Siri run on the A18 Pro, which also handles "
         "demanding games with hardware ray tracing."),
        ("feat-16promax-control", "Camera Control",
         "Press to launch the camera and capture, slide to zoom or change exposure, and open Visual Intelligence to "
         "identify places, plants and more."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the biggest screen for video, games and reading, battery life that easily "
        "lasts a long day, and Pro cameras with 5x zoom and 4K 120fps video. Coming from an iPhone 13 Pro Max, 14 Pro "
        "Max or older, you'll see a big jump in screen size, video and battery life.",
        "If you'd like the same cameras and chip in a phone that's easier to use one-handed, the iPhone 16 Pro is the "
        "one to look at. If you don't need ProMotion or the telephoto, the iPhone 16 Plus gives you a large screen, "
        "Apple Intelligence and Camera Control for less. Not sure which suits you? Ask in any of our stores and we'll "
        "talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-16promax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-16promax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-16promax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-16promax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-16promax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-16promax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-16promax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-16promax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 16 Pro Max
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was pre-launch rumour ("Expected to feature", "Likely to introduce", "is rumoured"). Rewritten
    as fact: the phone is out and every feature is confirmed.
  - "Smart Capture" doesn't exist on this phone. Removed.
  - "dedicated Capture button" renamed to Apple's name, "Camera Control".
  - "advanced periscope zoom" listed as new: the 5x tetraprism telephoto was already on the iPhone 15 Pro Max.
    Now stated plainly, and flagged in "Before you buy".
  - "upgraded Siri with on-device processing" and "improved night shots" were vague. Replaced with specifics:
    Apple Intelligence features, the 48MP Ultra Wide (15 Pro Max had 12MP), 4K 120fps video, 33-hour battery.
  - "Screen size: 6.9\\" ... OLED" kept; resolution, ppi and brightness added.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.

SOURCES: apple.com and support.apple.com were blocked from this session's network, so figures were checked
  against Apple's launch figures as reported (33 h video / 29 h on the 15 Pro Max, 227g, 2868 × 1320 at 460 ppi,
  25W MagSafe with a 30W adapter) and match the iPhone 16 Pro page for shared hardware. Worth a final glance
  against support.apple.com/en-gb/121032 before publishing.

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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 16 Pro Max", "Apple", "iPhone 16 Pro Max",
             "Apple iPhone 16 Pro Max with a 6.9-inch ProMotion Super Retina XDR display, A18 Pro chip, Apple Intelligence, "
             "Camera Control, up to 33 hours of video playback and a 48MP triple camera with 5x telephoto and 4K 120fps "
             "Dolby Vision video, in titanium. 60-point quality checked by CrC Repair® with a two-year warranty and a "
             "free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black Titanium", "White Titanium", "Natural Titanium", "Desert Titanium"]
images = [(f"Main image: {c}", f"Apple iPhone 16 Pro Max in {c}, front and back view",
           f"The iPhone 16 Pro Max in {c}, with a 6.9-inch ProMotion display and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 16 Pro Max triple camera: 48MP Fusion, 48MP Ultra Wide and 5x Telephoto",
     "The iPhone 16 Pro Max triple camera, with a 48MP Fusion main camera, 48MP Ultra Wide and 5x tetraprism telephoto."),
    ("Camera Control", "Side of the iPhone 16 Pro Max showing the Camera Control button",
     "Camera Control on the iPhone 16 Pro Max: press to capture, slide to zoom or adjust exposure."),
    ("Screen on, front", "iPhone 16 Pro Max 6.9-inch Super Retina XDR display with Dynamic Island switched on",
     "The 6.9-inch ProMotion OLED screen of the iPhone 16 Pro Max, with Always-On and up to 2,000 nits outdoors."),
    ("Apple Intelligence on screen", "iPhone 16 Pro Max showing Apple Intelligence Writing Tools on screen",
     "Apple Intelligence on the iPhone 16 Pro Max, with Writing Tools helping to rewrite and summarise text."),
    ("In the box", "Apple iPhone 16 Pro Max with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 16 Pro Max with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 16 Pro Max", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 16 Pro Max in titanium with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

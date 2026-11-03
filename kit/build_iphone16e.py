"""iPhone 16e — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-16e"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 16e"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-16e/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-16e"   # ❓ pattern from the iPhone 15 Pro link; confirm
TAGLINE = "Compact powerhouse, premium AI in your pocket."

META_TITLE = "Buy iPhone 16e | Apple Intelligence | CrC Repair®"
META_DESC = ("Buy an iPhone 16e with the A18 chip, Apple Intelligence, a 48MP camera and up to 26 hours of video. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 16e: Apple Intelligence, huge battery, 2-year warranty"
OG_DESC = "A18 chip, Apple Intelligence, a 48MP Fusion camera and up to 26 hours of video playback. Fully checked, two-year cover."
X_TITLE = "iPhone 16e with a 2-year warranty | CrC Repair®"
X_DESC = "Apple Intelligence on a budget: A18 chip, 48MP camera, 26-hour battery. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 16 series", "Model family. Links the iPhone 16e, 16, 16 Plus, 16 Pro and 16 Pro Max listings."),
    ("iPhone 16e", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. ❓ Use your own wording (Pre-owned or Refurbished) and keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-16e-box", "What comes with the iPhone 16e?",
     "The phone comes with a charging cable as standard. If you need a plug, screen protector, case or wireless "
     "charger, browse our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories "
     "is applied automatically in the basket."),
    ("faq-16e-ai", "What can Apple Intelligence do on the iPhone 16e?",
     "Apple Intelligence brings Writing Tools to rewrite, proofread and summarise text, Clean Up to remove "
     "distractions from photos, Image Playground and Genmoji for creating images, notification summaries and a "
     "more capable Siri. New features arrive with iOS updates."),
    ("faq-16e-vs-15", "What's the difference between the iPhone 16e and iPhone 15?",
     "The 16e has the newer A18 chip, supports Apple Intelligence (the iPhone 15 doesn't), adds the Action button "
     "and lasts much longer, with up to 26 hours of video against 20. The iPhone 15 keeps a few extras: the "
     "Dynamic Island, an ultra-wide camera and MagSafe. Both use USB-C."),
    ("faq-16e-vs-16", "What's the difference between the iPhone 16e and iPhone 16?",
     "Both run Apple Intelligence on an A18 chip. The iPhone 16 adds an ultra-wide camera, the Dynamic Island, "
     "MagSafe and Camera Control. The 16e has a single 48MP camera and a notch, but its battery lasts longer, up "
     "to 26 hours of video against the iPhone 16's 22."),
    ("faq-16e-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers. 5G runs on Apple's own "
     "C1 modem. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-16e-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-16e-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Black and White"),
    ("Display", "6.1-inch Super Retina XDR (OLED) · 2532 × 1170 · 460 ppi · notch"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A18 · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Apple Intelligence", "Supported"),
    ("Rear camera", "48MP Fusion camera with 2x optical-quality telephoto"),
    ("Photography", "Photonic Engine · Night mode · Smart HDR 5 · Portrait mode"),
    ("Video", "4K up to 60fps · Dolby Vision HDR"),
    ("Front camera", "12MP TrueDepth with autofocus · Face ID"),
    ("Buttons", "Action button"),
    ("Build", "Aluminium frame · Ceramic Shield front · 167g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 26 hours video playback"),
    ("Charging", "USB-C · fast charge to 50% in about 30 minutes (20W adapter) · Qi wireless up to 7.5W · no MagSafe"),
    ("Connectivity", "5G (Apple C1 modem) · Wi-Fi 6 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Emergency SOS via satellite · Crash Detection"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — Apple Intelligence and all-day battery", [
        f"The <strong>{P}</strong> is the most affordable way into the iPhone 16 family. It runs the same "
        "<strong>A18 chip</strong> as the iPhone 16 and supports <strong>Apple Intelligence</strong>, Apple's "
        "built-in AI for rewriting text, cleaning up photos, creating images and a smarter Siri.",
        "Its battery is the standout, with up to 26 hours of video playback, more than the standard iPhone 16. You "
        "also get a sharp 48MP camera with 2x zoom, a 6.1-inch OLED screen, USB-C, the Action button and 5G through "
        "Apple's own C1 modem, all in a clean, minimalist design.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>One rear camera.</strong> The 48MP Fusion camera covers standard and 2x shots, but there's no "
        "ultra-wide lens, so you can't take wide-angle or macro photos.",
        "<strong>No MagSafe.</strong> Standard Qi wireless chargers work at up to 7.5W, but MagSafe chargers won't "
        "align magnetically or charge at full speed. USB-C handles everyday charging.",
        "<strong>Notch, not Dynamic Island.</strong> The screen keeps the classic notch, and there's no Camera "
        "Control button or Action mode video, which are on the iPhone 16.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-16e-ai", "Apple Intelligence",
         "Rewrite and summarise text with Writing Tools, remove distractions with Clean Up, create images with Image "
         "Playground and Genmoji, and get more help from Siri, all built into the phone."),
        ("feat-16e-battery", "Battery that keeps going",
         "Up to 26 hours of video playback, more than the iPhone 16. Fast charging over USB-C reaches about 50% in "
         "around 30 minutes with a 20W adapter."),
        ("feat-16e-a18", "A18 chip",
         "The A18 is fast and efficient, keeping games, photo editing and Apple Intelligence running smoothly, and "
         "Apple supports the phone with iOS 27."),
        ("feat-16e-camera", "48MP Fusion camera",
         "One camera does two jobs: detailed 24MP and 48MP photos as standard, and a 2x telephoto crop for "
         "close-ups and portraits at optical quality."),
        ("feat-16e-action", "Action button",
         "Swap the mute switch for a programmable button. Use it for silent mode, the camera, the torch, a Focus mode, "
         "translation or your own Shortcut."),
        ("feat-16e-c1", "5G on Apple's C1 modem",
         "The 16e debuted Apple's first in-house modem, designed for fast, power-efficient 5G. Add USB-C and IP68 "
         "water resistance, and it's ready for everyday life."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's ideal if you want Apple Intelligence, a long-lasting battery and a modern iPhone without paying for "
        "extras you might not use. It's a big step up from an iPhone 11, 12 or 13, especially in battery life and "
        "everyday speed.",
        "If an ultra-wide camera, MagSafe or the Dynamic Island matter to you, the iPhone 16 is the better match. Not "
        "sure which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-16e-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-16e-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-16e-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-16e-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-16e-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-16e-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-16e-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-16e-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 16e
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against UK carrier specs and Apple's own feature notes):
  - "iPhone 16e vs iPhone 15: Dynamic Island, USB-C port, better camera" was WRONG and has been replaced. The 16e
    has a notch (no Dynamic Island), the iPhone 15 already has USB-C, and the 15 has an extra ultra-wide camera.
    The real differences are now in an FAQ: A18 chip, Apple Intelligence, Action button, much longer battery.
  - "Apple's most affordable 2025 model" removed (dated). Now "the most affordable way into the iPhone 16 family".
  - "Memory" relabelled "Storage"; "premium AI in you pocket" typo fixed to "your" in the short description.
  - "Click here" link given descriptive anchor text.
  - Kept the old copy's honest points: no MagSafe and no ultra-wide camera, now in "Before you buy".
  - Added: 26-hour battery figure, C1 modem, no Camera Control or Action mode video, iPhone 16 comparison.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED} (pattern from the iPhone 15 Pro). Please confirm.
  2. Condition wording for the tag: Pre-owned or Refurbished?

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence Action Fusion C1 MagSafe Dynamic Island".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 16e", "Apple", "iPhone 16e",
             "Apple iPhone 16e with the A18 chip, Apple Intelligence, a 48MP Fusion camera with 2x telephoto, a 6.1-inch "
             "Super Retina XDR display and up to 26 hours of video playback. 60-point quality checked by CrC Repair® "
             "with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

images = [(f"Main image: {c}", f"Apple iPhone 16e in {c}, front and back view",
           f"The iPhone 16e in {c}, with a 6.1-inch OLED display and a single 48MP Fusion camera.") for c in ("Black", "White")]
images += [
    ("Camera close-up", "Close-up of the iPhone 16e 48MP Fusion camera",
     "The single 48MP Fusion camera on the iPhone 16e, with a 2x optical-quality telephoto option."),
    ("Screen on, front", "iPhone 16e 6.1-inch Super Retina XDR display switched on",
     "The 6.1-inch OLED Super Retina XDR screen of the iPhone 16e."),
    ("Apple Intelligence on screen", "iPhone 16e showing Apple Intelligence Writing Tools on screen",
     "Apple Intelligence on the iPhone 16e, with Writing Tools helping to rewrite and proofread text."),
    ("Side and Action button", "Side view of the iPhone 16e showing the Action button",
     "The programmable Action button on the side of the iPhone 16e."),
    ("Bottom and USB-C port", "Bottom edge of the iPhone 16e with USB-C port and speakers",
     "The USB-C charging port and speaker grilles on the bottom of the iPhone 16e."),
    ("In the box", "Apple iPhone 16e with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 16e with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 16e", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 16e with Apple Intelligence, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm.",
], tags=TAGS)
print("built")

"""iPhone 13 mini — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-13-mini"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 13 mini"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-13-mini/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-13-mini"   # ❓ pattern confirmed; capitalisation of "mini" not confirmed
TAGLINE = "All-day power in your pocket."

META_TITLE = "Buy iPhone 13 mini | 5G, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy a compact iPhone 13 mini with 5G, a 5.4-inch OLED screen, the A15 Bionic and Cinematic mode. "
             "60-point checked, 2-year warranty and free Device MOT.")
OG_TITLE = "iPhone 13 mini: full power, pocket size, 2-year warranty"
OG_DESC = "A15 Bionic, 5G, a dual 12MP camera and Cinematic mode in a 140g phone. Fully checked and covered for two years."
X_TITLE = "iPhone 13 mini with a 2-year warranty | CrC Repair®"
X_DESC = "Pocket-sized 5G iPhone with the A15 Bionic and Cinematic mode. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 13 series", "Model family. Links the iPhone 13 mini, 13, 13 Pro and 13 Pro Max listings."),
    ("iPhone 13 mini", "Exact model, matching how people search. Apple writes \"mini\" in lower case."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-13mini-box", "What comes with the iPhone 13 mini?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-13mini-vs-12mini", "What's the difference between the iPhone 13 mini and iPhone 12 mini?",
     "The 13 mini has the faster A15 Bionic chip (the 12 mini has the A14), longer battery life of up to 17 hours of "
     "video against 15, Cinematic mode, Photographic Styles and sensor-shift stabilisation on the main camera. Its "
     "screen is brighter, the notch is smaller, and storage starts at 128GB instead of 64GB."),
    ("faq-13mini-vs-13", "Should I choose the iPhone 13 mini or the iPhone 13?",
     "They share the same A15 Bionic chip, cameras and features. The iPhone 13 has a larger 6.1-inch screen and "
     "longer battery life, up to 19 hours of video against 17. The mini is the one to pick if you want a phone "
     "that's easy to use one-handed: it's 5.4 inches and weighs 140g, against 173g."),
    ("faq-13mini-ios", "Is the iPhone 13 mini still supported by Apple?",
     "Yes. Apple supports the iPhone 13 mini with iOS 27. Apple Intelligence isn't available on it, though, as it "
     "needs an iPhone 15 Pro or later."),
    ("faq-13mini-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-13mini-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-13mini-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB"),
    ("Colours", "Pink, Blue, Midnight, Starlight, Green and (PRODUCT)RED"),
    ("Display", "5.4-inch Super Retina XDR (OLED) · 2340 × 1080 · 476 ppi"),
    ("Brightness", "800 nits typical · 1,200 nits HDR"),
    ("Chip", "A15 Bionic · 6-core CPU · 4-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Dual 12MP: Main (ƒ/1.6, sensor-shift stabilisation) and Ultra Wide (ƒ/2.4, 120°)"),
    ("Zoom", "2x optical zoom out · up to 5x digital zoom"),
    ("Photography", "Photographic Styles · Night mode · Smart HDR 4 · Portrait mode"),
    ("Video", "4K up to 60fps · Cinematic mode (1080p at 30fps) · Dolby Vision HDR"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Aluminium frame · Ceramic Shield front · 140g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 17 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (20W adapter) · MagSafe and Qi wireless charging"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — full iPhone power in a pocket-sized phone", [
        f"The <strong>{P}</strong> fits a 5.4-inch Super Retina XDR screen into a phone that weighs just 140g, so it "
        "sits comfortably in one hand and slips into any pocket. Inside is the same <strong>A15 Bionic</strong> chip as "
        "the full-size iPhone 13, and Apple supports it with iOS 27.",
        "You get the same dual 12MP camera as the iPhone 13 too, with sensor-shift stabilisation, Photographic Styles "
        "and <strong>Cinematic mode</strong> for film-style focus effects in video. Add 5G, MagSafe, a Ceramic Shield "
        "front and up to 17 hours of video playback, and it's a small phone that doesn't cut corners.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Smaller screen, smaller battery.</strong> Up to 17 hours of video is good for its size, but the "
        "iPhone 13 lasts longer (up to 19 hours). If you watch a lot of video or play games, a bigger phone may suit "
        "you better.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 13 mini charges through Apple's Lightning port; USB-C "
        "arrived with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>No Apple Intelligence or Crash Detection.</strong> Apple supports it with iOS 27, but Apple "
        "Intelligence needs an iPhone 15 Pro or later, and Crash Detection arrived with the iPhone 14.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-13mini-size", "Truly one-handed",
         "At 131.5mm tall and 140g, it's easy to use with one thumb and disappears into a pocket, while the edge-to-edge "
         "OLED screen still gives you a 5.4-inch display."),
        ("feat-13mini-a15", "A15 Bionic",
         "The same chip as the full-size iPhone 13, so apps, games and photo editing run just as quickly on the mini. "
         "Apple supports it with iOS 27."),
        ("feat-13mini-cinematic", "Cinematic mode",
         "Record video with a shallow depth of field that shifts focus automatically between people, and change the "
         "focus after you've filmed."),
        ("feat-13mini-camera", "Dual 12MP camera",
         "The main camera has sensor-shift stabilisation for steadier photos and video, Night mode works on both "
         "cameras, and Photographic Styles let you set the look you like."),
        ("feat-13mini-battery", "Longer battery than the 12 mini",
         "Up to 17 hours of video playback, two more than the iPhone 12 mini, with fast charging to around 50% in "
         "30 minutes using a 20W adapter."),
        ("feat-13mini-tough", "5G, MagSafe and IP68",
         "5G for fast downloads, MagSafe chargers and accessories that snap into place, and a Ceramic Shield front with "
         "IP68 water and dust resistance."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a modern 5G iPhone that's genuinely small: easy to use one-handed, light in "
        "a pocket, and without giving up the chip or cameras of the full-size model. Coming from an iPhone SE, 12 mini "
        "or older, you'll notice the faster chip, better camera and longer battery.",
        "If battery life matters most, the iPhone 13 has a bigger screen and battery. If you want USB-C, look at the "
        "iPhone 15 or later, and for Apple Intelligence you'll need an iPhone 15 Pro or later. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-13mini-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-13mini-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-13mini-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-13mini-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-13mini-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-13mini-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-13mini-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-13mini-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 13 mini
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - "iPhone 13 Mini" written as Apple names it: "iPhone 13 mini" (lower-case m), including the tag.
  - "vs 12 Mini: Longer battery, Cinematic Mode" was correct but thin. Now specific: A15 vs A14, 17 vs 15 hours
    of video, Cinematic mode, Photographic Styles, sensor-shift stabilisation, 128GB base storage.
  - Added what the old copy left out: Lightning (not USB-C), iOS 27 support, no Apple Intelligence or
    Crash Detection, full spec list.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct (Green was added in March 2022).

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (5.4-inch, 2340 × 1080 at 476 ppi, 140g, 17 h video, Bluetooth 5.0) and the
  iOS 27 compatibility list (iPhone 11 and later). MagSafe wattage is left out on purpose: Apple's spec sheet
  says up to 15W, but the mini models are limited to 12W in practice, so no figure is safer.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Is "mini" lower case in your booking system,
     or "iPhone-13-Mini"?
  2. Tagline kept from the old copy: "{TAGLINE}"

CONFIRMED BY GABOR (3 Nov 2026): condition tag "Pre-owned"; booking link pattern repairs/Apple/<Model>.

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Cinematic Photographic Styles SIM Please MP IP68".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 13 mini", "Apple", "iPhone 13 mini",
             "Apple iPhone 13 mini with 5G, a 5.4-inch Super Retina XDR display, the A15 Bionic chip, a dual 12MP camera "
             "with sensor-shift stabilisation and Cinematic mode, and MagSafe, in a 140g body. 60-point quality checked "
             "by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Pink", "Blue", "Midnight", "Starlight", "Green", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone 13 mini in {c}, front and back view",
           f"The iPhone 13 mini in {c}, with a 5.4-inch Super Retina XDR display and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 13 mini dual camera with Main and Ultra Wide lenses",
     "The dual 12MP camera on the iPhone 13 mini, with sensor-shift stabilisation and Cinematic mode."),
    ("In the hand", "iPhone 13 mini held in one hand, showing its compact size",
     "The iPhone 13 mini in the hand: a 5.4-inch screen in a 140g phone that's easy to use one-handed."),
    ("Screen on, front", "iPhone 13 mini 5.4-inch Super Retina XDR display switched on",
     "The 5.4-inch OLED Super Retina XDR screen of the iPhone 13 mini, up to 1,200 nits for HDR."),
    ("In the box", "Apple iPhone 13 mini with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 13 mini with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 13 mini", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 13 mini with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm whether \"mini\" is lower case in the booking system.",
], tags=TAGS)
print("built")

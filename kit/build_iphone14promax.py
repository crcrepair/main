"""iPhone 14 Pro Max — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-14-pro-max"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 14 Pro Max"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-14-pro-max/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-14-Pro-Max"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "The best just got better."

META_TITLE = "Buy iPhone 14 Pro Max | 48MP, 29h Battery | CrC Repair®"
META_DESC = ("Buy an iPhone 14 Pro Max with a 6.7-inch Always-On screen, Dynamic Island, 48MP camera and a 29-hour "
             "battery. 60-point checked, 2-year warranty, free MOT.")
OG_TITLE = "iPhone 14 Pro Max: 48MP camera, Dynamic Island, 29-hour battery"
OG_DESC = "The biggest iPhone 14, with a 48MP camera, Always-On ProMotion display, Dynamic Island and a 29-hour battery. 2-year cover."
X_TITLE = "iPhone 14 Pro Max with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch Always-On screen, Dynamic Island, 48MP camera with 3x zoom, 29-hour battery. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 14 series", "Model family. Links the iPhone 14, 14 Plus, 14 Pro and 14 Pro Max listings."),
    ("iPhone 14 Pro Max", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-14promax-box", "What comes with the iPhone 14 Pro Max?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-14promax-vs-13promax", "What's the difference between the iPhone 14 Pro Max and iPhone 13 Pro Max?",
     "The 14 Pro Max replaces the notch with the Dynamic Island, adds an Always-On display that's brighter outdoors "
     "(2,000 nits against 1,200), a 48MP main camera in place of 12MP with a 2x option, the faster A16 Bionic chip, "
     "Action mode video, Crash Detection and Emergency SOS via satellite. Battery life is up to 29 hours of video "
     "against 28. Both have the 3x telephoto and 120Hz ProMotion."),
    ("faq-14promax-vs-14pro", "Should I choose the iPhone 14 Pro Max or the iPhone 14 Pro?",
     "They share the same chip, cameras, Dynamic Island and Always-On display. The Pro Max has a larger 6.7-inch "
     "screen and the longest battery of the two, up to 29 hours of video against 23, but it's bigger and heavier at "
     "240g against 206g. Pick the Max for screen and battery, the Pro for one-handed use."),
    ("faq-14promax-island", "What is the Dynamic Island?",
     "The Dynamic Island is the pill-shaped area at the top of the screen that replaces the notch. It expands to show "
     "what's happening in the background: music, timers, directions, calls and Live Activities such as a food delivery, "
     "so you can glance or tap without leaving the app you're in."),
    ("faq-14promax-ios", "Is the iPhone 14 Pro Max still supported by Apple?",
     "Yes. Apple supports the iPhone 14 Pro Max with iOS 27. Apple Intelligence isn't available on it, though, as it "
     "needs an iPhone 15 Pro or later."),
    ("faq-14promax-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-14promax-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB · 1TB"),
    ("Colours", "Space Black, Silver, Gold and Deep Purple"),
    ("Display", "6.7-inch Super Retina XDR (OLED) · 2796 × 1290 · 460 ppi · Dynamic Island"),
    ("Refresh rate", "ProMotion, adaptive from 1Hz to 120Hz · Always-On display"),
    ("Brightness", "1,000 nits typical · 1,600 nits HDR · 2,000 nits outdoors"),
    ("Chip", "A16 Bionic · 6-core CPU · 5-core GPU · 16-core Neural Engine"),
    ("Main camera", "48MP · ƒ/1.78 · second-generation sensor-shift stabilisation · 2x option (12MP, 48mm)"),
    ("Ultra Wide camera", "12MP · ƒ/2.2 · 120° · macro photography"),
    ("Telephoto camera", "12MP · 3x optical zoom (77mm) · ƒ/2.8"),
    ("Zoom range", "0.5x, 1x, 2x and 3x optical-quality · up to 15x digital"),
    ("Photography", "Photonic Engine · Night mode · ProRAW at 48MP · Smart HDR 4 · LiDAR scanner"),
    ("Video", "4K up to 60fps · Action mode · Cinematic mode in 4K · ProRes · Dolby Vision HDR"),
    ("Front camera", "12MP TrueDepth with autofocus · Face ID"),
    ("Build", "Stainless steel frame · Ceramic Shield front · 240g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 29 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 35 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.3 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Safety", "Crash Detection · Emergency SOS via satellite"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — Dynamic Island, 48MP camera, longest battery", [
        f"The <strong>{P}</strong> was the top iPhone of 2022, and it introduced two things that defined the Pro line "
        "since: the <strong>Dynamic Island</strong>, which replaces the notch with a live area for alerts and "
        "activities, and the <strong>Always-On display</strong>, which shows the time and widgets while the screen is "
        "locked. The 6.7-inch ProMotion screen reaches 2,000 nits outdoors, and the A16 Bionic chip runs it all.",
        "The camera is the first iPhone with a <strong>48MP main sensor</strong>, which gives a 2x option at full "
        "quality and ProRAW at 48MP, alongside a 3x telephoto and an Ultra Wide with macro. Action mode steadies "
        "handheld video, and the battery lasts up to 29 hours of video, the longest of any iPhone at launch. Crash "
        "Detection and Emergency SOS via satellite add peace of mind.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Big and heavy.</strong> At 240g and 160.7mm tall it's the largest and heaviest iPhone 14. If you'd "
        "rather have the same cameras in a phone that's easier to use one-handed, the iPhone 14 Pro is 206g.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 14 Pro Max charges through Apple's Lightning port; USB-C "
        "arrived with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>No Apple Intelligence.</strong> Apple supports the phone with iOS 27, but Apple Intelligence needs "
        "an iPhone 15 Pro or later. Photos are 12MP by default; 48MP needs ProRAW, and those files are large.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-14promax-battery", "Up to 29 hours of video",
         "The longest battery life of any iPhone at launch, six hours more than the iPhone 14 Pro, with fast charging "
         "to around 50% in 35 minutes using a 20W adapter."),
        ("feat-14promax-island", "Dynamic Island and Always-On",
         "The Dynamic Island shows music, timers, calls and Live Activities without leaving your app, and the Always-On "
         "display keeps the time, widgets and wallpaper visible on the lock screen at 1Hz to save power."),
        ("feat-14promax-camera", "48MP main camera",
         "The quad-pixel sensor captures four times the detail for ProRAW, and crops to a 2x view at full quality, so "
         "you get four useful focal lengths: 0.5x, 1x, 2x and 3x."),
        ("feat-14promax-display", "6.7-inch ProMotion display at 2,000 nits",
         "The brightest iPhone screen at launch, readable in direct sunlight, with a refresh rate that adapts from 1Hz "
         "to 120Hz."),
        ("feat-14promax-video", "Action mode and pro video",
         "Action mode smooths out shake and bumps for steady handheld footage, Cinematic mode now records in 4K, and "
         "ProRes and Dolby Vision suit creators."),
        ("feat-14promax-safety", "Crash Detection and satellite SOS",
         "If you're in a severe car crash, the phone can detect it and call the emergency services. Where there's no "
         "mobile or Wi-Fi signal, Emergency SOS via satellite can still send a message for help."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the biggest screen, the longest battery and the 48MP Pro camera at a "
        "pre-owned price, for video, games, photography and editing. Coming from an iPhone 11 Pro Max, 12 Pro Max or "
        "13 Pro Max, you'll notice the Dynamic Island, the Always-On display, the brighter screen and the 2x option.",
        "If you'd like the same cameras in a phone that's easier to use one-handed, the iPhone 14 Pro is the one to "
        "look at. For USB-C and Apple Intelligence, you'll need an iPhone 15 Pro or later, which also adds a 5x "
        "telephoto on the Pro Max. Not sure which suits you? Ask in any of our stores and we'll talk you through the "
        "options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-14promax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-14promax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-14promax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-14promax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-14promax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-14promax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-14promax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-14promax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 14 Pro Max
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was correct (Dynamic Island, 48MP, ProMotion, biggest battery, brighter display, A16). Kept its
    facts and made them specific: 1–120Hz Always-On, 2,000 nits, 2x option, 3x telephoto, 29 vs 28 hours, 240g.
  - "biggest battery" / "best-in-class" / "crown jewel" softened to what's verifiable: "longest of any iPhone at
    launch" (29 h), and "the top iPhone of 2022".
  - "Screen Size", "Special Features" written in sentence case; "Storage" label kept (the old copy already had it).
  - Added what the old copy left out: size and weight warning, Lightning (not USB-C), 48MP needs ProRAW,
    iOS 27 support, no Apple Intelligence, Crash Detection and satellite SOS, a Dynamic Island FAQ, full spec list.
  - "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct.

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.7-inch, 2796 × 1290 at 460 ppi, 240g, 29 h video, 48MP main) and the iOS 27
  compatibility list. The 14 Pro figures quoted in the FAQ (206g, 23 h) are Apple's.

CONFIRMED BY GABOR (3 Nov 2026):
  1. Booking link value: ?selected={BOOKING_SELECTED}
  2. Condition tag: Pre-owned
  3. Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence Crash Detection SOS Bionic MagSafe Lightning USB-C Cinematic Action Photonic Engine Dynamic Island Always-On ProMotion ProRes ProRAW LiDAR Dolby Vision Night Live Activities GPU SIM Please MP IP68 OLED 5G G Hz".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 14 Pro Max", "Apple", "iPhone 14 Pro Max",
             "Apple iPhone 14 Pro Max with a 6.7-inch Always-On ProMotion Super Retina XDR display, Dynamic Island, the "
             "A16 Bionic chip, a 48MP main camera with 3x telephoto, Action mode, Crash Detection and up to 29 hours of "
             "video playback, in stainless steel. 60-point quality checked by CrC Repair® with a two-year warranty and "
             "a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Space Black", "Silver", "Gold", "Deep Purple"]
images = [(f"Main image: {c}", f"Apple iPhone 14 Pro Max in {c}, front and back view",
           f"The iPhone 14 Pro Max in {c}, with a 6.7-inch Always-On display, Dynamic Island and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 14 Pro Max triple camera: 48MP Main, Ultra Wide and 3x Telephoto",
     "The iPhone 14 Pro Max triple camera, with a 48MP main sensor, 12MP Ultra Wide and 3x telephoto."),
    ("Dynamic Island", "iPhone 14 Pro Max showing the Dynamic Island with music playing",
     "The Dynamic Island on the iPhone 14 Pro Max, expanded to show now-playing controls."),
    ("Always-On display", "iPhone 14 Pro Max locked, with the Always-On display showing the time and widgets",
     "The Always-On display of the iPhone 14 Pro Max, dimmed to 1Hz to save battery."),
    ("In the box", "Apple iPhone 14 Pro Max with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 14 Pro Max with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 14 Pro Max", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 14 Pro Max in stainless steel with triple camera and Dynamic Island, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
], tags=TAGS)
print("built")

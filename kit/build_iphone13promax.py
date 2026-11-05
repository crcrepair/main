"""iPhone 13 Pro Max — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-13-pro-max"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone 13 Pro Max"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-13-pro-max/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-13-Pro-Max"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "The biggest and most advanced iPhone of its time."

META_TITLE = "Buy iPhone 13 Pro Max | 120Hz, 28h Battery | CrC Repair®"
META_DESC = ("Buy an iPhone 13 Pro Max with a 6.7-inch 120Hz ProMotion screen, 3x telephoto, macro and a 28-hour "
             "battery. 60-point checked, 2-year warranty, free MOT.")
OG_TITLE = "iPhone 13 Pro Max: 6.7-inch 120Hz screen, 28-hour battery"
OG_DESC = "The biggest iPhone 13, with ProMotion, 3x telephoto, macro and ProRes video, and up to 28 hours of battery. 2-year cover."
X_TITLE = "iPhone 13 Pro Max with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch 120Hz ProMotion screen, triple camera with macro, and up to 28 hours of video. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone 13 series", "Model family. Links the iPhone 13 mini, 13, 13 Pro and 13 Pro Max listings."),
    ("iPhone 13 Pro Max", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-13promax-box", "What comes with the iPhone 13 Pro Max?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or MagSafe charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-13promax-vs-12promax", "What's the difference between the iPhone 13 Pro Max and iPhone 12 Pro Max?",
     "The 13 Pro Max adds a 120Hz ProMotion screen, a 3x telephoto (the 12 Pro Max's is 2.5x), macro photography, "
     "ProRes and Cinematic mode video, a 1TB storage option and much longer battery life: up to 28 hours of video "
     "against 20. Its A15 Bionic chip has a 5-core GPU, and the screen is brighter with a smaller notch."),
    ("faq-13promax-vs-13pro", "Should I choose the iPhone 13 Pro Max or the iPhone 13 Pro?",
     "They share the same chip, cameras, ProMotion screen technology and video features. The Pro Max has a larger "
     "6.7-inch screen and the longest battery of the two, up to 28 hours of video against 22, but it's bigger and "
     "heavier at 240g against 203g. Pick the Max for screen and battery, the Pro for one-handed use."),
    ("faq-13promax-ios", "Is the iPhone 13 Pro Max still supported by Apple?",
     "Yes. Apple supports the iPhone 13 Pro Max with iOS 27. Apple Intelligence isn't available on it, though, as it "
     "needs an iPhone 15 Pro or later."),
    ("faq-13promax-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can use two numbers, and 5G works wherever "
     "your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-13promax-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-13promax-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "128GB · 256GB · 512GB · 1TB"),
    ("Colours", "Graphite, Gold, Silver, Sierra Blue and Alpine Green"),
    ("Display", "6.7-inch Super Retina XDR (OLED) · 2778 × 1284 · 458 ppi"),
    ("Refresh rate", "ProMotion, adaptive from 10Hz to 120Hz"),
    ("Brightness", "1,000 nits typical · 1,200 nits HDR"),
    ("Chip", "A15 Bionic · 6-core CPU · 5-core GPU · 16-core Neural Engine"),
    ("Rear cameras", "Triple 12MP: Wide (ƒ/1.5, sensor-shift stabilisation), Ultra Wide (ƒ/1.8, 120°) and Telephoto (ƒ/2.8)"),
    ("Zoom", "3x optical zoom in · 2x optical zoom out · 6x optical zoom range · up to 15x digital"),
    ("Photography", "Macro photography · Night mode on all cameras · Photographic Styles · Smart HDR 4 · ProRAW · LiDAR scanner"),
    ("Video", "4K up to 60fps · ProRes 4K at 30fps (1080p on the 128GB model) · Cinematic mode · Dolby Vision HDR · macro video"),
    ("Front camera", "12MP TrueDepth · Night mode · Face ID"),
    ("Build", "Stainless steel frame · Ceramic Shield front · 240g"),
    ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
    ("Battery", "Up to 28 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 35 minutes (20W adapter) · MagSafe up to 15W · Qi up to 7.5W"),
    ("Connectivity", "5G · Wi-Fi 6 · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Supported by iOS 27"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the biggest screen and the longest battery", [
        f"The <strong>{P}</strong> is the largest iPhone 13, with a 6.7-inch Super Retina XDR screen that uses "
        "<strong>ProMotion</strong> to adapt from 10Hz to 120Hz, so scrolling and games feel fluid. Its battery is the "
        "headline: up to 28 hours of video playback, the longest of any iPhone at the time. The <strong>A15 Bionic</strong> "
        "has a 5-core GPU, the frame is stainless steel, and Apple supports it with iOS 27.",
        "The cameras are the same as the iPhone 13 Pro: a 3x telephoto, an Ultra Wide that focuses as close as 2cm for "
        "<strong>macro photography</strong>, and Night mode on every lens. Video adds ProRes, Cinematic mode and Dolby "
        "Vision, and storage goes up to 1TB. The big screen makes it the one for editing, gaming and films.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Big and heavy.</strong> At 240g and 160.8mm tall it's the largest and heaviest iPhone 13. If you'd "
        "rather have the same cameras in a phone that's easier to use one-handed, the iPhone 13 Pro is 203g.",
        "<strong>Lightning, not USB-C.</strong> The iPhone 13 Pro Max charges through Apple's Lightning port; USB-C "
        "arrived with the iPhone 15. MagSafe and Qi wireless chargers work as normal.",
        "<strong>ProRes is limited on 128GB, and no Apple Intelligence.</strong> The 128GB model records ProRes at "
        "1080p; 256GB and above record 4K. Apple supports the phone with iOS 27, but Apple Intelligence needs an "
        "iPhone 15 Pro or later.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-13promax-battery", "Up to 28 hours of video",
         "The longest battery life of any iPhone at launch, eight hours more than the iPhone 12 Pro Max, with fast "
         "charging to around 50% in 35 minutes using a 20W adapter."),
        ("feat-13promax-display", "6.7-inch ProMotion display",
         "The biggest iPhone 13 screen, with a refresh rate that adapts from 10Hz to 120Hz and 1,000 nits of brightness "
         "in daylight. Ideal for editing, games and films."),
        ("feat-13promax-telephoto", "3x telephoto camera",
         "A 77mm-equivalent telephoto gets you closer for portraits and detail without digital zoom, giving a 6x "
         "optical zoom range from Ultra Wide to Telephoto."),
        ("feat-13promax-macro", "Macro photography",
         "The Ultra Wide camera focuses from just 2cm, so flowers, textures and small details fill the frame. Macro "
         "works in video too, including slow motion and time-lapse."),
        ("feat-13promax-video", "ProRes and Cinematic mode",
         "Record ProRes for professional editing, use Cinematic mode for film-style focus shifts, and capture Dolby "
         "Vision HDR at 4K 60fps."),
        ("feat-13promax-a15", "A15 Bionic with 5-core GPU",
         "The extra GPU core over the iPhone 13 helps with gaming, 4K editing and ProRes. Storage runs from 128GB to "
         "1TB, and Apple supports the phone with iOS 27."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the biggest screen for video, games and editing, battery life that easily "
        "lasts a long day, and the Pro cameras with telephoto, macro and ProRes. Coming from an iPhone 11 Pro Max, "
        "12 Pro Max or older, you'll notice the smoother screen, better zoom and much longer battery.",
        "If you'd like the same cameras in a phone that's easier to use one-handed, the iPhone 13 Pro is the one to "
        "look at. If you don't need the telephoto or 120Hz, the iPhone 13 gives you the same chip and main camera for "
        "less. For USB-C you'll need an iPhone 15 or later, and for Apple Intelligence an iPhone 15 Pro or later. Not "
        "sure which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-13promax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-13promax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-13promax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-13promax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-13promax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-13promax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-13promax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-13promax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 13 Pro Max
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was correct ("camera upgrades are identical to the 13 Pro, but battery life is even longer").
    Kept its facts and made them specific: 28 vs 22 hours of video (vs 20 on the 12 Pro Max), 240g, 10–120Hz,
    3x telephoto (12 Pro Max was 2.5x), 2cm macro, ProRes 4K (1080p on 128GB).
  - Colours: added Alpine Green, which Apple added in March 2022. The old copy listed four.
  - "vs 12 Pro Max: Longer battery, macro lens, ProMotion 120Hz" kept and expanded in the FAQ.
  - Added what the old copy left out: size and weight warning, Lightning (not USB-C), ProRes storage limit,
    iOS 27 support, no Apple Intelligence or Crash Detection, full spec list.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.7-inch, 2778 × 1284 at 458 ppi, 240g / 8.46 oz, 28 h video, 35-minute fast
  charge) and the iOS 27 compatibility list. Some resellers quote 238g; 240g is Apple's figure.

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
      ok_caps="iPhone Pro Max Apple Intelligence Crash Detection Bionic MagSafe Lightning USB-C Cinematic Photographic Styles ProMotion ProRes ProRAW LiDAR Dolby Vision GPU SIM Please MP IP68 Hz".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone 13 Pro Max", "Apple", "iPhone 13 Pro Max",
             "Apple iPhone 13 Pro Max with a 6.7-inch 120Hz ProMotion Super Retina XDR display, the A15 Bionic chip with "
             "5-core GPU, a triple 12MP camera with 3x telephoto and macro photography, ProRes and Cinematic mode video, "
             "and up to 28 hours of video playback, in stainless steel. 60-point quality checked by CrC Repair® with a "
             "two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Graphite", "Gold", "Silver", "Sierra Blue", "Alpine Green"]
images = [(f"Main image: {c}", f"Apple iPhone 13 Pro Max in {c}, front and back view",
           f"The iPhone 13 Pro Max in {c}, with a 6.7-inch ProMotion display and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone 13 Pro Max triple camera with Wide, Ultra Wide and Telephoto lenses",
     "The triple 12MP camera on the iPhone 13 Pro Max, with 3x telephoto, macro photography and LiDAR scanner."),
    ("Screen on, front", "iPhone 13 Pro Max 6.7-inch ProMotion Super Retina XDR display switched on",
     "The 6.7-inch 120Hz ProMotion OLED screen of the iPhone 13 Pro Max, up to 1,000 nits in daylight."),
    ("Macro shot", "Macro photo taken on the iPhone 13 Pro Max Ultra Wide camera",
     "Macro photography on the iPhone 13 Pro Max: the Ultra Wide camera focuses from as close as 2cm."),
    ("In the box", "Apple iPhone 13 Pro Max with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone 13 Pro Max with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone 13 Pro Max", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone 13 Pro Max in stainless steel with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
], tags=TAGS)
print("built")

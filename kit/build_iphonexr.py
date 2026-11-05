"""iPhone XR — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-xr"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone XR"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-xr/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-XR"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "Bold colours, powerful core."

META_TITLE = "Buy iPhone XR | 6 Colours, 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone XR with a 6.1-inch screen, the A12 Bionic, Face ID and all-day battery, in six colours. "
             "60-point checked, 2-year warranty, free Device MOT.")
OG_TITLE = "iPhone XR: six colours, all-day battery, 2-year warranty"
OG_DESC = "A12 Bionic, a 6.1-inch Liquid Retina screen, Face ID and up to 16 hours of video. Fully checked and covered for two years."
X_TITLE = "iPhone XR with a 2-year warranty | CrC Repair®"
X_DESC = "Six colours, a 6.1-inch screen, Face ID and all-day battery at a budget price. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone X series", "Model family. Links the iPhone X, XR, XS and XS Max listings."),
    ("iPhone XR", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("4G", "Connectivity. The iPhone XR is 4G LTE; 5G arrived with the iPhone 12."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-xr-box", "What comes with the iPhone XR?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-xr-ios", "Is the iPhone XR still supported by Apple?",
     "Partly. The iPhone XR's last major version is iOS 18; it doesn't run iOS 26 or iOS 27, so it won't get new "
     "features. Apple has carried on releasing iOS 18 security updates for it, and all the everyday apps still work. "
     "If you want the latest iOS features, look at the iPhone 11 or newer."),
    ("faq-xr-vs-x", "What's the difference between the iPhone XR and iPhone X?",
     "The XR has a bigger 6.1-inch screen (the X is 5.8-inch), the faster A12 Bionic chip, better battery life, six "
     "colours and a lower price. The X has a sharper OLED screen, a second telephoto camera and a stainless steel "
     "frame. Both have Face ID and wireless charging."),
    ("faq-xr-vs-11", "Should I choose the iPhone XR or the iPhone 11?",
     "They're the same size with the same screen. The 11 adds an Ultra Wide camera, Night mode, the faster A13 chip, "
     "an hour more battery and, most importantly, it still runs the latest iOS. The XR is the cheaper option if you "
     "mainly want calls, messaging, social apps and a good camera in daylight."),
    ("faq-xr-5g", "Does the iPhone XR work with 5G?",
     "No. It uses 4G LTE, which works on every UK network. Apple introduced 5G with the iPhone 12."),
    ("faq-xr-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-xr-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 128GB · 256GB"),
    ("Colours", "Black, White, Blue, Yellow, Coral and (PRODUCT)RED"),
    ("Display", "6.1-inch Liquid Retina HD (LCD) · 1792 × 828 · 326 ppi · True Tone"),
    ("Brightness", "625 nits typical"),
    ("Chip", "A12 Bionic · Neural Engine"),
    ("Rear camera", "Single 12MP Wide · ƒ/1.8 · optical image stabilisation"),
    ("Zoom", "Up to 5x digital zoom"),
    ("Photography", "Portrait mode with Depth Control · Smart HDR · Portrait Lighting (three effects)"),
    ("Video", "4K up to 60fps · 1080p slo-mo at 240fps · extended dynamic range up to 30fps"),
    ("Front camera", "7MP TrueDepth · Portrait mode · Face ID"),
    ("Build", "Aluminium frame · glass front and back · 194g"),
    ("Water and dust", "IP67 (up to 1 metre for 30 minutes)"),
    ("Battery", "Up to 16 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (18W adapter) · Qi wireless"),
    ("Connectivity", "4G LTE · Wi-Fi 5 (802.11ac) · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Last major version iOS 18, with security updates (no iOS 26 or 27)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — six colours, Face ID and all-day battery", [
        f"The <strong>{P}</strong> is the iPhone that brought Face ID and the edge-to-edge screen to a friendlier "
        "price, and it's still one of the best-value ways into a modern-looking iPhone. The 6.1-inch Liquid Retina LCD "
        "is bright and colour-accurate with True Tone, and the <strong>A12 Bionic</strong> chip keeps everyday apps, "
        "messaging and social media quick.",
        "The single 12MP camera takes sharp photos in daylight with Smart HDR and Portrait mode, and records 4K video. "
        "Battery life is up to 16 hours of video, better than the iPhone X and XS it launched alongside. It comes in "
        "<strong>six colours</strong>, with a charging cable as standard.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>No new iOS features.</strong> The iPhone XR's last major version is iOS 18. It still gets Apple's "
        "security updates and runs the everyday apps, but it won't get iOS 26 or 27 features. If staying current "
        "matters, the iPhone 11 is the same size and still supported.",
        "<strong>LCD screen, single camera.</strong> The Liquid Retina LCD is sharp and accurate but lacks the deep "
        "blacks of OLED, and there's one rear camera: no Ultra Wide, no Night mode and no optical zoom.",
        "<strong>Lightning and 4G.</strong> It charges through the Lightning port (Qi wireless works too, without "
        "MagSafe magnets) and connects over 4G LTE rather than 5G. Water resistance is IP67, to 1 metre.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-xr-colours", "Six bold colours",
         "Choose from Black, White, Blue, Yellow, Coral or (PRODUCT)RED. The glass back and aluminium frame match the "
         "colour all the way round."),
        ("feat-xr-display", "6.1-inch Liquid Retina display",
         "An edge-to-edge LCD with True Tone, which adjusts the white balance to the room, and wide colour for "
         "accurate photos and video. The same size and resolution as the iPhone 11."),
        ("feat-xr-faceid", "Face ID",
         "Unlock the phone, sign in to apps and pay with Apple Pay by looking at it. The TrueDepth camera also takes "
         "Portrait mode selfies."),
        ("feat-xr-camera", "12MP camera with Smart HDR",
         "The Wide camera has a bright ƒ/1.8 lens and optical image stabilisation. Smart HDR balances bright skies and "
         "shadows, and Portrait mode with Depth Control blurs the background behind people, adjustable after the shot."),
        ("feat-xr-battery", "All-day battery",
         "Up to 16 hours of video playback, an hour and a half more than the iPhone X. With an 18W or higher adapter it "
         "fast-charges to about 50% in around 30 minutes, and Qi wireless charging works too."),
        ("feat-xr-a12", "A12 Bionic",
         "Apple's first 7-nanometre chip handles apps, games and 4K video editing smoothly, with a Neural Engine for "
         "Face ID and photo processing."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's a good choice if you want a big-screen iPhone with Face ID at the lowest price, for everyday use, as a "
        "first phone for a family member, or as a spare. The screen, battery and daylight camera are all still good, "
        "and it works on every UK network.",
        "If you'd like Night mode, an Ultra Wide camera and the latest iOS features, the iPhone 11 costs a little more "
        "and is the same size. For 5G and MagSafe you'll need an iPhone 12 or later, and for Apple Intelligence an "
        "iPhone 15 Pro or later. Not sure which suits you? Ask in any of our stores and we'll talk you through the "
        "options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-xr-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-xr-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-xr-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-xr-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-xr-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-xr-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-xr-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-xr-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone XR
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was correct (Liquid Retina LCD, A12, Face ID, single 12MP with Portrait mode and Smart HDR,
    aluminium and glass, long battery, value). Kept its facts and made them specific: 326 ppi, True Tone, ƒ/1.8,
    16-hour battery, IP67, 4G.
  - "vs iPhone X: Bigger display, more colour options, lower price point" kept and expanded in the FAQ, including
    what the X has that the XR doesn't (OLED, telephoto, steel).
  - IMPORTANT ADDITION: the iPhone XR does NOT run iOS 26 or iOS 27. Its last major version is iOS 18, with
    security updates continuing. The old copy didn't mention software at all. Now stated in "Before you buy",
    the spec list and an FAQ, with the iPhone 11 suggested for buyers who want current iOS. This is the honest
    position and avoids returns; please check you're happy with the wording.
  - "Portrait Mode" written as Apple does: "Portrait mode".
  - Added what the old copy left out: single camera (no Ultra Wide, Night mode or optical zoom), Lightning and
    Qi (no MagSafe), 4G not 5G, IP67, XR vs 11 FAQ, full spec list. Tag is "4G", as on the iPhone 11 listings.
  - "Memory" relabelled "Storage"; "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct.

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.1-inch, 1792 × 828 at 326 ppi, 194g, 16 h video, IP67, Wi-Fi 5) and the
  iOS 26/27 compatibility lists (iPhone 11 and later; XR, XS and XS Max dropped at iOS 26, with iOS 18 security
  updates still being released as of 2026). The iPhone 11 page already quotes "up to 1 hour longer than iPhone XR",
  consistent with 16 h here.

QUESTIONS FOR GABOR:
  1. The iOS 18 wording: happy with "last major version is iOS 18, with security updates"? If Apple stops the
     security updates, the FAQ and spec line should be softened to "no longer updated".

CONFIRMED BY GABOR (3 Nov 2026): booking link ?selected={BOOKING_SELECTED}; condition tag "Pre-owned".
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone XR Apple Intelligence Bionic MagSafe Lightning Liquid Retina HD Face ID Smart HDR Depth Control Portrait Lighting True Tone Qi SIM Please MP IP67 LCD OLED 4G 5G G Hz X".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone XR", "Apple", "iPhone XR",
             "Apple iPhone XR with a 6.1-inch Liquid Retina LCD, the A12 Bionic chip, Face ID, a 12MP camera with Smart "
             "HDR and Portrait mode, and up to 16 hours of video playback, in six colours. 60-point quality checked by "
             "CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Blue", "Yellow", "Coral", "(PRODUCT)RED"]
images = [(f"Main image: {c}", f"Apple iPhone XR in {c}, front and back view",
           f"The iPhone XR in {c}, with a 6.1-inch Liquid Retina display and single 12MP camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone XR single 12MP rear camera",
     "The 12MP Wide camera on the iPhone XR, with optical image stabilisation, Smart HDR and Portrait mode."),
    ("Screen on, front", "iPhone XR 6.1-inch Liquid Retina display switched on",
     "The 6.1-inch Liquid Retina LCD of the iPhone XR, with True Tone and Face ID."),
    ("All colours", "Apple iPhone XR in all six colours lined up: Black, White, Blue, Yellow, Coral and (PRODUCT)RED",
     "The six colours of the iPhone XR, with glass backs that match the aluminium frame."),
    ("In the box", "Apple iPhone XR with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone XR with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone XR", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone XR in six colours, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
    "Software: the page says the XR's last major version is iOS 18 with security updates. If Apple stops those, soften the FAQ and spec line.",
], tags=TAGS)
print("built")

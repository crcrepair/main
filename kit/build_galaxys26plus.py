"""Samsung Galaxy S26+ — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's basic spec sheet plus verified sources; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-s26-plus"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy S26+"
FULL = "Samsung Galaxy S26+"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/s-series/samsung-galaxy-s26-plus/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-S26plus"   # CONFIRMED by Gabor, 12 Nov 2026 (first confirmed Samsung value)
TAGLINE = "The big-screen Galaxy S26, with magnetic charging."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy S26+ | 6.7-inch, Galaxy AI | CrC Repair®"
META_DESC = 'Buy a Samsung Galaxy S26+ with a 6.7-inch QHD+ 120Hz screen, Galaxy AI, 50MP triple camera and Qi2 magnetic charging. 60-point checked, 2-year warranty.'
OG_TITLE = "Galaxy S26+: 6.7-inch QHD+ screen, Galaxy AI, 2-year warranty"
OG_DESC = 'The big-screen Galaxy S26, with Galaxy AI, a 50MP triple camera and Qi2 magnetic charging. Fully checked, 2-year cover.'
X_TITLE = "Samsung Galaxy S26+ with a 2-year warranty | CrC Repair®"
X_DESC = "6.7-inch QHD+ 120Hz screen, Galaxy AI, 50MP triple camera, 4,900mAh battery and 45W charging. 60-point checked, free MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy S26 series", "Model family. Links the Galaxy S26, S26+ and S26 Ultra listings."),
    ("Galaxy S26+", "Exact model, as Samsung writes it. If WooCommerce dislikes the + in a tag slug, use \"Galaxy S26 Plus\"."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-s26p-box", "What comes with the Galaxy S26+?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-s26p-vs-s25p", "What's the difference between the Galaxy S26+ and S25+?",
     "The S26+ has Samsung's new Exynos 2600 chip in the UK in place of the S25+'s Snapdragon, built-in magnets for "
     "Qi2 wireless charging, Bluetooth 6.0, a vapour chamber for cooler gaming, the new mobile DNIe engine for colour "
     "accuracy, a redesigned translucent camera island and a more rounded frame, plus newer Galaxy AI features. The "
     "6.7-inch QHD+ screen, cameras, 4,900mAh battery and 45W charging are the same."),
    ("faq-s26p-chip", "Does the UK Galaxy S26+ have a Snapdragon chip?",
     "No. In the UK and Europe the S26 and S26+ use Samsung's own Exynos 2600, a 10-core chip built on a 2nm process; "
     "only the S26 Ultra has the Snapdragon 8 Elite Gen 5 for Galaxy here. The Exynos 2600 is a fast flagship chip "
     "that runs Galaxy AI on the phone, and it's what Samsung sells through every UK network."),
    ("faq-s26p-qi2", "Does the Galaxy S26+ work with magnetic chargers and accessories?",
     "Yes. The S26+ has Qi2 magnets built into the phone, so magnetic wireless chargers, stands and wallets snap "
     "straight on without a special case, something the S25+ and even the S26 Ultra can't do without one."),
    ("faq-s26p-updates", "Is the Galaxy S26+ still supported by Samsung?",
     "Yes. Samsung promised seven years of Android upgrades and security updates from its 2026 launch, so it launched "
     "on Android 16 with One UI 8.5, has since moved to Android 17 with One UI 9, and will keep getting new versions "
     "and security updates until 2033."),
    ("faq-s26p-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-s26p-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 12GB RAM"),
    ("Colours", "Black, White, Sky Blue and Cobalt Violet · Silver Shadow and Pink Gold (Samsung online exclusives)"),
    ("Display", "6.7-inch Dynamic AMOLED 2X · QHD+ · flat · mobile DNIe colour engine"),
    ("Refresh rate", "Adaptive 1Hz to 120Hz (LTPO) · Always-On display"),
    ("Brightness", "Up to 2,600 nits peak"),
    ("Glass", "Corning Gorilla Glass Victus 2, front and back"),
    ("Chip", "Samsung Exynos 2600 (UK and Europe) · 2nm · 10-core CPU · vapour chamber cooling"),
    ("Main camera", "50MP · optical image stabilisation"),
    ("Ultra Wide camera", "12MP · 120°"),
    ("Telephoto camera", "10MP · 3x optical zoom · stabilised"),
    ("Zoom range", "0.6x to 3x optical · digital zoom up to 30x"),
    ("Photography", "ProVisual Engine · Nightography photo and video · Expert RAW · Photo Assist · Generative Edit"),
    ("Video", "8K at 30fps · 4K at 60fps · 10-bit HDR · Log video · Audio Eraser"),
    ("Front camera", "12MP · autofocus"),
    ("Build", "Rounded Armor Aluminum frame · 190g · translucent camera island"),
    ("Water and dust", "IP68 (up to 1.5 metres for 30 minutes)"),
    ("Battery", "4,900mAh"),
    ("Charging", "USB-C 3.2 · 45W wired fast charging (adapter sold separately) · Qi2 magnetic wireless charging · reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 6.0 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Security", "Ultrasonic in-display fingerprint reader · face recognition · Knox Vault"),
    ("Software", "Launched on Android 16 with One UI 8.5, now Android 17 with One UI 9 · seven years of updates (to 2033)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the big-screen Galaxy S26, with magnetic charging", [
        f"The <strong>{FULL}</strong> pairs a 6.7-inch QHD+ screen, bright enough for sunlight at 2,600 nits and "
        "tuned by Samsung's new mobile DNIe engine, with a big 4,900mAh battery that charges at 45W. It's the first "
        "Galaxy S with <strong>Qi2 magnets built in</strong>, so magnetic chargers and accessories snap straight on, and "
        "the redesigned translucent camera island and rounded frame give it the 2026 look.",
        "Inside is Samsung's <strong>Exynos 2600</strong>, a 2nm flagship chip with 12GB of RAM and a vapour chamber "
        "to keep it cool in games. The 50MP triple camera has a 3x telephoto and Nightography for photos and video, "
        "<strong>Galaxy AI</strong> adds Photo Assist and Circle to Search, and Samsung promises <strong>seven years of "
        "updates</strong>.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Exynos chip in the UK.</strong> UK and European S26+ phones use Samsung's Exynos 2600, not the "
        "Snapdragon 8 Elite Gen 5 sold in the US. It's a fast 2nm flagship chip and runs Galaxy AI on the phone; only "
        "the S26 Ultra has the Snapdragon in the UK.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter. Qi2 magnetic wireless charging works with any Qi2 charger.",
        "<strong>No Privacy Display or S Pen.</strong> The S26 Ultra's built-in Privacy Display, 200MP camera, 5x zoom "
        "and S Pen aren't on the S26+. Some Galaxy AI features use the cloud and need a Samsung account.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-s26p-qi2", "Qi2 magnets built in",
         "Magnetic wireless chargers, car mounts, stands and wallets snap straight onto the phone, with no special case "
         "needed, a first for the Galaxy S range and something the S26 Ultra doesn't have."),
        ("feat-s26p-display", "6.7-inch QHD+ display",
         "A sharper screen than the S26's FHD+, with 2,600 nits peak brightness, an adaptive 1–120Hz refresh rate, "
         "Gorilla Glass Victus 2 and Samsung's mobile DNIe engine for more accurate colour."),
        ("feat-s26p-chip", "Exynos 2600 with a vapour chamber",
         "Samsung's 2nm flagship chip with a 10-core CPU and 12GB of RAM, cooled by a larger vapour chamber so games "
         "and 8K video stay fast without the phone getting hot."),
        ("feat-s26p-battery", "4,900mAh battery, 45W charging",
         "Comfortably a full day, with 45W wired charging to around 65% in 30 minutes, Qi2 magnetic wireless charging "
         "and reverse wireless charging for earbuds or a watch."),
        ("feat-s26p-camera", "50MP triple camera",
         "A 50MP main camera with optical stabilisation, a 3x telephoto for portraits and detail, and a 120° Ultra Wide, "
         "with Nightography for low-light photos and video and the ProVisual Engine for colour and detail."),
        ("feat-s26p-ai", "Galaxy AI and seven years of updates",
         "Photo Assist edits pictures from a typed description, Circle to Search finds anything on screen, and Live "
         "Translate and Now Brief carry over, on a phone Samsung will keep updating until 2033."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a big, sharp screen, a strong battery, magnetic accessories and the newest "
        "Galaxy AI without paying for the Ultra's stylus and camera extras. Coming from an S23+, S24+ or S25+, you'll "
        "notice the Qi2 magnets, the brighter screen, the cooler chip and the new design.",
        "If you want the Privacy Display, the 200MP camera, the 5x zoom or the S Pen, look at the Galaxy S26 Ultra. If "
        "you'd prefer something smaller, the Galaxy S26 has the same chip and cameras in a 6.3-inch phone. Not sure "
        "which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-s26p-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-s26p-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-s26p-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-s26p-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-s26p-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-s26p-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with genuine Samsung parts only, with a lifetime "
         "warranty on the screen repair."),
        ("own-s26p-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-s26p-sell", "Sell or trade in",
         "Upgrading, or finished with your phone? We'll make you an offer. Take cash, or put the value towards your "
         "next device. Find out " + L("/we-buy/", "how we buy phones") + "."),
    ]),

    cta_pair((f"Need your {P} repaired?",
              "Book online for a quick estimate, or bring your Galaxy into your nearest store.",
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
PAGE:              WooCommerce product description — Samsung Galaxy S26+
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

BOOKING LINK: ?selected={BOOKING_SELECTED}, CONFIRMED by Gabor (12 Nov 2026). This is the first confirmed Samsung
  value and shows the pattern: Galaxy-<Model> with "plus" in lower case and no hyphen. The earlier S23+, S24+ and
  S25+ pages used "Galaxy-S2x-Plus" and need the same change.

SOURCE: no old marketing copy, only Gabor's basic spec sheet (6.7-inch, 12GB, 10-core 3.8/3.26/2.76GHz chip = Exynos
  2600, 50MP + 10MP + 12MP with 3x optical and 30x digital, 12MP front, Android 16, Wi-Fi 7, Bluetooth 6.0, UWB,
  USB 3.2, colours Black / Pink Gold / Silver Shadow / Cobalt Violet / Sky Blue / White, 256/512GB, Galaxy AI photo
  editing, Circle to Search, Nightography video, vapour chamber, Knox Vault, mobile DNIe engine, translucent camera
  island, rounded aluminium frame, "full magnetic wireless charging support" = built-in Qi2 magnets). All used as
  given; "Sivler" corrected to Silver. The rest comes from UK reviews and launch coverage: Exynos 2600 in the UK,
  QHD+ 2,600 nits LTPO, Gorilla Glass Victus 2 front and back, 4,900mAh, 45W wired, 190g, announced 25 Feb 2026,
  UK launch price £1,099 (256GB), One UI 8.5 on Android 16 at launch, seven years of updates. samsung.com and
  review sites could not be fetched directly from this session (network); search results only.

NOTES:
  - Chip ❓: Exynos 2600 for UK/European stock. If any units are US imports with the Snapdragon, tell me.
  - IP68: not found in the S26+ search results, but confirmed for the S26 and standard across the S range; stated.
  - Qi2 wireless wattage, exact dimensions and resolution not confirmed; stated without figures.
  - Software: launched on One UI 8.5 / Android 16; One UI 9 / Android 17 has since rolled out. The page says both.
    ❓ Check a handset.

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. Chip and software (above). Colours: trim the six listed to what you stock. Tagline (above).
  2. Tag "Galaxy S26+": if WooCommerce mangles the + in the tag slug, use "Galaxy S26 Plus".

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov); booking link (12 Nov). Not a Black Friday deal (12 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Ultra S Pen Snapdragon Elite Gen Exynos Dynamic AMOLED FHD+ QHD+ QHD LTPO Nightography Expert RAW ProVisual Engine Audio Eraser Log HDR Gorilla Glass Victus Always-On One UI Android Galaxy AI Circle Search Live Translate Now Brief Nudge Photo Assist Generative Edit Privacy Display Knox Vault DNIe Armor Aluminum Qi2 Bluetooth Please MP IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S23 S24 S25 S26 W SIM Corning UK Europe US Wide GB".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

t = open(T + "product-short-description-template-iphone-15-pro.html").read()
for o, n in [("CrC product SHORT description: iPhone 15 Pro.", f"CrC product SHORT description: {FULL}."),
             ("<strong>Titanium strength. Pro power. Next-level performance</strong>", f"<strong>{TAGLINE}</strong>"),
             ("Already have an iPhone 15 Pro?", f"Already have a {FULL}?"),
             ('?selected=repairs/Apple/iPhone-15-Pro"', f'?selected={BOOKING_SELECTED}"')]:
    assert t.count(o) == 1, o
    t = t.replace(o, n)
open(O + f"{SLUG}-short-description.html", "w").write(t)

if BLACK_FRIDAY:
    b = open(T + "product-short-description-template-black-friday.html", "rb").read()
    for o, n in [(b"CrC product SHORT description: Samsung Galaxy S23 Ultra.", f"CrC product SHORT description: {FULL}.".encode()),
                 (b"<strong>The ultimate Galaxy with 200MP pro-grade camera.</strong>", f"<strong>{TAGLINE}</strong>".encode()),
                 (b"Sharper price on the Galaxy S23 Ultra.", f"Sharper price on the {P}.".encode()),
                 (b"Already have a Samsung Galaxy S23 Ultra?", f"Already have a {FULL}?".encode()),
                 (b'?selected=repairs/Samsung/Galaxy-S23-Ultra"', f'?selected={BOOKING_SELECTED}"'.encode())]:
        assert b.count(o) == 1, o
        b = b.replace(o, n)
    open(O + f"{SLUG}-short-description-black-friday.html", "wb").write(b)

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy S26+",
             "Samsung Galaxy S26+ with a 6.7-inch QHD+ 120Hz Dynamic AMOLED 2X display, Exynos 2600 chip, 12GB RAM, Galaxy "
             "AI, 50MP triple camera with 3x telephoto, 4,900mAh battery with 45W and Qi2 magnetic wireless charging, 5G "
             "and seven years of updates. 60-point quality checked by CrC Repair® with a two-year warranty and a free "
             "Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Black", "White", "Sky Blue", "Cobalt Violet", "Silver Shadow", "Pink Gold"]
images = [(f"Main image: {c}", f"Samsung Galaxy S26+ in {c}, front and back view",
           f"The Galaxy S26+ in {c}, with a flat 6.7-inch QHD+ display, translucent camera island and triple camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the Samsung Galaxy S26+ triple camera in its translucent island: 50MP main, Ultra Wide and 3x telephoto",
     "The Galaxy S26+ triple camera, with a 50MP main sensor, 12MP Ultra Wide and 10MP 3x telephoto."),
    ("Magnetic charging", "Samsung Galaxy S26+ on a magnetic Qi2 wireless charger",
     "Qi2 magnets built into the Galaxy S26+, so magnetic chargers and accessories snap straight on."),
    ("Galaxy AI", "Samsung Galaxy S26+ showing Photo Assist editing a photo from a typed prompt",
     "Galaxy AI on the Galaxy S26+: Photo Assist, Circle to Search, Live Translate and Now Brief."),
    ("Screen on, front", "Samsung Galaxy S26+ 6.7-inch Dynamic AMOLED 2X display switched on",
     "The 6.7-inch QHD+ 120Hz screen of the Galaxy S26+, up to 2,600 nits."),
    ("In the box", "Samsung Galaxy S26+ with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy S26+ with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy S26+ with triple camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and UK launch coverage. The tagline is new: please approve or replace.",
    "Chip: the page says Exynos 2600, correct for UK/European stock. If any units are US imports with the Snapdragon, say so.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Six colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product. If WooCommerce mangles the + in \"Galaxy S26+\", use \"Galaxy S26 Plus\".",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>, confirmed by Gabor.",
    "Software line says launched on One UI 8.5, now One UI 9. Check against a handset before publishing.",
], tags=TAGS)
print("built")

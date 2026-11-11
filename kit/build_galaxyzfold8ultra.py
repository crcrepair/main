"""Samsung Galaxy Z Fold8 Ultra — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's basic spec sheet plus verified sources; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-z-fold-8-ultra"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy Z Fold8 Ultra"
FULL = "Samsung Galaxy Z Fold8 Ultra"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/f-series/samsung-galaxy-z-fold-8-ultra/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-Z-Fold8-Ultra"   # ❓ Samsung pattern still to confirm
TAGLINE = "The 8-inch Fold with a 200MP camera."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy Z Fold8 Ultra | 8-inch | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy Z Fold8 Ultra with an 8-inch folding screen, 200MP camera with 3x zoo"
             "m and a 5,000mAh battery. 60-point checked, 2-year warranty.")
OG_TITLE = "Galaxy Z Fold8 Ultra: 8-inch screen, 200MP camera, 2-year cover"
OG_DESC = "Samsung's biggest foldable: an 8-inch anti-reflective screen, 200MP camera with 3x zoom and 5,000mAh battery. 2-year cover."
X_TITLE = "Samsung Galaxy Z Fold8 Ultra with a 2-year warranty | CrC Repair®"
X_DESC = "8-inch folding screen, 200MP camera with 3x zoom, Snapdragon 8 Elite Gen 5 and 5,000mAh battery. 60-point checked, free MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy Z Fold series", "Model family. Links the Z Fold7, Z Fold8 and Z Fold8 Ultra listings."),
    ("Galaxy Z Fold8 Ultra", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-fold8u-box", "What comes with the Galaxy Z Fold8 Ultra?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-fold8u-vs-fold8", "What's the difference between the Galaxy Z Fold8 Ultra and Z Fold8?",
     "The Ultra has a bigger 8-inch inner screen with an anti-reflective coating (the Fold8 is 7.6-inch), a 6.5-inch "
     "cover screen against 5.5-inch, a 200MP main camera with a 3x telephoto in place of the Fold8's two 50MP cameras, "
     "a 5,000mAh battery against 4,800mAh, and it's thinner unfolded at 4.1mm. It's also heavier at 215g against 201g "
     "and costs more. Both have the same chip, software and seven years of updates."),
    ("faq-fold8u-vs-fold7", "What's the difference between the Galaxy Z Fold8 Ultra and Z Fold7?",
     "The Fold8 Ultra is the direct successor to the Fold7's slot: it keeps the tall 8-inch shape and the 200MP main "
     "camera, and adds a 50MP Ultra Wide in place of 12MP, an anti-reflective inner screen, a shallower crease, the "
     "newer Snapdragon 8 Elite Gen 5 for Galaxy chip, a bigger 5,000mAh battery and a slimmer, lighter body. It "
     "launched on Android 17 with One UI 9."),
    ("faq-fold8u-camera", "How good is the Galaxy Z Fold8 Ultra camera?",
     "It's the best camera Samsung has put in a foldable: the same 200MP main sensor as the Galaxy S Ultra phones, a "
     "50MP Ultra Wide and a 10MP 3x telephoto. It's a step behind the S26 Ultra's 5x zoom, and the telephoto gets "
     "grainy past 3x, but for everyday photos, portraits and video it's a proper flagship camera."),
    ("faq-fold8u-durability", "Is the Galaxy Z Fold8 Ultra waterproof?",
     "It's rated IP48: water-resistant to 1.5 metres for 30 minutes, and protected against solid objects over 1mm, "
     "but not fully dust-sealed, so keep it out of sand and pockets full of grit. The new dual-rail hinge is designed "
     "for a shallower crease and less flex."),
    ("faq-fold8u-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-fold8u-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 1TB · 12GB RAM (16GB on the 1TB model)"),
    ("Colours", "Graphite, Cream and Violet Shadow · Green Shadow (Samsung online exclusive)"),
    ("Main screen", "8.0-inch Dynamic AMOLED 2X, folding · 2504 × 2256 · adaptive 1Hz to 120Hz · anti-reflective · up to 3,000 nits"),
    ("Cover screen", "6.5-inch Dynamic AMOLED 2X · 2520 × 1080 · 120Hz"),
    ("Chip", "Snapdragon 8 Elite Gen 5 for Galaxy · octa-core"),
    ("Rear cameras", "200MP Wide with optical stabilisation · 50MP Ultra Wide · 10MP 3x telephoto (ƒ/2.4)"),
    ("Zoom range", "0.6x to 3x optical · optical-quality 2x · digital zoom to 30x"),
    ("Front cameras", "10MP on the cover screen · 10MP on the main screen"),
    ("Video", "8K at 30fps · 4K at 60fps"),
    ("Galaxy AI", "Now Nudge · My FanCam · Photo Assist · Circle to Search · Live Translate · Now Brief"),
    ("Build", "8.9mm folded · 4.1mm unfolded · 215g · dual-rail hinge with a shallower crease"),
    ("Water and dust", "IP48 (water to 1.5 metres for 30 minutes; not dust-sealed)"),
    ("Battery", "5,000mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · wireless charging · reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 6.0 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Side fingerprint reader in the power button · face recognition"),
    ("Software", "Android 17 with One UI 9 · seven years of Android upgrades and security updates (to 2033)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the biggest Fold, with the best camera", [
        f"The <strong>{FULL}</strong> is Samsung's top foldable: an <strong>8-inch</strong> inner screen with an "
        "anti-reflective coating and a shallower crease, a 6.5-inch cover screen that works as a normal phone, and a "
        "body just 4.1mm thin when open. The <strong>Snapdragon 8 Elite Gen 5 for Galaxy</strong> chip and 12GB of RAM "
        "run two or three apps at once without fuss.",
        "It's the first Fold with a flagship-grade camera: a <strong>200MP main sensor</strong>, a new 50MP Ultra Wide "
        "and a 3x telephoto. The 5,000mAh battery is the biggest in a Fold, charging at 45W, and <strong>Galaxy "
        "AI</strong> adds Now Nudge, My FanCam and Photo Assist, with seven years of updates to come.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>Tall shape, heavier than the Fold8.</strong> The Ultra keeps the taller Fold7-style shape rather "
        "than the Fold8's wider one, and at 215g it's 14g heavier. If you want the lighter, pocket-friendlier Fold, "
        "the Galaxy Z Fold8 is the one.",
        "<strong>IP48, not IP68.</strong> It's water-resistant to 1.5 metres, but only protected against particles "
        "over 1mm, so sand and fine dust are a risk for any folding phone. Treat it with a little more care than a "
        "normal phone.",
        "<strong>No charger in the box, and no magnets for Qi2.</strong> It comes with a USB-C cable; 45W charging "
        "needs a 45W USB-C PD adapter. Wireless charging works, but magnetic Qi2 accessories need a case with a ring.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-fold8u-screen", "8-inch anti-reflective screen",
         "The biggest screen on a Galaxy phone, with a new anti-reflective coating that cuts glare, up to 3,000 nits "
         "for sunlight, a 1–120Hz refresh rate and a shallower crease than the Fold7."),
        ("feat-fold8u-camera", "200MP camera with 3x zoom",
         "The same 200MP main sensor as the Galaxy S Ultra phones, a 50MP Ultra Wide that's four times the resolution "
         "of the Fold7's, and a 10MP 3x telephoto for portraits and detail."),
        ("feat-fold8u-thin", "4.1mm unfolded",
         "Thinner open than any Fold before it, 8.9mm closed, with a dual-rail hinge built for less flex and a flatter "
         "screen, and Flex Mode to stand it half-open for video calls and photos."),
        ("feat-fold8u-battery", "5,000mAh battery",
         "The biggest battery in a Fold, with 45W wired charging, wireless charging and reverse wireless charging for "
         "earbuds or a watch, and the efficiency of the Snapdragon 8 Elite Gen 5."),
        ("feat-fold8u-multitask", "Multitasking on a tablet-size screen",
         "Run up to three apps side by side, drag content between them, and let Now Nudge suggest a split-screen "
         "pairing from what you're doing, with a 6.5-inch cover screen for quick tasks closed."),
        ("feat-fold8u-updates", "Seven years of updates",
         "Launched on Android 17 with One UI 9, with Android upgrades and security updates promised until 2033, so a "
         "pre-owned Fold8 Ultra stays current for years."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want the biggest screen you can fold into a pocket, a camera that matches a "
        "flagship phone, and the longest battery life of any Fold, at a pre-owned price well below new. Coming from a "
        "Fold5, Fold6 or Fold7, you'll notice the brighter anti-reflective screen, the Ultra Wide camera and the "
        "battery.",
        "If you'd rather have a lighter, wider foldable and don't need the telephoto, the Galaxy Z Fold8 costs less. "
        "If you want a stylus, the Galaxy S26 Ultra has one built in, and its 5x zoom beats the Fold's 3x. Not sure "
        "which suits you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-fold8u-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-fold8u-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-fold8u-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-fold8u-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-fold8u-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-fold8u-screen", "Screen repair",
         f"Cracked cover screen or a damaged folding screen? We replace {P} screens with genuine Samsung parts only, "
         "with a lifetime warranty on the screen repair."),
        ("own-fold8u-repairs", "Battery, hinge and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to hinge, charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-fold8u-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy Z Fold8 Ultra
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

SOURCE: no old marketing copy, only Gabor's basic spec sheet (8.0-inch, 12GB, Snapdragon 8 Elite Gen 5 for Galaxy,
  200MP + 50MP + 10MP rear, 10MP front, Android 17, Bluetooth 6.0, colours Graphite / Cream / Green Shadow / Violet
  Shadow, 256GB / 512GB / 1TB, Now Nudge, My FanCam, Photo Assist, Quick Share, anti-reflective screen, shallower
  crease, higher-resolution Ultra Wide). All used as given. The rest comes from launch coverage and reviews
  (announced 22 Jul 2026, on sale 7 Aug 2026): 8-inch 2504 × 2256 main screen up to 3,000 nits, 6.5-inch 2520 × 1080
  120Hz cover screen, 5,000mAh, 45W wired, IP48, 215g, 8.9mm folded, 4.1mm unfolded, dual-rail hinge, 10MP 3x
  telephoto at ƒ/2.4, 16GB RAM on the 1TB model, One UI 9 on Android 17, seven years of updates, Green Shadow
  online-only, UK launch price £1,899 (256GB). samsung.com and review sites could not be fetched directly from this
  session (network); search results only.

LEFT OUT ON PURPOSE (not confirmed): S PEN SUPPORT (no source either way; the page doesn't mention the S Pen at
  all), frame metal (one source says titanium; not confirmed), wireless charging wattage (one source says 20W; stated
  as "wireless charging"), the Ultra Wide aperture (sources give ƒ/1.9 and ƒ/2.2).

REPAIR WARRANTY ❓: as on the Fold8 page, the template rule "phone screens = lifetime" is applied, including the folding
  inner screen. Confirm that's what CrC offers on foldables.

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. S Pen: does the Fold8 Ultra support it? If yes, I'll add a line; if no, a "Before you buy" point like the Fold8.
  2. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question.
  3. Foldable screen repair warranty (above).
  4. Colours: trim the four listed to what you stock.
  5. Tagline (above).

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (11 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Z Fold Fold5 Fold6 Fold7 Fold8 Ultra S Pen Snapdragon Elite Gen Dynamic AMOLED Flex Mode One UI Android Galaxy AI Circle Search Live Translate Now Brief Nudge Photo Assist My FanCam Quick Share Qi2 Bluetooth Please MP IP48 IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S26 W SIM Qualcomm Wide".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy Z Fold8 Ultra",
             "Samsung Galaxy Z Fold8 Ultra foldable phone with an 8-inch anti-reflective 120Hz main screen, 6.5-inch cover "
             "screen, Snapdragon 8 Elite Gen 5 for Galaxy chip, 12GB RAM, 200MP main camera with 50MP Ultra Wide and 3x "
             "telephoto, Galaxy AI, 5,000mAh battery with 45W charging, 5G and seven years of updates, 4.1mm thin unfolded. "
             "60-point quality checked by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Graphite", "Cream", "Violet Shadow", "Green Shadow"]
images = [(f"Main image: {c}", f"Samsung Galaxy Z Fold8 Ultra in {c}, open, showing the 8-inch main screen",
           f"The Galaxy Z Fold8 Ultra in {c}, unfolded to its 8-inch anti-reflective screen.") for c in colours]
images += [
    ("Closed, cover screen", "Samsung Galaxy Z Fold8 Ultra closed, showing the 6.5-inch cover screen",
     "The Galaxy Z Fold8 Ultra closed: a 6.5-inch 120Hz cover screen that works as a normal phone."),
    ("Side profile", "Samsung Galaxy Z Fold8 Ultra open from the side, showing the 4.1mm thickness",
     "The Galaxy Z Fold8 Ultra from the side: 4.1mm unfolded, 8.9mm folded, with the dual-rail hinge."),
    ("Camera close-up", "Close-up of the Samsung Galaxy Z Fold8 Ultra triple camera: 200MP main, 50MP Ultra Wide and 3x telephoto",
     "The Galaxy Z Fold8 Ultra triple camera, with a 200MP main sensor, 50MP Ultra Wide and 10MP 3x telephoto."),
    ("Multitasking", "Samsung Galaxy Z Fold8 Ultra open with three apps on the 8-inch screen",
     "Three apps at once on the Galaxy Z Fold8 Ultra's 8-inch screen, with Now Nudge suggesting the split."),
    ("In the box", "Samsung Galaxy Z Fold8 Ultra with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy Z Fold8 Ultra with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy Z Fold8 Ultra foldable phone open to its 8-inch screen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and launch coverage. The tagline is new: please approve or replace.",
    "S Pen support is deliberately not mentioned (no source confirms it either way). Tell me yes or no and I'll add the line.",
    "Screen repair warranty: the page applies the lifetime screen rule to the folding inner screen too. Confirm, or tell me the Fold rule.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Four colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern.",
], tags=TAGS)
print("built")

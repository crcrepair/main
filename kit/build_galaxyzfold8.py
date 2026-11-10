"""Samsung Galaxy Z Fold8 — long + short description, schema, SEO pack and tags (normal short description, no Black Friday).
Built from Gabor's basic spec sheet plus verified sources; no old marketing copy existed."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "samsung-galaxy-fold8"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "templates", "")
P = "Galaxy Z Fold8"
FULL = "Samsung Galaxy Z Fold8"
URL = "https://www.crcrepair.co.uk/store/product/phones/samsung-phones/f-series/samsung-galaxy-fold8/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Samsung/Galaxy-Z-Fold8"   # ❓ Samsung pattern still to confirm; the URL slug drops the "Z"
TAGLINE = "The wider Fold: a 7.6-inch tablet that fits in your pocket."   # ❓ written by Claude: no old tagline supplied
BLACK_FRIDAY = False

META_TITLE = "Buy Samsung Galaxy Z Fold8 | 7.6-inch Fold | CrC Repair®"
META_DESC = ("Buy a Samsung Galaxy Z Fold8 with a wider 7.6-inch folding screen, 5.5-inch cover screen a"
             "nd Snapdragon 8 Elite Gen 5. 60-point checked, 2-year warranty.")
OG_TITLE = "Galaxy Z Fold8: the wider 7.6-inch foldable, 2-year warranty"
OG_DESC = "Samsung's lightest Fold yet: a wider 7.6-inch 4:3 screen, 5.5-inch cover screen and Snapdragon 8 Elite Gen 5. 2-year cover."
X_TITLE = "Samsung Galaxy Z Fold8 with a 2-year warranty | CrC Repair®"
X_DESC = "Wider 7.6-inch folding screen, 5.5-inch cover screen, Snapdragon 8 Elite Gen 5 and Galaxy AI. 60-point checked, free MOT."

TAGS = [
    ("Samsung", "Brand. The same tag on every Samsung product."),
    ("Galaxy", "Product line. Groups every Galaxy listing."),
    ("Galaxy Z Fold series", "Model family. Links the Z Fold7, Z Fold8 and Z Fold8 Ultra listings."),
    ("Galaxy Z Fold8", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("5G", "Connectivity."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-fold8-box", "What comes with the Galaxy Z Fold8?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-fold8-vs-fold7", "What's the difference between the Galaxy Z Fold8 and Z Fold7?",
     "The Fold8 changes shape: it's wider and shorter, so the cover screen feels like a normal phone and the 7.6-inch "
     "inner screen has a 4:3 shape that suits films, books and two apps side by side. It's lighter, has the newer "
     "Snapdragon 8 Elite Gen 5 for Galaxy chip, a slightly bigger 4,800mAh battery and launched on Android 17 with "
     "One UI 9. The Fold7's 200MP main camera and 3x telephoto moved to the Fold8 Ultra; the Fold8 has two 50MP "
     "cameras instead."),
    ("faq-fold8-vs-ultra", "Should I choose the Galaxy Z Fold8 or the Fold8 Ultra?",
     "They share the same chip, software, cover screen size and design. The Ultra has a bigger 8-inch inner screen, "
     "a 200MP main camera with a 3x telephoto, and costs a good deal more. The Fold8 is lighter and cheaper, with a "
     "7.6-inch inner screen and a 50MP main and Ultra Wide camera, which is plenty for everyday photos."),
    ("faq-fold8-spen", "Does the Galaxy Z Fold8 work with the S Pen?",
     "No. The Fold8's inner screen doesn't support the S Pen, so stylus notes and sketches aren't available on it. If "
     "you want a stylus, look at the Galaxy S26 Ultra, which has one built in."),
    ("faq-fold8-durability", "Is the Galaxy Z Fold8 waterproof?",
     "It's rated IP48: water-resistant to 1.5 metres for 30 minutes, and protected against solid objects over 1mm, "
     "but not fully dust-sealed, so keep it out of sand and pockets full of grit. The hinge is rated for 500,000 "
     "folds, and the cover screen uses Gorilla Glass Ceramic 3."),
    ("faq-fold8-warranty", f"What warranty comes with a {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-fold8-tradein", f"Can I trade in my old phone towards a {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage and memory", "256GB · 512GB · 1TB · 12GB RAM (16GB on the 1TB model)"),
    ("Colours", "Graphite, Cream and Lavender · Pistachio (Samsung online exclusive)"),
    ("Main screen", "7.6-inch Dynamic AMOLED 2X, folding · 2584 × 1828 · 4:3 shape · adaptive 1Hz to 120Hz"),
    ("Cover screen", "5.5-inch Dynamic AMOLED 2X · 1972 × 1248 · 120Hz · Gorilla Glass Ceramic 3"),
    ("Chip", "Snapdragon 8 Elite Gen 5 for Galaxy · octa-core"),
    ("Rear cameras", "50MP Wide with optical stabilisation · 50MP Ultra Wide · no telephoto"),
    ("Front cameras", "10MP on the cover screen · 10MP on the main screen"),
    ("Video", "8K at 30fps · 4K at 60fps"),
    ("Galaxy AI", "Now Nudge · My FanCam · Photo Assist · Circle to Search · Live Translate · Now Brief"),
    ("S Pen", "Not supported"),
    ("Build", "Armor Aluminum frame · 124 × 82 × 9.8mm folded · 4.5mm unfolded · 201g · hinge rated for 500,000 folds"),
    ("Water and dust", "IP48 (water to 1.5 metres for 30 minutes; not dust-sealed)"),
    ("Battery", "4,800mAh"),
    ("Charging", "USB-C · 45W wired fast charging (adapter sold separately) · wireless charging · reverse wireless"),
    ("Connectivity", "5G · Wi-Fi 7 · Bluetooth 6.0 · NFC · Ultra Wideband"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Biometrics", "Side fingerprint reader in the power button · face recognition"),
    ("Software", "Android 17 with One UI 9 · seven years of Android upgrades and security updates (to 2033)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — a wider foldable, lighter than ever", [
        f"The <strong>{FULL}</strong> is the first Fold with a new, wider shape. Closed, the 5.5-inch cover screen "
        "feels like a normal phone rather than a narrow remote; open, the <strong>7.6-inch</strong> inner screen has a "
        "4:3 shape that suits films, books and two apps side by side, with a less visible crease. It's Samsung's "
        "lightest Fold yet at 201g, and 4.5mm thin when open.",
        "Inside is the <strong>Snapdragon 8 Elite Gen 5 for Galaxy</strong> chip with 12GB of RAM, a 4,800mAh battery "
        "with 45W charging and <strong>Galaxy AI</strong>, including Now Nudge for quick split-screen multitasking and "
        "My FanCam for video. Twin 50MP cameras cover wide and ultra-wide shots, and Samsung promises seven years of "
        "updates.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>No telephoto, no S Pen.</strong> The Fold8 has a 50MP main and a 50MP Ultra Wide camera; zoom is "
        "digital, cropped from the main sensor. The inner screen doesn't support the S Pen. Both are Fold8 Ultra "
        "features.",
        "<strong>IP48, not IP68.</strong> It's water-resistant to 1.5 metres, but only protected against particles "
        "over 1mm, so sand and fine dust are a risk for any folding phone. Treat it with a little more care than a "
        "normal phone.",
        "<strong>No charger in the box.</strong> It comes with a USB-C cable. For 45W fast charging you'll need a 45W "
        "USB-C PD adapter.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Samsung's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-fold8-shape", "A wider, more natural shape",
         "The cover screen is a normal phone width, so typing one-handed is easy, and the inner screen opens to a 4:3 "
         "tablet that fits films and documents better than the tall Fold7 did."),
        ("feat-fold8-light", "Samsung's lightest Fold",
         "At 201g and 4.5mm unfolded, it's lighter than many ordinary flagships, with an Armor Aluminum frame, Gorilla "
         "Glass Ceramic 3 on the cover screen and a hinge rated for 500,000 folds."),
        ("feat-fold8-multitask", "Multitasking with Now Nudge",
         "Run apps side by side on the big screen, drag content between them, and let Now Nudge suggest a split-screen "
         "pairing from what you're doing."),
        ("feat-fold8-chip", "Snapdragon 8 Elite Gen 5 for Galaxy",
         "Qualcomm's latest flagship chip, tuned for Samsung, with the speed and efficiency for two apps at once, "
         "gaming on the big screen and on-device Galaxy AI."),
        ("feat-fold8-ai", "Galaxy AI for photos and video",
         "Photo Assist edits pictures from a typed description, My FanCam tracks one person in a video and reframes it, "
         "and Circle to Search, Live Translate and Now Brief carry over from the S series."),
        ("feat-fold8-updates", "Seven years of updates",
         "Launched on Android 17 with One UI 9, with Android upgrades and security updates promised until 2033, so a "
         "pre-owned Fold8 stays current for years."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's the right choice if you want a phone that opens into a tablet for reading, films, email and two apps at "
        "once, and you'd rather have a lighter, more pocketable foldable than the biggest screen. Coming from a Fold4, "
        "Fold5 or Fold6, you'll notice the wider shape, the weight and the faster chip.",
        "If you want the best camera and the largest screen, the Galaxy Z Fold8 Ultra adds the 200MP camera, a 3x "
        "telephoto and an 8-inch screen. If you want a stylus, the Galaxy S26 Ultra has one built in. If you don't "
        "need a folding screen at all, the Galaxy S26 Ultra also has the better camera for less. Not sure which suits "
        "you? Ask in any of our stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-fold8-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-fold8-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-fold8-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-fold8-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-fold8-mot", "Free Device MOT", "Every 6 months",
         "Bring your Galaxy in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own a {P}?", "Whatever you need next, we can help:", [
        ("own-fold8-screen", "Screen repair",
         f"Cracked cover screen or a damaged folding screen? We replace {P} screens with genuine Samsung parts only, "
         "with a lifetime warranty on the screen repair."),
        ("own-fold8-repairs", "Battery, hinge and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to hinge, charging port and camera faults, our "
         "technicians fix it in store with genuine Samsung parts and a one-year warranty. See our "
         + L("/samsung-repair/", "Samsung repair") + " service."),
        ("own-fold8-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Samsung Galaxy Z Fold8
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html
Not a Black Friday deal: normal short description only.

Samsung rules as on the other Galaxy pages: genuine Samsung parts only, /samsung-repair/ pillar, Samsung's update
policy, "a Galaxy". Layout, CSS, icons and store capsules identical to every other product page.

SOURCE: no old marketing copy, only Gabor's basic spec sheet (7.6-inch, 12GB, Snapdragon 8 Elite Gen 5 for Galaxy,
  50MP + 50MP rear, 10MP front, Android 17, Bluetooth 6.0, colours Cream / Graphite / Lavender / Pistachio, 256GB /
  512GB / 1TB, Now Nudge, My FanCam, Photo Assist, Quick Share). All used as given; the sheet's "1B" storage read
  as 1TB. The rest comes from launch coverage and reviews (announced 22 Jul 2026, on sale 7 Aug 2026): wider 4:3
  design, 7.6-inch 2584 × 1828 main screen, 5.5-inch 1972 × 1248 120Hz cover screen with Gorilla Glass Ceramic 3,
  4,800mAh, 45W wired, IP48, 124 × 82 × 9.8mm folded, 4.5mm unfolded, 201g (one review says 199g), hinge rated for
  500,000 folds, no telephoto, no S Pen support, 16GB RAM on the 1TB model, One UI 9 on Android 17, seven years of
  updates, Pistachio online-only, UK launch price £1,699 (256GB). Fold8 Ultra: 8-inch, 200MP + 3x telephoto.
  samsung.com and review sites could not be fetched directly from this session (network); search results only.

LEFT OUT ON PURPOSE (not confirmed): wireless charging wattage (one source says 20W; stated as "wireless charging"
  without a figure), main-screen peak brightness, exact hinge name, whether the main screen has Gorilla Glass.

REPAIR WARRANTY ❓: the template rule "phone screens = lifetime" is applied to the Fold8, including the folding inner
  screen. Confirm that's what CrC offers on foldables; if the inner screen is one year, say so and I'll change the card.

TAGLINE: no old tagline existed. "{TAGLINE}" is mine; please approve or replace.

QUESTIONS FOR GABOR:
  1. Booking link value: used ?selected={BOOKING_SELECTED}. Same Samsung pattern question; note the URL slug has no "Z".
  2. Foldable screen repair warranty (above).
  3. Colours: trim the four listed to what you stock.
  4. Tagline (above).

CONFIRMED BY GABOR: condition tag "Pre-owned" (3 Nov). Not a Black Friday deal (10 Nov).

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="Galaxy Samsung Z Fold Fold4 Fold5 Fold6 Fold7 Fold8 Ultra S Pen Snapdragon Elite Gen Dynamic AMOLED Gorilla Glass Ceramic Armor Aluminum One UI Android Galaxy AI Circle Search Live Translate Now Brief Nudge Photo Assist My FanCam Quick Share Bluetooth Please MP IP48 IP68 RAM USB-C PD Wi-Fi Ultra Wideband 5G G Hz 8K 4K S26 W SIM Corning Qualcomm Wide".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, FULL, "Samsung", "Galaxy Z Fold8",
             "Samsung Galaxy Z Fold8 foldable phone with a wider 7.6-inch 4:3 120Hz main screen, 5.5-inch cover screen, "
             "Snapdragon 8 Elite Gen 5 for Galaxy chip, 12GB RAM, twin 50MP cameras, Galaxy AI, 4,800mAh battery with 45W "
             "charging, 5G and seven years of updates, at 201g. 60-point quality checked by CrC Repair® with a two-year "
             "warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Graphite", "Cream", "Lavender", "Pistachio"]
images = [(f"Main image: {c}", f"Samsung Galaxy Z Fold8 in {c}, open, showing the 7.6-inch main screen",
           f"The Galaxy Z Fold8 in {c}, unfolded to its wider 7.6-inch 4:3 screen.") for c in colours]
images += [
    ("Closed, cover screen", "Samsung Galaxy Z Fold8 closed, showing the 5.5-inch cover screen",
     "The Galaxy Z Fold8 closed: a normal-width 5.5-inch 120Hz cover screen."),
    ("Side profile", "Samsung Galaxy Z Fold8 half-open from the side, showing the hinge and 4.5mm thickness",
     "The Galaxy Z Fold8 from the side: 9.8mm folded, 4.5mm unfolded, with a hinge rated for 500,000 folds."),
    ("Camera close-up", "Close-up of the Samsung Galaxy Z Fold8 twin 50MP rear cameras",
     "The Galaxy Z Fold8 rear cameras: a 50MP main with optical stabilisation and a 50MP Ultra Wide."),
    ("Multitasking", "Samsung Galaxy Z Fold8 open with two apps side by side on the main screen",
     "Two apps side by side on the Galaxy Z Fold8's 7.6-inch screen, with Now Nudge suggesting the split."),
    ("In the box", "Samsung Galaxy Z Fold8 with the charging cable supplied by CrC Repair®",
     "What you receive: the Galaxy Z Fold8 with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", FULL, [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Samsung Galaxy Z Fold8 foldable phone open to its 7.6-inch screen, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "No old copy existed for this product; the page is written from Gabor's spec sheet and launch coverage. The tagline is new: please approve or replace.",
    "Screen repair warranty: the page applies the lifetime screen rule to the folding inner screen too. Confirm, or tell me the Fold rule.",
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest. Four colours are listed; trim to what you stock.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code>. Please confirm the Samsung pattern, and whether the booking system includes the Z.",
], tags=TAGS)
print("built")

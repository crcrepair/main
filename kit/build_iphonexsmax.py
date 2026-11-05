"""iPhone XS Max — long + short description, schema, SEO pack and tags, from the approved template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

SLUG = "iphone-xs-max"
O = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products") + "/"
P = "iPhone XS Max"
URL = "https://www.crcrepair.co.uk/store/product/phones/apple-phones/apple-iphone-xs-max/"
ACCESSORIES = "https://www.crcrepair.co.uk/store/product-category/accessories/"
BOOKING_SELECTED = "repairs/Apple/iPhone-XS-Max"   # pattern confirmed by Gabor, 3 Nov 2026
TAGLINE = "Bigger, brighter, and built for performance."

META_TITLE = "Buy iPhone XS Max | OLED, Dual Camera | CrC Repair®"
META_DESC = ("Buy an iPhone XS Max with a 6.5-inch OLED screen, dual camera with 2x zoom and Face ID in stainless "
             "steel. 60-point checked, 2-year warranty, free MOT.")
OG_TITLE = "iPhone XS Max: 6.5-inch OLED, dual camera, 2-year warranty"
OG_DESC = "A12 Bionic, a 6.5-inch Super Retina OLED screen, dual 12MP camera with 2x zoom and Face ID. Fully checked, 2-year cover."
X_TITLE = "iPhone XS Max with a 2-year warranty | CrC Repair®"
X_DESC = "Big 6.5-inch OLED screen, dual camera with 2x zoom and Face ID in stainless steel. 60-point checked, free Device MOT."

TAGS = [
    ("Apple", "Brand. The same tag on every Apple product."),
    ("iPhone", "Product line. Groups every iPhone listing."),
    ("iPhone X series", "Model family. Links the iPhone X, XR, XS and XS Max listings."),
    ("iPhone XS Max", "Exact model, matching how people search."),
    ("Pre-owned", "Condition. Confirmed wording: keep it identical on every listing."),
    ("4G", "Connectivity. The iPhone XS Max is 4G LTE; 5G arrived with the iPhone 12."),
]

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-xsmax-box", "What comes with the iPhone XS Max?",
     "The phone comes with a charging cable as standard. For a plug, screen protector, case or wireless charger, browse "
     "our " + L(ACCESSORIES, "phone accessories") + ". Your 15% discount on selected accessories is applied "
     "automatically in the basket."),
    ("faq-xsmax-ios", "Is the iPhone XS Max still supported by Apple?",
     "Partly. The iPhone XS Max's last major version is iOS 18; it doesn't run iOS 26 or iOS 27, so it won't get new "
     "features. Apple has carried on releasing iOS 18 security updates for it, and all the everyday apps still work. "
     "If you want the latest iOS features, look at the iPhone 11 or newer."),
    ("faq-xsmax-vs-x", "What's the difference between the iPhone XS Max and iPhone X?",
     "The XS Max has a much larger 6.5-inch screen (the X is 5.8-inch), the faster A12 Bionic chip, Smart HDR and a "
     "better dual camera, dual SIM with eSIM, better water resistance (IP68 against IP67), louder stereo speakers and "
     "a Gold colour option. Both have Face ID, an OLED screen, a 2x telephoto and a stainless steel frame."),
    ("faq-xsmax-vs-xr", "Should I choose the iPhone XS Max or the iPhone XR?",
     "The XS Max has the bigger, sharper OLED screen, a second telephoto camera for 2x optical zoom, a stainless steel "
     "frame and better water resistance. The XR has an LCD screen, a single camera, an aluminium frame, more colours "
     "and a slightly longer battery, and it's cheaper. Both have the same A12 chip and the same software support."),
    ("faq-xsmax-5g", "Does the iPhone XS Max work with 5G?",
     "No. It uses 4G LTE, which works on every UK network. Apple introduced 5G with the iPhone 12."),
    ("faq-xsmax-warranty", f"What warranty comes with an {P} from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-xsmax-tradein", f"Can I trade in my old phone towards an {P}?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

SPECS = [
    ("Storage", "64GB · 256GB · 512GB"),
    ("Colours", "Space Grey, Silver and Gold"),
    ("Display", "6.5-inch Super Retina (OLED) · 2688 × 1242 · 458 ppi · HDR · True Tone"),
    ("Brightness", "625 nits typical"),
    ("Chip", "A12 Bionic · Neural Engine"),
    ("Rear cameras", "Dual 12MP: Wide (ƒ/1.8) and Telephoto (ƒ/2.4) · optical stabilisation on both"),
    ("Zoom", "2x optical zoom · up to 10x digital zoom"),
    ("Photography", "Smart HDR · Portrait mode with Depth Control · Portrait Lighting (five effects)"),
    ("Video", "4K up to 60fps · 1080p slo-mo at 240fps · stereo recording"),
    ("Front camera", "7MP TrueDepth · Portrait mode · Face ID"),
    ("Audio", "Stereo speakers with wider stereo sound"),
    ("Build", "Stainless steel frame · glass front and back · 208g"),
    ("Water and dust", "IP68 (up to 2 metres for 30 minutes)"),
    ("Battery", "Up to 15 hours video playback"),
    ("Charging", "Lightning · fast charge to 50% in about 30 minutes (18W adapter) · Qi wireless"),
    ("Connectivity", "4G LTE · Wi-Fi 5 (802.11ac) · Bluetooth 5.0 · NFC"),
    ("SIM", "Dual SIM (nano-SIM and eSIM)"),
    ("Software", "Last major version iOS 18, with security updates (no iOS 26 or 27)"),
]

sections = [
    jumpnav(NAV),

    overview_enquiry(f"{P} — the big-screen iPhone, in stainless steel", [
        f"The <strong>{P}</strong> had the largest iPhone screen when it launched: a 6.5-inch Super Retina OLED with "
        "HDR, deep blacks and True Tone, in a polished <strong>stainless steel</strong> frame with glass front and "
        "back. The <strong>A12 Bionic</strong> chip, Apple's first 7-nanometre chip, keeps apps, games and Face ID "
        "quick.",
        "The dual 12MP camera pairs a Wide lens with a 2x telephoto, both optically stabilised, and Smart HDR "
        "balances bright skies and shadows. Stereo speakers give wider sound for films, and it was the first iPhone "
        "with <strong>dual SIM</strong> (nano-SIM and eSIM), handy for a work number or travel. Battery life is up to "
        "15 hours of video, and it comes with a charging cable as standard.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>No new iOS features.</strong> The iPhone XS Max's last major version is iOS 18. It still gets Apple's "
        "security updates and runs the everyday apps, but it won't get iOS 26 or 27 features. If staying current "
        "matters, the iPhone 11 Pro Max is the next big-screen model that's still supported.",
        "<strong>No Night mode or Ultra Wide.</strong> The dual camera is Wide and Telephoto. Night mode and the "
        "Ultra Wide lens arrived with the iPhone 11, so low-light photos are weaker than on newer models.",
        "<strong>Lightning and 4G.</strong> It charges through the Lightning port (Qi wireless works too, without "
        "MagSafe magnets) and connects over 4G LTE rather than 5G. At 208g it's a large, heavy phone.",
    ]),

    speclist("specs", f"{P} technical specifications", "The key hardware at a glance:", SPECS,
             after="Figures are Apple's."),

    cards("features", f"What makes the {P} stand out", None, [
        ("feat-xsmax-display", "6.5-inch Super Retina OLED",
         "The largest iPhone screen at launch, with 458 ppi, HDR for films, true blacks and True Tone, which adjusts "
         "the white balance to the room. The same size as the iPhone 11 Pro Max."),
        ("feat-xsmax-camera", "Dual camera with 2x zoom",
         "A 12MP Wide and a 12MP Telephoto, both with optical stabilisation, give 2x optical zoom for portraits and "
         "detail. Smart HDR and Portrait mode with Depth Control blur the background, adjustable after the shot."),
        ("feat-xsmax-steel", "Stainless steel and IP68",
         "A polished stainless steel frame with glass front and back, rated IP68 for water and dust to 2 metres, "
         "better than the iPhone X's IP67."),
        ("feat-xsmax-dualsim", "Dual SIM with eSIM",
         "Use a physical nano-SIM and an eSIM at once, for a work and a personal number or a local data plan when "
         "travelling. The XS Max was the first iPhone to offer it."),
        ("feat-xsmax-faceid", "Face ID",
         "Unlock the phone, sign in to apps and pay with Apple Pay by looking at it. The TrueDepth camera also takes "
         "Portrait mode selfies."),
        ("feat-xsmax-a12", "A12 Bionic and stereo sound",
         "Apple's first 7-nanometre chip handles apps, games and 4K video editing smoothly, and the stereo speakers "
         "give wider, louder sound for video and music."),
    ]),

    lede("who-for", f"Is the {P} right for you?", [
        "It's a good choice if you want a big OLED screen, a telephoto camera and a premium steel build at a low "
        "price, for films, reading and everyday use. The screen and build still feel high-end, and it works on every "
        "UK network.",
        "If you'd like Night mode, an Ultra Wide camera and the latest iOS features, the iPhone 11 Pro Max is the same "
        "size and still supported. For 5G and MagSafe you'll need an iPhone 12 or later, and for Apple Intelligence an "
        "iPhone 15 Pro or later. Not sure which suits you? Ask in any of our stores and we'll talk you through the "
        "options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-xsmax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-xsmax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-xsmax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-xsmax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-xsmax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-xsmax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-xsmax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-xsmax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone XS Max
PRODUCT URL:       {URL}
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description. Block editor: Code editor. Classic editor: TEXT tab only.
SEO, social copy, product tags and image alt texts: {SLUG}-seo-pack.html · Schema: {SLUG}-schema.html

CHANGES FROM THE OLD DESCRIPTION (checked against Apple's published specs):
  - The old copy was correct (6.5-inch OLED, largest at launch, A12, dual SIM, dual camera with Smart HDR, stereo
    sound, premium build). Kept its facts and made them specific: 2688 × 1242 at 458 ppi, ƒ/1.8 and ƒ/2.4 with
    optical stabilisation on both, 2x optical zoom, IP68 to 2 metres, 208g, 15-hour battery.
  - "Difference vs iPhone X" kept and expanded in the FAQ, including what the two share (Face ID, OLED, 2x
    telephoto, steel) so the upgrade isn't overstated.
  - IMPORTANT ADDITION: the iPhone XS Max does NOT run iOS 26 or iOS 27. Its last major version is iOS 18, with
    security updates continuing. The old copy didn't mention software at all. Now stated in "Before you buy", the
    spec list and an FAQ, with the iPhone 11 Pro Max suggested for buyers who want current iOS. Same wording as
    the iPhone XR page.
  - Added what the old copy left out: no Night mode or Ultra Wide, Lightning and Qi (no MagSafe), 4G not 5G,
    weight, XS Max vs XR FAQ, full spec list. Tag is "4G", as on the iPhone 11 and XR listings.
  - "Screen Size", "Special Features" written in sentence case; "Storage" label kept (the old copy already had it).
  - "choosen" spelling fixed; "click here" given descriptive anchor text.
  - Colours and storage in the old copy were correct.

SOURCES: apple.com and support.apple.com are blocked from this session's network. Figures were checked against
  Apple's spec sheet as reported (6.5-inch, 2688 × 1242 at 458 ppi, 208g, IP68, dual 12MP with telephoto) and the
  iOS 26/27 compatibility lists (XR, XS and XS Max dropped at iOS 26, iOS 18 security updates still released in
  2026). The 15 h video and 2 m depth are Apple's launch figures.

QUESTIONS FOR GABOR:
  1. The iOS 18 wording, as on the XR page: happy with "last major version is iOS 18, with security updates"?

CONFIRMED BY GABOR (3 Nov 2026): booking link ?selected={BOOKING_SELECTED}; condition tag "Pre-owned".
Tagline kept from the old copy: "{TAGLINE}"

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(O + f"{SLUG}-product-description.html", sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone XS XR Max Apple Intelligence Bionic MagSafe Lightning Super Retina Face ID Smart HDR Depth Control Portrait Lighting True Tone Qi SIM Please MP IP68 IP67 LCD OLED 4G 5G G Hz X Night Ultra Wide".split(),
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

build_schema(O + f"{SLUG}-schema.html", URL, "Apple iPhone XS Max", "Apple", "iPhone XS Max",
             "Apple iPhone XS Max with a 6.5-inch Super Retina OLED display, the A12 Bionic chip, Face ID, a dual 12MP "
             "camera with 2x optical zoom and Smart HDR, dual SIM and a stainless steel frame. 60-point quality checked "
             "by CrC Repair® with a two-year warranty and a free Device MOT every six months.",
             [(k, v.replace(" · ", ", ")) for k, v in SPECS], FAQ)

colours = ["Space Grey", "Silver", "Gold"]
images = [(f"Main image: {c}", f"Apple iPhone XS Max in {c}, front and back view",
           f"The iPhone XS Max in {c}, with a 6.5-inch Super Retina OLED display and dual camera.") for c in colours]
images += [
    ("Camera close-up", "Close-up of the iPhone XS Max dual 12MP camera with Wide and Telephoto lenses",
     "The dual 12MP camera on the iPhone XS Max, with 2x optical zoom, optical stabilisation and Smart HDR."),
    ("Screen on, front", "iPhone XS Max 6.5-inch Super Retina OLED display switched on",
     "The 6.5-inch Super Retina OLED screen of the iPhone XS Max, with HDR, True Tone and Face ID."),
    ("Side view", "Side of the iPhone XS Max showing the polished stainless steel frame",
     "The polished stainless steel frame of the iPhone XS Max, with glass front and back."),
    ("In the box", "Apple iPhone XS Max with the charging cable supplied by CrC Repair®",
     "What you receive: the iPhone XS Max with a charging cable included as standard."),
]

seo_pack(O + f"{SLUG}-seo-pack.html", "Apple iPhone XS Max", [
    ("SEO title", META_TITLE, "aim: under 60"),
    ("Meta description", META_DESC, "aim: 150–155"),
    ("Facebook title (og:title)", OG_TITLE, "aim: under 65"),
    ("Facebook description (og:description)", OG_DESC, "aim: 110–125"),
    ("X title (twitter:title)", X_TITLE, "aim: under 70"),
    ("X description (twitter:description)", X_DESC, "aim: under 125"),
    ("Facebook/X image alt text", "Apple iPhone XS Max in stainless steel with dual camera, sold by CrC Repair® with a two-year warranty", "for the social share image"),
], images, notes=[
    "Image alt texts are written for a standard set of shots, because I didn't have the actual images. Use the rows that match your photos and delete the rest.",
    "Tags: colours and storage sizes belong in product <b>attributes</b> (variations), not tags. Keep tag names spelled exactly the same on every product.",
    "Tag archive pages (/product-tag/…) should be <b>noindex</b> in SEOPress → Titles &amp; Metas → Taxonomies.",
    f"Short description booking link uses <code>?selected={BOOKING_SELECTED}</code> (confirmed pattern).",
    "Software: the page says the XS Max's last major version is iOS 18 with security updates. If Apple stops those, soften the FAQ and spec line.",
], tags=TAGS)
print("built")

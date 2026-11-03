"""iPhone 15 Pro Max WooCommerce product description — built from the approved iPhone 15 Pro template."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from product_kit import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", "products", "") + "iphone-15-pro-max-product-description.html"
P = "iPhone 15 Pro Max"

META_TITLE = "Buy iPhone 15 Pro Max | 2-Year Warranty | CrC Repair®"
META_DESC = ("Buy an iPhone 15 Pro Max with 5x telephoto zoom, titanium design and A17 Pro chip. 60-point checked, "
             "2-year warranty and a free Device MOT every 6 months.")

NAV = [("before-you-buy", "Before you buy", "info"), ("specs", "Specifications", "cpu"),
       ("why-us", "Why buy from us", "star"), ("warranty", "Warranty", "shield"),
       ("book", "Book a repair", "wrench"), ("own-one", "Already own?", "phone")]

FAQ = [
    ("faq-15promax-charger", "Does the iPhone 15 Pro Max come with a charger?",
     "Apple's own box includes a USB-C charge cable but no power adapter. Any USB-C charger will work. For fast "
     "charging (about 50% in around 30 minutes) you need a 20W or higher USB-C power adapter."),
    ("faq-15promax-zoom", "How good is the 5x zoom?",
     "The telephoto camera gives true 5x optical zoom, the equivalent of a 120mm lens, so you can get close-up shots "
     "from across a room, a pitch or a stage without losing detail. Digital zoom goes up to 25x. The telephoto "
     "has its own 3D sensor-shift stabilisation, which keeps zoomed photos and video steady."),
    ("faq-15promax-ai", "Does the iPhone 15 Pro Max support Apple Intelligence?",
     "Yes. The iPhone 15 Pro Max and 15 Pro are the earliest iPhones that support Apple Intelligence. Features "
     "such as Writing Tools and Clean Up in Photos come with the latest version of iOS."),
    ("faq-15promax-sim", "Will it work with my SIM and network?",
     "UK models take a physical nano-SIM and also support eSIM, so you can run two numbers on one phone. 5G works "
     "wherever your network offers it. Ask us if you'd like to confirm the network status of a specific handset."),
    ("faq-15promax-vs-pro", "What's the difference between the iPhone 15 Pro Max and 15 Pro?",
     "The Pro Max has a bigger 6.7-inch display, a 5x telephoto camera (the 15 Pro has 3x) and a larger battery, "
     "with up to 29 hours of video playback against 23. Both share the A17 Pro chip, the 48MP main camera and the "
     "titanium design. The 15 Pro is smaller and lighter, at 187g against 221g."),
    ("faq-15promax-warranty", "What warranty comes with an iPhone 15 Pro Max from CrC Repair®?",
     "Every device we sell comes with a hassle-free two-year warranty, plus a free Device MOT every six months to "
     "keep it running smoothly."),
    ("faq-15promax-tradein", "Can I trade in my old phone towards an iPhone 15 Pro Max?",
     "Yes. Bring your current phone into one of our stores for an offer, and take cash or put the value towards "
     "your next device. See " + L("/we-buy/", "how we buy phones and devices") + " for details."),
]

sections = [
    jumpnav(NAV),

    overview_enquiry("iPhone 15 Pro Max — titanium design, 5x zoom", [
        "The <strong>iPhone 15 Pro Max</strong> is the largest iPhone 15, with a 6.7-inch ProMotion display and the "
        "first 5x telephoto camera ever fitted to an iPhone. Together with the iPhone 15 Pro, it was the first iPhone "
        "built around a titanium frame and a 3-nanometre chip, the A17 Pro. At 221g it is 19g lighter than the "
        "iPhone 14 Pro Max.",
        "It charges over <strong>USB-C</strong>, can record ProRes video straight to an external drive, and swaps the "
        "mute switch for a customisable Action button. The battery gives up to 29 hours of video playback, the longest "
        "in the iPhone 15 range, and it supports <strong>Apple Intelligence</strong>.",
    ]),

    note("before-you-buy", "Before you buy — good to know", [
        "<strong>USB-C, not Lightning.</strong> Older Lightning cables and accessories need Apple's USB-C to "
        "Lightning adapter. MagSafe cases, wallets and chargers work as normal.",
        "<strong>No power adapter.</strong> Apple doesn't put one in the box. Any USB-C charger works, and a 20W or "
        "higher adapter gives you fast charging.",
        "<strong>It's a big phone.</strong> The 6.7-inch screen and 221g weight suit two-handed use. If you'd rather "
        "use your phone one-handed, the iPhone 15 Pro has the same chip and main camera in a 6.1-inch body, with 3x "
        "zoom instead of 5x.",
    ]),

    speclist("specs", "iPhone 15 Pro Max technical specifications", "The key hardware at a glance:", [
        ("Storage", "256GB · 512GB · 1TB"),
        ("Colours", "Natural, Blue, White and Black Titanium"),
        ("Display", "6.7-inch Super Retina XDR (OLED) · 2796 × 1290 · 460 ppi"),
        ("Refresh rate", "ProMotion up to 120Hz · Always-On display"),
        ("Chip", "A17 Pro (3nm) · 6-core CPU · 6-core GPU · 16-core Neural Engine"),
        ("Graphics", "Up to 20% faster GPU than A16 Bionic · hardware ray tracing"),
        ("Main camera", "48MP · ƒ/1.78 · sensor-shift stabilisation · 2x option"),
        ("Ultra Wide camera", "12MP · 120° field of view"),
        ("Telephoto camera", "12MP · 5x optical zoom (120mm) · 3D sensor-shift stabilisation"),
        ("Zoom range", "Up to 25x digital zoom"),
        ("Front camera", "12MP TrueDepth · Face ID"),
        ("Video", "4K up to 60fps · ProRes (4K 60fps to an external drive) · Log recording"),
        ("Build", "Titanium frame · Ceramic Shield front · 221g"),
        ("Water and dust", "IP68 (up to 6 metres for 30 minutes)"),
        ("Battery", "Up to 29 hours video playback"),
        ("Charging", "USB-C · MagSafe and Qi2 up to 15W"),
        ("Data transfer", "USB 3 up to 10Gb/s (with a USB 3 cable)"),
        ("Connectivity", "5G · Wi-Fi 6E · Bluetooth 5.3 · NFC"),
        ("SIM", "Dual SIM (nano-SIM and eSIM)"),
        ("Safety", "Emergency SOS via satellite · Crash Detection"),
    ], after="Figures are Apple's."),

    cards("features", "What makes the iPhone 15 Pro Max stand out", None, [
        ("feat-15promax-zoom", "5x telephoto zoom",
         "A tetraprism design folds the light path inside the phone to give a 120mm, 5x optical zoom. That means sharp "
         "close-ups of sport, wildlife or a school play from your seat. It's the only iPhone 15 with 5x zoom."),
        ("feat-15promax-titanium", "Titanium, and lighter",
         "The aerospace-grade titanium frame cuts the weight to 221g, 19g less than the iPhone 14 Pro Max, which you "
         "notice on a phone this size. Ceramic Shield protects the front, with a textured matte glass back."),
        ("feat-15promax-a17", "A17 Pro chip",
         "Apple's first 3nm chip handles everyday tasks and heavy apps with ease. Its GPU is up to 20% faster than the "
         "A16 Bionic and adds hardware ray tracing, so console games such as Resident Evil Village and Assassin's "
         "Creed Mirage run on the phone itself."),
        ("feat-15promax-video", "Pro video over USB-C",
         "Shoot ProRes and Log video for professional editing, and record 4K at 60fps ProRes directly to an external "
         "drive. With a USB 3 cable, files move to a computer at up to 10Gb/s."),
        ("feat-15promax-battery", "Longest battery in the range",
         "Up to 29 hours of video playback, more than any other iPhone 15. MagSafe and Qi2 wireless charging run at up "
         "to 15W, and the USB-C port charges everything else you carry."),
        ("feat-15promax-ai", "Apple Intelligence",
         "The iPhone 15 Pro Max runs Apple Intelligence, including Writing Tools, Clean Up in Photos and a more capable "
         "Siri. Features arrive with iOS updates."),
    ]),

    lede("who-for", "Is the iPhone 15 Pro Max right for you?", [
        "It suits you if you want the biggest screen, the longest zoom and the longest battery life in the iPhone 15 "
        "range: for watching video, gaming, or photographing things you can't get close to. It's a natural upgrade "
        "from an older Pro Max, adding 5x zoom, USB-C and a lighter titanium build.",
        "If you'd prefer a phone you can use comfortably in one hand, the iPhone 15 Pro gives you the same chip, main "
        "camera and titanium design in a 6.1-inch size, with 3x zoom. Not sure which suits you? Ask in any of our "
        "stores and we'll talk you through the options.",
    ]),

    whyus("why-us", f"Why buy your {P} from CrC Repair®", [
        ("why-15promax-check", "60-point quality check",
         "Every device goes through a comprehensive 60-point check before it's sold, so you get top performance and "
         "reliability."),
        ("why-15promax-sources", "Verified, trusted stock",
         "All devices come from verified, trusted sources. We never sell grey-market or crime-linked stock."),
        ("why-15promax-accessories", "15% off accessories",
         "Get 15% off selected accessories with every device purchase."),
    ], intro="Every device we sell meets our own standards, backed by an award-winning UK repair business."),

    warranty("warranty", "Two-year warranty and free Device MOT", [
        ("warranty-15promax-phone", "Phone warranty", "Two years",
         f"A hassle-free two-year warranty covers your {P} from the day you buy it."),
        ("warranty-15promax-mot", "Free Device MOT", "Every 6 months",
         "Bring your iPhone in for a free Device MOT every six months to keep it running smoothly."),
    ], after="Warranty cover is subject to our " + L("/terms/", "terms and conditions") + ".<br>"
             "Looking for something else? Browse our " + L("/store/", "pre-owned phones and devices") + "."),

    cards("own-one", f"Already own an {P}?", "Whatever you need next, we can help:", [
        ("own-15promax-screen", "Screen repair",
         f"Cracked or unresponsive screen? We replace {P} screens with a lifetime warranty on the screen repair. "
         "Choose a premium screen or a " + L("/genuine-apple-parts/", "Genuine Apple part") + "."),
        ("own-15promax-repairs", "Battery and other repairs",
         "From " + L("/battery-replacement/", "battery replacement") + " to charging and camera faults, our "
         "technicians fix it in store with a one-year warranty. See our " + L("/iphone-repair/", "iPhone repair") +
         " service."),
        ("own-15promax-sell", "Sell or trade in",
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
PAGE:              WooCommerce product description — Apple iPhone 15 Pro Max
TEMPLATE:          claude/product-description-template-iphone-15-pro.html (approved 2 Nov 2026) + template guide
WHERE IT GOES:     Product > Description (the long description, NOT the short description).
                   Block editor: paste into the Code editor (Ctrl+Shift+Alt+M).
                   Classic editor: paste into the TEXT tab only and never switch to Visual.
SUGGESTED META (SEOPress):
  Title:        {META_TITLE}   ({len(META_TITLE)} chars, script-counted)
  Description:  {META_DESC}   ({len(META_DESC)} chars, script-counted)

Enquiry form: [contact-form-7 id="7e17e9a" title="Product enquiry"] (shared product form).
Warranties: device sold = two years + free Device MOT every 6 months; phone screen repairs = lifetime;
other repairs = one year.

CHANGES FROM THE OLD DESCRIPTION (specs checked against Apple's iPhone 15 Pro Max tech specs):
  - "Memory: 256GB, 512GB, 1TB" relabelled "Storage" (those are storage options; the phone has 8GB of RAM).
  - "Lighter yet more durable" replaced with the verified figure: 221g, 19g lighter than the iPhone 14 Pro Max.
  - "Console-level gaming" now names the console games released for it.
  - "Customizable" changed to British spelling. Store-locator link fixed (/store/store-locator/ -> /store-locator/).
  - Added: full spec list, 25x digital zoom, 29-hour battery, Apple Intelligence, Qi2, dual SIM, the size trade-off.

QUESTIONS FOR GABOR:
  1. Network status: are these handsets unlocked? The copy doesn't claim they are.
  2. Battery health: show a minimum (or the actual %) on listings?
  3. Box contents for pre-owned units? The FAQ only describes Apple's own box.

INTERNAL LINKS IN THIS PAGE ({len(hrefs)}):
{chr(10).join('  ' + h_ for h_ in hrefs)}
================================================================
-->
"""


build(OUT, sections, header, META_TITLE, META_DESC,
      ok_caps="iPhone Pro Max Apple Intelligence A17".split(),
      section_icons={"enquiry": "chat", "before-you-buy": "info", "specs": "cpu", "why-us": "star",
                     "warranty": "shield", "book": "wrench", "sell": "cash", "own-one": "phone"})

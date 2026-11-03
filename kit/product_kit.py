"""Shared builder for CrC WooCommerce product descriptions (.crc-page design system)."""
import json, re, html, os, sys

W = os.path.dirname(os.path.abspath(__file__))
B = "https://www.crcrepair.co.uk"
CSS = open(os.path.join(W, "css.html")).read().rstrip("\n")

def L(path, text):
    href = path if path.startswith(("http", "tel:", "mailto:")) else B + path
    return f'<a href="{href}">{text}</a>'


def para(text, cls=None, align=None):
    attrs = {}
    if cls: attrs["className"] = cls
    if align: attrs["align"] = align
    a = (" " + json.dumps(attrs)) if attrs else ""
    klass = ([f"has-text-align-{align}"] if align else []) + ([cls] if cls else [])
    c = f' class="{" ".join(klass)}"' if klass else ""
    return f"<!-- wp:paragraph{a} -->\n<p{c}>{text}</p>\n<!-- /wp:paragraph -->"


def head(level, text):
    a = "" if level == 2 else f' {{"level":{level}}}'
    return f'<!-- wp:heading{a} -->\n<h{level} class="wp-block-heading">{text}</h{level}>\n<!-- /wp:heading -->'


def group(cls, inner, anchor=None):
    attrs = {}
    if anchor: attrs["anchor"] = anchor
    attrs["className"] = cls
    idp = f' id="{anchor}"' if anchor else ""
    return (f"<!-- wp:group {json.dumps(attrs, separators=(',', ':'))} -->\n"
            f'<div class="wp-block-group {cls}"{idp}>\n{inner}\n</div>\n<!-- /wp:group -->')


def rawhtml(s):
    return f"<!-- wp:html -->\n{s}\n<!-- /wp:html -->"


def J(*parts):
    return "\n".join(p for p in parts if p)


def jumpnav(items):
    links = "\n".join(f'  <a href="#{a}">{t}</a>' for a, t in items)
    return rawhtml(f'<nav class="jumpnav" aria-label="On this page">\n{links}\n</nav>')


def chips(anchor, h2, intro, items, after=None):
    sp = "\n".join(f"  <span><b>{b}</b>{t}</span>" for b, t in items)
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            rawhtml(f'<div class="chips">\n{sp}\n</div>'),
                            para(after, cls="stores-after") if after else ""), anchor=anchor)


def cards(anchor, h2, intro, items, after=None, cols="c3", extra=None):
    cs = [group("card rcard", J(head(3, h3), *[para(x) for x in (body if isinstance(body, list) else [body])]), anchor=a)
          for a, h3, body in items]
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            group(f"grid {cols}", "\n\n".join(cs)),
                            para(after, cls="stores-after") if after else "", extra or ""), anchor=anchor)


def note(anchor, h2, paras):
    return group("block", J(head(2, h2), group("note card", J(*[para(p) for p in paras]))), anchor=anchor)


def lede(anchor, h2, paras, after=None):
    return group("block", J(head(2, h2), group("card lede", J(*[para(p) for p in paras])),
                            para(after, cls="stores-after") if after else ""), anchor=anchor)


def warranty(anchor, h2, items, after):
    cs = [group("warranty card", J(head(3, h3), para(big, cls="big"), para(t)), anchor=a) for a, h3, big, t in items]
    return group("block", J(head(2, h2), group("grid c2", "\n".join(cs)), para(after, cls="stores-after")), anchor=anchor)


def whyus(anchor, h2, tiles, intro=None):
    ts = [group("why-tile", J(head(3, h3), para(t)), anchor=a) for a, h3, t in tiles]
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            group("grid c3", "\n".join(ts))), anchor=anchor)


def cta_banner(h2, text, btns):
    acts = '<div class="actions">\n' + "\n".join(
        f'  <a class="btn {cls}" href="{B + href if href.startswith("/") else href}">{label}</a>' for cls, href, label in btns) + "\n</div>"
    return group("cta-banner", J(group("txt", J(head(2, h2), para(text))), rawhtml(acts)))


def faq(h2, items):
    ds = []
    for i, (fid, q, a) in enumerate(items):
        op = " open" if i == 0 else ""
        ds.append(f'<details{op} id="{fid}">\n  <summary><h3>{q}</h3></summary>\n  <div class="a">{a}</div>\n</details>')
    return group("block faq", J(head(2, h2), rawhtml("\n".join(ds))), anchor="faq")

ICONS = {  # simple stroke icons (inherit the pill's text colour, so they turn white on hover)
    "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/>',
    "cpu": '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M20 9h3M20 14h3M1 9h3M1 14h3"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "wrench": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    "phone": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
    "cash": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2"/><path d="M6 12h.01M18 12h.01"/>',
    "chat": '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
    "gamepad": '<rect x="2" y="6" width="20" height="12" rx="2"/><path d="M6 12h4M8 10v4M15 13h.01M18 11h.01"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


def jumpnav(items):
    """items: (anchor, label) or (anchor, label, icon-name)."""
    links = "\n".join(f'  <a href="#{it[0]}">{icon(it[2]) if len(it) > 2 else ""}{it[1]}</a>' for it in items)
    return rawhtml(f'<nav class="jumpnav" aria-label="On this page">\n{links}\n</nav>')


STORES = [  # (display name, tel digits, tel human) — store-information.md
    ("Bournemouth", "01202776491", "01202 776491"),
    ("Colchester", "01206573500", "01206 573500"),
    ("Farringdon", "02071015461", "020 7101 5461"),
    ("Glasgow", "01412219633", "0141 221 9633"),
    ("Norwich", "01603853209", "01603 853209"),
    ("Romford", "01708202461", "01708 202461"),
    ("Stoke-on-Trent", "07988300056", "07988 300056"),
    ("Surrey Quays", "02073455323", "020 7345 5323"),
    ("Whetstone", "02038415717", "020 3841 5717"),
    ("Wolverhampton", "01902953971", "01902 953971"),
]

# Product-page addition: capsule buttons for the 10-store block. Kept in its OWN style block so the
# shared .crc-page CSS block stays verbatim.
EXTRA_CSS = """<!-- wp:html -->
<style>
  .crc-page .jumpnav{justify-content:center!important}
  .crc-page .jumpnav a{display:inline-flex;align-items:center;gap:7px}
  .crc-page .jumpnav svg{width:16px;height:16px;flex-shrink:0;color:var(--accent)}
  .crc-page .jumpnav a:hover svg{color:#fff}
  .crc-page .storepills{justify-items:stretch}
  .crc-page .storepills a{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;text-decoration:none;background:var(--white);color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:14px 18px;box-shadow:0 2px 10px rgba(16,20,24,.05);transition:background .15s,border-color .15s,color .15s}
  .crc-page .storepills a strong{font-size:15px;font-weight:700;line-height:1.3}
  .crc-page .storepills a:hover,.crc-page .storepills a:focus-visible{background:var(--accent);border-color:var(--accent);color:#fff}
  @media (max-width:560px){
    .crc-page .grid.c5.storepills{grid-template-columns:repeat(2,1fr);gap:10px}
    .crc-page .storepills a{padding:10px 12px}
    .crc-page .storepills a strong{font-size:14px}
  }
</style>
<!-- /wp:html -->"""


def storepills(anchor, h2, intro, after):
    pills = "\n".join(f'  <a href="tel:{d}" aria-label="Call Pocket Geek {n} on {h}"><strong>{n}</strong></a>'
                      for n, d, h in STORES)
    return group("block", J(head(2, h2), para(intro, cls="sectionintro"),
                            rawhtml(f'<div class="grid c5 storepills">\n{pills}\n</div>'),
                            para(after, cls="stores-after")), anchor=anchor)


def build(out_path, sections, header_fn, meta_title, meta_desc, ok_caps=(), section_icons=None):
    body = "\n\n".join(sections)
    page = (f'<!-- wp:group {{"className":"crc-page"}} -->\n<div class="wp-block-group crc-page">\n\n{body}\n\n'
            f'</div>\n<!-- /wp:group -->')
    if section_icons:
        page = add_heading_icons(page, section_icons)
    hrefs = []
    for h_ in re.findall(r'href="([^"#][^"]*)"', page):
        if h_ not in hrefs:
            hrefs.append(h_)
    hdr = header_fn(hrefs)
    assert "-->" not in hdr[4:-5], "comment close inside header"
    out = hdr + "\n" + CSS + "\n\n" + EXTRA_CSS + "\n\n" + page + "\n"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w").write(out)
    probs = []
    if len(re.findall(r"<!-- wp:(?!.*?/-->)", out)) != out.count("<!-- /wp:"): probs.append("wp open/close mismatch")
    if out.count("<!-- wp:group") != out.count("<!-- /wp:group"): probs.append("group mismatch")
    if len(re.findall(r"<div\b", page)) != page.count("</div>"): probs.append("div mismatch")
    if re.search(r"<h1", page): probs.append("H1 present")
    levels = [int(x) for x in re.findall(r"<h(\d)", page)]
    if levels[0] != 2: probs.append("first heading not H2")
    for a, b in zip(levels, levels[1:]):
        if b > a + 1: probs.append(f"skipped {a}->{b}")
    ids = re.findall(r'id="([^"]+)"', page)
    for a in re.findall(r'<a href="#([^"]+)"', page):
        if a not in ids: probs.append(f"missing anchor #{a}")
    if len(ids) != len(set(ids)): probs.append("duplicate ids")
    if "repairs/" in out.replace("high-quality-repairs/", ""): probs.append("plural repairs URL")
    caps = set("CrC Repair® Device MOT FAQ I".split()) | set(ok_caps)
    for hd in re.findall(r"<h[23][^>]*>(.*?)</h[23]>", page):
        t = re.sub(r"<[^>]+>", "", html.unescape(hd))
        for w_ in re.findall(r"[A-Za-z][\w'®\-]*", t)[1:]:
            if w_[0].isupper() and w_ not in caps: probs.append(f"sentence case? '{w_}' in: {t}")
    print("PROBLEMS:", probs or "none")
    print("title", len(meta_title), "desc", len(meta_desc))
    print("links:", hrefs)
    print(out_path, os.path.getsize(out_path), "bytes")


def speclist(anchor, h2, intro, items, after=None):
    """Specs as ONE card containing a native Gutenberg bulleted list."""
    lis = "\n".join(f"<!-- wp:list-item -->\n<li><strong>{b}:</strong> {t}</li>\n<!-- /wp:list-item -->" for b, t in items)
    lst = f'<!-- wp:list -->\n<ul class="wp-block-list">\n{lis}\n</ul>\n<!-- /wp:list -->'
    return group("block", J(head(2, h2), para(intro, cls="sectionintro") if intro else "",
                            group("card lede", lst),
                            para(after, cls="stores-after") if after else ""), anchor=anchor)



# ---- section heading icons: a CSS mask on h2::before, so the heading block markup stays plain Gutenberg
from urllib.parse import quote as _q


def _icon_uri(name):
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' "
           f"stroke-linecap='round' stroke-linejoin='round'>{ICONS[name]}</svg>").replace('"', "'")
    return "data:image/svg+xml," + _q(svg, safe="/:=' ")


ICON_CSS = "\n".join(
    [".crc-page h2[class*='crc-ico-']::before{content:\"\";display:inline-block;width:.95em;height:.95em;"
     "margin-right:10px;vertical-align:-.12em;background-color:var(--accent);"
     "-webkit-mask:var(--ico) no-repeat center/contain;mask:var(--ico) no-repeat center/contain}",
     ".crc-page .cta-banner h2[class*='crc-ico-']::before{background-color:#fff}"]
    + [f".crc-page h2.crc-ico-{n}{{--ico:url(\"{_icon_uri(n)}\")}}" for n in ICONS])


def add_heading_icons(page, mapping):
    """mapping: {section anchor: icon name}. Adds a class to that section's first H2 (valid Gutenberg markup)."""
    for anchor, name in mapping.items():
        i = page.index(f'id="{anchor}"')
        old = '<!-- wp:heading -->\n<h2 class="wp-block-heading">'
        j = page.index(old, i)
        new = (f'<!-- wp:heading {{"className":"crc-ico-{name}"}} -->\n'
               f'<h2 class="wp-block-heading crc-ico-{name}">')
        page = page[:j] + new + page[j + len(old):]
    return page

EXTRA_CSS = EXTRA_CSS.replace("</style>", "  " + ICON_CSS.replace("\n", "\n  ") + "\n</style>")


def cta_pair(left, right, anchor="book"):
    """Two equal (50/50) cta-banners side by side; each is (h2, text, btns, anchor-or-None). Stacks on mobile."""
    def one(h2, text, btns, a, cls="cta-banner"):
        acts = '<div class="actions">\n' + "\n".join(
            f'  <a class="btn {cls}" href="{B + href if href.startswith("/") else href}">{label}</a>' for cls, href, label in btns) + "\n</div>"
        return group(cls, J(group("txt", J(head(2, h2), para(text))), rawhtml(acts)), anchor=a)
    return group("block", group("grid c2", J(one(*left), one(*right, cls="cta-banner sell"))), anchor=anchor)


# light-grey variant for the right-hand "sell" banner
SELL_CSS = """.crc-page .cta-banner.sell{background:#eef1f5;color:var(--ink);border:1px solid var(--line)}
.crc-page .cta-banner.sell h2{color:var(--ink)}
.crc-page .cta-banner.sell h2::after{background:var(--accent)}
.crc-page .cta-banner.sell p{color:var(--ink-soft)}
.crc-page .cta-banner.sell h2[class*='crc-ico-']::before{background-color:var(--accent)}
.crc-page .cta-banner.sell .btn.light{background:var(--accent);color:#fff}
.crc-page .cta-banner.sell .btn.light:hover{background:var(--accent-dark);color:#fff}
.crc-page .cta-banner.sell .btn.ghost{border-color:var(--accent);color:var(--accent)}
.crc-page .cta-banner.sell .btn.ghost:hover{background:rgba(65,128,213,.08);color:var(--accent-dark)}"""
EXTRA_CSS = EXTRA_CSS.replace("</style>", "  " + SELL_CSS.replace("\n", "\n  ") + "\n</style>")



# ---- template: overview (left) + Contact Form 7 "Any questions?" box (right), 50/50, stacks on mobile
ENQUIRY_SHORTCODE = '[contact-form-7 id="7e17e9a" title="Product enquiry"]'
ENQUIRY_CSS = """<style>
  .crc-page .ov-split{align-items:stretch}
  .crc-page .ov-col{display:flex;flex-direction:column}
  .crc-page .ov-col > .card{flex:1}
  .crc-page .enquiry.card{background:var(--accent);border-color:var(--accent);color:#fff}
  .crc-page .enquiry h2{color:#fff}
  .crc-page .enquiry h2::after{background:#fff}
  .crc-page .enquiry h2[class*='crc-ico-']::before{background-color:#fff}
  .crc-page .enquiry .wpcf7-form p{margin:0 0 12px}
  .crc-page .enquiry .wpcf7-form p:last-of-type{margin-bottom:0}
  .crc-page .enquiry .wpcf7-form br{display:none}
  .crc-page .enquiry .wpcf7-form label{display:block;font-size:14px;font-weight:600;color:#fff}
  .crc-page .enquiry .wpcf7-form-control-wrap{display:block;margin-top:6px}
  .crc-page .enquiry .wpcf7-form input.wpcf7-text,.crc-page .enquiry .wpcf7-form input.wpcf7-tel,
  .crc-page .enquiry .wpcf7-form input.wpcf7-email,.crc-page .enquiry .wpcf7-form textarea{display:block!important;width:100%!important;
    box-sizing:border-box!important;margin:0!important;padding:11px 14px!important;border:1px solid rgba(255,255,255,.7)!important;
    border-radius:10px!important;background:#fff!important;color:var(--ink)!important;font-family:inherit!important;font-size:15px!important;
    line-height:1.4!important;box-shadow:none!important}
  .crc-page .enquiry .wpcf7-form textarea{height:120px!important;min-height:120px;resize:vertical}
  .crc-page .enquiry .wpcf7-form input:focus,.crc-page .enquiry .wpcf7-form textarea:focus{outline:3px solid rgba(255,255,255,.55)!important;outline-offset:1px}
  .crc-page .enquiry .wpcf7-form input.wpcf7-submit{display:block!important;width:100%!important;margin:4px 0 0!important;padding:13px 20px!important;
    border:0!important;border-radius:999px!important;background:#fff!important;color:var(--accent)!important;font-family:inherit!important;
    font-size:15px!important;font-weight:700!important;text-transform:none!important;letter-spacing:normal!important;box-shadow:none!important;cursor:pointer}
  .crc-page .enquiry .wpcf7-form input.wpcf7-submit:hover{background:#dbe7f7!important;color:var(--accent-dark)!important}
  .crc-page .enquiry .wpcf7-form p:has(.wpcf7-submit){position:relative}
  .crc-page .enquiry .wpcf7-spinner{position:absolute!important;right:16px;top:50%;margin:-12px 0 0!important}
  .crc-page .enquiry .wpcf7-not-valid-tip{color:#ffe08a;font-size:13px;font-weight:600;margin-top:4px}
  .crc-page .enquiry .wpcf7-not-valid{border-color:#ffe08a!important}
  .crc-page .enquiry .wpcf7 form .wpcf7-response-output{margin:14px 0 0;padding:10px 14px;border:1px solid rgba(255,255,255,.8);border-radius:10px;color:#fff;font-size:14px}
</style>"""


def overview_enquiry(h2, paras):
    return group("block", group("grid c2 ov-split", J(
        group("ov-col", J(head(2, h2), group("card lede", J(*[para(x) for x in paras])))),
        group("card enquiry", J(head(2, "Any questions?"), rawhtml(ENQUIRY_CSS),
                                "<!-- wp:shortcode -->\n" + ENQUIRY_SHORTCODE + "\n<!-- /wp:shortcode -->"), anchor="enquiry"),
    )), anchor="overview")


# ---- SEO pack: schema file + SEOPress/social/image copy (added 2 Nov 2026)
def _plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def build_schema(out_path, product_url, name, brand, model, description, props, faq_items, category="Mobile phones"):
    """Product node with WooCommerce's own @id (<url>#product) so Google merges it with WooCommerce's
    Product schema (which keeps price/stock). No offers here. Plus FAQPage from the on-page FAQs."""
    pid = product_url + "#product"
    product = {"@type": "Product", "@id": pid, "name": name, "url": product_url,
               "brand": {"@type": "Brand", "name": brand}, "model": model, "category": category,
               "description": description,
               "additionalProperty": [{"@type": "PropertyValue", "name": k, "value": v} for k, v in props]}
    faqpage = {"@type": "FAQPage", "@id": product_url + "#faq", "about": {"@id": pid},
               "mainEntity": [{"@type": "Question", "name": _plain(q),
                               "acceptedAnswer": {"@type": "Answer", "text": _plain(a)}} for _, q, a in faq_items]}
    js = json.dumps({"@context": "https://schema.org", "@graph": [product, faqpage]}, ensure_ascii=False, indent=2)
    json.loads(js)
    assert "&amp;" not in js
    hdr = f"""<!--
SCHEMA (JSON-LD) for: {name}
URL: {product_url}
Paste as a Custom HTML block at the END of the long description (block editor), or at the end of the Text tab
(classic editor). It ADDS to WooCommerce's Product schema: same @id ({pid}), so Google merges the two.
Price, stock and offers stay with WooCommerce. FAQ text matches the on-page FAQ word for word.
Check after publishing: Google Rich Results Test on the product URL should show ONE Product item plus the FAQ.
-->
"""
    out = hdr + '<!-- wp:html -->\n<script type="application/ld+json">\n' + js + "\n</script>\n<!-- /wp:html -->\n"
    open(out_path, "w").write(out)
    return js


def seo_pack(out_path, product, rows, images, notes=(), tags=None):
    """rows: [(label, value, limit_text)] ; images: [(slot, alt, description)]"""
    def esc(s): return html.escape(s, quote=False)
    trs = "\n".join(f'<tr><th>{esc(l)}</th><td><div class="v">{esc(v)}</div><div class="n">{len(v)} characters · {esc(lim)}</div></td></tr>'
                    for l, v, lim in rows)
    imgs = "\n".join(f'<tr><th>{esc(s)}</th><td><div class="lab">Alt text</div><div class="v">{esc(a)}</div>'
                     f'<div class="lab">Description</div><div class="v">{esc(d)}</div></td></tr>' for s, a, d in images)
    nts = "".join(f"<li>{n}</li>" for n in notes)
    tag_html = ""
    if tags:
        chips = "".join(f'<span class="tag">{esc(t)}</span>' for t, _ in tags)
        why = "\n".join(f"<tr><th>{esc(t)}</th><td>{esc(w)}</td></tr>" for t, w in tags)
        tag_html = (f'<h2>WooCommerce product tags</h2><p class="sub">Add these in Products → Edit → Product tags. '
                    f'Copy-paste line: <span class="v">{esc(", ".join(t for t, _ in tags))}</span></p>'
                    f'<div class="tags">{chips}</div><table>{why}</table>')
    doc = f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>SEO pack: {esc(product)}</title>
<style>
 body{{margin:0;background:#f6f7f9;font-family:Montserrat,system-ui,-apple-system,sans-serif;color:#101418;line-height:1.55}}
 .wrap{{max-width:900px;margin:0 auto;padding:30px 22px 60px}} h1{{font-size:24px;margin:0 0 4px}} .sub{{color:#3d4650;margin:0 0 24px}}
 h2{{font-size:17px;margin:30px 0 10px;padding-bottom:8px;border-bottom:3px solid #4180d5}}
 table{{width:100%;border-collapse:separate;border-spacing:0 10px}} th{{text-align:left;vertical-align:top;width:190px;padding:12px 14px;font-size:14px;color:#3d4650}}
 td{{background:#fff;border:1px solid #dfe4e9;border-radius:10px;padding:12px 14px}}
 .v{{font-size:15px;user-select:all}} .n{{font-size:12.5px;color:#6b7580;margin-top:6px}} .lab{{font-size:12px;font-weight:700;color:#2c5da3;margin:6px 0 2px}}
 .lab:first-child{{margin-top:0}} ul{{color:#3d4650;padding-left:20px}}
 .tags{{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 4px}} .tag{{background:#fff;border:1px solid #dfe4e9;border-left:4px solid #4180d5;border-radius:999px;padding:6px 14px;font-weight:600;font-size:14px}}
 @media (max-width:640px){{th{{display:block;width:auto;padding:4px 2px}} td{{display:block}} tr{{display:block;margin-bottom:12px}}}}
</style></head><body><div class="wrap">
<h1>SEO pack: {esc(product)}</h1>
<p class="sub">Paste into SEOPress (Titles &amp; metas and Social tabs) and the Media Library. Click a value once to select it. Counts are script-counted.</p>
<h2>SEOPress and social</h2>
<table>{trs}</table>
{tag_html}
<h2>Product images: alt text and description</h2>
<table>{imgs}</table>
<h2>Notes</h2><ul>{nts}</ul>
</div></body></html>"""
    open(out_path, "w").write(doc)

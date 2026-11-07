#!/usr/bin/env python3
"""Structural checks for a homepage HTML export + its schema file.

Usage: python3 homepage/check_homepage.py homepage/home_page_v2.1.html homepage/home_page_schema_v2.html
Checks: Gutenberg block open/close balance, <div> balance, exactly one H1, no skipped heading levels,
every #anchor target exists, unique ids, no URL ending in "repairs", no "click here", valid JSON-LD,
and every visible FAQ question/answer present word for word in the FAQPage node.
"""
import html, json, re, sys


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def main(page_path, schema_path):
    out = open(page_path, encoding="utf-8").read()
    probs = []
    opens = len(re.findall(r"<!-- wp:(?!.*?/-->)", out))
    closes = out.count("<!-- /wp:")
    if opens != closes: probs.append(f"wp open/close mismatch {opens}/{closes}")
    if len(re.findall(r"<div\b", out)) != out.count("</div>"): probs.append("div mismatch")
    if len(re.findall(r"<h1\b", out)) != 1: probs.append("H1 count != 1")
    levels = [int(x) for x in re.findall(r"<h(\d)", out)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1: probs.append(f"skipped heading {a}->{b}")
    ids = re.findall(r'\sid="([^"]+)"', out)
    for a in re.findall(r'href="#([^"]+)"', out):
        if a not in ids: probs.append(f"missing anchor #{a}")
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes: probs.append(f"duplicate ids {sorted(dupes)}")
    for h in re.findall(r'href="([^"]+)"', out):
        if h.rstrip("/").endswith("repairs"): probs.append(f"URL ends in repairs: {h}")
    if "click here" in out.lower(): probs.append("'click here' link text")
    if re.match(r"\s*<p>\s*<!--", out): probs.append("file starts with a <p>-wrapped comment (WordPress classic-block artefact)")

    txt = open(schema_path, encoding="utf-8").read()
    body = re.search(r"<script[^>]*>(.*)</script>", txt, re.S).group(1)
    graph = json.loads(body)
    faq_nodes = [n for n in graph["@graph"] if n.get("@type") == "FAQPage"]
    if len(faq_nodes) != 1: probs.append("FAQPage node count != 1")
    qs = re.findall(r"<summary><h3>(.*?)</h3></summary>\s*<div class=\"a\">(.*?)</div>", out, re.S)
    sq = {(e["name"], e["acceptedAnswer"]["text"]) for e in faq_nodes[0]["mainEntity"]} if faq_nodes else set()
    pq = {(strip_tags(q), strip_tags(a).strip()) for q, a in qs}
    if pq != sq:
        probs.append(f"FAQ mismatch: page-only={sorted(x[0] for x in pq - sq)} schema-only={sorted(x[0] for x in sq - pq)}")
    print("PROBLEMS:", probs or "none")
    print("headings:", "".join(f"h{l}" for l in levels))
    print(f"FAQ pairs on page {len(pq)}, in schema {len(sq)}; schema nodes {len(graph['@graph'])}")
    return 1 if probs else 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))

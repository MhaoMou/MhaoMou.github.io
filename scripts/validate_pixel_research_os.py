#!/usr/bin/env python3
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
LEGACY_INDEX = ROOT / "index.md"
CSS = ROOT / "assets/css/pixel-research-os.css"
JS = ROOT / "assets/js/pixel-research-os.js"

REQUIRED_FILES = [
    "assets/files/curriculum_vitae.pdf",
    "assets/img/IMG_5612.jpeg",
    "assets/img/avatar.png",
    "assets/img/braess_fig6.png",
    "assets/img/comp.jpg",
    "assets/img/favicon.png",
    "assets/img/favicon-dark.png",
]

REQUIRED_TEXT = [
    "MINGHAO.EXE",
    "Pixel Research OS",
    "Minghao Mou",
    "Ph.D. candidate",
    "Elmore Family School of Electrical and Computer Engineering",
    "Purdue University",
    "Dr. Junjie Qin",
    "Chinese University of Hong Kong, Shenzhen",
    "Dr. Shuang Li",
    "mmou@purdue.edu",
    "Coupled Energy Infrastructure Systems",
    "Generative Models",
    "Optimal Control",
    "Braess' Paradoxes in Coupled Power and Transportation Systems",
    "Nexus Cognizant Pricing of Workplace Electric Vehicle Charging",
    "Sean Qian",
    "Preprint",
    "Oral Presentation",
    "American Control Conference, 2024",
    "arXiv preprint arXiv:2512.12197, 2025",
    "May 2026",
    "Apr. 2026",
    "Dec. 2025",
    "Dec. 2023",
    "May 2023",
]

REQUIRED_IDS = [
    "about",
    "research",
    "news",
    "publications",
    "projects",
    "teaching",
    "cv",
    "contact",
]

REQUIRED_LINKS = [
    "assets/css/pixel-research-os.css",
    "assets/js/pixel-research-os.js",
    "assets/files/curriculum_vitae.pdf",
    "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en",
    "https://github.com/MhaoMou",
    "https://www.linkedin.com/in/minghao-mou-14a090289/",
    "https://arxiv.org/pdf/2512.12197",
    "https://arxiv.org/abs/2512.12197",
    "https://doi.org/10.48550/arXiv.2512.12197",
    "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866",
    "https://scholar.googleusercontent.com/scholar.bib?q=info:2aKsKkaCZN8J:scholar.google.com/&output=citation&scisdr=ClEwu4xGEIz_i9RBe8o:AFWwaeYAAAAAZ2NHY8rMyvVbiTtta4oAMCCgeKw&scisig=AFWwaeYAAAAAZ2NHY9hCxuAekf9tLmJHrGasrPE&scisf=4&ct=citation&cd=-1&hl=en",
]


class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.section_ids = set()
        self.alt_texts = []
        self.hrefs = []
        self.srcs = []
        self.links = set()
        self.has_main = False
        self.has_nav = False
        self.has_h1 = False
        self.buttons = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
            if tag == "section":
                self.section_ids.add(attrs["id"])
        if tag == "img":
            self.alt_texts.append(attrs.get("alt", ""))
            if attrs.get("src"):
                self.add_src(attrs["src"])
        if tag in {"a", "link"} and attrs.get("href"):
            self.add_href(attrs["href"])
        if tag == "script" and attrs.get("src"):
            self.add_src(attrs["src"])
        if tag == "main":
            self.has_main = True
        if tag == "nav":
            self.has_nav = True
        if tag == "h1":
            self.has_h1 = True
        if tag == "button" or (tag == "a" and "button" in attrs.get("class", "")):
            self.buttons += 1

    def add_href(self, value):
        normalized = unescape(value)
        self.hrefs.append(normalized)
        self.links.add(normalized)

    def add_src(self, value):
        normalized = unescape(value)
        self.srcs.append(normalized)
        self.links.add(normalized)


def fail(message):
    print(f"FAIL: {message}")
    return 1


def main():
    failures = []

    if not INDEX.exists():
        failures.append("index.html is missing")
    if not CSS.exists():
        failures.append("assets/css/pixel-research-os.css is missing")
    if not JS.exists():
        failures.append("assets/js/pixel-research-os.js is missing")
    if LEGACY_INDEX.exists():
        failures.append("index.md still exists; rename it after migrating content")

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"required asset missing: {rel}")

    html = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
    js = JS.read_text(encoding="utf-8") if JS.exists() else ""

    for text in REQUIRED_TEXT:
        if text not in html:
            failures.append(f"required text missing from index.html: {text}")

    parser = StructureParser()
    parser.feed(html)

    for link in REQUIRED_LINKS:
        if unescape(link) not in parser.links:
            failures.append(f"required link missing from index.html: {link}")

    if not parser.has_main:
        failures.append("index.html needs a <main> landmark")
    if not parser.has_nav:
        failures.append("index.html needs a <nav> landmark")
    if not parser.has_h1:
        failures.append("index.html needs an <h1>")

    for section_id in REQUIRED_IDS:
        if section_id not in parser.section_ids:
            failures.append(f"required section id missing: {section_id}")

    if any(not alt.strip() for alt in parser.alt_texts):
        failures.append("all images need non-empty alt text")

    if "prefers-reduced-motion" not in css:
        failures.append("CSS must include prefers-reduced-motion handling")
    if ":focus-visible" not in css:
        failures.append("CSS must include visible focus styles")
    if "--accent" not in css or "--bg" not in css:
        failures.append("CSS must define centralized design tokens")
    if "matchMedia" not in js:
        failures.append("JS must use matchMedia for reduced-motion or responsive behavior")

    if re.search(r"Level\s+\d+|95%|99%", html, re.IGNORECASE):
        failures.append("remove fake skill levels or gamified expertise claims")
    blocked_markers = ("TO" + "DO", "TB" + "D", "FIX" + "ME")
    if any(marker in html + css + js for marker in blocked_markers):
        failures.append("remove unfinished implementation markers")

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    print("PASS: Pixel Research OS static validation")
    return 0

if __name__ == "__main__":
    sys.exit(main())

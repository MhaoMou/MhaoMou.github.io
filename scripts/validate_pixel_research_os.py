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
CONFIG = ROOT / "_config.yml"
SITE = ROOT / "_site"

LEGACY_ACC_BIBTEX_URL = (
    "https://scholar.googleusercontent.com/scholar.bib?"
    "q=info:2aKsKkaCZN8J:scholar.google.com/&output=citation&"
    "scisdr=ClEwu4xGEIz_i9RBe8o:AFWwaeYAAAAAZ2NHY8rMyvVbiTtta4oAMCCgeKw&"
    "scisig=AFWwaeYAAAAAZ2NHY9hCxuAekf9tLmJHrGasrPE&scisf=4&ct=citation&"
    "cd=-1&hl=en"
)

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

REQUIRED_ANCHOR_HREFS = [
    "assets/files/curriculum_vitae.pdf",
    "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en",
    "https://github.com/MhaoMou",
    "https://www.linkedin.com/in/minghao-mou-14a090289/",
    "https://arxiv.org/pdf/2512.12197",
    "https://arxiv.org/abs/2512.12197",
    "https://doi.org/10.48550/arXiv.2512.12197",
    "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866",
    LEGACY_ACC_BIBTEX_URL,
]

REQUIRED_STYLESHEET_HREFS = [
    "assets/css/pixel-research-os.css",
]

REQUIRED_SCRIPT_SRCS = [
    "assets/js/pixel-research-os.js",
]

REQUIRED_IMAGE_SRCS = [
    "assets/img/IMG_5612.jpeg",
    "assets/img/braess_fig6.png",
    "assets/img/comp.jpg",
]

REQUIRED_FAVICON_HREFS = [
    "assets/img/favicon.png",
    "assets/img/favicon-dark.png",
]

REQUIRED_V2_CLASSES = [
    "desktop-shell",
    "desktop-titlebar",
    "desktop-workspace",
    "hero-desktop",
    "lab-console",
    "identity-panel",
    "desktop-taskbar",
    "command-center",
    "research-module",
    "paper-record",
    "system-log",
    "terminal-panel",
]

FORBIDDEN_HERO_IMAGE_SRC = "assets/img/IMG_5612.jpeg"
ABOUT_PORTRAIT_SRC = "assets/img/IMG_5612.jpeg"

VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

NON_RENDERED_TAGS = {"script", "style", "template"}

REQUIRED_EXCLUDES = [
    "legacy-index.md",
    "docs/superpowers/",
    "scripts/",
]


class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.section_ids = set()
        self.image_alts = []
        self.text_parts = []
        self.skip_text_depth = 0
        self.anchors = set()
        self.stylesheets = set()
        self.favicons = set()
        self.scripts = set()
        self.images = set()
        self.classes = set()
        self.hero_image_srcs = []
        self.about_image_srcs = []
        self.scope_stack = []
        self.nonrendered_stack = []
        self.has_main = False
        self.has_nav = False
        self.has_h1 = False

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs = dict(attrs)
        if attrs.get("class"):
            self.classes.update(attrs["class"].split())
        if tag not in VOID_ELEMENTS:
            starts_nonrendered = tag in NON_RENDERED_TAGS or "hidden" in attrs
            if starts_nonrendered:
                self.skip_text_depth += 1
            self.nonrendered_stack.append(starts_nonrendered)
            explicit_scope = scope_for_attrs(attrs)
            inherited_scope = self.scope_stack[-1] if self.scope_stack else ""
            self.scope_stack.append(explicit_scope or inherited_scope)
        if tag == "section" and attrs.get("id"):
            self.section_ids.add(attrs["id"])
        if tag == "img":
            src = self.normalize(attrs.get("src", ""))
            alt = self.normalize(attrs.get("alt", ""))
            self.image_alts.append((src, alt))
            if src:
                self.images.add(src)
            current_scope = scope_for_attrs(attrs) or (self.scope_stack[-1] if self.scope_stack else "")
            if current_scope == "hero" and src:
                self.hero_image_srcs.append(src)
            if current_scope == "about" and src:
                self.about_image_srcs.append(src)
        if tag == "a" and attrs.get("href"):
            self.anchors.add(self.normalize(attrs["href"]))
        if tag == "link" and attrs.get("href"):
            rel_tokens = set(self.normalize(attrs.get("rel", "")).lower().split())
            if "stylesheet" in rel_tokens:
                self.stylesheets.add(self.normalize(attrs["href"]))
            if "icon" in rel_tokens:
                self.favicons.add(self.normalize(attrs["href"]))
        if tag == "script" and attrs.get("src"):
            self.scripts.add(self.normalize(attrs["src"]))
        if tag == "main":
            self.has_main = True
        if tag == "nav":
            self.has_nav = True
        if tag == "h1":
            self.has_h1 = True

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag not in VOID_ELEMENTS and self.scope_stack:
            self.scope_stack.pop()
        if tag not in VOID_ELEMENTS and self.nonrendered_stack:
            if self.nonrendered_stack.pop() and self.skip_text_depth:
                self.skip_text_depth -= 1

    def handle_data(self, data):
        if not self.skip_text_depth:
            self.text_parts.append(data)

    def normalize(self, value):
        return unescape(value)


def scope_for_attrs(attrs):
    element_id = attrs.get("id") or ""
    class_tokens = set((attrs.get("class") or "").split())
    if element_id in {"hero", "about"}:
        return element_id
    if "hero-desktop" in class_tokens:
        return "hero"
    return ""


def normalize_visible_text(value):
    return " ".join(unescape(value).split())


def strip_css_comments(value):
    return re.sub(r"/\*.*?\*/", "", value, flags=re.DOTALL)


def strip_js_comments(value):
    result = []
    index = 0
    quote = None
    escaped = False

    while index < len(value):
        char = value[index]
        next_char = value[index + 1] if index + 1 < len(value) else ""

        if quote:
            result.append(char)
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            index += 1
            continue

        if char in {"'", '"', "`"}:
            quote = char
            result.append(char)
            index += 1
            continue

        if char == "/" and next_char == "/":
            index += 2
            while index < len(value) and value[index] not in "\r\n":
                index += 1
            if index < len(value):
                result.append(value[index])
                index += 1
            continue

        if char == "/" and next_char == "*":
            index += 2
            while index + 1 < len(value) and value[index:index + 2] != "*/":
                index += 1
            index = min(index + 2, len(value))
            result.append(" ")
            continue

        result.append(char)
        index += 1

    return "".join(result)


def has_reduced_motion_rule(css):
    return re.search(
        r"@media[^{]*prefers-reduced-motion[^{]*\{",
        strip_css_comments(css),
        re.IGNORECASE,
    )


def has_focus_visible_selector(css):
    return re.search(r":focus-visible\b[^{}]*\{", strip_css_comments(css))


def has_design_tokens(css):
    uncommented_css = strip_css_comments(css)
    return (
        re.search(r"--accent\s*:", uncommented_css)
        and re.search(r"--bg\s*:", uncommented_css)
    )


def has_match_media_call(js):
    return re.search(r"\bmatchMedia\s*\(", strip_js_comments(js))


def has_viewport_scaled_font_size(css):
    return re.search(
        r"\bfont(?:-size)?\s*:[^;{}]*[0-9.]\s*(?:vw|vh|vmin|vmax)\b",
        strip_css_comments(css),
        re.IGNORECASE,
    )


def has_forbidden_cursor(css):
    return re.search(r"cursor\s*:\s*crosshair\b", strip_css_comments(css), re.IGNORECASE)


def has_forbidden_background_effect(css):
    return re.search(r"\bradial-gradient\s*\(", strip_css_comments(css), re.IGNORECASE)


def has_large_border_radius(css):
    uncommented_css = strip_css_comments(css)
    border_radius_values = re.findall(
        r"\bborder(?:-[a-z]+)*-radius\s*:\s*([^;{}]+)",
        uncommented_css,
        re.IGNORECASE,
    )

    for value in border_radius_values:
        if re.search(r"\b(?:var|calc)\s*\(", value, re.IGNORECASE):
            return True
        for number, unit in re.findall(
            r"(-?(?:\d+|\d*\.\d+))\s*(px|%|rem|em)\b",
            value,
            re.IGNORECASE,
        ):
            radius = float(number)
            normalized_unit = unit.lower()
            if normalized_unit == "px" and radius > 9:
                return True
            if normalized_unit in {"%", "rem", "em"} and radius != 0:
                return True

    return False


def has_soft_visual_effect(css):
    uncommented_css = strip_css_comments(css)
    if re.search(r"\bbackdrop-filter\s*:", uncommented_css, re.IGNORECASE):
        return True
    if re.search(r"(?<!-)filter\s*:[^;{}]*\bblur\s*\(", uncommented_css, re.IGNORECASE):
        return True

    box_shadow_values = re.findall(
        r"\bbox-shadow\s*:\s*([^;{}]+)",
        uncommented_css,
        re.IGNORECASE,
    )
    for value in box_shadow_values:
        for length in re.findall(r"(-?(?:\d+|\d*\.\d+))\s*px\b", value, re.IGNORECASE):
            if float(length) >= 16:
                return True

    return False


def has_paper_database_label(text):
    return "PAPER_DATABASE" in text or "PAPER DATABASE" in text


def has_system_log_label(text):
    return "SYSTEM LOG" in text


def has_fake_expertise_claim(text):
    return re.search(
        r"\blevel\s+\d+\b|"
        r"(?<!\d)(?:90|95|99)\s*(?:%|\bpercent\b)(?!\d)|"
        r"(?<!\d)(?:5\s*/\s*5|10\s*/\s*10)(?!\d)|"
        r"\bexpert\s+level\b",
        text,
        re.IGNORECASE,
    )


def main():
    failures = []

    if not INDEX.exists():
        failures.append("index.html is missing")
    if not CSS.exists():
        failures.append("assets/css/pixel-research-os.css is missing")
    if not JS.exists():
        failures.append("assets/js/pixel-research-os.js is missing")
    if not CONFIG.exists():
        failures.append("_config.yml is missing")
    if LEGACY_INDEX.exists():
        failures.append("index.md still exists; rename it after migrating content")

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"required asset missing: {rel}")

    html = INDEX.read_text(encoding="utf-8") if INDEX.exists() else ""
    css = CSS.read_text(encoding="utf-8") if CSS.exists() else ""
    js = JS.read_text(encoding="utf-8") if JS.exists() else ""
    config = CONFIG.read_text(encoding="utf-8") if CONFIG.exists() else ""

    parser = StructureParser()
    parser.feed(html)
    visible_text = normalize_visible_text(" ".join(parser.text_parts))

    for text in REQUIRED_TEXT:
        if normalize_visible_text(text) not in visible_text:
            failures.append(f"required text missing from index.html: {text}")

    for link in REQUIRED_ANCHOR_HREFS:
        if unescape(link) not in parser.anchors:
            failures.append(f"required anchor href missing from index.html: {link}")
    for link in REQUIRED_STYLESHEET_HREFS:
        if unescape(link) not in parser.stylesheets:
            failures.append(f"required stylesheet href missing from index.html: {link}")
    for link in REQUIRED_SCRIPT_SRCS:
        if unescape(link) not in parser.scripts:
            failures.append(f"required script src missing from index.html: {link}")
    for link in REQUIRED_IMAGE_SRCS:
        if unescape(link) not in parser.images:
            failures.append(f"required image src missing from index.html: {link}")
    for link in REQUIRED_FAVICON_HREFS:
        if unescape(link) not in parser.favicons:
            failures.append(f"required favicon href missing from index.html: {link}")

    for class_name in REQUIRED_V2_CLASSES:
        if class_name not in parser.classes:
            failures.append(f"required v2 class missing from index.html: {class_name}")

    if FORBIDDEN_HERO_IMAGE_SRC in parser.hero_image_srcs:
        failures.append("hero must use illustrated lab/console art, not the real portrait")

    if ABOUT_PORTRAIT_SRC not in parser.about_image_srcs:
        failures.append("ABOUT.EXE must contain the real portrait image")

    if not has_paper_database_label(visible_text):
        failures.append("Paper Database label missing")

    if not has_system_log_label(visible_text):
        failures.append("System Log label missing")

    if has_viewport_scaled_font_size(css):
        failures.append("CSS must not scale font-size with viewport units")

    if has_large_border_radius(css):
        failures.append("large rounded card radii are not allowed")

    if has_soft_visual_effect(css):
        failures.append("blur/glass/soft-shadow visual effects are not allowed")

    if not parser.has_main:
        failures.append("index.html needs a <main> landmark")
    if not parser.has_nav:
        failures.append("index.html needs a <nav> landmark")
    if not parser.has_h1:
        failures.append("index.html needs an <h1>")

    for section_id in REQUIRED_IDS:
        if section_id not in parser.section_ids:
            failures.append(f"required section id missing: {section_id}")

    for src, alt in parser.image_alts:
        if not alt.strip():
            failures.append(f"image missing alt text: {src or '<missing src>'}")

    if not has_reduced_motion_rule(css):
        failures.append("CSS must include prefers-reduced-motion handling")
    if not has_focus_visible_selector(css):
        failures.append("CSS must include visible focus styles")
    if not has_design_tokens(css):
        failures.append("CSS must define centralized design tokens")
    if not has_match_media_call(js):
        failures.append("JS must use matchMedia for reduced-motion or responsive behavior")
    if has_forbidden_cursor(css):
        failures.append("CSS must not use a crosshair cursor")
    if has_forbidden_background_effect(css):
        failures.append("CSS must not use radial-gradient orb effects")

    if has_fake_expertise_claim(visible_text):
        failures.append("remove fake skill levels or gamified expertise claims")
    blocked_markers = ("to" + "do", "tb" + "d", "fix" + "me")
    if any(marker in (html + css + js).lower() for marker in blocked_markers):
        failures.append("remove unfinished implementation markers")
    for excluded_path in REQUIRED_EXCLUDES:
        if f"- {excluded_path}" not in config:
            failures.append(f"_config.yml must exclude implementation-only path: {excluded_path}")
    if SITE.exists():
        forbidden_outputs = [
            SITE / "legacy-index.html",
            SITE / "docs/superpowers",
            SITE / "scripts/validate_pixel_research_os.py",
        ]
        for path in forbidden_outputs:
            if path.exists():
                failures.append(f"Jekyll output should not publish implementation artifact: {path.relative_to(ROOT)}")

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    print("PASS: Pixel Research OS static validation")
    return 0

if __name__ == "__main__":
    sys.exit(main())

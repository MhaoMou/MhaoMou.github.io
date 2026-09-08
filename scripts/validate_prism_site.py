#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "package.json",
    "package-lock.json",
    "next.config.ts",
    "content/config.toml",
    "content/about.toml",
    "content/bio.md",
    "content/news.toml",
    "content/publications.bib",
    "content/publications.toml",
    "content/research.toml",
    "content/cv.toml",
    "content/cv.md",
    "public/favicon.png",
    "public/apple-touch-icon.png",
    "public/favicon.ico",
    "public/bio.jpg",
    "public/cv.pdf",
    "public/papers/braess_fig6.png",
    "public/papers/comp.jpg",
    ".github/workflows/deploy.yml",
    ".nojekyll",
]

REQUIRED_TEXT = {
    "content/config.toml": [
        'title = "Minghao Mou"',
        'favicon = "/favicon.png"',
        'name = "Minghao Mou"',
        'email = "mmou@purdue.edu"',
        "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en",
        "https://github.com/MhaoMou",
        "https://www.linkedin.com/in/minghao-mou-14a090289/",
        'target = "research"',
    ],
    "content/bio.md": [
        "Elmore Family School of Electrical and Computer Engineering",
        "Purdue University",
        "Dr. Junjie Qin",
        "Chinese University of Hong Kong, Shenzhen",
        "Dr. Shuang Li",
    ],
    "content/about.toml": [
        "Coupled Energy Infrastructure Systems",
        "Generative Models",
        "Optimal Control",
        "Selected Publications",
        "news.toml",
    ],
    "content/news.toml": [
        "May 2026",
        "Apr. 2026",
        "Dec. 2025",
        "Dec. 2023",
        "May 2023",
    ],
    "content/research.toml": [
        'type = "card"',
        "Coupled Energy Infrastructure Systems",
        "Generative Models",
        "Optimal Control",
        "Power and Transportation Coupling",
        "Workplace EV Charging",
    ],
    "content/publications.bib": [
        "Braess' Paradoxes in Coupled Power and Transportation Systems",
        "Nexus Cognizant Pricing of Workplace Electric Vehicle Charging",
        "Propelling DNA-Based Archival Storage With an Algorithmic Mindset",
        "Mou, Minghao",
        "Yang, Yaoyu",
        "Wei, Wei",
        "Qian, Sean",
        "Qin, Junjie",
        "10.1109/TMBMC.2026.3694522",
        "selected = {true}",
        "preview = {braess_fig6.png}",
        "preview = {comp.jpg}",
    ],
    ".github/workflows/deploy.yml": [
        "actions/setup-node@v4",
        "node-version: 22",
        "npm ci",
        "npm run build",
        "actions/upload-pages-artifact@v3",
        "actions/deploy-pages@v4",
    ],
    "src/app/layout.tsx": [
        "apple-touch-icon",
        "image/png",
        "/favicon.ico",
    ],
}

FORBIDDEN_SOURCE_PATHS = [
    "_config.yml",
    "_data",
    "_includes",
    "_layouts",
    "_sass",
    "Gemfile",
    "assets/css/pixel-research-os.css",
    "assets/js/pixel-research-os.js",
]

FORBIDDEN_TEXT_BY_GLOB = {
    "content/**/*": [
        "Jiale Liu",
        "University of Example",
        "Computational Physics",
        "prestigious journal",
        "Ada Lovelace",
        "Alan Turing",
    ],
    "src/**/*": [
        "jialeliu.com",
    ],
}

FORBIDDEN_OUTPUT_TEXT = [
    "desktop-shell",
    "LAB_CONSOLE.EXE",
    "Pixel Research OS",
    "Jiale Liu",
    "University of Example",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    failures = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"required file missing: {rel}")
        elif path.is_file() and path.stat().st_size == 0 and rel not in {".nojekyll"}:
            failures.append(f"required file is empty: {rel}")

    for rel in FORBIDDEN_SOURCE_PATHS:
        if (ROOT / rel).exists():
            failures.append(f"old active site artifact should be removed: {rel}")

    for rel, snippets in REQUIRED_TEXT.items():
        if not (ROOT / rel).exists():
            continue
        content = read(rel)
        for snippet in snippets:
            if snippet not in content:
                failures.append(f"required text missing from {rel}: {snippet}")

    for pattern, forbidden_values in FORBIDDEN_TEXT_BY_GLOB.items():
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            rel = path.relative_to(ROOT)
            for value in forbidden_values:
                if value in content:
                    failures.append(f"forbidden sample text remains in {rel}: {value}")

    package_json = read("package.json") if (ROOT / "package.json").exists() else ""
    if '"next"' not in package_json or '"react"' not in package_json:
        failures.append("package.json must contain PRISM/Next dependencies")
    if '"node": ">=22.0.0"' not in package_json:
        failures.append("package.json must keep the PRISM Node 22 engine requirement")

    next_config = read("next.config.ts") if (ROOT / "next.config.ts").exists() else ""
    if "output: 'export'" not in next_config and 'output: "export"' not in next_config:
        failures.append("next.config.ts must use static export")
    if re.search(r"\bbasePath\s*:", next_config):
        failures.append("root GitHub Pages site should not set basePath")
    if re.search(r"\bassetPrefix\s*:", next_config):
        failures.append("root GitHub Pages site should not set assetPrefix")

    workflow = read(".github/workflows/deploy.yml") if (ROOT / ".github/workflows/deploy.yml").exists() else ""
    if "push:" not in workflow or "branches:" not in workflow or "- main" not in workflow:
        failures.append("GitHub Pages workflow must deploy on pushes to main")

    out_index = ROOT / "out" / "index.html"
    if out_index.exists():
        output = out_index.read_text(encoding="utf-8", errors="replace")
        for snippet in FORBIDDEN_OUTPUT_TEXT:
            if snippet in output:
                failures.append(f"generated output still contains old/sample site text: {snippet}")
        for snippet in [
            "Minghao Mou",
            "Ph.D. candidate",
            "Selected Publications",
            "Coupled Energy Infrastructure Systems",
            "Propelling DNA-Based Archival Storage With an Algorithmic Mindset",
        ]:
            if snippet not in output:
                failures.append(f"generated homepage missing required text: {snippet}")

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    print("PASS: PRISM site validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())

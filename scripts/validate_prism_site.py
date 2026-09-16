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
    "content/blog.toml",
    "content/blog/multi-parametric-nonlinear-program.md",
    "content/research.toml",
    "content/cv.toml",
    "content/cv.md",
    "public/favicon.png",
    "public/apple-touch-icon.png",
    "public/favicon.ico",
    "public/bio.jpg",
    "public/cv.pdf",
    "public/papers/dna_storage_workflow.png",
    "public/papers/storage_binding_patterns.png",
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
        'institution = "Purdue ECE"',
        'email = "mmou@purdue.edu"',
        "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en",
        "https://github.com/MhaoMou",
        "https://www.linkedin.com/in/minghao-mou-14a090289/",
        'target = "research"',
        'title = "Blog"',
        'target = "blog"',
        'href = "/blog"',
    ],
    "content/bio.md": [
        "Purdue ECE",
        "Purdue University",
        "Dr. Junjie Qin",
        "Chinese University of Hong Kong, Shenzhen",
        "Dr. Shuang Li",
    ],
    "content/about.toml": [
        "Coupled Energy Infrastructure Systems",
        "Generative Models",
        "Optimal Control",
        "Learn to Optimize",
        "Selected Publications",
        "news.toml",
        'type = "latest_updates"',
        'type = "scholar_card"',
        'total_citations = 3',
        'h_index = 1',
        'i10_index = 0',
        'last_checked = "September 16, 2026"',
        'year = "2025"',
        'citations = 3',
    ],
    "content/blog.toml": [
        'type = "blog"',
        'title = "Blog"',
        "multi-parametric-nonlinear-program",
        "Multi-Parametric Nonlinear Program",
    ],
    "content/blog/multi-parametric-nonlinear-program.md": [
        "multi-parametric nonlinear programs",
        "Karush-Kuhn-Tucker",
        "Mangasarian-Fromovitz",
        "Differential Stability",
        "Sensitivity Analysis",
        "Anthony V. Fiacco",
        "Daniel Ralph",
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
        "Storage-Based Strategic Manipulation of Constraint-Binding Patterns in Power Networks",
        "Davoudi, Mehdi",
        "Mou, Minghao",
        "Yang, Yaoyu",
        "Wei, Wei",
        "Qian, Sean",
        "Qin, Junjie",
        "10.48550/arXiv.2609.15755",
        "10.1109/TMBMC.2026.3694522",
        "selected = {true}",
        "preview = {storage_binding_patterns.png}",
        "preview = {dna_storage_workflow.png}",
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
    "content/blog/learning-to-optimize.md",
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
    "Learning to Optimize",
    "/blog/learning-to-optimize",
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

    blog_post = ROOT / "content" / "blog" / "multi-parametric-nonlinear-program.md"
    if blog_post.exists():
        in_display_math = False
        for line_no, line in enumerate(blog_post.read_text(encoding="utf-8").splitlines(), 1):
            if "$$" in line and line.strip() != "$$":
                failures.append(
                    "display math delimiter must be on its own line in "
                    f"content/blog/multi-parametric-nonlinear-program.md:{line_no}"
                )
            if line.strip() == "$$":
                in_display_math = not in_display_math
            elif in_display_math and re.match(r"\s*#{1,6}\s+", line):
                failures.append(
                    "markdown heading appears inside an open display math block in "
                    f"content/blog/multi-parametric-nonlinear-program.md:{line_no}"
                )
        if in_display_math:
            failures.append("display math delimiters must be balanced in content/blog/multi-parametric-nonlinear-program.md")

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
            "Purdue ECE",
            "Learn to Optimize",
            "Latest Updates",
            "Google Scholar",
            "Blog",
        ]:
            if snippet not in output:
                failures.append(f"generated homepage missing required text: {snippet}")

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    about = read("content/about.toml") if (ROOT / "content/about.toml").exists() else ""
    if re.search(r'id\s*=\s*"news"\s*\n\s*type\s*=\s*"list"', about):
        print('FAIL: full News list section should be hidden from content/about.toml')
        return 1

    if out_index.exists():
        output = out_index.read_text(encoding="utf-8", errors="replace")
        for snippet in [
            'total_citations\\":3',
            "citations",
            "h-index",
            "i10-index",
            "Citation trend",
            "Last checked",
            "September 16, 2026",
        ]:
            if snippet not in output:
                print(f"FAIL: generated homepage missing Scholar metric text: {snippet}")
                return 1
        if re.search(r">\s*News\s*<", output):
            print("FAIL: generated homepage should not render the full News heading")
            return 1

    out_blog = ROOT / "out" / "blog" / "multi-parametric-nonlinear-program" / "index.html"
    if out_blog.exists():
        output = out_blog.read_text(encoding="utf-8", errors="replace")
        rendered_output = re.sub(r"<script\b[^>]*>.*?</script>", "", output, flags=re.IGNORECASE | re.DOTALL)
        for snippet in [
            "Multi-Parametric Nonlinear Program",
            "Karush-Kuhn-Tucker",
            "Mangasarian-Fromovitz",
            "katex",
        ]:
            if snippet not in rendered_output:
                print(f"FAIL: generated blog post missing required rendered text: {snippet}")
                return 1
        for artifact in ["$$", "eq:", "thm:", "###", "katex-error"]:
            if artifact in rendered_output:
                print(f"FAIL: generated blog post contains raw rendering artifact: {artifact}")
                return 1

    print("PASS: PRISM site validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())

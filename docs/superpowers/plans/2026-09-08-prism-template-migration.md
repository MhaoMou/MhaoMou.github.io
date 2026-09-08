# PRISM Template Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current Jekyll/Pixel Research OS site with a customized PRISM-based academic website and publish it through GitHub Pages Actions.

**Architecture:** Use PRISM as the upstream application source rather than hand-designing a new frontend. Current site content moves into PRISM's `content/` model, current static files move into `public/`, and GitHub Pages deploys the static `out/` artifact created by `npm run build`.

**Tech Stack:** Next.js 15 static export, React 19, TypeScript, Tailwind CSS, TOML/Markdown/BibTeX content, GitHub Actions Pages deployment, Python validation scripts, headless Chrome screenshot QA.

---

## File Structure

Create or replace these source groups:

- `content/config.toml`: global site metadata, author, social links, navigation, features.
- `content/about.toml`: homepage composition for profile, selected publications, and news.
- `content/bio.md`: exact academic biography prose.
- `content/news.toml`: dated news entries from the current site.
- `content/publications.bib`: BibTeX publication records with PRISM-specific metadata fields.
- `content/research.toml`: concise research/project cards derived from current research areas and papers.
- `content/cv.md`: CV page with direct link to `/cv.pdf`.
- `public/`: copied active assets from `assets/`, including `bio.jpg`, `cv.pdf`, publication preview images, and favicon outputs.
- `src/`, `next.config.ts`, `package.json`, `package-lock.json`, `tailwind.config.mjs`, `postcss.config.mjs`, `tsconfig.json`, `eslint.config.mjs`: imported from upstream PRISM, with minimal local changes.
- `.github/workflows/deploy.yml`: GitHub Pages deployment workflow triggered on pushes to `main`.
- `.nojekyll`: disables Jekyll processing for static export artifacts.
- `scripts/validate_prism_site.py`: repository-specific validation for content, assets, workflow, and generated output.

Remove or retire these old-site files from active deployment:

- `index.html`
- `_config.yml`
- `_data/`
- `_includes/`
- `_layouts/`
- `_sass/`
- `Gemfile`
- `Gemfile.lock` if present in the working tree
- `assets/css/pixel-research-os.css`
- `assets/js/pixel-research-os.js`
- `scripts/validate_pixel_research_os.py`

Keep these files if still useful as source history or docs:

- `docs/superpowers/specs/`
- `docs/superpowers/plans/`
- `legacy-index.md`
- `html_source_file/`

## Task 1: Isolate Work And Capture Baseline

**Files:**
- Create worktree: `.worktrees/prism-template-migration`
- Create screenshots:
  - `.superpowers/screenshots/prism-before-homepage-1440x900.png`
  - `.superpowers/screenshots/prism-before-homepage-390x844.png`

- [ ] **Step 1: Create isolated implementation worktree**

Run:

```bash
git status --short --branch
git worktree add .worktrees/prism-template-migration -b prism-template-migration
```

Expected:

```text
## main...origin/main [ahead 1]
Preparing worktree (new branch 'prism-template-migration')
```

- [ ] **Step 2: Capture current live before screenshots**

Run a local or live screenshot command using headless Chrome:

```bash
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --window-size=1440,900 \
  --screenshot=.superpowers/screenshots/prism-before-homepage-1440x900.png \
  'https://mhaomou.github.io/?before=prism'

'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --window-size=390,844 \
  --screenshot=.superpowers/screenshots/prism-before-homepage-390x844.png \
  'https://mhaomou.github.io/?before=prism'
```

Expected:

```text
... bytes written to file .superpowers/screenshots/prism-before-homepage-1440x900.png
... bytes written to file .superpowers/screenshots/prism-before-homepage-390x844.png
```

- [ ] **Step 3: Commit no code changes**

Run:

```bash
git status --short --branch
```

Expected:

```text
## prism-template-migration
```

No commit is needed for screenshots because `.superpowers/` is ignored.

## Task 2: Import PRISM Upstream Source

**Files:**
- Create/replace: PRISM root files and directories from `xyjoey/PRISM`
- Preserve temporarily: `assets/`, `docs/`, `legacy-index.md`, `html_source_file/`, `.gitignore`, `CNAME`, `.superpowers/`

- [ ] **Step 1: Download upstream PRISM into temporary directory**

Run:

```bash
rm -rf /private/tmp/prism-upstream
git clone --depth 1 https://github.com/xyjoey/PRISM.git /private/tmp/prism-upstream
```

Expected:

```text
Cloning into '/private/tmp/prism-upstream'...
```

- [ ] **Step 2: Verify upstream files exist**

Run:

```bash
test -f /private/tmp/prism-upstream/package.json
test -f /private/tmp/prism-upstream/next.config.ts
test -d /private/tmp/prism-upstream/src
test -d /private/tmp/prism-upstream/content
```

Expected: exit code `0`.

- [ ] **Step 3: Remove active old-site implementation files**

Run from `.worktrees/prism-template-migration`:

```bash
rm -rf _config.yml _data _includes _layouts _sass _site .sass-cache Gemfile Gemfile.lock index.html assets/css assets/js
```

Expected: active Jekyll homepage and Pixel Research OS assets are removed from the worktree.

- [ ] **Step 4: Copy PRISM source into the worktree**

Run:

```bash
rsync -a --exclude .git /private/tmp/prism-upstream/ ./
```

Expected files after copy:

```text
package.json
package-lock.json
next.config.ts
content/config.toml
src/app
public
```

- [ ] **Step 5: Preserve repository identity files**

Run:

```bash
test -f CNAME
test -d docs/superpowers/specs
test -d docs/superpowers/plans
```

If `CNAME` was overwritten or removed, recreate it with exactly:

```text
mhaomou.github.io
```

- [ ] **Step 6: Commit imported source**

Run:

```bash
git add -A
git commit -m "Import PRISM template source"
```

Expected: one commit containing upstream PRISM source and removal of active old-site files.

## Task 3: Configure PRISM For Minghao Mou

**Files:**
- Modify: `content/config.toml`
- Modify: `content/about.toml`
- Create/modify: `content/bio.md`
- Create/modify: `content/news.toml`
- Create/modify: `content/research.toml`
- Create/modify: `content/cv.md`
- Modify: navigation-related content files if PRISM requires them

- [ ] **Step 1: Write global config content**

Replace `content/config.toml` with:

```toml
[site]
title = "Minghao Mou"
description = "Personal academic website of Minghao Mou, Ph.D. candidate at Purdue ECE."
favicon = "/favicon.png"
last_updated = "September 2026"

[author]
name = "Minghao Mou"
title = "Ph.D. candidate"
institution = "Elmore Family School of Electrical and Computer Engineering, Purdue University"
avatar = "/bio.jpg"

[social]
email = "mmou@purdue.edu"
location = "West Lafayette, Indiana"
location_url = "https://www.purdue.edu/"
location_details = [
  "Elmore Family School of Electrical and Computer Engineering,",
  "Purdue University"
]
google_scholar = "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en"
orcid = ""
github = "https://github.com/MhaoMou"
linkedin = "https://www.linkedin.com/in/minghao-mou-14a090289/"

[features]
enable_likes = false
enable_one_page_mode = false

[i18n]
enabled = false
locales = ["en"]
default_locale = "en"
mode = "fixed"
fixed_locale = "en"
persist = false
switcher = false

[i18n.labels]
en = "English"

[[navigation]]
title = "About"
type = "page"
target = "about"
href = "/"

[[navigation]]
title = "Publications"
type = "page"
target = "publications"
href = "/publications"

[[navigation]]
title = "Research"
type = "page"
target = "research"
href = "/research"

[[navigation]]
title = "CV"
type = "page"
target = "cv"
href = "/cv"
```

- [ ] **Step 2: Write homepage composition**

Replace `content/about.toml` with:

```toml
type = "about"
title = "About"

[profile]
research_interests = [
  "Coupled Energy Infrastructure Systems",
  "Generative Models",
  "Optimal Control"
]

[[sections]]
id = "about"
type = "markdown"
source = "bio.md"
title = "About"

[[sections]]
id = "featured_publications"
type = "publications"
title = "Selected Publications"
filter = "selected"
limit = 5

[[sections]]
id = "news"
type = "list"
title = "News"
source = "news.toml"
```

- [ ] **Step 3: Write biography markdown**

Replace `content/bio.md` with:

```markdown
I am a Ph.D. candidate in the [Elmore Family School of Electrical and Computer Engineering](https://engineering.purdue.edu/ECE) at [Purdue University](https://www.purdue.edu), advised by [Dr. Junjie Qin](https://engineering.purdue.edu/people/junjie.qin.1).

My research interests include coupled energy infrastructure systems, generative models, and optimal control, with a focus on modeling and decision-making for interconnected energy and transportation systems.

I obtained my Bachelor's degree in Mathematics from [The Chinese University of Hong Kong, Shenzhen](https://www.cuhk.edu.cn/en) in 2023, where I was advised by [Dr. Shuang Li](https://shuangli01.github.io).
```

- [ ] **Step 4: Write news content**

Replace `content/news.toml` with:

```toml
[[items]]
date = "May 2026"
text = "I passed my PhD preliminary exam and am now a Ph.D. candidate."

[[items]]
date = "Apr. 2026"
text = "Our preprint Braess' Paradoxes in Coupled Power and Transportation Systems was revised on arXiv."

[[items]]
date = "Dec. 2025"
text = "Our preprint Braess' Paradoxes in Coupled Power and Transportation Systems was posted on arXiv."

[[items]]
date = "Dec. 2023"
text = "Our paper Nexus Cognizant Pricing of Workplace Electric Vehicle Charging was accepted to the American Control Conference 2024."

[[items]]
date = "May 2023"
text = "I graduated from The Chinese University of Hong Kong, Shenzhen with first-class honors."
```

- [ ] **Step 5: Write research page content**

Create `content/research.toml`:

```toml
type = "card"
title = "Research"

[[items]]
title = "Coupled Energy Infrastructure Systems"
description = "Modeling and analysis for infrastructure systems that connect energy, transportation, and decision-making layers."
url = "/publications"

[[items]]
title = "Generative Models"
description = "Learning-based models for representing complex system behavior and supporting research workflows."
url = "/publications"

[[items]]
title = "Optimal Control"
description = "Optimization and control methods for engineered systems with operational constraints."
url = "/publications"

[[items]]
title = "Power and Transportation Coupling"
description = "Research on Braess-type phenomena in coupled power and transportation systems."
url = "https://arxiv.org/abs/2512.12197"

[[items]]
title = "Workplace EV Charging"
description = "Pricing and operational design for workplace electric vehicle charging."
url = "https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866"
```

- [ ] **Step 6: Write CV page content**

Create `content/cv.md`:

```markdown
# CV

My current curriculum vitae is available here:

[Open CV PDF](/cv.pdf)
```

- [ ] **Step 7: Commit content configuration**

Run:

```bash
git add content/config.toml content/about.toml content/bio.md content/news.toml content/research.toml content/cv.md
git commit -m "Configure PRISM academic content"
```

Expected: one commit containing Minghao-specific PRISM content.

## Task 4: Convert Publications To BibTeX

**Files:**
- Modify: `content/publications.bib`
- Copy assets later used by records in Task 5

- [ ] **Step 1: Replace publications BibTeX**

Replace `content/publications.bib` with:

```bibtex
@article{mou2025braess,
  title = {Braess' Paradoxes in Coupled Power and Transportation Systems},
  author = {Mou, Minghao and Qin, Junjie},
  journal = {arXiv preprint arXiv:2512.12197},
  year = {2025},
  selected = {true},
  preview = {/images/braess_fig6.png},
  pdf = {https://arxiv.org/pdf/2512.12197},
  url = {https://arxiv.org/abs/2512.12197},
  doi = {10.48550/arXiv.2512.12197},
  description = {Preprint on Braess-type effects in coupled power and transportation systems.}
}

@inproceedings{mou2024nexus,
  title = {Nexus Cognizant Pricing of Workplace Electric Vehicle Charging},
  author = {Mou, Minghao and Qian, Sean and Qin, Junjie},
  booktitle = {American Control Conference},
  year = {2024},
  selected = {true},
  preview = {/images/comp.jpg},
  pdf = {https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866},
  url = {https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866},
  note = {Oral Presentation},
  description = {Conference paper on pricing for workplace electric vehicle charging.}
}
```

- [ ] **Step 2: Verify required publication text exists**

Run:

```bash
rg -n "Braess' Paradoxes|Nexus Cognizant|Minghao|Qian|Qin|selected|preview" content/publications.bib
```

Expected: matches for both publication records and metadata fields.

- [ ] **Step 3: Commit publication conversion**

Run:

```bash
git add content/publications.bib
git commit -m "Convert publications to PRISM BibTeX"
```

Expected: one commit with the PRISM publication database.

## Task 5: Move Assets And Add Favicon

**Files:**
- Create/replace: `public/bio.jpg`
- Create/replace: `public/cv.pdf`
- Create/replace: `public/images/braess_fig6.png`
- Create/replace: `public/images/comp.jpg`
- Create/replace: `public/favicon.png`
- Create/replace as needed: `public/favicon.ico`, `public/apple-touch-icon.png`

- [ ] **Step 1: Copy active current assets**

Run:

```bash
mkdir -p public/images
cp assets/img/IMG_5612.jpeg public/bio.jpg
cp assets/files/curriculum_vitae.pdf public/cv.pdf
cp assets/img/braess_fig6.png public/images/braess_fig6.png
cp assets/img/comp.jpg public/images/comp.jpg
```

Expected: all four files exist in `public/`.

- [ ] **Step 2: Materialize the attached icon**

If the attached image file exists in the local attachment store, copy it to `/private/tmp/minghao-pixel-icon.png`. Search with:

```bash
find /Users/minghao/.codex/attachments -maxdepth 4 -type f \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.webp' \) -print
```

If no image file is returned, ask the user to reattach the icon as a downloadable image file before continuing this task. Do not approximate or redraw the icon.

- [ ] **Step 3: Generate favicon files from the attached icon**

Run after `/private/tmp/minghao-pixel-icon.png` exists:

```bash
python3 - <<'PY'
from PIL import Image
from pathlib import Path

src = Path('/private/tmp/minghao-pixel-icon.png')
img = Image.open(src).convert('RGBA')

Path('public').mkdir(exist_ok=True)
img.resize((512, 512), Image.Resampling.NEAREST).save('public/favicon.png')
img.resize((180, 180), Image.Resampling.NEAREST).save('public/apple-touch-icon.png')
img.save('public/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
PY
```

Expected:

```text
public/favicon.png
public/apple-touch-icon.png
public/favicon.ico
```

- [ ] **Step 4: Verify icon and assets**

Run:

```bash
test -s public/favicon.png
test -s public/apple-touch-icon.png
test -s public/favicon.ico
test -s public/bio.jpg
test -s public/cv.pdf
test -s public/images/braess_fig6.png
test -s public/images/comp.jpg
```

Expected: exit code `0`.

- [ ] **Step 5: Commit assets**

Run:

```bash
git add public/bio.jpg public/cv.pdf public/images/braess_fig6.png public/images/comp.jpg public/favicon.png public/apple-touch-icon.png public/favicon.ico
git commit -m "Add PRISM site assets and favicon"
```

Expected: one commit containing active static assets.

## Task 6: Add GitHub Pages Deployment Workflow

**Files:**
- Create/modify: `.github/workflows/deploy.yml`
- Create/modify: `.nojekyll`
- Modify: `next.config.ts` only if needed for root-domain GitHub Pages

- [ ] **Step 1: Write deployment workflow**

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy PRISM site to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Build site
        run: npm run build

      - name: Add nojekyll marker
        run: touch out/.nojekyll

      - name: Preserve custom domain
        run: cp CNAME out/CNAME

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./out

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Add root nojekyll marker**

Run:

```bash
touch .nojekyll
```

Expected: `.nojekyll` exists in source root.

- [ ] **Step 3: Verify `next.config.ts` is root-domain safe**

Run:

```bash
rg -n "output: 'export'|trailingSlash|basePath|assetPrefix" next.config.ts
```

Expected:

```text
output: 'export'
trailingSlash: true
```

For `mhaomou.github.io`, do not add `basePath` or `assetPrefix`.

- [ ] **Step 4: Commit deployment config**

Run:

```bash
git add .github/workflows/deploy.yml .nojekyll next.config.ts
git commit -m "Add PRISM GitHub Pages deployment"
```

Expected: one commit with deployment workflow and no Jekyll marker.

## Task 7: Add PRISM Site Validator

**Files:**
- Create: `scripts/validate_prism_site.py`
- Modify: `.gitignore` if generated tool directories need ignoring

- [ ] **Step 1: Write validator**

Create `scripts/validate_prism_site.py`:

```python
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
    "content/research.toml",
    "content/cv.md",
    "public/favicon.png",
    "public/apple-touch-icon.png",
    "public/favicon.ico",
    "public/bio.jpg",
    "public/cv.pdf",
    "public/images/braess_fig6.png",
    "public/images/comp.jpg",
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
    "content/publications.bib": [
        "Braess' Paradoxes in Coupled Power and Transportation Systems",
        "Nexus Cognizant Pricing of Workplace Electric Vehicle Charging",
        "Mou, Minghao",
        "Qian, Sean",
        "Qin, Junjie",
        "selected = {true}",
        "preview = {/images/braess_fig6.png}",
        "preview = {/images/comp.jpg}",
    ],
    ".github/workflows/deploy.yml": [
        "actions/setup-node@v4",
        "node-version: 22",
        "npm ci",
        "npm run build",
        "actions/upload-pages-artifact@v3",
        "actions/deploy-pages@v4",
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

FORBIDDEN_OUTPUT_TEXT = [
    "desktop-shell",
    "LAB_CONSOLE.EXE",
    "Pixel Research OS",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> int:
    failures = []

    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            failures.append(f"required file missing: {rel}")

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

    out_index = ROOT / "out" / "index.html"
    if out_index.exists():
        output = out_index.read_text(encoding="utf-8", errors="replace")
        for snippet in FORBIDDEN_OUTPUT_TEXT:
            if snippet in output:
                failures.append(f"generated output still contains old site text: {snippet}")
        if "Minghao Mou" not in output:
            failures.append("generated homepage must contain Minghao Mou")

    if failures:
        for item in failures:
            print(f"FAIL: {item}")
        return 1

    print("PASS: PRISM site validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run validator red check before all migration tasks are complete if possible**

Run:

```bash
python3 scripts/validate_prism_site.py
```

Expected before the full migration is complete: FAIL with missing PRISM files or old-site artifacts.

- [ ] **Step 3: Run validator green check after prior tasks**

Run:

```bash
python3 scripts/validate_prism_site.py
```

Expected after prior tasks:

```text
PASS: PRISM site validation
```

- [ ] **Step 4: Commit validator**

Run:

```bash
git add scripts/validate_prism_site.py .gitignore
git commit -m "Add PRISM site validation"
```

Expected: one commit with repository-specific validation.

## Task 8: Install Dependencies And Build Locally

**Files:**
- No source files expected unless dependency lockfile changes
- Generated: `node_modules/`, `out/`

- [ ] **Step 1: Confirm Node 22 availability**

Run:

```bash
node --version
```

Expected: version starts with `v22.` or newer.

If `node` is unavailable or older than v22, install a local Node 22 binary into an ignored tools directory and run subsequent npm commands with that binary on `PATH`.

- [ ] **Step 2: Install dependencies**

Run:

```bash
npm ci
```

Expected:

```text
added ... packages
```

- [ ] **Step 3: Build static export**

Run:

```bash
npm run build
```

Expected: Next build succeeds and creates `out/index.html`.

- [ ] **Step 4: Run validation after build**

Run:

```bash
python3 scripts/validate_prism_site.py
git diff --check
```

Expected:

```text
PASS: PRISM site validation
```

`git diff --check` prints no output.

- [ ] **Step 5: Commit dependency/build config changes if needed**

If `package-lock.json`, config files, or source files changed during dependency/build fixes:

```bash
git add package-lock.json package.json next.config.ts src content public scripts
git commit -m "Fix PRISM build integration"
```

Expected: commit only real source/config changes, not `node_modules/` or `out/`.

## Task 9: Visual QA

**Files:**
- Create screenshots:
  - `.superpowers/screenshots/prism-after-homepage-1440x900.png`
  - `.superpowers/screenshots/prism-after-homepage-390x844.png`

- [ ] **Step 1: Serve static output locally**

Run:

```bash
python3 -m http.server 8766 --directory out
```

Expected:

```text
Serving HTTP on :: port 8766
```

- [ ] **Step 2: Capture desktop screenshot**

Run:

```bash
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --window-size=1440,900 \
  --screenshot=.superpowers/screenshots/prism-after-homepage-1440x900.png \
  http://127.0.0.1:8766/
```

Expected: screenshot file is written.

- [ ] **Step 3: Capture mobile screenshot**

Run:

```bash
'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --window-size=390,844 \
  --screenshot=.superpowers/screenshots/prism-after-homepage-390x844.png \
  http://127.0.0.1:8766/
```

Expected: screenshot file is written.

- [ ] **Step 4: Inspect screenshots**

Open both images and verify:

- The homepage visually follows PRISM, not Pixel Research OS.
- The profile photo is correctly placed.
- The favicon uses the attached pixel image.
- Text is readable and not clipped.
- Mobile first viewport shows the name, role, and navigation without horizontal overflow.
- Publications and selected work appear below the hero/homepage intro.

- [ ] **Step 5: Fix visual defects and commit**

If screenshot inspection finds a defect, patch the smallest relevant file, rerun:

```bash
npm run build
python3 scripts/validate_prism_site.py
```

Then commit:

```bash
git add content public src scripts
git commit -m "Polish PRISM visual QA"
```

Expected: no visible blocker remains in desktop or mobile screenshots.

## Task 10: Merge And Publish

**Files:**
- No new source files expected

- [ ] **Step 1: Final local verification**

Run:

```bash
npm run build
python3 scripts/validate_prism_site.py
git diff --check
git status --short --branch
```

Expected:

```text
PASS: PRISM site validation
## prism-template-migration
```

- [ ] **Step 2: Merge to main locally**

Run from repository root:

```bash
git checkout main
git merge prism-template-migration
```

Expected: fast-forward or clean merge.

- [ ] **Step 3: Verify merged main**

Run:

```bash
npm run build
python3 scripts/validate_prism_site.py
git diff --check
git status --short --branch
```

Expected:

```text
PASS: PRISM site validation
## main...origin/main [ahead N]
```

- [ ] **Step 4: Push main**

Run:

```bash
git push origin main
```

Expected:

```text
main -> main
```

- [ ] **Step 5: Confirm GitHub Pages deployment**

Because PRISM requires GitHub Actions Pages deployment, verify the repository Pages source is set to GitHub Actions. Then check the workflow status:

```bash
gh run list --workflow "Deploy PRISM site to GitHub Pages" --limit 3
```

Expected: latest run succeeds.

- [ ] **Step 6: Verify live site**

Run:

```bash
curl -L --max-time 20 -s 'https://mhaomou.github.io/?prism=live' | rg -n "Minghao Mou|Selected Publications|Coupled Energy Infrastructure Systems"
curl -L --max-time 20 -I 'https://mhaomou.github.io/favicon.png'
```

Expected:

- Live homepage contains PRISM-rendered Minghao content.
- Favicon request returns HTTP `200`.

- [ ] **Step 7: Cleanup**

Run:

```bash
git worktree remove .worktrees/prism-template-migration
git worktree prune
git branch -d prism-template-migration
```

Expected: migration worktree and merged branch are removed.

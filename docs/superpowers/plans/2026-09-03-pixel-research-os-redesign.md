# Pixel Research OS Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current academic homepage with a static `MINGHAO.EXE — Pixel Research OS` homepage that preserves existing academic content and GitHub Pages compatibility.

**Architecture:** Build a self-contained static homepage with `index.html`, one local CSS file, one small local JS file, and a Python validation script. Keep existing Jekyll/theme files as reference unless they conflict with the static homepage; retire `index.md` after its content is migrated so GitHub Pages has a single homepage source.

**Tech Stack:** Static HTML, CSS custom properties, vanilla JavaScript, Python 3 standard library validation, GitHub Pages static hosting.

---

## File Structure

- Create `index.html`: complete static homepage, semantic sections, SEO metadata, preserved academic content, and links to local CSS/JS.
- Create `assets/css/pixel-research-os.css`: design tokens, pixel OS shell, windows, buttons, publications, responsive behavior, focus states, and reduced-motion behavior.
- Create `assets/js/pixel-research-os.js`: progressive enhancement for boot text, active nav state, reduced-motion-safe behavior, and current year display.
- Create `scripts/validate_pixel_research_os.py`: standard-library checks for required content, required assets, required sections, no duplicate homepage source, and CSS/JS wiring.
- Modify `.gitignore` only if needed: keep `.superpowers/` ignored.
- Rename `index.md` to `legacy-index.md` after `index.html` is complete and validated, preserving the old content in repo history and preventing duplicate homepage generation.

## Content Constants

Use these exact existing facts:

- Name: `Minghao Mou`
- Academic status: `Ph.D. candidate`
- School: `Elmore Family School of Electrical and Computer Engineering`
- University: `Purdue University`
- Advisor: `Dr. Junjie Qin`
- Undergraduate institution: `Chinese University of Hong Kong, Shenzhen`
- Undergraduate advisor: `Dr. Shuang Li`
- Email: `mmou@purdue.edu`
- Research interests: `Coupled Energy Infrastructure Systems`, `Generative Models`, `Optimal Control`
- CV: `assets/files/curriculum_vitae.pdf`
- Portrait: `assets/img/IMG_5612.jpeg`
- Pixel avatar asset: `assets/img/avatar.png`
- Publication teasers: `assets/img/braess_fig6.png`, `assets/img/comp.jpg`
- Google Scholar: `https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en`
- GitHub: `https://github.com/MhaoMou`
- LinkedIn: `https://www.linkedin.com/in/minghao-mou-14a090289/`

## Task 1: Add Static Validation Script

**Files:**
- Create: `scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Create the validation script**

Create `scripts/validate_pixel_research_os.py` with this complete content:

```python
#!/usr/bin/env python3
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
]

class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.alt_texts = []
        self.hrefs = []
        self.srcs = []
        self.has_main = False
        self.has_nav = False
        self.has_h1 = False
        self.buttons = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "img":
            self.alt_texts.append(attrs.get("alt", ""))
            if attrs.get("src"):
                self.srcs.append(attrs["src"])
        if tag == "a" and attrs.get("href"):
            self.hrefs.append(attrs["href"])
        if tag == "main":
            self.has_main = True
        if tag == "nav":
            self.has_nav = True
        if tag == "h1":
            self.has_h1 = True
        if tag == "button" or (tag == "a" and "button" in attrs.get("class", "")):
            self.buttons += 1

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

    for link in REQUIRED_LINKS:
        if link not in html:
            failures.append(f"required link missing from index.html: {link}")

    parser = StructureParser()
    parser.feed(html)

    if not parser.has_main:
        failures.append("index.html needs a <main> landmark")
    if not parser.has_nav:
        failures.append("index.html needs a <nav> landmark")
    if not parser.has_h1:
        failures.append("index.html needs an <h1>")

    for section_id in REQUIRED_IDS:
        if section_id not in parser.ids:
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
```

- [ ] **Step 2: Run the validator and confirm it fails before implementation**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result:

```text
FAIL: index.html is missing
FAIL: assets/css/pixel-research-os.css is missing
FAIL: assets/js/pixel-research-os.js is missing
FAIL: index.md still exists; rename it after migrating content
```

Additional failures for missing content are acceptable at this step because the homepage has not been implemented.

- [ ] **Step 3: Commit the validator**

Run:

```bash
git add scripts/validate_pixel_research_os.py
git commit -m "Add Pixel Research OS validation"
```

Expected result:

```text
[main <hash>] Add Pixel Research OS validation
```

## Task 2: Build Static HTML Homepage

**Files:**
- Create: `index.html`
- Modify: `index.md` by renaming it to `legacy-index.md`

- [ ] **Step 1: Create `index.html`**

Create `index.html` as a full static HTML5 document with:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Minghao Mou | MINGHAO.EXE Pixel Research OS</title>
  <meta name="description" content="Personal academic webpage of Minghao Mou, a Ph.D. candidate at Purdue University working on coupled infrastructure systems, generative models, and optimal control.">
  <meta name="keywords" content="Minghao Mou, Purdue University, coupled infrastructure systems, generative models, optimal control, transportation electrification">
  <link rel="canonical" href="https://MhaoMou.github.io/">
  <meta property="og:title" content="Minghao Mou | Pixel Research OS">
  <meta property="og:description" content="Academic homepage of Minghao Mou, Ph.D. candidate at Purdue ECE.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://MhaoMou.github.io/">
  <meta property="og:image" content="https://MhaoMou.github.io/assets/img/IMG_5612.jpeg">
  <link rel="icon" media="(prefers-color-scheme: dark)" href="assets/img/favicon-dark.png" type="image/png">
  <link rel="icon" media="(prefers-color-scheme: light)" href="assets/img/favicon.png" type="image/png">
  <link rel="stylesheet" href="assets/css/pixel-research-os.css">
  <script src="assets/js/pixel-research-os.js" defer></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="os-topbar" aria-label="Pixel Research OS top bar">
    <a class="brand" href="#top" aria-label="Minghao Mou homepage">MINGHAO.EXE</a>
    <span class="system-label">Research OS</span>
    <span class="topbar-affiliation">Purdue ECE</span>
    <nav class="quick-links" aria-label="Quick links">
      <a href="https://github.com/MhaoMou">GitHub</a>
      <a href="https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&amp;hl=en">Scholar</a>
      <a href="assets/files/curriculum_vitae.pdf">CV</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <div class="desktop-grid" id="top">
    <nav class="desktop-nav" aria-label="Section navigation">
      <a href="#about"><span aria-hidden="true">▣</span> ABOUT</a>
      <a href="#research"><span aria-hidden="true">◇</span> RESEARCH</a>
      <a href="#news"><span aria-hidden="true">▤</span> NEWS</a>
      <a href="#publications"><span aria-hidden="true">▥</span> PAPERS</a>
      <a href="#projects"><span aria-hidden="true">▧</span> PROJECTS</a>
      <a href="#teaching"><span aria-hidden="true">▨</span> TEACHING</a>
      <a href="#cv"><span aria-hidden="true">▩</span> CV</a>
      <a href="#contact"><span aria-hidden="true">▰</span> CONTACT</a>
    </nav>

    <main id="main">
      <section class="hero-window pixel-window" aria-labelledby="hero-title">
        <div class="window-titlebar"><span>MINGHAO.EXE</span><span aria-hidden="true">_ □ ×</span></div>
        <div class="hero-content">
          <div class="pixel-avatar" aria-label="Pixel avatar panel">
            <img src="assets/img/avatar.png" alt="Pixel-style avatar for Minghao Mou">
          </div>
          <div class="hero-copy">
            <p class="boot-line" data-boot-line>BOOTING MINGHAO.EXE...</p>
            <h1 id="hero-title">Minghao Mou</h1>
            <p class="hero-role">Ph.D. candidate @ Purdue ECE</p>
            <p class="hero-description">Researching coupled energy infrastructure systems, generative models, and optimal control.</p>
            <div class="hero-actions">
              <a class="pixel-button primary" href="#publications">Enter Research</a>
              <a class="pixel-button" href="assets/files/curriculum_vitae.pdf">Open CV.PDF</a>
              <a class="pixel-button" href="#contact">Contact</a>
            </div>
          </div>
        </div>
      </section>

      <section id="about" class="pixel-window split-window" aria-labelledby="about-title">
        <div class="window-titlebar"><h2 id="about-title">ABOUT.EXE</h2><span>STATUS: ACTIVE</span></div>
        <div class="window-body split-body">
          <div>
            <dl class="status-grid">
              <div><dt>Status</dt><dd>Ph.D. candidate</dd></div>
              <div><dt>Affiliation</dt><dd>Elmore Family School of Electrical and Computer Engineering, Purdue University</dd></div>
              <div><dt>Advisor</dt><dd><a href="https://engineering.purdue.edu/people/junjie.qin.1">Dr. Junjie Qin</a></dd></div>
              <div><dt>Location</dt><dd>West Lafayette, Indiana</dd></div>
            </dl>
            <p>I am a Ph.D. candidate in <a href="https://engineering.purdue.edu/ECE">Elmore Family School of Electrical and Computer Engineering</a> at <a href="https://www.purdue.edu">Purdue University</a>, advised by <a href="https://engineering.purdue.edu/people/junjie.qin.1">Dr. Junjie Qin</a>. I obtained my Bachelor's degree in Mathematics from <a href="https://www.cuhk.edu.cn/en">Chinese University of Hong Kong, Shenzhen</a> in 2023, where I was advised by <a href="https://shuangli01.github.io">Dr. Shuang Li</a>.</p>
          </div>
          <figure class="portrait-frame">
            <img src="assets/img/IMG_5612.jpeg" alt="Portrait of Minghao Mou">
            <figcaption>PROFILE_IMG.PNG</figcaption>
          </figure>
        </div>
      </section>

      <section id="research" class="pixel-window" aria-labelledby="research-title">
        <div class="window-titlebar"><h2 id="research-title">RESEARCH_MODULES/</h2><span>3 INSTALLED</span></div>
        <div class="module-grid">
          <article class="module-card"><p class="module-index">[01]</p><h3>Coupled Energy Infrastructure Systems</h3><p>Modeling and analysis for infrastructure systems that connect energy, transportation, and decision-making layers.</p></article>
          <article class="module-card"><p class="module-index">[02]</p><h3>Generative Models</h3><p>Learning-based models for representing complex system behavior and supporting research workflows.</p></article>
          <article class="module-card"><p class="module-index">[03]</p><h3>Optimal Control</h3><p>Optimization and control methods for engineered systems with operational constraints.</p></article>
        </div>
      </section>

      <section id="news" class="pixel-window" aria-labelledby="news-title">
        <div class="window-titlebar"><h2 id="news-title">NEWS.LOG</h2><span>RECENT EVENTS</span></div>
        <ol class="news-log">
          <li><time datetime="2026-05">May 2026</time><span>I passed my PhD preliminary exam and now a PhD candidate.</span></li>
          <li><time datetime="2026-04">Apr. 2026</time><span>Our preprint <em>Braess' Paradoxes in Coupled Power and Transportation Systems</em> was revised on arXiv.</span></li>
          <li><time datetime="2025-12">Dec. 2025</time><span>Our preprint <em>Braess' Paradoxes in Coupled Power and Transportation Systems</em> was on arXiv.</span></li>
          <li><time datetime="2023-12">Dec. 2023</time><span>Our paper <em>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging</em> was accepted to ACC 2024.</span></li>
          <li><time datetime="2023-05">May 2023</time><span>I graduated from CUHKSZ with first-class honors.</span></li>
        </ol>
      </section>

      <section id="publications" class="pixel-window" aria-labelledby="publications-title">
        <div class="window-titlebar"><h2 id="publications-title">PUBLICATION_DATABASE</h2><span>ORDER: CURRENT</span></div>
        <div class="publication-list">
          <article class="publication-card">
            <img src="assets/img/braess_fig6.png" alt="Teaser figure for Braess' Paradoxes in Coupled Power and Transportation Systems">
            <div><p class="pub-badge">arXiv · Preprint</p><h3>Braess' Paradoxes in Coupled Power and Transportation Systems</h3><p class="authors"><strong>Minghao Mou</strong>, Junjie Qin</p><p class="venue">arXiv preprint arXiv:2512.12197, 2025</p><div class="pub-links"><a href="https://arxiv.org/pdf/2512.12197">PDF</a><a href="https://arxiv.org/abs/2512.12197">arXiv</a><a href="https://doi.org/10.48550/arXiv.2512.12197">DOI</a></div></div>
          </article>
          <article class="publication-card">
            <img src="assets/img/comp.jpg" alt="Teaser figure for Nexus Cognizant Pricing of Workplace Electric Vehicle Charging">
            <div><p class="pub-badge">ACC · Oral Presentation</p><h3>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging</h3><p class="authors"><strong>Minghao Mou</strong>, Sean Qian, Junjie Qin</p><p class="venue">American Control Conference, 2024</p><div class="pub-links"><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866">PDF</a><a href="https://scholar.googleusercontent.com/scholar.bib?q=info:2aKsKkaCZN8J:scholar.google.com/&amp;output=citation&amp;scisdr=ClEwu4xGEIz_i9RBe8o:AFWwaeYAAAAAZ2NHY8rMyvVbiTtta4oAMCCgeKw&amp;scisig=AFWwaeYAAAAAZ2NHY9hCxuAekf9tLmJHrGasrPE&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=en">BibTeX</a></div></div>
          </article>
        </div>
      </section>

      <section id="projects" class="pixel-window" aria-labelledby="projects-title">
        <div class="window-titlebar"><h2 id="projects-title">PROJECTS/</h2><span>PROGRAM FILES</span></div>
        <div class="module-grid">
          <article class="module-card"><p class="module-index">PVI_SOLVER.EXE</p><h3>Braess' Paradoxes in Coupled Power and Transportation Systems</h3><p>Research program connected to the arXiv preprint on coupled power and transportation systems.</p><a href="https://arxiv.org/abs/2512.12197">Open arXiv record</a></article>
          <article class="module-card"><p class="module-index">EV_PRICING.EXE</p><h3>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging</h3><p>Research program connected to the ACC 2024 paper on workplace electric vehicle charging.</p><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866">Open paper</a></article>
          <article class="module-card muted"><p class="module-index">NEXT_PROGRAM.SLOT</p><h3>Future project entry</h3><p>This section is reserved for a later project description supplied by Minghao Mou.</p></article>
        </div>
      </section>

      <section id="teaching" class="pixel-window terminal-window" aria-labelledby="teaching-title">
        <div class="window-titlebar"><h2 id="teaching-title">TEACHING/</h2><span>DIRECTORY</span></div>
        <div class="terminal-body"><p><span class="prompt">$</span> ls teaching</p><p>No teaching entries are currently listed on this website.</p></div>
      </section>

      <section id="cv" class="pixel-window" aria-labelledby="cv-title">
        <div class="window-titlebar"><h2 id="cv-title">CV.PDF</h2><span>READY</span></div>
        <p>Download the current curriculum vitae as a PDF.</p>
        <a class="pixel-button primary" href="assets/files/curriculum_vitae.pdf">Download CV</a>
      </section>

      <section id="contact" class="pixel-window terminal-window" aria-labelledby="contact-title">
        <div class="window-titlebar"><h2 id="contact-title">CONTACT_TERMINAL</h2><span>ONLINE</span></div>
        <div class="terminal-body">
          <p><span class="prompt">$</span> whoami</p><p>Minghao Mou</p>
          <p><span class="prompt">$</span> email</p><p><a href="mailto:mmou@purdue.edu">mmou@purdue.edu</a></p>
          <p><span class="prompt">$</span> links</p><p><a href="https://github.com/MhaoMou">GitHub</a> · <a href="https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&amp;hl=en">Google Scholar</a> · <a href="https://www.linkedin.com/in/minghao-mou-14a090289/">LinkedIn</a> · <a href="assets/files/curriculum_vitae.pdf">CV</a></p>
        </div>
      </section>
    </main>
  </div>
</body>
</html>
```

- [ ] **Step 2: Retire the old homepage source**

Run:

```bash
mv index.md legacy-index.md
```

Expected result:

```text
legacy-index.md exists and index.md no longer exists.
```

- [ ] **Step 3: Run validator and confirm CSS/JS failures remain**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result:

```text
FAIL: assets/css/pixel-research-os.css is missing
FAIL: assets/js/pixel-research-os.js is missing
```

- [ ] **Step 4: Commit the static HTML migration**

Run:

```bash
git add index.html legacy-index.md index.md
git commit -m "Add static Pixel Research OS homepage"
```

Expected result:

```text
[main <hash>] Add static Pixel Research OS homepage
```

## Task 3: Implement Pixel Research OS CSS

**Files:**
- Create: `assets/css/pixel-research-os.css`

- [ ] **Step 1: Add CSS design system and layout**

Create `assets/css/pixel-research-os.css` with these required blocks:

```css
:root {
  --bg: #11110f;
  --surface: #20201c;
  --surface-alt: #2b2a25;
  --text: #f6f0df;
  --text-muted: #c5bdac;
  --accent: #c49a3a;
  --accent-strong: #e4be62;
  --terminal: #7ee787;
  --border: #050505;
  --shadow: #050505;
  --danger: #d56b5d;
  --pixel: 4px;
  --radius: 0;
  --space-1: 0.35rem;
  --space-2: 0.65rem;
  --space-3: 1rem;
  --space-4: 1.5rem;
  --space-5: 2.25rem;
  --font-pixel: "Courier New", "Lucida Console", monospace;
  --font-body: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --duration: 160ms;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  min-height: 100vh;
  color: var(--text);
  background:
    linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px),
    linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
    var(--bg);
  background-size: 24px 24px;
  font-family: var(--font-body);
  line-height: 1.6;
}
a { color: var(--accent-strong); text-decoration: none; }
a:hover { text-decoration: underline; }
.skip-link {
  position: absolute;
  left: 1rem;
  top: -4rem;
  z-index: 30;
  background: var(--accent);
  color: var(--border);
  padding: 0.5rem 0.75rem;
}
.skip-link:focus { top: 1rem; }
:focus-visible {
  outline: 3px solid var(--terminal);
  outline-offset: 3px;
}
.os-topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: grid;
  grid-template-columns: auto auto 1fr auto;
  gap: var(--space-3);
  align-items: center;
  min-height: 54px;
  padding: 0.65rem clamp(0.75rem, 2vw, 1.5rem);
  background: var(--surface-alt);
  border-bottom: var(--pixel) solid var(--border);
  box-shadow: 0 var(--pixel) 0 var(--shadow);
  font-family: var(--font-pixel);
  text-transform: uppercase;
}
.brand { color: var(--accent-strong); font-weight: 800; letter-spacing: 0; }
.system-label, .topbar-affiliation { color: var(--text-muted); font-size: 0.85rem; }
.quick-links, .desktop-nav, .hero-actions, .pub-links { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.quick-links a, .desktop-nav a, .pixel-button, .pub-links a {
  display: inline-flex;
  align-items: center;
  min-height: 38px;
  padding: 0.45rem 0.7rem;
  color: var(--text);
  background: var(--surface);
  border: 2px solid var(--border);
  box-shadow: 3px 3px 0 var(--shadow);
  font-family: var(--font-pixel);
  font-size: 0.82rem;
  line-height: 1.2;
  text-transform: uppercase;
}
.quick-links a:hover, .desktop-nav a:hover, .pixel-button:hover, .pub-links a:hover {
  background: var(--accent);
  color: var(--border);
  text-decoration: none;
  transform: translate(1px, 1px);
  box-shadow: 2px 2px 0 var(--shadow);
}
.pixel-button.primary { background: var(--accent); color: var(--border); font-weight: 800; }
.desktop-grid {
  display: grid;
  grid-template-columns: minmax(170px, 220px) minmax(0, 1fr);
  gap: var(--space-5);
  width: min(1180px, calc(100% - 2rem));
  margin: 2rem auto 4rem;
}
.desktop-nav {
  position: sticky;
  top: 78px;
  align-self: start;
  flex-direction: column;
}
main { display: grid; gap: var(--space-5); min-width: 0; }
.pixel-window {
  background: var(--surface);
  border: var(--pixel) solid var(--border);
  box-shadow: 8px 8px 0 var(--shadow);
}
.window-titlebar {
  display: flex;
  justify-content: space-between;
  gap: var(--space-3);
  align-items: center;
  padding: 0.65rem 0.85rem;
  color: var(--border);
  background: var(--accent);
  border-bottom: var(--pixel) solid var(--border);
  font-family: var(--font-pixel);
  font-size: 0.82rem;
  text-transform: uppercase;
}
.window-titlebar h2 { margin: 0; font-size: inherit; letter-spacing: 0; }
.window-body, .hero-content { padding: clamp(1rem, 3vw, 2rem); }
.hero-content {
  display: grid;
  grid-template-columns: minmax(120px, 180px) minmax(0, 1fr);
  gap: var(--space-5);
  align-items: center;
}
.pixel-avatar {
  aspect-ratio: 1;
  display: grid;
  place-items: center;
  background: var(--surface-alt);
  border: var(--pixel) solid var(--border);
  box-shadow: 6px 6px 0 var(--shadow);
  image-rendering: pixelated;
}
.pixel-avatar img { width: 72%; image-rendering: pixelated; }
.boot-line, .module-index, .pub-badge, .prompt { color: var(--terminal); font-family: var(--font-pixel); text-transform: uppercase; }
h1 {
  margin: 0;
  color: var(--accent-strong);
  font-family: var(--font-pixel);
  font-size: clamp(2rem, 7vw, 4.5rem);
  line-height: 1.1;
  letter-spacing: 0;
}
.hero-role { margin: 0.75rem 0 0; font-size: clamp(1rem, 2vw, 1.35rem); color: var(--text); }
.hero-description { max-width: 62ch; color: var(--text-muted); }
.split-body {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(180px, 260px);
  gap: var(--space-5);
}
.status-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-3);
  margin: 0 0 var(--space-4);
}
.status-grid div, .module-card, .publication-card, .terminal-body {
  background: var(--surface-alt);
  border: 2px solid var(--border);
  box-shadow: 4px 4px 0 var(--shadow);
  padding: var(--space-3);
}
dt { color: var(--terminal); font-family: var(--font-pixel); font-size: 0.78rem; text-transform: uppercase; }
dd { margin: 0.2rem 0 0; }
.portrait-frame { margin: 0; }
.portrait-frame img {
  display: block;
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border: var(--pixel) solid var(--border);
  box-shadow: 6px 6px 0 var(--shadow);
}
.portrait-frame figcaption { margin-top: 0.65rem; color: var(--text-muted); font-family: var(--font-pixel); font-size: 0.78rem; }
.module-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: var(--space-3);
  padding: clamp(1rem, 3vw, 1.5rem);
}
.module-card h3, .publication-card h3 { margin: 0.2rem 0 0.5rem; color: var(--text); line-height: 1.3; }
.module-card.muted { opacity: 0.78; }
.news-log {
  display: grid;
  gap: var(--space-2);
  margin: 0;
  padding: clamp(1rem, 3vw, 1.5rem);
  list-style: none;
}
.news-log li {
  display: grid;
  grid-template-columns: 8rem minmax(0, 1fr);
  gap: var(--space-3);
  padding: var(--space-2);
  border-left: var(--pixel) solid var(--accent);
  background: rgba(255,255,255,0.035);
}
.news-log time { color: var(--accent-strong); font-family: var(--font-pixel); font-size: 0.78rem; }
.publication-list { display: grid; gap: var(--space-4); padding: clamp(1rem, 3vw, 1.5rem); }
.publication-card {
  display: grid;
  grid-template-columns: 180px minmax(0, 1fr);
  gap: var(--space-4);
}
.publication-card img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border: 2px solid var(--border);
}
.authors, .venue { margin: 0.25rem 0; color: var(--text-muted); }
.terminal-window .terminal-body { margin: clamp(1rem, 3vw, 1.5rem); }
@media (hover: hover) and (pointer: fine) {
  body { cursor: crosshair; }
  a, button { cursor: pointer; }
}
@media (max-width: 900px) {
  .os-topbar { grid-template-columns: 1fr; align-items: start; }
  .desktop-grid { grid-template-columns: 1fr; margin-top: 1rem; }
  .desktop-nav { position: static; flex-direction: row; }
  .module-grid { grid-template-columns: 1fr; }
  .split-body, .hero-content, .publication-card { grid-template-columns: 1fr; }
  .pixel-avatar { max-width: 180px; }
}
@media (max-width: 520px) {
  .desktop-grid { width: min(100% - 1rem, 1180px); gap: var(--space-4); }
  .pixel-window { border-width: 3px; box-shadow: 5px 5px 0 var(--shadow); }
  .window-titlebar { align-items: flex-start; flex-direction: column; }
  .status-grid, .news-log li { grid-template-columns: 1fr; }
  .quick-links a, .desktop-nav a, .pixel-button, .pub-links a { width: 100%; justify-content: center; }
  h1 { font-size: 2rem; }
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Step 2: Run validator and confirm only JS failure remains**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result:

```text
FAIL: assets/js/pixel-research-os.js is missing
```

- [ ] **Step 3: Commit CSS**

Run:

```bash
git add assets/css/pixel-research-os.css
git commit -m "Add Pixel Research OS design system"
```

Expected result:

```text
[main <hash>] Add Pixel Research OS design system
```

## Task 4: Add Progressive Enhancement JavaScript

**Files:**
- Create: `assets/js/pixel-research-os.js`

- [ ] **Step 1: Add JavaScript**

Create `assets/js/pixel-research-os.js` with this complete content:

```javascript
(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const bootLine = document.querySelector("[data-boot-line]");
  const navLinks = Array.from(document.querySelectorAll(".desktop-nav a"));
  const sections = navLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (bootLine && !reducedMotion.matches) {
    const states = [
      "BOOTING MINGHAO.EXE...",
      "LOADING RESEARCH MODULES...",
      "READY."
    ];
    let index = 0;
    const timer = window.setInterval(() => {
      index += 1;
      bootLine.textContent = states[index] || states[states.length - 1];
      if (index >= states.length - 1) {
        window.clearInterval(timer);
      }
    }, 420);
  } else if (bootLine) {
    bootLine.textContent = "READY.";
  }

  if ("IntersectionObserver" in window && navLinks.length && sections.length) {
    const linkById = new Map(navLinks.map((link) => [link.getAttribute("href").slice(1), link]));
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        const link = linkById.get(entry.target.id);
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach((item) => item.removeAttribute("aria-current"));
          link.setAttribute("aria-current", "location");
        }
      });
    }, { rootMargin: "-35% 0px -55% 0px", threshold: 0.01 });
    sections.forEach((section) => observer.observe(section));
  }
})();
```

- [ ] **Step 2: Run static validator**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result:

```text
PASS: Pixel Research OS static validation
```

- [ ] **Step 3: Commit JS**

Run:

```bash
git add assets/js/pixel-research-os.js
git commit -m "Add Pixel Research OS interactions"
```

Expected result:

```text
[main <hash>] Add Pixel Research OS interactions
```

## Task 5: Verify GitHub Pages Build Compatibility

**Files:**
- No source changes expected unless build reveals a compatibility issue.

- [ ] **Step 1: Run Jekyll build**

Run:

```bash
bundle exec jekyll build
```

Expected result:

```text
done in
```

If dependencies are missing, run:

```bash
bundle install
bundle exec jekyll build
```

Expected result:

```text
Bundle complete
done in
```

- [ ] **Step 2: Inspect generated homepage exists**

Run:

```bash
test -f _site/index.html
```

Expected result: command exits with status `0`.

- [ ] **Step 3: Commit any build-compatibility source fixes**

If Step 1 required source changes, run:

```bash
git add index.html assets/css/pixel-research-os.css assets/js/pixel-research-os.js legacy-index.md
git commit -m "Fix GitHub Pages static homepage build"
```

Expected result:

```text
[main <hash>] Fix GitHub Pages static homepage build
```

If there were no source changes, do not create an empty commit.

## Task 6: Local Visual And Responsive Check

**Files:**
- Modify source files only if the checks reveal concrete layout issues.

- [ ] **Step 1: Start a local static server**

Run:

```bash
python3 -m http.server 4173
```

Expected result:

```text
Serving HTTP on :: port 4173
```

- [ ] **Step 2: Inspect manually in browser if available**

Open:

```text
http://localhost:4173/
```

Check:

- Top bar links are immediately visible.
- Hero identifies Minghao Mou and Purdue ECE.
- Publications are readable.
- CV button is visible in the first viewport and in the CV section.
- No horizontal overflow at 375 px, 768 px, 1024 px, and 1440 px.
- Touch-size buttons are usable at mobile widths.
- Portrait and publication teaser images load.
- Focus states are visible by tabbing through links.

- [ ] **Step 3: Stop the local static server**

Stop the server with `Ctrl-C` in the running terminal session.

- [ ] **Step 4: Commit visual fixes if needed**

If source fixes were made, run:

```bash
git add index.html assets/css/pixel-research-os.css assets/js/pixel-research-os.js
git commit -m "Polish Pixel Research OS responsive layout"
```

Expected result:

```text
[main <hash>] Polish Pixel Research OS responsive layout
```

If no source fixes were needed, do not create an empty commit.

## Task 7: Final Validation And Handoff

**Files:**
- No source changes expected unless final validation reveals an issue.

- [ ] **Step 1: Run final static validation**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result:

```text
PASS: Pixel Research OS static validation
```

- [ ] **Step 2: Run final build**

Run:

```bash
bundle exec jekyll build
```

Expected result:

```text
done in
```

- [ ] **Step 3: Check git status**

Run:

```bash
git status --short --branch
```

Expected result: branch may be ahead of `origin/main`, but there should be no unstaged or staged source changes.

- [ ] **Step 4: Report outcome**

Report:

- Files created and renamed.
- Validation commands and results.
- Whether local visual inspection was performed.
- That no remote push was performed.

## Self-Review

Spec coverage:

- Static HTML rewrite: Task 2.
- Preserved content and links: Task 2 plus Task 1 validation.
- Pixel OS design system: Task 3.
- Lightweight JS interactions and reduced motion: Task 4.
- Mobile/accessibility requirements: Task 3 plus Task 6.
- GitHub Pages compatibility: Task 5 and Task 7.
- No push or destructive git operations: all commit steps are local only.

Plan scan:

- No unfinished implementation markers are used in source code snippets.
- Missing teaching content is represented by a factual statement, not an invented claim.
- Projects derive from existing publications and one clearly reserved future project entry.

Execution risk:

- `bundle exec jekyll build` may require `bundle install` if local gems are unavailable.
- Browser-based visual checks may be limited if no browser automation or local browser access is available.

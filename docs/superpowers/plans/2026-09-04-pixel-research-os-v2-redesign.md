# Pixel Research OS V2 Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the current homepage into a coherent app-like `MINGHAO.EXE — PIXEL RESEARCH OS` desktop/workstation while preserving all factual academic content and GitHub Pages compatibility.

**Architecture:** Keep the site as a static Jekyll-compatible homepage using `index.html`, one CSS file, and one small vanilla JavaScript file. The page remains semantic and crawlable without JavaScript, while CSS and JS create the desktop shell, monitor-first lab console, command-center windows, active taskbar state, local time, and restrained OS interactions.

**Tech Stack:** Static HTML, CSS custom properties, vanilla JavaScript, Python 3 standard-library validation, headless Chrome screenshot QA, Jekyll/GitHub Pages.

---

## File Structure

- Modify `index.html`: replace the current vertical stack with a desktop-shell page model, monitor-first hero console, identity panel, four-window command center, research modules, paper records, compact system log, `ABOUT.EXE`, `PROJECTS/`, `TEACHING/`, `CV.PDF`, and `CONTACT_TERMINAL`.
- Modify `assets/css/pixel-research-os.css`: rebuild the design tokens, shell layout, lab-console pixel art, reusable window system, paper records, research modules, taskbar, responsive layouts, focus states, and reduced-motion behavior.
- Modify `assets/js/pixel-research-os.js`: replace the current boot/nav enhancement with reduced-motion-aware OS state, active section/window tracking, local time, taskbar label updates, and optional panel-selection state.
- Modify `scripts/validate_pixel_research_os.py`: add v2 structural checks for the shell, hero console, real portrait placement, command center, Paper Database, System Log, and visual-safeguard rules.
- Use existing local assets only: `assets/img/IMG_5612.jpeg`, `assets/img/braess_fig6.png`, `assets/img/comp.jpg`, `assets/img/favicon.png`, `assets/img/favicon-dark.png`, `assets/files/curriculum_vitae.pdf`.
- Keep `.superpowers/` ignored. Do not commit screenshots or brainstorm mockups unless Minghao explicitly asks.

## Content Constants

Use these exact facts and links in the implementation:

- Name: `Minghao Mou`
- Role: `Ph.D. candidate at Purdue ECE`
- Full affiliation: `Elmore Family School of Electrical and Computer Engineering, Purdue University`
- Advisor: `Dr. Junjie Qin`
- Undergraduate institution: `Chinese University of Hong Kong, Shenzhen`
- Undergraduate advisor: `Dr. Shuang Li`
- Email: `mmou@purdue.edu`
- Research interests: `Coupled Energy Infrastructure Systems`, `Generative Models`, `Optimal Control`
- CV: `assets/files/curriculum_vitae.pdf`
- Real portrait: `assets/img/IMG_5612.jpeg`
- Publication teasers: `assets/img/braess_fig6.png`, `assets/img/comp.jpg`
- Google Scholar: `https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en`
- GitHub: `https://github.com/MhaoMou`
- LinkedIn: `https://www.linkedin.com/in/minghao-mou-14a090289/`
- Purdue: `https://www.purdue.edu`
- Purdue ECE: `https://engineering.purdue.edu/ECE`
- Advisor page: `https://engineering.purdue.edu/people/junjie.qin.1`
- CUHKSZ: `https://www.cuhk.edu.cn/en`
- Dr. Shuang Li: `https://shuangli01.github.io`
- Braess PDF: `https://arxiv.org/pdf/2512.12197`
- Braess arXiv: `https://arxiv.org/abs/2512.12197`
- Braess DOI: `https://doi.org/10.48550/arXiv.2512.12197`
- ACC paper PDF: `https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866`
- ACC BibTeX: `https://scholar.googleusercontent.com/scholar.bib?q=info:2aKsKkaCZN8J:scholar.google.com/&output=citation&scisdr=ClEwu4xGEIz_i9RBe8o:AFWwaeYAAAAAZ2NHY8rMyvVbiTtta4oAMCCgeKw&scisig=AFWwaeYAAAAAZ2NHY9hCxuAekf9tLmJHrGasrPE&scisf=4&ct=citation&cd=-1&hl=en`

## Task 1: Strengthen Static Validation For V2

**Files:**
- Modify: `scripts/validate_pixel_research_os.py`
- Test: `python3 scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Add v2 required sections and selectors**

Update the validation constants so the validator checks the new shell and visual system. Keep all existing required factual content and links. Add these constants near the other required lists:

```python
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
```

- [ ] **Step 2: Add parser support for classes and hero/about scope**

Extend `StructureParser.__init__`:

```python
self.classes = set()
self.hero_image_srcs = []
self.about_image_srcs = []
self.section_stack = []
```

Extend `handle_starttag`:

```python
if attrs.get("class"):
    self.classes.update(attrs["class"].split())
if tag in {"section", "header", "main", "footer"} and attrs.get("id"):
    self.section_stack.append(attrs["id"])
if tag == "img":
    src = self.normalize(attrs.get("src", ""))
    current_scope = self.section_stack[-1] if self.section_stack else ""
    if current_scope == "hero" and src:
        self.hero_image_srcs.append(src)
    if current_scope == "about" and src:
        self.about_image_srcs.append(src)
```

Extend `handle_endtag`:

```python
if tag.lower() in {"section", "header", "main", "footer"} and self.section_stack:
    self.section_stack.pop()
```

- [ ] **Step 3: Add v2 assertions**

In `main()`, after the required favicon/link checks, add:

```python
for class_name in REQUIRED_V2_CLASSES:
    if class_name not in parser.classes:
        failures.append(f"required v2 class missing from index.html: {class_name}")

if FORBIDDEN_HERO_IMAGE_SRC in parser.hero_image_srcs:
    failures.append("hero must use illustrated lab/console art, not the real portrait")

if ABOUT_PORTRAIT_SRC not in parser.about_image_srcs:
    failures.append("ABOUT.EXE must contain the real portrait image")

if "PAPER_DATABASE" not in html and "PAPER DATABASE" not in html:
    failures.append("Paper Database label missing")

if "SYSTEM LOG" not in html:
    failures.append("System Log label missing")

if re.search(r"font-size\s*:[^;{}]*[0-9.]\s*vw\b", css, re.IGNORECASE):
    failures.append("CSS must not scale font-size with viewport width")

if re.search(r"border-radius\s*:\s*(1[0-9]|[2-9][0-9])px", css, re.IGNORECASE):
    failures.append("large rounded card radii are not allowed")

if re.search(r"\b(backdrop-filter|filter\s*:\s*blur|box-shadow\s*:[^;]*rgba\([^)]*,\s*0\.[0-9]+\\)[^;]*[1-9][0-9]px)", css, re.IGNORECASE):
    failures.append("blur/glass/soft-shadow visual effects are not allowed")
```

- [ ] **Step 4: Run the validator and confirm it fails against the current site**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
```

Expected result: FAIL entries for missing v2 classes such as `desktop-shell`, `lab-console`, `identity-panel`, `desktop-taskbar`, and `command-center`.

- [ ] **Step 5: Commit the validator change**

Run:

```bash
git add scripts/validate_pixel_research_os.py
git commit -m "Strengthen Pixel Research OS v2 validation"
```

Expected result: one commit containing only `scripts/validate_pixel_research_os.py`.

## Task 2: Rebuild The Semantic Desktop Shell HTML

**Files:**
- Modify: `index.html`
- Test: `python3 scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Replace the body with the v2 shell skeleton**

Keep the existing `<head>` metadata, favicon links, stylesheet link, and script link. Replace only the `<body>` contents with this shell structure, then fill each marked region in the following steps:

```html
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="desktop-shell" id="top">
    <header class="desktop-titlebar" aria-label="Pixel Research OS title bar">
      <a class="brand-lockup" href="#top" aria-label="Minghao Mou homepage">
        <span class="brand-mark" aria-hidden="true">■</span>
        <span>MINGHAO RESEARCH OS</span>
      </a>
      <span class="titlebar-chip">Purdue ECE</span>
      <nav class="desktop-nav" aria-label="Primary navigation">
        <a href="#research">Research</a>
        <a href="#publications">Papers</a>
        <a href="assets/files/curriculum_vitae.pdf">CV</a>
        <a href="#contact">Contact</a>
      </nav>
    </header>

    <main id="main" class="desktop-workspace">
      <section id="hero" class="hero-desktop" aria-labelledby="hero-title">
        <!-- Fill in Task 2 Step 2. -->
      </section>

      <section class="command-center" aria-label="Research OS command center">
        <!-- Fill in Task 2 Steps 3-7. -->
      </section>
    </main>

    <footer class="desktop-taskbar" aria-label="Pixel Research OS taskbar">
      <a class="taskbar-start" href="#top">■ START</a>
      <nav class="taskbar-nav" aria-label="Persistent navigation">
        <a href="#research">Research</a>
        <a href="#publications">Papers</a>
        <a href="assets/files/curriculum_vitae.pdf">CV.PDF</a>
        <a href="#contact">Contact</a>
      </nav>
      <span class="taskbar-status" data-status-line>SYSTEM READY</span>
      <time class="taskbar-time" data-local-time aria-label="Local time"></time>
    </footer>
  </div>
</body>
```

- [ ] **Step 2: Add the monitor-first hero console and identity panel**

Inside `section#hero`, add:

```html
<div class="lab-console pixel-window active-window">
  <div class="window-titlebar">
    <span>LAB_CONSOLE.EXE</span>
    <span aria-hidden="true">● ● ●</span>
  </div>
  <div class="console-stage" aria-label="Pixel-art research workstation">
    <div class="console-monitor">
      <div class="monitor-toolbar">PVI_GRID_VIEW</div>
      <svg class="console-plot" viewBox="0 0 240 150" role="img" aria-labelledby="plot-title plot-desc">
        <title id="plot-title">Optimization plot and network diagram</title>
        <desc id="plot-desc">A stylized research monitor showing an optimization curve and connected grid nodes.</desc>
        <polyline points="14,124 46,102 74,108 104,64 142,76 178,44 222,24" />
        <g class="plot-nodes">
          <circle cx="46" cy="102" r="6" />
          <circle cx="104" cy="64" r="6" />
          <circle cx="178" cy="44" r="6" />
          <circle cx="222" cy="24" r="6" />
        </g>
        <g class="grid-network">
          <line x1="42" y1="42" x2="88" y2="22" />
          <line x1="42" y1="42" x2="88" y2="82" />
          <line x1="88" y1="22" x2="136" y2="58" />
          <line x1="88" y1="82" x2="136" y2="58" />
        </g>
      </svg>
    </div>
    <div class="console-desk" aria-hidden="true">
      <span class="desk-paper paper-a"></span>
      <span class="desk-paper paper-b"></span>
      <span class="avatar-silhouette"></span>
      <span class="desk-keyboard"></span>
    </div>
    <div class="console-notes" aria-hidden="true">
      <span>energy</span>
      <span>flows</span>
      <span>control</span>
    </div>
  </div>
</div>

<aside class="identity-panel pixel-window" aria-labelledby="hero-title">
  <div class="window-titlebar">
    <span>PROFILE.SYS</span>
    <span>ONLINE</span>
  </div>
  <div class="identity-body">
    <p class="boot-line" data-boot-line>BOOTING MINGHAO.EXE...</p>
    <h1 id="hero-title">Minghao Mou</h1>
    <p class="hero-role">Ph.D. candidate at Purdue ECE</p>
    <p class="hero-description">Researching Coupled Energy Infrastructure Systems, Generative Models, and Optimal Control.</p>
    <ul class="identity-tags" aria-label="Research areas">
      <li>Coupled Energy Infrastructure Systems</li>
      <li>Generative Models</li>
      <li>Optimal Control</li>
    </ul>
    <div class="hero-actions">
      <a class="pixel-button primary" href="#research">Research</a>
      <a class="pixel-button primary" href="assets/files/curriculum_vitae.pdf">Open CV.PDF</a>
      <a class="pixel-button" href="#publications">Publications</a>
      <a class="pixel-button" href="#contact">Contact</a>
    </div>
  </div>
</aside>
```

- [ ] **Step 3: Add `RESEARCH_MODULES/` window**

Inside `.command-center`, add:

```html
<section id="research" class="pixel-window command-window research-window" aria-labelledby="research-title" data-window="Research">
  <div class="window-titlebar">
    <h2 id="research-title">RESEARCH_MODULES/</h2>
    <span>3 installed</span>
  </div>
  <div class="module-grid">
    <article class="research-module">
      <p class="module-index">MODULE_01</p>
      <h3>Coupled Energy Infrastructure Systems</h3>
      <p>Modeling and analysis for infrastructure systems that connect energy, transportation, and decision-making layers.</p>
      <a href="#publications">Inspect related papers</a>
    </article>
    <article class="research-module">
      <p class="module-index">MODULE_02</p>
      <h3>Generative Models</h3>
      <p>Learning-based models for representing complex system behavior and supporting research workflows.</p>
      <a href="#publications">Inspect related papers</a>
    </article>
    <article class="research-module">
      <p class="module-index">MODULE_03</p>
      <h3>Optimal Control</h3>
      <p>Optimization and control methods for engineered systems with operational constraints.</p>
      <a href="#publications">Inspect related papers</a>
    </article>
  </div>
</section>
```

- [ ] **Step 4: Add `PAPER_DATABASE` window**

Inside `.command-center`, add:

```html
<section id="publications" class="pixel-window command-window papers-window" aria-labelledby="publications-title" data-window="Papers">
  <div class="window-titlebar">
    <h2 id="publications-title">PAPER_DATABASE</h2>
    <span>2 records</span>
  </div>
  <div class="paper-list">
    <article class="paper-record">
      <div class="paper-teaser">
        <img src="assets/img/braess_fig6.png" alt="Teaser figure for Braess' Paradoxes in Coupled Power and Transportation Systems">
      </div>
      <div class="paper-body">
        <p class="record-id">PAPER_002 · arXiv / Preprint</p>
        <h3>Braess' Paradoxes in Coupled Power and Transportation Systems</h3>
        <p class="authors"><strong>Minghao Mou</strong>, Junjie Qin</p>
        <p class="venue">arXiv preprint arXiv:2512.12197, 2025</p>
        <p class="paper-note">Preprint</p>
        <div class="pub-links">
          <a href="https://arxiv.org/pdf/2512.12197">PDF</a>
          <a href="https://arxiv.org/abs/2512.12197">arXiv</a>
          <a href="https://doi.org/10.48550/arXiv.2512.12197">DOI</a>
        </div>
      </div>
    </article>
    <article class="paper-record">
      <div class="paper-teaser">
        <img src="assets/img/comp.jpg" alt="Teaser figure for Nexus Cognizant Pricing of Workplace Electric Vehicle Charging">
      </div>
      <div class="paper-body">
        <p class="record-id">PAPER_001 · ACC / Oral Presentation</p>
        <h3>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging</h3>
        <p class="authors"><strong>Minghao Mou</strong>, Sean Qian, Junjie Qin</p>
        <p class="venue">American Control Conference, 2024</p>
        <p class="paper-note">Oral Presentation</p>
        <div class="pub-links">
          <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866">PDF</a>
          <a href="https://scholar.googleusercontent.com/scholar.bib?q=info:2aKsKkaCZN8J:scholar.google.com/&amp;output=citation&amp;scisdr=ClEwu4xGEIz_i9RBe8o:AFWwaeYAAAAAZ2NHY8rMyvVbiTtta4oAMCCgeKw&amp;scisig=AFWwaeYAAAAAZ2NHY9hCxuAekf9tLmJHrGasrPE&amp;scisf=4&amp;ct=citation&amp;cd=-1&amp;hl=en">BibTeX</a>
        </div>
      </div>
    </article>
  </div>
</section>
```

- [ ] **Step 5: Add `ABOUT.EXE` window**

Inside `.command-center`, add:

```html
<section id="about" class="pixel-window command-window about-window" aria-labelledby="about-title" data-window="About">
  <div class="window-titlebar">
    <h2 id="about-title">ABOUT.EXE</h2>
    <span>Status: Active</span>
  </div>
  <div class="about-layout">
    <div class="about-copy">
      <dl class="status-grid">
        <div>
          <dt>Status</dt>
          <dd>Ph.D. candidate</dd>
        </div>
        <div>
          <dt>Affiliation</dt>
          <dd>Elmore Family School of Electrical and Computer Engineering, Purdue University</dd>
        </div>
        <div>
          <dt>Advisor</dt>
          <dd><a href="https://engineering.purdue.edu/people/junjie.qin.1">Dr. Junjie Qin</a></dd>
        </div>
        <div>
          <dt>Email</dt>
          <dd><a href="mailto:mmou@purdue.edu">mmou@purdue.edu</a></dd>
        </div>
      </dl>
      <p>I am a Ph.D. candidate in <a href="https://engineering.purdue.edu/ECE">Elmore Family School of Electrical and Computer Engineering</a> at <a href="https://www.purdue.edu">Purdue University</a>, advised by <a href="https://engineering.purdue.edu/people/junjie.qin.1">Dr. Junjie Qin</a>. I obtained my Bachelor's degree in Mathematics from <a href="https://www.cuhk.edu.cn/en">Chinese University of Hong Kong, Shenzhen</a> in 2023, where I was advised by <a href="https://shuangli01.github.io">Dr. Shuang Li</a>.</p>
    </div>
    <figure class="portrait-frame">
      <img src="assets/img/IMG_5612.jpeg" alt="Portrait of Minghao Mou">
      <figcaption>PROFILE_IMG.PNG</figcaption>
    </figure>
  </div>
</section>
```

- [ ] **Step 6: Add compact `SYSTEM LOG`, `PROJECTS/`, `TEACHING/`, `CV.PDF`, and `CONTACT_TERMINAL` content**

Inside `.command-center`, add one combined support window to keep the four-window structure:

```html
<section id="news" class="pixel-window command-window support-window" aria-labelledby="support-title" data-window="Log">
  <div class="window-titlebar">
    <h2 id="support-title">SYSTEM LOG + PROJECTS/</h2>
    <span>Support</span>
  </div>
  <div class="support-grid">
    <div class="system-log">
      <h3>SYSTEM LOG</h3>
      <ol>
        <li><time datetime="2026-05">May 2026</time><span>I passed my PhD preliminary exam and am now a Ph.D. candidate.</span></li>
        <li><time datetime="2026-04">Apr. 2026</time><span>Our preprint <em>Braess' Paradoxes in Coupled Power and Transportation Systems</em> was revised on arXiv.</span></li>
        <li><time datetime="2025-12">Dec. 2025</time><span>Our preprint <em>Braess' Paradoxes in Coupled Power and Transportation Systems</em> was on arXiv.</span></li>
        <li><time datetime="2023-12">Dec. 2023</time><span>Our paper <em>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging</em> was accepted to ACC 2024.</span></li>
        <li><time datetime="2023-05">May 2023</time><span>I graduated from CUHKSZ with first-class honors.</span></li>
      </ol>
    </div>
    <div id="projects" class="project-folder">
      <h3>PROJECTS/</h3>
      <article>
        <h4>PVI_SOLVER.EXE</h4>
        <p>Braess' Paradoxes in Coupled Power and Transportation Systems.</p>
        <a href="https://arxiv.org/abs/2512.12197">Open arXiv record</a>
      </article>
      <article>
        <h4>EV_PRICING.EXE</h4>
        <p>Nexus Cognizant Pricing of Workplace Electric Vehicle Charging.</p>
        <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866">Open paper</a>
      </article>
    </div>
    <div id="teaching" class="terminal-panel">
      <h3>TEACHING/</h3>
      <p><span class="prompt">$</span> ls teaching</p>
      <p>No teaching entries are currently listed on this website.</p>
    </div>
    <div id="cv" class="terminal-panel">
      <h3>CV.PDF</h3>
      <p>Download the current curriculum vitae as a PDF.</p>
      <a class="pixel-button primary" href="assets/files/curriculum_vitae.pdf">Open CV.PDF</a>
    </div>
    <div id="contact" class="terminal-panel contact-panel">
      <h3>CONTACT_TERMINAL</h3>
      <p><span class="prompt">$</span> email</p>
      <p><a href="mailto:mmou@purdue.edu">mmou@purdue.edu</a></p>
      <p><a href="https://github.com/MhaoMou">GitHub</a> | <a href="https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&amp;hl=en">Google Scholar</a> | <a href="https://www.linkedin.com/in/minghao-mou-14a090289/">LinkedIn</a> | <a href="assets/files/curriculum_vitae.pdf">CV</a></p>
    </div>
  </div>
</section>
```

- [ ] **Step 7: Confirm the BibTeX URL and run validation**

Run:

```bash
rg -n "scholar\\.bib" index.html _data/publications.yml
python3 scripts/validate_pixel_research_os.py
```

Expected result: the Scholar BibTeX URL appears in `index.html` and `_data/publications.yml`. The validator may still fail for missing CSS or JS class/style checks until later tasks.

- [ ] **Step 8: Commit the HTML shell**

Run:

```bash
git add index.html
git commit -m "Rebuild Pixel Research OS v2 homepage shell"
```

Expected result: one commit containing only `index.html`.

## Task 3: Rebuild The Visual System CSS

**Files:**
- Modify: `assets/css/pixel-research-os.css`
- Test: `python3 scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Replace global tokens and base styles**

Replace the top token block and base styles with variables in this shape:

```css
:root {
  --bg: #11110d;
  --bg-grid: rgba(246, 240, 223, 0.035);
  --surface: #1d1d18;
  --surface-alt: #29291f;
  --surface-strong: #343225;
  --text: #f4eedc;
  --text-muted: #c6bdab;
  --accent: #c89b3c;
  --accent-strong: #e2bd63;
  --terminal: #78d88a;
  --cyan: #7dbac3;
  --border: #050505;
  --shadow: #050505;
  --pixel: 3px;
  --space-1: 0.35rem;
  --space-2: 0.65rem;
  --space-3: 1rem;
  --space-4: 1.5rem;
  --space-5: 2rem;
  --font-ui: "Courier New", "Lucida Console", monospace;
  --font-body: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --duration: 150ms;
}
```

Ensure `body` uses `var(--font-body)` and a subtle grid texture. Keep text readable and avoid any `font-size: ...vw`.

- [ ] **Step 2: Add reusable window and button styles**

Add styles for:

```css
.pixel-window,
.window-titlebar,
.pixel-button,
.desktop-nav a,
.taskbar-nav a,
.research-module,
.paper-record,
.terminal-panel {
  border-color: var(--border);
}
```

Use hard shadows only:

```css
.pixel-window {
  background: var(--surface);
  border: var(--pixel) solid var(--border);
  box-shadow: 7px 7px 0 var(--shadow);
}

.window-titlebar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  min-height: 38px;
  padding: 0.55rem 0.75rem;
  color: var(--border);
  background: var(--accent);
  border-bottom: var(--pixel) solid var(--border);
  font-family: var(--font-ui);
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
}

.pixel-button,
.desktop-nav a,
.taskbar-nav a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 40px;
  padding: 0.5rem 0.75rem;
  color: var(--text);
  background: var(--surface-alt);
  border: 2px solid var(--border);
  box-shadow: 3px 3px 0 var(--shadow);
  font-family: var(--font-ui);
  font-size: 0.78rem;
  line-height: 1.15;
  text-transform: uppercase;
  transition: transform var(--duration) ease, box-shadow var(--duration) ease, background var(--duration) ease, color var(--duration) ease;
}
```

- [ ] **Step 3: Build the desktop shell and first viewport**

Add desktop layout rules:

```css
.desktop-shell {
  min-height: 100vh;
  display: grid;
  grid-template-rows: auto 1fr auto;
}

.desktop-titlebar,
.desktop-taskbar {
  position: sticky;
  z-index: 20;
  background: var(--surface-strong);
  border-color: var(--border);
}

.desktop-titlebar {
  top: 0;
  display: grid;
  grid-template-columns: auto auto minmax(0, 1fr);
  align-items: center;
  gap: var(--space-3);
  min-height: 56px;
  padding: 0.55rem clamp(0.75rem, 2vw, 1.5rem);
  border-bottom: var(--pixel) solid var(--border);
}

.desktop-workspace {
  width: min(1380px, calc(100% - 2rem));
  margin: 0 auto;
  padding: var(--space-4) 0 calc(var(--space-5) + 64px);
}

.hero-desktop {
  min-height: clamp(620px, 82vh, 820px);
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(340px, 0.88fr);
  gap: var(--space-4);
  align-items: center;
}
```

- [ ] **Step 4: Draw the monitor-first lab console in CSS**

Style `.lab-console`, `.console-stage`, `.console-monitor`, `.console-desk`, `.console-notes`, `.avatar-silhouette`, `.desk-paper`, and `.desk-keyboard` so the hero has actual environmental storytelling. Use only CSS boxes and the inline SVG from Task 2. Required traits:

```css
.console-stage {
  position: relative;
  min-height: 430px;
  overflow: hidden;
  background:
    linear-gradient(90deg, rgba(246, 240, 223, 0.04) 1px, transparent 1px),
    linear-gradient(rgba(246, 240, 223, 0.04) 1px, transparent 1px),
    var(--surface-alt);
  background-size: 18px 18px;
  padding: var(--space-4);
}

.console-monitor {
  position: relative;
  width: min(78%, 560px);
  min-height: 270px;
  background: #0c0d0b;
  border: var(--pixel) solid var(--border);
  box-shadow: 6px 6px 0 var(--shadow);
}

.console-plot polyline,
.console-plot line {
  fill: none;
  stroke: var(--terminal);
  stroke-width: 4;
  vector-effect: non-scaling-stroke;
}

.console-plot circle {
  fill: var(--accent-strong);
  stroke: var(--border);
  stroke-width: 2;
}
```

Do not use the real portrait in the hero.

- [ ] **Step 5: Style identity panel, command center, modules, and paper records**

Add layout rules:

```css
.identity-panel {
  align-self: center;
}

.identity-body {
  padding: var(--space-5);
}

.identity-body h1 {
  margin: 0;
  color: var(--accent-strong);
  font-family: var(--font-ui);
  font-size: clamp(2.8rem, 4rem, 4.4rem);
  line-height: 1.05;
  letter-spacing: 0;
}

.command-center {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--space-4);
  align-items: start;
}

.research-module,
.paper-record,
.terminal-panel,
.project-folder article,
.system-log li {
  background: var(--surface-alt);
  border: 2px solid var(--border);
  box-shadow: 4px 4px 0 var(--shadow);
}

.paper-record {
  display: grid;
  grid-template-columns: minmax(150px, 210px) minmax(0, 1fr);
  gap: var(--space-3);
  padding: var(--space-3);
}
```

Ensure Research and Papers look richer internally than System Log even though the outer command windows are equal.

- [ ] **Step 6: Add interaction, focus, and reduced-motion rules**

Add:

```css
:focus-visible {
  outline: 3px solid var(--terminal);
  outline-offset: 3px;
}

@media (hover: hover) and (pointer: fine) {
  .research-module:hover,
  .paper-record:hover {
    transform: translateY(-3px);
    box-shadow: 6px 6px 0 var(--shadow);
    border-color: var(--accent);
  }

  .pixel-button:hover,
  .desktop-nav a:hover,
  .taskbar-nav a:hover {
    transform: translate(1px, 1px);
    box-shadow: 2px 2px 0 var(--shadow);
    background: var(--accent);
    color: var(--border);
    text-decoration: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Step 7: Add responsive rules**

Add breakpoints:

```css
@media (max-width: 1024px) {
  .hero-desktop {
    grid-template-columns: 1fr;
    min-height: auto;
  }

  .command-center {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .desktop-titlebar {
    position: static;
    grid-template-columns: 1fr;
  }

  .desktop-workspace {
    width: min(100% - 1rem, 1380px);
    padding-top: var(--space-2);
  }

  .hero-desktop {
    gap: var(--space-3);
  }

  .identity-panel {
    order: -1;
  }

  .console-stage {
    min-height: 260px;
    padding: var(--space-3);
  }

  .console-monitor {
    width: 100%;
    min-height: 180px;
  }

  .paper-record,
  .about-layout,
  .support-grid,
  .status-grid {
    grid-template-columns: 1fr;
  }

  .desktop-taskbar {
    grid-template-columns: 1fr;
    align-items: stretch;
  }

  .taskbar-nav {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```

Verify the mobile first screen shows identity/actions before long navigation.

- [ ] **Step 8: Run validation and commit CSS**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
git diff --check
git add assets/css/pixel-research-os.css
git commit -m "Rebuild Pixel Research OS v2 visual system"
```

Expected result: validation may still fail only for JS-specific behavior until Task 4. `git diff --check` must pass.

## Task 4: Rebuild The JavaScript Enhancement Layer

**Files:**
- Modify: `assets/js/pixel-research-os.js`
- Test: `python3 scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Replace the JS with progressive enhancement**

Replace `assets/js/pixel-research-os.js` with:

```javascript
(function () {
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const bootLine = document.querySelector("[data-boot-line]");
  const statusLine = document.querySelector("[data-status-line]");
  const localTime = document.querySelector("[data-local-time]");
  const navLinks = Array.from(document.querySelectorAll(".desktop-nav a[href^='#'], .taskbar-nav a[href^='#']"));
  const windows = Array.from(document.querySelectorAll("[data-window]"));

  function setStatus(text) {
    if (statusLine) statusLine.textContent = text;
  }

  function updateClock() {
    if (!localTime) return;
    const value = new Intl.DateTimeFormat([], {
      hour: "2-digit",
      minute: "2-digit"
    }).format(new Date());
    localTime.textContent = value;
    localTime.setAttribute("datetime", new Date().toISOString());
  }

  function runBootLine() {
    if (!bootLine) return;
    if (reducedMotion.matches) {
      bootLine.textContent = "SYSTEM READY.";
      return;
    }
    const states = [
      "BOOTING MINGHAO.EXE...",
      "LOADING RESEARCH MODULES...",
      "MOUNTING PAPER DATABASE...",
      "SYSTEM READY."
    ];
    let index = 0;
    const timer = window.setInterval(() => {
      index += 1;
      bootLine.textContent = states[index] || states[states.length - 1];
      if (index >= states.length - 1) {
        window.clearInterval(timer);
      }
    }, 360);
  }

  function setActiveSection(sectionId) {
    navLinks.forEach((link) => {
      const isActive = link.getAttribute("href") === `#${sectionId}`;
      if (isActive) {
        link.setAttribute("aria-current", "location");
      } else {
        link.removeAttribute("aria-current");
      }
    });
    windows.forEach((panel) => {
      const isActive = panel.id === sectionId;
      panel.classList.toggle("active-window", isActive);
      if (isActive) {
        setStatus(`${panel.dataset.window.toUpperCase()} ACTIVE`);
      }
    });
  }

  function observeSections() {
    if (!("IntersectionObserver" in window)) return;
    const sections = navLinks
      .map((link) => document.querySelector(link.getAttribute("href")))
      .filter(Boolean);
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          setActiveSection(entry.target.id);
        }
      });
    }, { rootMargin: "-35% 0px -50% 0px", threshold: 0.01 });
    sections.forEach((section) => observer.observe(section));
  }

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      const target = link.getAttribute("href").slice(1);
      if (target) setActiveSection(target);
    });
  });

  windows.forEach((panel) => {
    panel.addEventListener("focusin", () => setActiveSection(panel.id));
    panel.addEventListener("mouseenter", () => {
      if (!reducedMotion.matches) setStatus(`${panel.dataset.window.toUpperCase()} READY`);
    });
  });

  runBootLine();
  observeSections();
  updateClock();
  if (localTime) window.setInterval(updateClock, 30000);
})();
```

- [ ] **Step 2: Run validation and commit JS**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
git diff --check
git add assets/js/pixel-research-os.js
git commit -m "Add Pixel Research OS v2 interactions"
```

Expected result: static validation passes or fails only for remaining HTML/CSS details that are addressed in Task 5.

## Task 5: Integrate, Build, And Fix Static Failures

**Files:**
- Modify if needed: `index.html`
- Modify if needed: `assets/css/pixel-research-os.css`
- Modify if needed: `assets/js/pixel-research-os.js`
- Modify if needed: `scripts/validate_pixel_research_os.py`

- [ ] **Step 1: Run all static checks**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
git diff --check
```

Expected result:

```text
PASS: Pixel Research OS static validation
```

`git diff --check` emits no output.

- [ ] **Step 2: Run Jekyll build using the known local Bundler workaround**

Run:

```bash
BUNDLE_FORCE_RUBY_PLATFORM=true bundle install --path /private/tmp/mhaomou-jekyll-bundle >/tmp/mhaomou-bundle-v2.log
bundle exec jekyll build
rm -rf .bundle
```

Expected result: Jekyll reports `done` and `_site/index.html` is generated. The known Ruby/Jekyll logger warnings are acceptable if the build exits `0`.

- [ ] **Step 3: Confirm generated site excludes internal artifacts**

Run:

```bash
find _site -maxdepth 3 -type f | sort
rg -n "docs/superpowers|validate_pixel_research_os|legacy-index" _site index.html
```

Expected result: `rg` finds no internal artifacts. `_site/index.html` exists with the v2 shell classes.

- [ ] **Step 4: Commit integration fixes**

If Step 1 or Step 2 required fixes, commit them:

```bash
git add index.html assets/css/pixel-research-os.css assets/js/pixel-research-os.js scripts/validate_pixel_research_os.py _config.yml
git commit -m "Polish Pixel Research OS v2 integration"
```

Expected result: skip this commit if there are no integration fixes beyond previous task commits.

## Task 6: Visual QA And Screenshot Comparison

**Files:**
- Local artifacts only: `.superpowers/screenshots/after-homepage-1440x900.png`, `.superpowers/screenshots/after-homepage-390x844.png`
- Do not commit `.superpowers/`.

- [ ] **Step 1: Capture after screenshots from the local built site**

Run a local static server from `_site`:

```bash
python3 -m http.server 8765 --directory _site
```

In a separate command, capture screenshots with headless Chrome:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless=new --disable-gpu --no-sandbox --disable-background-networking --disable-component-update --disable-sync --metrics-recording-only --disable-default-apps --no-first-run --user-data-dir=/private/tmp/mhaomou-chrome-after-desktop --window-size=1440,900 --screenshot=/Users/minghao/Documents/MhaoMou.github.io/.superpowers/screenshots/after-homepage-1440x900.png http://127.0.0.1:8765/
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless=new --disable-gpu --no-sandbox --disable-background-networking --disable-component-update --disable-sync --metrics-recording-only --disable-default-apps --no-first-run --user-data-dir=/private/tmp/mhaomou-chrome-after-mobile --window-size=390,844 --screenshot=/Users/minghao/Documents/MhaoMou.github.io/.superpowers/screenshots/after-homepage-390x844.png http://127.0.0.1:8765/
```

Stop the static server after both screenshots are written.

- [ ] **Step 2: Inspect screenshots visually**

Open these four files with the image viewer:

```text
.superpowers/screenshots/before-homepage-1440x900.png
.superpowers/screenshots/before-homepage-390x844.png
.superpowers/screenshots/after-homepage-1440x900.png
.superpowers/screenshots/after-homepage-390x844.png
```

Expected visual result:

- Desktop after screenshot opens with a coherent desktop shell, monitor-first lab console, identity panel, and bottom taskbar.
- Desktop after screenshot no longer reads as topbar plus left nav plus vertical section stack.
- Mobile after screenshot shows identity/actions and simplified hero content early, not a wall of navigation.
- Research Modules and Paper Database are more visually substantial than System Log.
- Paper titles are readable.
- There is no horizontal overflow or incoherent overlap.
- Real portrait appears only in `ABOUT.EXE`, not in the hero.

- [ ] **Step 3: Fix visual QA failures**

If a screenshot fails one of the expected visual results, edit the smallest relevant file:

```bash
git add index.html assets/css/pixel-research-os.css assets/js/pixel-research-os.js
git commit -m "Fix Pixel Research OS v2 visual QA"
```

Repeat Step 1 and Step 2 after each visual fix until both after screenshots satisfy the expected visual result.

## Task 7: Final Local Readiness Check

**Files:**
- No new files unless a final bugfix is needed.

- [ ] **Step 1: Run the final verification commands**

Run:

```bash
python3 scripts/validate_pixel_research_os.py
git diff --check
BUNDLE_FORCE_RUBY_PLATFORM=true bundle install --path /private/tmp/mhaomou-jekyll-bundle >/tmp/mhaomou-bundle-v2-final.log
bundle exec jekyll build
rm -rf .bundle
git status --short --branch
git rev-list --left-right --count HEAD...origin/main
```

Expected result:

- Validator passes.
- `git diff --check` emits no output.
- Jekyll build exits `0`.
- `.bundle` is removed after build.
- Git status shows only intentional ahead commits and no uncommitted implementation changes.
- The branch is ahead of `origin/main` because the spec and redesign commits are local until Minghao explicitly asks to push.

- [ ] **Step 2: Prepare final local report**

Report:

- commits created
- validation commands run
- screenshot paths
- visual comparison result
- whether the branch is ahead of remote
- that nothing was pushed

Do not push to GitHub. Wait for Minghao to explicitly request publication.

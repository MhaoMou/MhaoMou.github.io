# Pixel Research OS Redesign V2 Design

## Purpose

The current deployed homepage is not a sufficient Pixel Research OS. It preserves useful academic content and infrastructure, but the visual composition still reads as a conventional vertically stacked academic website with pixel-themed styling.

This redesign must create the impression that the visitor opened a small 16-bit research operating system built for Minghao Mou: memorable, custom, coherent, academic, playful but restrained, and technically polished.

The finished site must not feel like a generic retro template, a Windows 95 clone, a Pokemon fan site, a game developer portfolio, or a normal webpage with pixel borders.

## Non-Negotiable Constraints

- Preserve all factual academic content, links, publications, news, CV, contact information, teaser images, and working functionality.
- Do not invent facts, expertise scores, fake status, fake progress bars, fake levels, or generic hero copy.
- Do not push to the remote repository unless Minghao explicitly asks.
- Keep the site compatible with GitHub Pages and Jekyll deployment.
- Keep the page usable and meaningful if JavaScript fails.
- Respect accessibility: semantic HTML, keyboard access, focus states, contrast, alt text, reduced motion, readable type, and touch targets.
- Use no heavy WebGL/canvas libraries for the environmental art.

## Before Reference

Before any implementation work, the current deployed homepage was captured as the visual baseline:

- `.superpowers/screenshots/before-homepage-1440x900.png`
- `.superpowers/screenshots/before-homepage-390x844.png`

The desktop reference shows the current section-stack problem: sticky top bar, left navigation, and vertically stacked windows. The mobile reference shows navigation dominating the first screen before the hero appears.

After implementation, the redesigned site must be captured at:

- `1440 x 900`
- `390 x 844`

Those screenshots must be compared visually against the before references. The work is not complete merely because the build passes.

## Selected Direction

Approved direction:

- First viewport composition: **Lab Scene + Identity Panel**
- Hero lab scene: **Monitor-First Research Console**
- Below-hero layout: **Four-Window Command Center**
- Command-center priority: **Equal outer windows**, with Research and Papers carrying richer internal detail and System Log staying compact.
- Hero personalization: a small stylized pixel silhouette may appear in the research console.
- Real portrait placement: only inside `ABOUT.EXE`, as a clean profile image.
- Implementation approach: static GitHub Pages site with an app-like desktop interaction layer in plain HTML, CSS, and small JavaScript.

## Architecture

The homepage remains a single static page with semantic sections and IDs:

- `hero`
- `research`
- `publications`
- `news`
- `about`
- `projects`
- `teaching`
- `cv`
- `contact`

The page behaves like a lightweight desktop OS through visual composition and progressive enhancement:

- A persistent `DesktopShell` frames the experience.
- A top title bar establishes `MINGHAO RESEARCH OS` and Purdue ECE context.
- A main desktop area holds the hero research console and identity panel.
- A bottom taskbar/status strip provides persistent navigation, `SYSTEM READY`, CV, contact, and optional local time.
- In-page anchors remain single-click/tap controls.
- JavaScript enhances active-window state, nav state, quick panel behavior, status text, and local time.

No React/Vue build system is required. The app-like behavior must come from plain HTML/CSS/JS so the GitHub Pages path remains simple and robust.

## First Viewport

The first viewport should occupy roughly `75-90vh` on desktop and immediately communicate:

- Minghao Mou
- Ph.D. candidate at Purdue ECE
- Coupled Energy Infrastructure Systems
- Generative Models
- Optimal Control
- Research
- Publications
- CV
- Contact

Composition:

- The page opens inside a strong desktop shell, not a normal content column.
- The left side is a monitor-first pixel research console: plots, network nodes, energy-grid motifs, papers, terminal details, and a small silhouette.
- The right side is the academic identity panel: name, role, affiliation, existing research areas, and prominent actions.
- `OPEN CV.PDF` must be prominent in the hero.
- The hero must not use a pixelated real photo. The real portrait belongs in `ABOUT.EXE`.

## Visual System

The visual language is a custom Pixel Research Lab / Research OS.

Palette:

- Background: near-black or deep charcoal.
- Main surfaces: warm dark gray or dark olive-charcoal.
- Text: warm ivory.
- Primary accent: muted Purdue gold.
- Secondary accents: restrained terminal green or muted cyan for status labels, plots, and technical details.

Avoid excessive neon, rainbow pixel colors, bright Windows 95 blue, too much pure white, soft gradients, glass effects, blur, glow-heavy cyberpunk styling, and dominant one-hue palettes.

CSS colors must be centralized in variables.

Typography:

- Pixel/terminal typography only for title bars, labels, buttons, nav, status indicators, module IDs, and terminal prompts.
- Readable mono/sans typography for biography, paper titles, author lists, research descriptions, project descriptions, teaching, and news.
- Do not use viewport-scaled font sizes.
- Keep letter spacing at `0`.

Pixel treatment:

- Use 1-3 px hard borders, hard shadows, crisp separations, occasional stepped corners, and light grid/checker texture.
- Avoid rounded 16px cards, soft shadows, blur, overused scanlines, and constant motion.

## Reusable Components

The implementation should use a consistent component vocabulary rather than unrelated card styles:

- `DesktopShell`: top title bar, desktop area, bottom taskbar/status strip.
- `DesktopNav`: compact icon-label navigation for About, Research, Papers, Projects, CV, and Contact.
- `PixelWindow`: shared title bar, hard border, shadow, compact spacing, active/focus state.
- `PixelButton`: hard-edged button with clear hover, focus, and pressed states.
- `ResearchModule`: cartridge-like installed research module.
- `PaperRecord`: database/file record with teaser, metadata, notes, and links.
- `SystemLog`: compact chronological news log.
- `TerminalPanel`: restrained terminal panel for status/contact/teaching details.
- `LabConsole`: monitor-first pixel-art research scene.

## Content Inventory To Preserve

Identity:

- Minghao Mou
- Ph.D. candidate at Purdue ECE
- Elmore Family School of Electrical and Computer Engineering, Purdue University
- Email: `mmou@purdue.edu`

Links:

- GitHub: `https://github.com/MhaoMou`
- Google Scholar: `https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en`
- LinkedIn: `https://www.linkedin.com/in/minghao-mou-14a090289/`
- CV: `assets/files/curriculum_vitae.pdf`
- Purdue: `https://www.purdue.edu`
- Purdue ECE: `https://engineering.purdue.edu/ECE`
- Dr. Junjie Qin: `https://engineering.purdue.edu/people/junjie.qin.1`
- CUHKSZ: `https://www.cuhk.edu.cn/en`
- Dr. Shuang Li: `https://shuangli01.github.io`

Biography:

- Minghao is a Ph.D. candidate in Purdue ECE advised by Dr. Junjie Qin.
- Minghao obtained a Bachelor's degree in Mathematics from Chinese University of Hong Kong, Shenzhen in 2023, advised by Dr. Shuang Li.

Research interests:

- Coupled Energy Infrastructure Systems
- Generative Models
- Optimal Control

News:

- May 2026: passed PhD preliminary exam and became a Ph.D. candidate.
- Apr. 2026: Braess preprint revised on arXiv.
- Dec. 2025: Braess preprint appeared on arXiv.
- Dec. 2023: Nexus Cognizant Pricing paper accepted to ACC 2024.
- May 2023: graduated from CUHKSZ with first-class honors.

Publications:

1. `Braess' Paradoxes in Coupled Power and Transportation Systems`
   - Authors: Minghao Mou, Junjie Qin
   - Venue: arXiv preprint arXiv:2512.12197, 2025
   - Notes: Preprint
   - Teaser: `assets/img/braess_fig6.png`
   - PDF: `https://arxiv.org/pdf/2512.12197`
   - arXiv: `https://arxiv.org/abs/2512.12197`
   - DOI: `https://doi.org/10.48550/arXiv.2512.12197`

2. `Nexus Cognizant Pricing of Workplace Electric Vehicle Charging`
   - Authors: Minghao Mou, Sean Qian, Junjie Qin
   - Venue: American Control Conference, 2024
   - Notes: Oral Presentation
   - Teaser: `assets/img/comp.jpg`
   - PDF: `https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10644866`
   - BibTeX link preserved from the current site.

Assets:

- Real portrait: `assets/img/IMG_5612.jpeg`
- Existing avatar asset may remain in the repository, but should not be used as the hero identity if it reads as a generic template icon.
- Favicons: `assets/img/favicon.png`, `assets/img/favicon-dark.png`

## Research Modules

The current research interests become installed modules. Use only existing research areas.

Module examples:

- `MODULE_01`: Coupled Energy Infrastructure Systems
- `MODULE_02`: Generative Models
- `MODULE_03`: Optimal Control

Each module should feel like a cartridge or installed research package with:

- module ID
- research area title
- concise factual description derived conservatively from the existing wording and publication topics
- optional `INSPECT MODULE` anchor or affordance

No fake scores, levels, percentages, or unverified claims.

Hover behavior:

- translate upward by roughly 2-4 px
- hard-edged shadow increases
- accent border appears
- transition around 120-180 ms

## Paper Database

Publications must be one of the strongest parts of the page. They should look like database records or research files, not generic cards.

Each `PaperRecord` must preserve:

- teaser image
- title
- author names with `Minghao Mou` subtly highlighted
- venue/year
- notes
- PDF/arXiv/DOI/BibTeX links where present

Desktop layout may use two columns: teaser image plus metadata/actions. Mobile stacks teaser above metadata. Paper titles must remain readable and should not use tiny pixel fonts.

## System Log

News becomes `SYSTEM LOG`.

It should be compact and secondary. Show the most recent 3-5 entries first. If all five entries fit cleanly without dominating the page, all five may be visible.

The system log supports the homepage; it does not dominate the layout.

## About, Projects, Teaching, CV, Contact

`ABOUT.EXE`:

- Contained OS window, not a generic full-width section.
- Shows status, affiliation, advisor, email, concise biography, and real portrait.
- Real portrait uses `IMG_5612.jpeg` with professional cropping and alt text.

`PROJECTS/`:

- Project entries may be derived only from existing publications.
- Existing project-like entries are acceptable:
  - Braess coupled power and transportation systems
  - Nexus Cognizant workplace EV charging
- No fake progress bars or fake project statuses.

`TEACHING/`:

- Preserve that no teaching entries are currently listed.

`CV.PDF`:

- Must be prominent in the hero and taskbar/nav.
- Keep direct link to `assets/files/curriculum_vitae.pdf`.

`CONTACT_TERMINAL`:

- Preserve email, GitHub, Scholar, LinkedIn, and CV links.
- Terminal styling should remain readable and restrained.

## Interaction Model

Allowed interactions:

- single-click/tap navigation
- active-window highlight
- button press state
- module hover/focus lift
- paper record hover/focus lift
- blinking cursor or brief status text
- quick taskbar status/local time
- subtle open/close or panel-selection transition

Avoid:

- dragging windows
- double-click requirements
- keyboard-only navigation
- fake loading delays
- autoplay audio
- screen shake
- giant parallax
- constant motion
- bouncing cards

All interactions must respect `prefers-reduced-motion`.

## Responsive Design

Mobile is not a scaled-down desktop.

At roughly `375-390 px`:

- Remove decorative desktop clutter.
- Stack the hero with identity and actions immediately visible.
- Shrink the lab console and simplify decorative art.
- Convert navigation/taskbar into a compact sticky mobile control.
- Make windows full width.
- Stack paper teaser above metadata.
- Preserve readable typography.
- Preserve adequate touch targets.
- Avoid horizontal scrolling.

Verification viewports:

- `375 px` or `390 x 844`
- `768 x 1024`
- `1024 x 768`
- `1440 x 900`

## Validation And QA

Implementation is not complete until:

- static validator passes
- formatter/lint checks available for the repository pass
- Jekyll production build passes
- GitHub Pages compatibility is confirmed locally
- screenshots are captured after redesign at `1440 x 900` and `390 x 844`
- after screenshots are visually compared against the before references

Visual QA questions:

- Does the first viewport actually look like a research OS?
- Does it have a strong visual focal point?
- Is the monitor-first lab console visible?
- Are Research and Publications visually important?
- Does News feel secondary?
- Does it still look like a normal academic template?
- Is the site too dense or too empty?
- Are paper titles readable?
- Are there too many pixel fonts?
- Is there horizontal overflow?
- Does mobile feel intentionally redesigned?

## Acceptance Criteria

- The first viewport looks like a coherent Pixel Research OS desktop/workstation.
- The hero uses a monitor-first research console with plots, network/grid motifs, and a small stylized silhouette.
- The real portrait appears only in `ABOUT.EXE`.
- The post-hero area uses a four-window command center rather than a uniform vertical section stack.
- Research Modules and Paper Database are visually stronger than System Log.
- All factual content and existing links are preserved.
- The site remains accessible, responsive, readable, and GitHub Pages compatible.
- No final remote push occurs without explicit user instruction.

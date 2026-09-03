# Pixel Research OS Redesign Design

Date: 2026-09-03

## Objective

Redesign the existing `mhaomou.github.io` academic personal website into a distinctive static homepage named `MINGHAO.EXE — Pixel Research OS`.

The redesign should feel like a custom 16-bit research operating system while preserving academic usefulness. Publications, CV, research identity, affiliation, contact information, and profile links must remain easy to find without learning a game mechanic.

## Current Repository Audit

The repository is clean except for local `.superpowers/` brainstorming artifacts, which are ignored by this spec change. The active branch is `main`, tracking `origin/main`. A fetch confirmed local and remote are aligned with `0` commits ahead and `0` behind.

The current site is a GitHub Pages/Jekyll repository using the `yaoyao-liu/minimal-light` remote theme. Important files include:

- `_config.yml` for metadata, profile links, avatar, CV, favicon, and SEO fields.
- `index.md` for About, Research Interests, News, and Publications include.
- `_layouts/homepage.html` for the current page shell.
- `_includes/publications.md` and `_data/publications.yml` for publication rendering and data.
- `assets/files/curriculum_vitae.pdf` for the CV.
- `assets/img/IMG_5612.jpeg` for the portrait.
- `assets/img/braess_fig6.png` and `assets/img/comp.jpg` for publication teasers.
- `CNAME` for GitHub Pages domain configuration.

## Content Inventory To Preserve

Profile:

- Name: Minghao Mou.
- Status: Ph.D. candidate / Ph.D. student.
- Affiliation: Elmore Family School of Electrical and Computer Engineering, Purdue University.
- Advisor: Dr. Junjie Qin.
- Education: Bachelor's degree in Mathematics from Chinese University of Hong Kong, Shenzhen, 2023.
- Undergraduate advisor: Dr. Shuang Li.
- Email: `mmou@purdue.edu`.
- Links: Google Scholar, GitHub, LinkedIn, CV.

Research interests:

- Coupled Energy Infrastructure Systems.
- Generative Models.
- Optimal Control.

News:

- May 2026: Passed PhD preliminary exam and became a PhD candidate.
- Apr. 2026: Braess preprint revised on arXiv.
- Dec. 2025: Braess preprint appeared on arXiv.
- Dec. 2023: Nexus Cognizant Pricing paper accepted to ACC 2024.
- May 2023: Graduated from CUHKSZ with first-class honors.

Publications:

- `Braess' Paradoxes in Coupled Power and Transportation Systems`, Minghao Mou and Junjie Qin, arXiv preprint arXiv:2512.12197, 2025. Preserve PDF, arXiv, DOI, teaser, and Preprint note.
- `Nexus Cognizant Pricing of Workplace Electric Vehicle Charging`, Minghao Mou, Sean Qian, and Junjie Qin, American Control Conference, 2024. Preserve PDF, BibTeX, teaser, and Oral Presentation note.

No invented publications, awards, affiliations, roles, teaching appointments, or research results may be added.

## Chosen Approach

Use a static HTML rewrite inside the existing repository.

The deployed homepage will center on a self-contained `index.html` with local CSS and lightweight JavaScript. During implementation, the current `index.md` homepage source should be retired only after its content has been migrated, so GitHub Pages has a single clear homepage output. Other existing Jekyll files can remain for history and reference unless they interfere with deployment. The redesign must keep the repository compatible with GitHub Pages and preserve existing assets, `CNAME`, CV PDF, favicon files, and SEO-relevant metadata.

## Information Architecture

The first viewport should immediately identify the person and academic role while establishing the Pixel Research OS identity.

Primary shell elements:

- Top system bar: `MINGHAO.EXE`, `Research OS`, `Purdue ECE`, and quick links to GitHub, Scholar, CV, and email/contact.
- Obvious navigation: About, Research, News, Publications, Projects, Teaching, CV, Contact.
- Hero window: pixel-avatar treatment, Minghao Mou, Ph.D. candidate at Purdue ECE, current research themes, and direct buttons to Research, Publications, CV, and Contact.

Main sections:

- `ABOUT.EXE`: Current biography, advisor, Purdue ECE affiliation, CUHKSZ education, real portrait in a pixel-framed profile window, and profile links.
- `RESEARCH_MODULES/`: Three factual research modules from the existing site: Coupled Energy Infrastructure Systems, Generative Models, and Optimal Control.
- `NEWS.LOG`: Existing news items in chronological display matching the current content.
- `PUBLICATION_DATABASE`: Publication list preserving ordering, authors, venue text, links, images, and notes.
- `PROJECTS/`: Project-style entries derived from the existing publications, plus clearly labeled future placeholder slots if needed.
- `TEACHING/`: Terminal-style section with an explicit placeholder because no teaching content is currently present.
- `CV.PDF`: Persistent and prominent CV access.
- `CONTACT_TERMINAL`: Email, Purdue affiliation, GitHub, Google Scholar, LinkedIn, and CV using only public existing information.

## Visual System

The visual tone should be roughly balanced as:

- 60% retro pixel desktop / operating-system interface.
- 25% developer terminal aesthetic.
- 15% classic Pokemon / GameBoy-style menu language.

The implementation should avoid generic portfolio styling and avoid making the page feel like a full game.

Design tokens should centralize:

- Palette: near-black desktop background, warm off-white text, muted Purdue-like gold accent, subdued gray surfaces, and one restrained terminal accent.
- Type: pixel font for OS chrome, titles, labels, badges, and buttons; readable mono or sans font for paragraphs and publication details.
- Spacing, border widths, shadow offsets, animation timing, and responsive breakpoints.

Core UI patterns:

- Crisp pixel borders.
- Hard-edged offset shadows.
- Retro OS windows with title bars.
- Pixel buttons with depress states.
- Terminal panels and prompts.
- RPG-style selection arrows for section accents.
- Subtle dither or grid backgrounds.
- Small pixel-style icons.
- Restrained motion only.

Avoid:

- Excessive gradients.
- Glassmorphism.
- Generic modern SaaS cards.
- Large rounded corners.
- Heavy blur.
- Neon cyberpunk dominance.
- Saturated rainbow palettes.
- Large animations.
- 3D effects.
- Illegibly small pixel fonts.

## Interaction Design

Interactions should enhance feedback without blocking navigation.

Allowed interactions:

- Very brief boot/status text such as `BOOTING MINGHAO.EXE`, `LOADING RESEARCH MODULES`, `READY`.
- Pixel button depress animation.
- Window focus hover state.
- Blinking terminal cursor.
- Publication link hover states.
- Optional desktop-only pixel cursor, disabled on touch devices and never interfering with text selection.

Navigation must never require keyboard controls, puzzles, character movement, or waiting for fake loading delays. No audio should autoplay.

All motion must respect `prefers-reduced-motion: reduce`.

## Responsive Design

Desktop:

- Use a desktop OS composition with a persistent top bar, visible navigation, and stacked research windows.
- Publications should remain wide and readable.
- Decorative background details should not compete with academic content.

Mobile:

- Convert the desktop shell into full-width panels.
- Use compact navigation buttons rather than desktop-icon-only navigation.
- Reduce border and shadow thickness where appropriate.
- Stack publication teaser images above text.
- Maintain large touch targets.
- Disable custom cursor.
- Prevent horizontal overflow at approximately 375 px, 768 px, 1024 px, and 1440 px+ widths.

## Accessibility Requirements

The redesign must preserve usability despite the retro style:

- Use semantic HTML landmarks and section headings.
- Keep the name and research identity as real text, not only imagery.
- Provide visible focus states.
- Use descriptive link text and alt text.
- Keep contrast adequate.
- Do not communicate information only through color.
- Respect reduced-motion preferences.
- Avoid ARIA unless native HTML is insufficient.
- Keep paragraph and publication text comfortably readable.

## SEO And Metadata

Preserve or improve:

- Page title.
- Meta description.
- Keywords.
- Canonical URL.
- Favicons.
- Open Graph metadata where practical.
- Semantic heading hierarchy.

The redesign should keep Minghao Mou, Purdue ECE, and research topics discoverable as HTML text.

## Implementation Notes

Primary files expected during implementation:

- `index.html`: main static homepage.
- `assets/css/pixel-research-os.css`: design tokens, layout, responsive behavior, and component styling.
- `assets/js/pixel-research-os.js`: small progressive enhancement script.

Existing assets should be reused:

- `assets/img/IMG_5612.jpeg` as the real portrait in About/contact.
- `assets/img/avatar.png` or a CSS/pixel placeholder for the hero pixel-avatar treatment.
- Publication teaser images already referenced by `_data/publications.yml`.
- `assets/files/curriculum_vitae.pdf` for CV access.
- Existing favicon files unless a later explicit asset task replaces them.

No heavy dependencies should be introduced for minor effects.

## Validation Plan

After implementation:

- Run the relevant static/Jekyll build command available in the repository.
- Fix build errors introduced by the redesign.
- Run formatting or lint checks if available.
- Verify that GitHub Pages compatibility is preserved.
- Inspect the site locally at desktop and mobile widths if tooling is available.
- Check for horizontal overflow, unreadable text, missing assets, broken internal anchors, obvious broken external links, console errors, and layout shifts.

## Out Of Scope

- Rewriting the site into React, Next.js, Astro, or another framework.
- Publishing or pushing to remote.
- Force-pushing, rewriting history, deleting branches, or destructive Git operations.
- Inventing academic content.
- Building a draggable window manager.
- Creating a full RPG/game.
- Autoplaying audio.
- Replacing academic substance with placeholder-only visuals.

## Open Implementation Decision

The user selected visible sections for Projects, Teaching, and Contact. Projects may derive entries from existing publications, Teaching should use an explicit future-update placeholder because no teaching content is currently present, and Contact should use the existing public links and email rather than a placeholder. Any placeholder must be clearly marked and must not read as a factual claim.

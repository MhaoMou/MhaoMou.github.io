# PRISM Template Migration Design

Date: 2026-09-08

## Goal

Replace the current hand-designed Jekyll/static homepage with the `xyjoey/PRISM` academic website template and customize it for Minghao Mou's academic profile.

The redesign should look like PRISM, not like another custom pixel-art iteration. The site should remain a GitHub Pages personal website at `https://mhaomou.github.io/`.

## Template Source

Use `https://github.com/xyjoey/PRISM` as the upstream template base.

Relevant upstream facts checked before this spec:

- PRISM is a Next.js, Tailwind CSS, and TypeScript academic homepage builder.
- PRISM stores editable content in `content/` using TOML, Markdown, and BibTeX.
- PRISM supports static export through `next.config.ts` with `output: 'export'`.
- PRISM's documented build output is the `out/` directory.
- PRISM's GitHub Pages deployment path uses GitHub Actions with Node 22 and deploys the `out/` artifact.

## Scope

In scope:

- Replace the current homepage implementation with PRISM source files.
- Preserve site identity, URL, SEO metadata, profile content, CV link, social links, and publication links.
- Convert current academic content into PRISM's content model.
- Add the attached pixel image as the site icon/favicon.
- Add a GitHub Pages workflow that builds PRISM and deploys the exported `out/` directory.
- Keep existing source history and assets needed by the new site.
- Capture before/after screenshots for desktop and mobile visual QA before publishing.

Out of scope:

- Designing a new visual language from scratch.
- Keeping the current Pixel Research OS theme.
- Adding fake metrics, gamified expertise levels, or inflated claims.
- Adding blog content that the current site does not already have.
- Migrating to Cloudflare Pages or Vercel.

## Content Mapping

Global config:

- Name: Minghao Mou
- Title: Ph.D. candidate
- Institution: Purdue University / Elmore Family School of Electrical and Computer Engineering
- Email: `mmou@purdue.edu`
- Site URL: `https://mhaomou.github.io/`
- Social links: Google Scholar, GitHub, LinkedIn
- CV: existing `assets/files/curriculum_vitae.pdf`, copied or referenced from PRISM `public/`

Homepage:

- About paragraph from the current site, including Purdue ECE, Dr. Junjie Qin, CUHKSZ, and Dr. Shuang Li.
- Research interests:
  - Coupled Energy Infrastructure Systems
  - Generative Models
  - Optimal Control
- News entries:
  - May 2026: PhD preliminary exam passed; now a Ph.D. candidate.
  - Apr. 2026: Braess preprint revised on arXiv.
  - Dec. 2025: Braess preprint posted on arXiv.
  - Dec. 2023: ACC 2024 acceptance.
  - May 2023: CUHKSZ graduation with first-class honors.

Publications:

- Convert the current publication records to `content/publications.bib`.
- Preserve titles, authors, venues, PDF/arXiv/DOI/BibTeX links, selected-publication flags, preview images, and short descriptions where supported by PRISM.
- Keep publication order sensible, newest first.

Optional pages:

- Research/projects content should be concise and based only on current research areas and paper-derived projects.
- Teaching should be omitted or shown as a minimal page only if PRISM navigation requires it. Empty filler pages are not acceptable.
- Awards/services should be omitted unless real content exists in the current site.

## Assets

Required assets:

- Real profile photo: `assets/img/IMG_5612.jpeg`
- CV PDF: `assets/files/curriculum_vitae.pdf`
- Publication figures: `assets/img/braess_fig6.png`, `assets/img/comp.jpg`
- New favicon/icon: the attached pixel image from the user message

Asset handling:

- Copy active assets into PRISM's `public/` structure, using stable names such as `/bio.jpg`, `/cv.pdf`, `/images/braess_fig6.png`, and `/images/comp.jpg`.
- Generate favicon outputs from the attached image, at minimum `public/favicon.png` and any PRISM-configured icon path.
- Avoid retaining unused Pixel Research OS CSS/JS in the deployed output.

## Architecture

The target source layout should follow PRISM's structure:

- `content/` for site content
- `public/` for static files
- `src/` for PRISM application code
- `package.json`, `package-lock.json`, `next.config.ts`, `tsconfig.json`, Tailwind/PostCSS config
- `.github/workflows/deploy.yml` for GitHub Pages deployment
- `.nojekyll` if required for deployed output behavior

The old Jekyll files should be removed or made inert so GitHub Pages does not try to build them as the primary site.

## Deployment

Use GitHub Actions as the production deployment path.

Workflow requirements:

- Trigger on pushes to `main`.
- Use Node 22.
- Install dependencies from lockfile if available.
- Run PRISM build.
- Upload `out/` with `actions/upload-pages-artifact`.
- Deploy with `actions/deploy-pages`.

Repository Pages settings may need to use "GitHub Actions" as the source. If the repository is still configured to deploy from branch root, the pushed migration may not become live until that setting is changed.

## Validation

Automated validation should confirm:

- Required profile, affiliation, advisor, email, links, research areas, news entries, and publication titles are present in PRISM content.
- Required assets exist in `public/`.
- The favicon path points to the new pixel icon.
- Build output exists in `out/`.
- No old Pixel Research OS homepage shell is present in the generated output.
- No implementation-only docs/scripts are published.

Manual/visual validation should confirm:

- Desktop screenshot at 1440x900.
- Mobile screenshot at 390x844.
- Homepage visibly matches PRISM's template direction.
- Navigation works.
- Publications render correctly.
- CV and external publication links work.
- Favicon displays from the attached pixel image.

## Risks

- PRISM requires Node 22 or later. The local shell currently does not provide a default `node`; a local Node 20 binary exists but does not satisfy PRISM's documented engine requirement.
- Installing PRISM dependencies requires network access to npm.
- GitHub Pages must be configured for GitHub Actions deployment; branch-root Pages deployment is not sufficient for a Next static export unless only `out/` is pushed.
- This is a larger migration than editing the current static files, so rollback should be a normal git revert to the last Jekyll/static commit if needed.

## Acceptance Criteria

- The site source is PRISM-based.
- The homepage no longer looks like Pixel Research OS.
- The attached pixel image is used as the webpage icon.
- Current academic content is preserved accurately.
- `npm run build` produces a static `out/` site.
- Desktop and mobile screenshots show a polished PRISM-style academic homepage.
- The live URL serves the PRISM-based site after publishing.

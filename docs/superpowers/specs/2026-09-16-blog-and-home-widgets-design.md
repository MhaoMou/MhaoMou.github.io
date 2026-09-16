# Blog and Home Widgets Design

## Goal

Add a first-class blog section to the PRISM-based academic website, update the profile wording and research interests, and add two homepage widgets: Latest Updates and Google Scholar / citations.

## Scope

This change updates the website content model and frontend components. It will:

- Replace the displayed affiliation text `Elmore Family School of Electrical and Computer Engineering, Purdue University` with `Purdue ECE` in the profile and bio-facing content.
- Add `Learn to Optimize` to the homepage research-interest chips.
- Add a `Blog` navigation item and a dedicated `/blog` page.
- Implement the heavier blog option: structured blog metadata and individual blog detail pages, not only a single Markdown index.
- Add a Latest Updates widget on the homepage using the existing news feed.
- Add a Google Scholar / citations link card on the homepage, linking to the existing Google Scholar profile.
- Extend the validation script so the new structure is guarded.

## Architecture

The existing site is a Next.js static export that reads TOML, Markdown, and BibTeX from `content/`. The blog will follow this pattern by storing blog index metadata in `content/blog.toml` and post bodies in `content/blog/*.md`. A new blog page component will render the post list, and a dynamic post route will render individual posts at `/blog/<slug>`.

Homepage widgets will remain content-driven. The Latest Updates widget will reuse `content/news.toml`; the Google Scholar widget will read `google_scholar` from `content/config.toml`. This avoids a live citation scrape during static builds and keeps deployment deterministic.

## Content Design

`content/config.toml`:

- `author.institution` becomes `Purdue ECE`.
- `social.location_details` becomes a compact Purdue ECE / Purdue location block.
- A new navigation item appears after `Research`:
  - `title = "Blog"`
  - `type = "page"`
  - `target = "blog"`
  - `href = "/blog"`

`content/bio.md`:

- The opening sentence uses `[Purdue ECE](https://engineering.purdue.edu/ECE)` while preserving the Purdue context.

`content/about.toml`:

- `Learn to Optimize` is appended to `profile.research_interests`.
- Homepage sections gain widget configuration for Latest Updates and Google Scholar.

`content/blog.toml`:

- Defines `type = "blog"`, title, description, and post metadata.
- Initial posts include at least one starter post so `/blog` is not empty.

`content/blog/*.md`:

- Stores editable Markdown bodies for blog posts.

## UI Design

The blog index should feel consistent with the current PRISM publication/research pages: compact, text-forward, and academic. Each post card should show title, date, summary, and tags. The post page should render Markdown in the same typographic style as the current `TextPage`, with a back link to Blog.

The Latest Updates widget should be a concise homepage panel showing the newest three news items. The Google Scholar widget should be a compact link card with the Google Scholar label, the profile URL, and a short line such as “Publication profile and citation record.” No live citation counts are required, because Google Scholar does not provide a stable public API and scraping it would make the static build fragile.

## Testing And Verification

Add or update validation in `scripts/validate_prism_site.py` to require:

- `Purdue ECE`
- `Learn to Optimize`
- the Blog navigation item and blog content files
- the Latest Updates widget marker
- the Google Scholar widget marker

Run:

- `python3 scripts/validate_prism_site.py`
- `git diff --check`
- `env -u ELECTRON_RUN_AS_NODE PATH="/private/tmp/node-v22.13.1-darwin-arm64/bin:$PATH" npm run build`

If publishing, commit, push to `main`, wait for the GitHub Pages workflow, and verify the live `/blog/` page plus homepage content.

## Non-Goals

- No live Google Scholar scraping.
- No comments, RSS, search, or tagging filters in the first blog version.
- No redesign of the PRISM theme beyond the requested widgets and blog section.

# Scholar Trend Widget Design

## Goal

Reduce homepage duplication by hiding the long News section while keeping a compact Latest Updates widget, and make the Google Scholar card show citation metrics and a citation trend instead of only linking to the Scholar profile.

## Homepage Content

The homepage keeps the `latest_updates` section sourced from `content/news.toml` and removes the separate full `news` list section from `content/about.toml`. This preserves recent activity while avoiding two news surfaces with the same source data.

## Scholar Card

The Scholar card remains a homepage widget but becomes a metrics card. It shows total citations, h-index, i10-index, a compact yearly citation trend bar chart, a last-checked note, and a link to the public Google Scholar profile. The data is maintained in `content/about.toml` rather than fetched client-side, because Google Scholar does not provide a stable public API and live scraping would be fragile on a static GitHub Pages site.

Current public profile values checked on September 16, 2026:

- Citations: `3`
- h-index: `1`
- i10-index: `0`

## Data Model

The `scholar_card` section accepts:

- `total_citations`
- `h_index`
- `i10_index`
- `last_checked`
- `trend`, an array of `{ year, citations }` entries

The initial trend records the currently visible citation year signal as `2025 = 3`.

## Verification

The site validator should fail if the full News section is active, if the Scholar card lacks metrics/trend data, or if generated homepage output still shows a full `News` heading. The production build must continue to statically export the homepage and blog routes.

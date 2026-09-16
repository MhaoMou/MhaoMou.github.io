# Scholar Trend Widget Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hide the long homepage News section and replace the Google Scholar link card with a metrics-and-trend widget.

**Architecture:** Keep all Scholar metrics in static TOML content and pass them through the existing `SectionConfig` flow from `src/app/page.tsx` to `HomePageClient`. Render the chart directly in `ScholarWidget` with CSS bars, avoiding additional chart dependencies.

**Tech Stack:** Next.js static export, React, TypeScript, Tailwind CSS, TOML content.

---

### Task 1: Validator Expectations

**Files:**
- Modify: `scripts/validate_prism_site.py`

- [ ] Require `content/about.toml` to contain Scholar metric fields and trend data.
- [ ] Require `content/about.toml` not to contain the old `id = "news"` full list section.
- [ ] Require generated homepage output to contain citation metrics and not contain a standalone News heading.
- [ ] Run `python3 scripts/validate_prism_site.py` and confirm it fails before production changes.

### Task 2: Static Content Model

**Files:**
- Modify: `content/about.toml`
- Modify: `src/app/page.tsx`
- Modify: `src/components/home/HomePageClient.tsx`

- [ ] Remove the full News section from `content/about.toml`.
- [ ] Add Scholar metric fields and trend entries to the existing `scholar_card` section.
- [ ] Extend `SectionConfig` on server and client to carry the metrics and trend fields.
- [ ] Keep `scholarUrl` resolved from `content/config.toml`.

### Task 3: Scholar Widget UI

**Files:**
- Modify: `src/components/home/ScholarWidget.tsx`

- [ ] Render total citations, h-index, and i10-index as compact metric blocks.
- [ ] Render the trend as fixed-height bars with year labels and accessible text.
- [ ] Keep the Google Scholar profile link.
- [ ] Handle empty trend data gracefully.

### Task 4: Verification and Publish

**Files:**
- No additional source files expected.

- [ ] Run `python3 scripts/validate_prism_site.py`.
- [ ] Run `npm run build` with Node 22.
- [ ] Check generated homepage HTML for `3 citations`, `h-index`, `Citation trend`, and no full `News` heading.
- [ ] Commit, push to `main`, wait for the Pages workflow, and verify live HTML.

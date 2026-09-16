# Blog and Home Widgets Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a structured blog system, update Purdue ECE/profile wording, add `Learn to Optimize`, and add Latest Updates plus Google Scholar homepage widgets.

**Architecture:** Keep the site static and content-driven. Add a new `blog` page type, blog metadata in TOML, post bodies in Markdown, a `/blog` index through the existing dynamic-page route, and a nested `/blog/[post]` static route for post detail pages. Add homepage widgets as new about-section types that reuse existing content/config data.

**Tech Stack:** Next.js 15 static export, React 19, TypeScript, TOML content via `smol-toml`, Markdown via `react-markdown`, existing Python validator.

---

## File Structure

- Modify `scripts/validate_prism_site.py`: add failing expectations for Purdue ECE, Learn to Optimize, blog content/routes, and widgets.
- Modify `content/config.toml`: shorten institution/location text and add Blog navigation.
- Modify `content/bio.md`: use Purdue ECE in the opening sentence.
- Modify `content/about.toml`: add research interest and widget sections.
- Create `content/blog.toml`: blog index metadata and post metadata.
- Create `content/blog/learning-to-optimize.md`: starter editable blog post.
- Modify `src/types/page.ts`: add `BlogPostMeta` and `BlogPageConfig`.
- Modify `src/lib/content.ts`: add helper to read blog Markdown from `content/blog/`.
- Modify `src/components/pages/DynamicPageClient.tsx`: render blog pages.
- Create `src/components/pages/BlogPage.tsx`: blog index component.
- Create `src/components/pages/BlogPostPage.tsx`: blog post component.
- Modify `src/app/[slug]/page.tsx`: load `blog` dynamic page data.
- Create `src/app/blog/[post]/page.tsx`: static post route.
- Modify `src/app/page.tsx`: process new homepage widget section types.
- Modify `src/components/home/HomePageClient.tsx`: render widget sections.
- Create `src/components/home/LatestUpdatesWidget.tsx`: compact latest news widget.
- Create `src/components/home/ScholarWidget.tsx`: Google Scholar link card.

### Task 1: Add Failing Validator Coverage

**Files:**
- Modify: `scripts/validate_prism_site.py`

- [ ] **Step 1: Write the failing validation expectations**

Add these requirements before implementing site changes:

```python
REQUIRED_FILES = [
    # existing entries...
    "content/blog.toml",
    "content/blog/learning-to-optimize.md",
]
```

Add required text:

```python
REQUIRED_TEXT = {
    "content/config.toml": [
        # existing entries...
        'institution = "Purdue ECE"',
        'title = "Blog"',
        'target = "blog"',
        'href = "/blog"',
    ],
    "content/bio.md": [
        "Purdue ECE",
        "Dr. Junjie Qin",
    ],
    "content/about.toml": [
        # existing entries...
        "Learn to Optimize",
        'type = "latest_updates"',
        'type = "scholar_card"',
    ],
    "content/blog.toml": [
        'type = "blog"',
        'title = "Blog"',
        "learning-to-optimize",
        "Learning to Optimize",
    ],
    "content/blog/learning-to-optimize.md": [
        "Learning to Optimize",
        "optimization",
    ],
}
```

Add generated-output checks:

```python
for snippet in [
    "Purdue ECE",
    "Learn to Optimize",
    "Latest Updates",
    "Google Scholar",
    "Blog",
]:
    if snippet not in output:
        failures.append(f"generated homepage missing required text: {snippet}")
```

- [ ] **Step 2: Run validator to verify RED**

Run:

```bash
python3 scripts/validate_prism_site.py
```

Expected: FAIL for missing `content/blog.toml`, `content/blog/learning-to-optimize.md`, Purdue ECE text, Learn to Optimize, Blog navigation, and widget markers.

- [ ] **Step 3: Commit validator RED checkpoint**

Run:

```bash
git add scripts/validate_prism_site.py
git commit -m "Add blog and widget validation expectations"
```

Expected: commit succeeds.

### Task 2: Add Content Configuration

**Files:**
- Modify: `content/config.toml`
- Modify: `content/bio.md`
- Modify: `content/about.toml`
- Create: `content/blog.toml`
- Create: `content/blog/learning-to-optimize.md`

- [ ] **Step 1: Update profile config**

In `content/config.toml`, set:

```toml
[author]
name = "Minghao Mou"
title = "Ph.D. candidate"
institution = "Purdue ECE"
avatar = "/bio.jpg"
```

Set compact location details:

```toml
location_details = [
  "Purdue ECE,",
  "Purdue University"
]
```

Add Blog navigation after Research:

```toml
[[navigation]]
title = "Blog"
type = "page"
target = "blog"
href = "/blog"
```

- [ ] **Step 2: Update bio wording**

Replace the opening sentence in `content/bio.md` with:

```markdown
I am a Ph.D. candidate in [Purdue ECE](https://engineering.purdue.edu/ECE) at [Purdue University](https://www.purdue.edu), advised by [Dr. Junjie Qin](https://engineering.purdue.edu/people/junjie.qin.1).
```

- [ ] **Step 3: Update homepage interests and widget sections**

In `content/about.toml`, set:

```toml
[profile]
research_interests = [
  "Coupled Energy Infrastructure Systems",
  "Generative Models",
  "Optimal Control",
  "Learn to Optimize"
]
```

Add widget sections after the existing news section:

```toml
[[sections]]
id = "latest_updates_widget"
type = "latest_updates"
title = "Latest Updates"
source = "news.toml"
limit = 3

[[sections]]
id = "scholar_widget"
type = "scholar_card"
title = "Google Scholar"
description = "Publication profile and citation record."
```

- [ ] **Step 4: Add blog metadata**

Create `content/blog.toml`:

```toml
type = "blog"
title = "Blog"
description = "Notes on research, optimization, energy systems, and academic life."

[[posts]]
slug = "learning-to-optimize"
title = "Learning to Optimize"
date = "2026-09-16"
summary = "A working note on optimization as a way to think about models, infrastructure, and decision-making."
tags = ["Optimization", "Research", "Learning"]
source = "blog/learning-to-optimize.md"
```

- [ ] **Step 5: Add starter blog post body**

Create `content/blog/learning-to-optimize.md`:

```markdown
# Learning to Optimize

Optimization is more than a mathematical tool in my research. It is a way to ask what choices are available, what constraints matter, and how local decisions reshape system-level outcomes.

I plan to use this blog for short research notes, reading reflections, and occasional thoughts about power systems, transportation systems, generative models, and learning-based optimization.
```

- [ ] **Step 6: Run validator**

Run:

```bash
python3 scripts/validate_prism_site.py
```

Expected: still FAIL, but failures should now be limited to generated-output checks or missing frontend support for blog/widget rendering.

- [ ] **Step 7: Commit content changes**

Run:

```bash
git add content/config.toml content/bio.md content/about.toml content/blog.toml content/blog/learning-to-optimize.md
git commit -m "Add blog content and homepage widget config"
```

Expected: commit succeeds.

### Task 3: Add Blog Types And Content Loader

**Files:**
- Modify: `src/types/page.ts`
- Modify: `src/lib/content.ts`

- [ ] **Step 1: Add blog page types**

Update `src/types/page.ts`:

```ts
export interface BasePageConfig {
    type: 'about' | 'publication' | 'card' | 'text' | 'blog';
    title: string;
    description?: string;
}

export interface BlogPostMeta {
    slug: string;
    title: string;
    date: string;
    summary: string;
    tags?: string[];
    source: string;
}

export interface BlogPageConfig extends BasePageConfig {
    type: 'blog';
    posts: BlogPostMeta[];
}
```

- [ ] **Step 2: Add blog Markdown reader**

Update `src/lib/content.ts`:

```ts
export function getBlogMarkdownContent(filename: string, locale?: string): string {
  return readFirstAvailableFile(filename, locale);
}
```

Use this helper for blog post sources such as `blog/learning-to-optimize.md`.

- [ ] **Step 3: Run type/build check for expected missing component errors**

Run:

```bash
env -u ELECTRON_RUN_AS_NODE PATH="/private/tmp/node-v22.13.1-darwin-arm64/bin:$PATH" npm run build
```

Expected: FAIL because blog components/routes are not implemented yet, or because `blog` data is not handled by unions.

- [ ] **Step 4: Commit types and loader**

Run:

```bash
git add src/types/page.ts src/lib/content.ts
git commit -m "Add blog page types"
```

Expected: commit succeeds.

### Task 4: Implement Blog Index And Post Pages

**Files:**
- Create: `src/components/pages/BlogPage.tsx`
- Create: `src/components/pages/BlogPostPage.tsx`
- Modify: `src/components/pages/DynamicPageClient.tsx`
- Modify: `src/app/[slug]/page.tsx`
- Create: `src/app/blog/[post]/page.tsx`

- [ ] **Step 1: Create blog index component**

Create `src/components/pages/BlogPage.tsx`:

```tsx
'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import { BlogPageConfig } from '@/types/page';

interface BlogPageProps {
  config: BlogPageConfig;
}

export default function BlogPage({ config }: BlogPageProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.4 }}
      className="max-w-3xl mx-auto"
    >
      <h1 className="text-4xl font-serif font-bold text-primary mb-4">{config.title}</h1>
      {config.description && (
        <p className="text-lg text-neutral-600 dark:text-neutral-500 mb-8 max-w-2xl">
          {config.description}
        </p>
      )}
      <div className="space-y-4">
        {config.posts.map((post) => (
          <Link
            key={post.slug}
            href={`/blog/${post.slug}`}
            className="block rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5 transition-all duration-200 hover:border-accent hover:shadow-md"
          >
            <div className="text-xs text-neutral-500 mb-2">{post.date}</div>
            <h2 className="text-xl font-semibold text-primary mb-2">{post.title}</h2>
            <p className="text-sm text-neutral-600 dark:text-neutral-500 mb-3">{post.summary}</p>
            {post.tags && post.tags.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {post.tags.map((tag) => (
                  <span key={tag} className="text-xs rounded-md bg-neutral-100 dark:bg-neutral-800 px-2 py-1 text-neutral-600 dark:text-neutral-400">
                    {tag}
                  </span>
                ))}
              </div>
            )}
          </Link>
        ))}
      </div>
    </motion.div>
  );
}
```

- [ ] **Step 2: Create blog post component**

Create `src/components/pages/BlogPostPage.tsx`:

```tsx
'use client';

import Link from 'next/link';
import { motion } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import { BlogPostMeta } from '@/types/page';

interface BlogPostPageProps {
  post: BlogPostMeta;
  content: string;
}

export default function BlogPostPage({ post, content }: BlogPostPageProps) {
  return (
    <motion.article
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.2 }}
      className="max-w-3xl mx-auto"
    >
      <Link href="/blog" className="text-sm font-medium text-accent hover:bg-accent/10 rounded">
        Back to Blog
      </Link>
      <header className="mt-6 mb-8">
        <div className="text-sm text-neutral-500 mb-2">{post.date}</div>
        <h1 className="text-4xl font-serif font-bold text-primary mb-4">{post.title}</h1>
        <p className="text-lg text-neutral-600 dark:text-neutral-500">{post.summary}</p>
      </header>
      <div className="text-neutral-700 dark:text-neutral-600 leading-relaxed">
        <ReactMarkdown
          components={{
            h1: ({ children }) => <h1 className="text-3xl font-serif font-bold text-primary mt-8 mb-4">{children}</h1>,
            h2: ({ children }) => <h2 className="text-2xl font-serif font-bold text-primary mt-8 mb-4 border-b border-neutral-200 dark:border-neutral-800 pb-2">{children}</h2>,
            h3: ({ children }) => <h3 className="text-xl font-semibold text-primary mt-6 mb-3">{children}</h3>,
            p: ({ children }) => <p className="mb-4 last:mb-0">{children}</p>,
            ul: ({ children }) => <ul className="list-disc list-inside mb-4 space-y-1 ml-4">{children}</ul>,
            ol: ({ children }) => <ol className="list-decimal list-inside mb-4 space-y-1 ml-4">{children}</ol>,
            li: ({ children }) => <li className="mb-1">{children}</li>,
            a: ({ ...props }) => (
              <a {...props} target="_blank" rel="noopener noreferrer" className="text-accent font-medium transition-all duration-200 rounded hover:bg-accent/10 hover:shadow-sm" />
            ),
            blockquote: ({ children }) => (
              <blockquote className="border-l-4 border-accent/50 pl-4 italic my-4 text-neutral-600 dark:text-neutral-500">
                {children}
              </blockquote>
            ),
            strong: ({ children }) => <strong className="font-semibold text-primary">{children}</strong>,
            em: ({ children }) => <em className="italic text-neutral-600 dark:text-neutral-500">{children}</em>,
          }}
        >
          {content}
        </ReactMarkdown>
      </div>
    </motion.article>
  );
}
```

- [ ] **Step 3: Wire blog index into dynamic page client**

Update `src/components/pages/DynamicPageClient.tsx` imports and union:

```tsx
import BlogPage from '@/components/pages/BlogPage';
import { BlogPageConfig } from '@/types/page';

export type DynamicPageLocaleData =
  | { type: 'publication'; config: PublicationPageConfig; publications: Publication[] }
  | { type: 'text'; config: TextPageConfig; content: string }
  | { type: 'card'; config: CardPageConfig }
  | { type: 'blog'; config: BlogPageConfig };
```

Add render branch:

```tsx
{pageData.type === 'blog' && (
  <BlogPage config={pageData.config} />
)}
```

- [ ] **Step 4: Load blog page data**

Update `src/app/[slug]/page.tsx` imports:

```ts
import { BlogPageConfig } from '@/types/page';
```

Add branch in `loadDynamicPageData`:

```ts
if (pageConfig.type === 'blog') {
  return {
    type: 'blog',
    config: pageConfig as BlogPageConfig,
  };
}
```

- [ ] **Step 5: Add blog post static route**

Create `src/app/blog/[post]/page.tsx`:

```tsx
import { notFound } from 'next/navigation';
import { Metadata } from 'next';
import { getPageConfig, getBlogMarkdownContent } from '@/lib/content';
import BlogPostPage from '@/components/pages/BlogPostPage';
import { BlogPageConfig } from '@/types/page';

function getBlogConfig(): BlogPageConfig | null {
  return getPageConfig<BlogPageConfig>('blog');
}

export function generateStaticParams() {
  const config = getBlogConfig();
  return (config?.posts || []).map((post) => ({ post: post.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ post: string }> }): Promise<Metadata> {
  const { post: slug } = await params;
  const config = getBlogConfig();
  const post = config?.posts.find((item) => item.slug === slug);
  if (!post) {
    return {};
  }
  return {
    title: `${post.title} | Blog`,
    description: post.summary,
  };
}

export default async function BlogPostRoute({ params }: { params: Promise<{ post: string }> }) {
  const { post: slug } = await params;
  const config = getBlogConfig();
  const post = config?.posts.find((item) => item.slug === slug);

  if (!post) {
    notFound();
  }

  const content = getBlogMarkdownContent(post.source);
  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <BlogPostPage post={post} content={content} />
    </div>
  );
}
```

- [ ] **Step 6: Run build**

Run:

```bash
env -u ELECTRON_RUN_AS_NODE PATH="/private/tmp/node-v22.13.1-darwin-arm64/bin:$PATH" npm run build
```

Expected: PASS or only fail on homepage widget types not implemented yet.

- [ ] **Step 7: Commit blog components and routes**

Run:

```bash
git add src/types/page.ts src/lib/content.ts src/components/pages/BlogPage.tsx src/components/pages/BlogPostPage.tsx src/components/pages/DynamicPageClient.tsx 'src/app/[slug]/page.tsx' 'src/app/blog/[post]/page.tsx'
git commit -m "Add structured blog pages"
```

Expected: commit succeeds.

### Task 5: Implement Homepage Widgets

**Files:**
- Modify: `src/app/page.tsx`
- Modify: `src/components/home/HomePageClient.tsx`
- Create: `src/components/home/LatestUpdatesWidget.tsx`
- Create: `src/components/home/ScholarWidget.tsx`

- [ ] **Step 1: Create Latest Updates widget**

Create `src/components/home/LatestUpdatesWidget.tsx`:

```tsx
'use client';

import { motion } from 'framer-motion';
import { NewsItem } from '@/components/home/News';

interface LatestUpdatesWidgetProps {
  items: NewsItem[];
  title?: string;
}

export default function LatestUpdatesWidget({ items, title = 'Latest Updates' }: LatestUpdatesWidgetProps) {
  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.5 }}
      className="rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5"
    >
      <h2 className="text-xl font-serif font-bold text-primary mb-4">{title}</h2>
      <div className="space-y-3">
        {items.map((item, index) => (
          <div key={`${item.date}-${index}`} className="flex items-start gap-3">
            <span className="text-xs text-neutral-500 mt-1 w-16 flex-shrink-0">{item.date}</span>
            <p className="text-sm text-neutral-700 dark:text-neutral-500">{item.content}</p>
          </div>
        ))}
      </div>
    </motion.section>
  );
}
```

- [ ] **Step 2: Create Scholar widget**

Create `src/components/home/ScholarWidget.tsx`:

```tsx
'use client';

import { motion } from 'framer-motion';
import { ExternalLink } from 'lucide-react';

interface ScholarWidgetProps {
  href?: string;
  title?: string;
  description?: string;
}

export default function ScholarWidget({
  href,
  title = 'Google Scholar',
  description = 'Publication profile and citation record.',
}: ScholarWidgetProps) {
  if (!href) {
    return null;
  }

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6, delay: 0.55 }}
      className="rounded-lg border border-neutral-200 dark:border-neutral-800 bg-white dark:bg-neutral-900 p-5"
    >
      <h2 className="text-xl font-serif font-bold text-primary mb-2">{title}</h2>
      <p className="text-sm text-neutral-600 dark:text-neutral-500 mb-4">{description}</p>
      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-2 rounded-md bg-neutral-100 dark:bg-neutral-800 px-3 py-2 text-sm font-medium text-neutral-700 dark:text-neutral-300 transition-colors hover:bg-accent hover:text-white"
      >
        View profile
        <ExternalLink className="h-4 w-4" />
      </a>
    </motion.section>
  );
}
```

- [ ] **Step 3: Extend homepage section types**

In `src/app/page.tsx`, change:

```ts
type: 'markdown' | 'publications' | 'list';
```

to:

```ts
type: 'markdown' | 'publications' | 'list' | 'latest_updates' | 'scholar_card';
```

Add section fields:

```ts
description?: string;
scholarUrl?: string;
```

Add switch cases:

```ts
case 'latest_updates': {
  const newsData = section.source ? getTomlContent<{ news: NewsItem[] }>(section.source, locale) : null;
  return {
    ...section,
    items: (newsData?.news || []).slice(0, section.limit || 3),
  };
}
case 'scholar_card':
  return {
    ...section,
    scholarUrl: getConfig(locale).social.google_scholar,
  };
```

- [ ] **Step 4: Render widgets on homepage**

In `src/components/home/HomePageClient.tsx`, import:

```tsx
import LatestUpdatesWidget from '@/components/home/LatestUpdatesWidget';
import ScholarWidget from '@/components/home/ScholarWidget';
```

Extend section type:

```ts
type: 'markdown' | 'publications' | 'list' | 'latest_updates' | 'scholar_card';
description?: string;
scholarUrl?: string;
```

Add render branches:

```tsx
case 'latest_updates':
  return (
    <LatestUpdatesWidget
      key={section.id}
      items={section.items || []}
      title={section.title}
    />
  );
case 'scholar_card':
  return (
    <ScholarWidget
      key={section.id}
      href={section.scholarUrl}
      title={section.title}
      description={section.description}
    />
  );
```

- [ ] **Step 5: Run validator and build**

Run:

```bash
python3 scripts/validate_prism_site.py
env -u ELECTRON_RUN_AS_NODE PATH="/private/tmp/node-v22.13.1-darwin-arm64/bin:$PATH" npm run build
```

Expected: validator PASS and build PASS.

- [ ] **Step 6: Commit widget implementation**

Run:

```bash
git add src/app/page.tsx src/components/home/HomePageClient.tsx src/components/home/LatestUpdatesWidget.tsx src/components/home/ScholarWidget.tsx
git commit -m "Add homepage update and scholar widgets"
```

Expected: commit succeeds.

### Task 6: Final Verification And Publish

**Files:**
- No new source files beyond previous tasks.

- [ ] **Step 1: Run full local verification**

Run:

```bash
python3 scripts/validate_prism_site.py
git diff --check
env -u ELECTRON_RUN_AS_NODE PATH="/private/tmp/node-v22.13.1-darwin-arm64/bin:$PATH" npm run build
```

Expected: all commands exit 0.

- [ ] **Step 2: Inspect static output**

Run:

```bash
rg -n "Purdue ECE|Learn to Optimize|Latest Updates|Google Scholar|Learning to Optimize" out
```

Expected: all required strings appear in `out/index.html`, `out/blog/index.html`, or static RSC text files.

- [ ] **Step 3: Commit any validation fixes**

If Task 6 finds small missing validator/source issues, fix them and commit:

```bash
git add <changed-files>
git commit -m "Finalize blog and widget validation"
```

Expected: no commit is needed if all previous tasks already passed.

- [ ] **Step 4: Push**

Run:

```bash
git push origin main
```

Expected: push succeeds.

- [ ] **Step 5: Watch GitHub Pages workflow**

Run:

```bash
gh run list --repo MhaoMou/MhaoMou.github.io --branch main --limit 3
gh run watch <new-run-id> --repo MhaoMou/MhaoMou.github.io --exit-status
```

Expected: build and deploy jobs pass.

- [ ] **Step 6: Verify live site**

Run:

```bash
curl -L --max-time 30 'https://mhaomou.github.io/?v=<commit>' | rg -n "Purdue ECE|Learn to Optimize|Latest Updates|Google Scholar"
curl -L --max-time 30 'https://mhaomou.github.io/blog/?v=<commit>' | rg -n "Blog|Learning to Optimize"
curl -L --max-time 30 'https://mhaomou.github.io/blog/learning-to-optimize/?v=<commit>' | rg -n "Learning to Optimize|optimization"
```

Expected: all live checks find the requested strings.

## Self-Review

- Spec coverage: all requested items are covered by tasks: Purdue ECE text, Learn to Optimize, structured blog index/post pages, Latest Updates widget, Google Scholar card, validation, build, and publish.
- Marker scan: no incomplete-work markers or unspecified implementation steps remain.
- Type consistency: `BlogPageConfig`, `BlogPostMeta`, `latest_updates`, `scholar_card`, `scholarUrl`, and `NewsItem` names are consistent across tasks.

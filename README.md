# Yaksh Patel — Personal Website

A clean, fast, sidebar-based personal website powered by **Jekyll** and hosted on **GitHub Pages**. Inspired by the design language of [leimao.github.io](https://leimao.github.io/) — readable typography, a persistent author sidebar, and content-first layout.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Site Structure](#site-structure)
3. [Where to Edit What](#where-to-edit-what)
   - [Personal Info & Global Settings](#1-personal-info--global-settings--_configyml)
   - [Your Photo / Avatar](#2-your-photo--avatar)
   - [Home Page](#3-home-page--indexmd)
   - [About Page](#4-about-page--aboutindexmd)
   - [Writing Blog Posts](#5-writing-blog-posts--_posts)
   - [Adding Projects](#6-adding-projects--_projects)
   - [Publications Page](#7-publications-page--publicationsindexmd)
   - [Navigation Menu](#8-navigation-menu)
   - [Sidebar Categories & Stats](#9-sidebar-categories--stats)
   - [Design & Colors](#10-design--colors--assetscssmainscsss)
4. [Deploying to GitHub Pages](#deploying-to-github-pages)
5. [Running Locally](#running-locally)
6. [Adding New Pages](#adding-new-pages)
7. [Writing Tips](#writing-tips)
   - [Front Matter Reference](#front-matter-reference)
   - [Code Blocks](#code-blocks)
   - [Math Equations](#math-equations)
   - [Images in Posts](#images-in-posts)
8. [Dark / Light Theme](#dark--light-theme)
9. [FAQ & Troubleshooting](#faq--troubleshooting)

---

## Quick Start

```bash
# 1. Clone your repo
git clone https://github.com/Yaksh-Patel/Yaksh-Patel.github.io
cd Yaksh-Patel.github.io

# 2. Install dependencies
gem install bundler
bundle install

# 3. Compile CSS
gem install sass
sass assets/css/main.scss assets/css/main.css

# 4. Serve locally (auto-reloads on file save)
bundle exec jekyll serve --livereload

# 5. Open http://localhost:4000
```

> **GitHub Pages** will build and deploy automatically when you push to `main`.  
> The GitHub Actions workflow at `.github/workflows/deploy.yml` handles this for you.

---

## Site Structure

```
.
├── _config.yml                  ← Global settings, author info, nav links
│
├── _layouts/
│   ├── default.html             ← Master layout: header, sidebar, footer
│   ├── post.html                ← Blog post layout
│   └── project.html             ← Project detail layout
│
├── _posts/                      ← Blog posts (one .md file per post)
│   └── YYYY-MM-DD-title.md
│
├── _projects/                   ← Project write-ups (one .md file per project)
│   └── my-project.md
│
├── assets/
│   ├── css/
│   │   ├── main.scss            ← All styles (edit here for design changes)
│   │   └── main.css             ← Compiled output (do NOT edit directly)
│   ├── js/
│   │   └── main.js              ← Theme toggle, mobile nav, search
│   └── images/
│       ├── avatar.jpg           ← Sidebar profile photo (replace this)
│       └── avatar-large.jpg     ← Larger photo for About/Home (replace this)
│
├── index.md                     ← Home page content
├── about/index.md               ← About page content
├── blog/index.html              ← Blog listing (paginated)
├── projects/index.html          ← Projects listing
├── publications/index.md        ← Publications page
├── 404.md                       ← Custom 404 page
│
├── .github/workflows/
│   └── deploy.yml               ← Auto-deploy to GitHub Pages on push
│
├── Gemfile                      ← Ruby gem dependencies
└── README.md                    ← This file
```

---

## Where to Edit What

### 1. Personal Info & Global Settings → `_config.yml`

This is **the most important file**. Every section is annotated. Key things to update:

| Setting | What it does |
|---------|-------------|
| `title` | Your name — shown in browser tab and navbar logo |
| `tagline` | Short subtitle shown on the page |
| `description` | Used for SEO meta tags |
| `author.name` | Your full name (used in sidebar and footer) |
| `author.bio` | 1–2 sentence bio shown in sidebar |
| `author.location` | City shown under your photo |
| `author.avatar` | Path to your sidebar photo |
| `author.email` | Contact email |
| `author.github` | GitHub username (just the username, not full URL) |
| `author.linkedin` | LinkedIn username |
| `author.twitter` | Twitter/X handle (leave blank to hide the button) |
| `author.kaggle` | Kaggle username (leave blank to hide) |
| `stats.posts` | Override the post count in sidebar (or leave to auto-count) |
| `stats.projects` | Override project count |
| `stats.years_experience` | Years in the field |
| `sidebar_categories` | Categories shown in sidebar with counts |

After editing `_config.yml`, **restart `jekyll serve`** — config changes don't hot-reload.

---

### 2. Your Photo / Avatar

**Sidebar photo** (small circle):
1. Add your photo to `assets/images/avatar.jpg`
2. In `_config.yml`, set `author.avatar: "/assets/images/avatar.jpg"`

**Home page / About page photo** (larger):
1. Add photo to `assets/images/avatar-large.jpg`
2. In `index.md`, replace the placeholder block:
   ```html
   <!-- BEFORE -->
   <div class="hero-photo-placeholder">🧑‍💻</div>

   <!-- AFTER -->
   <img src="/assets/images/avatar-large.jpg" alt="Yaksh Patel" class="hero-photo" />
   ```
3. In `about/index.md`, uncomment the `<img>` line and remove the comment.

**Favicon**:
1. Add a 32×32 or 64×64 PNG to `assets/images/favicon.png`
2. It's already referenced in `_layouts/default.html` — nothing else needed.

---

### 3. Home Page → `index.md`

Edit the three paragraphs in the `.home-hero` section:

```markdown
<!-- index.md -->
<p>
  I build machine learning systems...   ← Edit this intro
</p>

<p>
  Previously I worked on...   ← Edit your story / background
</p>

<p>
  I believe in writing...   ← Edit your mission / site purpose
</p>
```

The **Recent Posts** and **Selected Projects** sections auto-populate from your `_posts/` and `_projects/` folders — no manual edits needed there.

---

### 4. About Page → `about/index.md`

Sections to personalise:

| Section | How to edit |
|---------|-------------|
| "Who am I" paragraphs | Edit the `<p>` blocks under `<h2>Who am I</h2>` |
| Experience timeline | Edit/add `<div class="timeline-item">` blocks |
| Education timeline | Same pattern as Experience |
| Skills grid | Change skill names and `width` percentages in `.skill-fill` |
| Contact paragraph | Update email/links |

**Adding a timeline entry:**
```html
<div class="timeline-item">
  <div class="tl-period">2022 – 2024</div>
  <div class="tl-title">Your Job Title</div>
  <div class="tl-org">Company Name · City</div>
  <div class="tl-desc">What you did there in 1–2 sentences.</div>
</div>
```

**Adding a skill:**
```html
<div class="skill-box">
  <div class="skill-name">Skill Name</div>
  <div class="skill-bar">
    <div class="skill-fill" style="width:80%"></div>  <!-- 0–100% -->
  </div>
</div>
```

---

### 5. Writing Blog Posts → `_posts/`

**File naming is critical** — Jekyll requires this exact format:
```
_posts/YYYY-MM-DD-your-post-title.md
```

Example: `_posts/2024-03-10-understanding-woe-encoding.md`

**Minimal front matter:**
```yaml
---
layout: post
title: "Understanding WoE Encoding for Credit Risk"
date: 2024-03-10
categories: [credit-risk]
tags: [python, feature-engineering, WoE]
excerpt: "One sentence summary shown on the blog listing page."
---

Your post content starts here...
```

**Full front matter options:**
```yaml
---
layout: post
title: "Post Title"
date: 2024-03-10           # Publication date
categories: [machine-learning]  # One category recommended
tags: [python, xgboost, tutorial]  # As many tags as you like
read_time: 8               # Minutes — shown next to date
excerpt: "One sentence summary."
mathjax: true              # Set to true if post uses LaTeX math
---
```

**Organising posts:**
- Use `categories` for broad groupings (e.g. `machine-learning`, `credit-risk`, `python`, `statistics`)
- Use `tags` for specific topics (e.g. `XGBoost`, `WoE`, `feature-engineering`)
- The sidebar category list auto-counts posts per category

---

### 6. Adding Projects → `_projects/`

Create a file in `_projects/` — the filename becomes the URL slug:
```
_projects/credit-scoring-pipeline.md  →  /projects/credit-scoring-pipeline/
```

**Project front matter:**
```yaml
---
layout: project
title: "Credit Scoring Pipeline"
date: 2024-01-15              # Used for sorting (newest first)
description: "One-line summary shown on the projects listing page."
github: "https://github.com/Yaksh-Patel/project-name"   # Leave blank to hide
demo: "https://your-demo-url.com"                        # Leave blank to hide
paper: "https://arxiv.org/abs/xxxx.xxxxx"                # Leave blank to hide
status: "Completed"           # Completed / In Progress / Archived
tags: [Python, XGBoost, MLflow, Credit Risk]
---

## Overview
Your detailed project write-up goes here...
```

The projects listing page (`projects/index.html`) and home page auto-populate from these files.

---

### 7. Publications Page → `publications/index.md`

Add a `.publication-item` block for each paper:

```html
<div class="publication-item">
  <div class="pub-title">Your Paper Title</div>
  <div class="pub-authors">Yaksh Patel, Co-author Name</div>
  <div class="pub-venue">NeurIPS 2024 / Journal Name, Volume X</div>
  <div class="pub-links">
    <a href="https://..." class="pub-link">PDF</a>
    <a href="https://arxiv.org/abs/..." class="pub-link">arXiv</a>
    <a href="https://github.com/..." class="pub-link">Code</a>
  </div>
</div>
```

If you have no publications, remove `Publications` from the `nav_pages` list in `_config.yml`.

---

### 8. Navigation Menu

Edit the `nav_pages` list in `_config.yml`:

```yaml
nav_pages:
  - title: "Home"
    url: "/"
  - title: "About"
    url: "/about/"
  - title: "Projects"
    url: "/projects/"
  - title: "Blog"
    url: "/blog/"
  - title: "Publications"         # Remove this entry to hide the link
    url: "/publications/"
```

To **add a new nav item**, create the page file first (see [Adding New Pages](#adding-new-pages)), then add an entry here.

---

### 9. Sidebar Categories & Stats

**Categories** (shown with post counts in sidebar):
```yaml
# _config.yml
sidebar_categories:
  - label: "machine-learning"    # Must match the category name used in posts
    url: "/blog/category/machine-learning/"
  - label: "credit-risk"
    url: "/blog/category/credit-risk/"
```

**Stats** (the three numbers under your photo):
```yaml
# _config.yml
stats:
  posts: 12               # Override auto-count, or leave blank for auto
  projects: 5             # Override auto-count, or leave blank for auto
  years_experience: 4     # Always set manually
```

---

### 10. Design & Colors → `assets/css/main.scss`

All colours are CSS custom properties at the top of `main.scss`. Edit the `:root` block:

```scss
:root {
  --accent: #2563a8;         /* Primary blue — links, active states, highlights */
  --bg: #fafaf8;             /* Page background */
  --bg-card: #ffffff;        /* Card/box background */
  --text: #1a1916;           /* Main text colour */
  --text-muted: #6b6860;     /* Secondary text */
  --font-body: 'DM Sans', sans-serif;    /* Body font */
  --font-serif: 'Lora', Georgia, serif;  /* Headings font */
  --font-mono: 'JetBrains Mono', monospace;  /* Code font */
}
```

The `[data-theme="dark"]` block below it mirrors the same variables for dark mode.

**After editing SCSS**, recompile:
```bash
sass assets/css/main.scss assets/css/main.css
```

Or run the watcher (auto-recompiles on save):
```bash
sass --watch assets/css/main.scss:assets/css/main.css
```

> **Fonts**: The Google Fonts `@import` at the top of `main.scss` loads DM Sans, Lora, and JetBrains Mono. To change fonts, replace the import URL and update the `--font-*` variables.

---

## Deploying to GitHub Pages

The site deploys **automatically** when you push to `main`. The workflow at `.github/workflows/deploy.yml` handles building Jekyll and publishing.

**One-time GitHub setup:**
1. Go to your repo → **Settings** → **Pages**
2. Set **Source** to `GitHub Actions`
3. Push your changes — the site builds in ~2 minutes

**Verify the deployment:**
- Go to **Actions** tab in GitHub to watch the build
- Your site will be live at `https://yaksh-patel.github.io`

---

## Running Locally

```bash
# Install Ruby gems
bundle install

# Compile SCSS (first time and after any CSS edits)
sass assets/css/main.scss assets/css/main.css

# Start local server with live-reload
bundle exec jekyll serve --livereload

# Open http://localhost:4000
```

**Common flags:**
```bash
# Show draft posts (files in _drafts/ folder)
bundle exec jekyll serve --drafts

# Build without serving (output in _site/)
bundle exec jekyll build
```

---

## Adding New Pages

1. Create a folder and `index.md` (or a standalone `.md` file):
   ```
   talks/index.md        →  /talks/
   cv.md                 →  /cv/
   ```

2. Add front matter:
   ```yaml
   ---
   layout: default
   title: "Talks"
   permalink: /talks/
   ---

   Your page content here.
   ```

3. Add to `nav_pages` in `_config.yml` if you want it in the navbar.

---

## Writing Tips

### Front Matter Reference

```yaml
---
layout: post          # post | project | default
title: ""             # Post title (required)
date: YYYY-MM-DD      # Publication date (required for posts)
categories: []        # List — use one category per post
tags: []              # List — any number of tags
excerpt: ""           # 1-sentence summary for listing pages
read_time: 5          # Minutes — displayed next to date
mathjax: true         # Enable LaTeX rendering for this post
---
```

### Code Blocks

Use fenced code blocks with a language hint for syntax highlighting:

````markdown
```python
import numpy as np
arr = np.array([1, 2, 3])
```

```sql
SELECT customer_id, COUNT(*) AS total_loans
FROM loans
WHERE status = 'default'
GROUP BY customer_id;
```

```bash
jekyll serve --livereload
```
````

Supported languages: `python`, `sql`, `bash`, `yaml`, `json`, `javascript`, `r`, `scala`, and [many more](https://rouge-ruby.github.io/docs/file.Languages.html).

### Math Equations

MathJax is enabled globally. Use `$...$` for inline and `$$...$$` for display:

```markdown
The Gini coefficient is $G = 2 \cdot \text{AUC} - 1$.

$$
\text{LogLoss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{p}_i) + (1-y_i)\log(1-\hat{p}_i) \right]
$$
```

### Images in Posts

```markdown
![Caption for the image](/assets/images/my-chart.png)
```

Place images in `assets/images/` organised by post if you prefer:
```
assets/images/posts/2024-03-10-woe-encoding/woe-chart.png
```

---

## Dark / Light Theme

- The toggle button in the top-right corner switches themes.
- The user's preference is saved to `localStorage` and persists across visits.
- If no preference is saved, the system's OS preference is used automatically.
- All colours are CSS variables — both themes are defined in `main.scss`.

---

## FAQ & Troubleshooting

**Q: My changes aren't showing up after editing `_config.yml`**  
A: Restart `jekyll serve` — config changes are not picked up by the live-reload watcher.

**Q: How do I add a CV / resume download?**  
A: Put your PDF in `assets/` (e.g. `assets/yaksh-patel-cv.pdf`) and link to it anywhere:
```markdown
[Download CV](/assets/yaksh-patel-cv.pdf)
```

**Q: How do I write a draft post without it going live?**  
A: Create the file in `_drafts/` (no date in the filename) and serve with `--drafts` flag locally. Drafts are never included in the production build.

**Q: Can I have multiple categories per post?**  
A: Yes — `categories: [machine-learning, python]` — but the sidebar count only matches single-category assignments.

**Q: How do I change the number of posts per page?**  
A: In `_config.yml`, change `paginate: 10` to your preferred number.

**Q: How do I add Google Analytics?**  
A: Add your measurement ID to `_config.yml`:
```yaml
google_analytics: "G-XXXXXXXXXX"
```
Then add the GA script snippet to `_layouts/default.html` just before `</head>`.

**Q: How do I add a comment section to posts?**  
A: [Giscus](https://giscus.app/) (GitHub Discussions-based, free) is recommended. Generate the embed script from giscus.app and add it to `_layouts/post.html` below `{{ content }}`.

**Q: The CSS isn't updating**  
A: Re-run `sass assets/css/main.scss assets/css/main.css`. The `.css` file must be committed — Jekyll on GitHub Pages doesn't compile SCSS without a plugin.

---

*Built with [Jekyll](https://jekyllrb.com/) · Hosted on [GitHub Pages](https://pages.github.com/)*

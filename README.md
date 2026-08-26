# Yaksh Patel — Personal Website

Jekyll site on GitHub Pages. Design direction: **engineering instrument** — cool ink
neutrals, one signal-teal accent, geometric display type over a humanist body face, and
monospace reserved strictly for metadata. Hairlines and a dot mesh instead of shadows.

Live at **https://yaksh-patel.github.io**

---

## Run it locally

```bash
bundle install
bundle exec jekyll serve --livereload   # http://localhost:4000
```

Needs Ruby ≥ 2.7 (Jekyll 4.3). macOS system Ruby is 2.6 — install a newer one via
`rbenv` or `brew install ruby` first.

## Deploy

Push to `main`. `.github/workflows/deploy.yml` builds with Jekyll and publishes to Pages.

> **The SCSS compiles through Jekyll — never commit a built `assets/css/main.css`.**
> `main.scss` carries front matter, which is what tells Jekyll to compile it. A committed
> `main.css` sits at the same output path and silently shadows the compiled result, so the
> site ships a stale stylesheet while the build reports success. Both built files are
> gitignored for this reason.

---

## Where to edit what

| I want to change… | Edit |
|---|---|
| Name, role, tagline, socials, nav | `_config.yml` → `author`, `nav_pages` |
| Hero headline, blurb, affiliations | `_config.yml` → `hero` |
| "What I work on" cards | `_config.yml` → `focus_areas` |
| Hero stat numbers | `index.md` → `.hero-stats` |
| Homepage sections and order | `index.md` |
| Bio, timeline, toolkit chips | `about/index.md` |
| Colors, type, spacing | `assets/css/main.scss` (design tokens at the top) |
| Theme toggle, reveal, search | `assets/js/main.js` |

### Design tokens

Everything visual comes from custom properties defined twice at the top of `main.scss` —
once on `:root` for light, once on `[data-theme="dark"]`. **Change a color there, not in a
rule.** Any new color needs a value in both blocks or dark mode breaks.

```scss
--accent          /* signal teal: links, active nav, indices, primary buttons */
--text / --text-muted / --text-faint    /* three-step hierarchy, use all three */
--surface / --surface-2 / --bg / --bg-alt
--border / --border-soft                /* hairlines; --border-soft is the quieter one */
--font-display / --font-body / --font-mono
```

Mono is metadata only — labels, indices, dates, tags. Never body copy.

---

## Adding content

### A blog post — `_posts/YYYY-MM-DD-title.md`

```yaml
---
title: "Post title"
date: 2026-08-26
categories: [ml-systems]
tags: [Python, MLOps]
read_time: 8        # optional
---
```

`layout` and `narrow` come from `_config.yml` defaults; don't set them per post.

### A project — `_projects/name.md`

```yaml
---
title: "Project name"
date: 2026-07-27
description: "One sentence for the card."
github: "https://github.com/..."
demo: ""            # empty is fine — blank fields are hidden
paper: ""
status: "Working on-device"
platform: "Android · Kotlin"                 # renders as "Stack"
role: "Ideation, architecture, review loop"  # renders as "My role"
built_with: "Claude Code, Codex"
ai_assisted: true   # routes the card into the AI Lab section + adds the badge
tags: [Kotlin, Android]
---
```

`ai_assisted: true` is the only switch that matters for placement: the Work page splits
projects into **Applied ML** and **AI Lab** on that flag, and the flag also adds the
`AI-built` badge and the attribution note on the project page.

> Empty strings are **truthy** in Liquid, and `!= blank` does not help — Jekyll has no
> ActiveSupport, so neither `nil` nor `""` responds to `blank?`. The templates normalise
> every optional field with `| default: "" | strip` and compare against `""`. Follow that
> pattern when adding fields, or you get buttons linking nowhere.

---

## Structure

```
_config.yml            identity, hero copy, focus cards, nav, collections
_layouts/
  default.html         shell: header, mobile nav, footer, no-flash theme script
  post.html            blog article
  project.html         project page (badge, spec rows, AI attribution)
_includes/
  icons.html           inline SVG sprite — no external icon requests
  project-card.html    one card, shared by homepage and Work page
  post-card.html       one card, shared by homepage and Writing page
  social-links.html    GitHub / LinkedIn / Email button row
index.md               homepage sections (full_bleed: true)
about/ projects/ blog/ publications/
_posts/ _projects/
assets/css/main.scss   the whole design system
assets/js/main.js      theme, nav, header hairline, reveal, live search
```

### Layout flags

- `full_bleed: true` — content escapes the `.wrap` container so sections can span the
  viewport. Used by `index.md`; each section then wraps its own content.
- `narrow: true` — constrains to a ~720px reading measure. Set by default for posts and
  projects, and manually on About / Publications / 404.

Cards live in `_includes/` on purpose: the homepage and listing pages render the same
partial, so they cannot drift apart.

---

## Notes

- **Theme** is set by an inline script in `<head>` before first paint, so there's no flash
  of the wrong palette. `main.js` only handles the toggle and the icon swap.
- **Icons** are one inline SVG sprite referenced with `<use href="#i-name">`; they inherit
  `currentColor`. Add new symbols to `_includes/icons.html`.
- **Reveal-on-scroll** is opt-in per element with `class="reveal"`, and is disabled under
  `prefers-reduced-motion`.
- **Blog search** filters cards live as you type — no reload, no query round trip.

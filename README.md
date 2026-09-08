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
| Writing topics (the sections under Writing) | `_config.yml` → `topics` + a stub in `blog/topics/` |
| Theme toggle, reveal, writing filters | `assets/js/main.js` |

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
categories: [statistics]      # topic slugs — these place the post in a section
tags: [experimentation, power]
read_time: 8                  # optional
excerpt: "One sentence for the card and the search index."
---
```

`layout` and `narrow` come from `_config.yml` defaults; don't set them per post.

**`categories` is the routing field.** Each entry must match a `slug` under
`topics:` in `_config.yml`, because that is what files the post into a section,
lights up its filter chip, and turns the pill on its card into a link. More than
one is fine — a post listing `[statistics, philosophy]` shows up under both. A
category that is not a known topic still renders as a plain grey pill, but it
gets no section and no filter.

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

## The Writing section

Writing is split by topic, and every topic is reachable two ways on purpose.

**Topic pages** — `/blog/topics/<slug>/` — are real pages. They are linkable,
crawlable, in the sitemap, and they work with JavaScript switched off. Each one
is a stub in `blog/topics/` holding nothing but front matter and a single
`{% include writing-topic.html %}`, so the pages cannot drift apart.

**Filter chips** on `/blog/` do the same job without a page load: topic, year,
and a live search over titles, tags, categories and excerpts. The state
round-trips through the query string, so `/blog/?topic=statistics&year=2026` is
a link you can send someone.

Posts are grouped under sticky year headings, newest first, so scrolling to a
date works as well as filtering to one.

### Adding a topic

1. Add an entry to `topics:` in `_config.yml` — `slug`, `label`, `blurb`.
2. Copy any file in `blog/topics/`, and change `topic:`, `title:` and
   `permalink:` to the new slug.

That is the whole job; counts, chips, cards and the topic grid all read from
`site.topics`. A topic with no posts yet stays visible with its chip disabled
and its card reading "nothing yet" — the list is meant to show the range of the
reading, not only what has been written up.

> Pagination is deliberately **off**. The archive filters in the browser, so
> paging it would hide cards the filter is supposed to find, and would publish a
> second copy of the listing at `/blog/page2/`.

### Hand-drawn diagrams

Sketches like the one in the statistical-power post are inline SVG includes:
real plotted geometry pushed through a turbulence displacement filter, lettered
in a handwriting face, on a fixed eggshell ground that does **not** invert with
the theme — dark mode only takes the glare off.

`_includes/diagram-power-*.html` are **generated**. The curves are real
Gaussians, so edit the generator and re-run it rather than nudging coordinates
in the include:

```bash
python3 tools/gen_sketch.py _includes
```

Markup for one, in a post:

```html
<figure class="sketch sketch--wide">
  <div class="sketch-frame">{% include diagram-power-curves.html %}</div>
  <figcaption>One line on what the picture shows.</figcaption>
</figure>
```

`sketch--wide` lets the sheet break out of the 720px reading measure, which the
pen labels need; `sketch-frame` gives it the border and, on phones, a sideways
scroll so the sheet stops shrinking instead of becoming illegible.

Two things to keep in mind if you draw another:

- Give filters an explicit `filterUnits="userSpaceOnUse"` region. With the
  default bounding-box units, any horizontal or vertical line has a zero-area
  bbox, the filter region collapses to nothing, and the stroke silently
  disappears.
- Don't displace text. A handwriting face already reads as hand-made; running
  glyphs through the filter just melts them.

### Math

`$$ ... $$` for display, `$ ... $` for inline. Both work: kramdown 2.x converts
`$$..$$` into `\[..\]` (block) or `\(..\)` (inline), which is exactly what
MathJax 3 reads, and it leaves single-`$` spans alone for MathJax to pick up via
the `inlineMath` config in `_layouts/default.html`.

Two things that do **not** work, both verified against kramdown 2.4.0:

- **Never write raw `\[ .. \]` or `\( .. \)` in markdown body text.** Kramdown
  treats the backslash as an escape and strips it, so `\( x^2 \)` reaches the
  browser as a literal `( x^2 )` and MathJax never sees a delimiter. They survive
  only inside a block-level HTML element, where kramdown passes the content
  through untouched. Just use `$$`.
- **Two dollar signs in one paragraph become math.** Because `$..$` is enabled as
  an inline delimiter site-wide, prose like "it cost $5 and then $10 more"
  typesets "5 and " as an equation. Put currency in backticks — MathJax skips
  `code` and `pre` — or keep it to one `$` per paragraph.

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
  post-card.html       one card, shared by homepage, Writing and topic pages
  post-archive.html    posts grouped under sticky year headings
  writing-toolbar.html search + topic + year filter chips
  writing-topic.html   the entire body of a topic page
  topic-nav.html       the topic grid, built from site.topics
  diagram-power-*.html hand-drawn inline SVG sketches for one post
  social-links.html    GitHub / LinkedIn / Email button row
index.md               homepage sections (full_bleed: true)
about/ projects/ blog/ publications/
blog/topics/           one stub per topic — front matter plus one include
_posts/ _projects/
tools/gen_sketch.py    generates the hand-drawn SVG sketches (excluded from the build)
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
- **Writing filters** apply search, topic and year in one pass over the cards, reading
  pre-computed `data-` attributes rather than DOM text, and mirror their state into the
  query string. A year heading whose posts are all filtered out hides itself.
- **Topic pages** are the no-JavaScript path to the same content, which is why both
  mechanisms exist.

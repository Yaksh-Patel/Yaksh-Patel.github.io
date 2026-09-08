---
title: "The day statistical power stopped being a formula"
date: 2026-09-08
categories: [statistics]
tags: [experimentation, hypothesis-testing, power, a-b-testing]
read_time: 7
excerpt: "One diagram of two overlapping curves, and four things I had been computing for years turned into things I could see."
---

I have run power calculations for years. Plug in the baseline, plug in the minimum
effect I care about, get a sample size, argue with someone about whether we can
really wait three weeks for it. I could do the arithmetic in my sleep. What I
could not do, if you had stopped me mid-meeting and asked, was *draw* it.

Today I finally saw the picture, and it reorganised the whole thing in my head.
So here it is, redrawn by hand, because I want to remember it as a picture rather
than as a formula I trust.

<figure class="sketch sketch--wide">
  <div class="sketch-frame">{% include diagram-power-curves.html %}</div>
  <figcaption>Two distributions of the same measurement: what you'd see if the treatment does nothing, and what you'd see if it works.</figcaption>
</figure>

## How to read it

The horizontal axis is every difference-in-means you could observe. Not the truth —
the *observation*. Every value your experiment could hand back.

The left curve is the range of results you'd get if the treatment does nothing.
The right curve is the range you'd get if it has the true effect. The dashed line
is your decision rule: anything right of it, you call significant.

That's the whole apparatus. Two curves and a line.

The thing I had never internalised is what sets the width of those curves. Both
curves have the same width, and that width is the standard error:

$$
\text{SE} \;=\; \sigma \sqrt{\frac{2}{n}}
$$

for a two-group comparison. Once that clicked, every lever became visible instead
of algebraic. I stopped asking "what does the formula say" and started asking
"what does this do to the picture".

<figure class="sketch sketch--wide">
  <div class="sketch-frame">{% include diagram-power-levers.html %}</div>
  <figcaption>The same two curves, redrawn four times. Faint pencil is the version being changed away from.</figcaption>
</figure>

## Sample size ↑ → power ↑

`n` is in the denominator of SE, so more users make both curves narrower. Narrow
curves overlap less, and the dashed line — which sits at 1.96 × SE from zero —
slides closer to zero. More of the green curve ends up on the winning side.

Two things move at once here, and I had only ever thought about the first. The
curves get tighter *and* the bar comes down to meet them. That is why sample size
feels like such a blunt, reliable instrument: it is the only lever that improves
both halves of the picture at the same time.

## Effect size ↑ → power ↑

A bigger true effect slides the right curve further right, away from the dashed
line. Nothing about the curves' width changes; they just separate.

Which is the honest version of something I have said badly in a lot of meetings.
When someone asks "can we detect a 0.5% lift", the answer has nothing to do with
how good the experiment is. It is a question about how far apart two fixed-width
curves are sitting. Small effects are hard to detect because the two worlds they
describe genuinely look almost identical from the inside.

## α ↑ → power ↑

Raising α from 0.05 to 0.10 moves the dashed line left (from 1.96 SE to 1.645 SE).
More of the green curve clears it. But more of the purple curve clears it too —
that's the price.

This is the fundamental Type I / Type II tradeoff, and drawn this way it stops
being two abstractions with confusable names. It's one line. Slide it left and you
catch more real effects and more noise. Slide it right and you catch less of both.
**You cannot lower both error rates without adding data**, because moving the line
cannot change where the curves are or how wide they are. Only `n` does that.

## Variance ↑ → power ↓

σ is in the numerator of SE. A noisier metric widens both curves, they overlap
more, and the dashed line pushes further right. Same true effect, less detectable.

I think this is the lever I have most consistently under-weighted. It never shows
up as a decision anyone makes — nobody chooses a noisier metric on purpose. It
arrives by default, in the choice of what to measure, and it degrades an
experiment in exactly the same way as cutting the sample size would.

## What I actually took from it

Four levers, and the picture tells you what kind of thing each one is.

| Lever | What it moves in the picture |
|---|---|
| Sample size | Narrows both curves, and pulls the line inward |
| Effect size | Slides the right curve; widths untouched |
| α | Slides the line only — the curves never move |
| Variance | Widens both curves, and pushes the line out |

Only two of the four are really mine to choose. The effect size is whatever the
treatment actually does; the variance is mostly a property of the metric. What is
left is `n` and α — how much data I am willing to gather, and how much noise I am
willing to mistake for signal.

The version of this I had in my head before today was a function call. The version
I have now is a sheet of paper with two bells on it, and I can ask it questions.

---
layout: project
title: "Nothing Widgets"
date: 2026-05-04
description: "A minimal Android widget pack — live ringer, steps, and compass surfaces that scale to whatever home-screen slot you drop them into. Dark, dot-matrix, deliberately sparse."
github: "https://github.com/Yaksh-Patel/Nothings-Widget"
demo: ""
paper: ""
status: "In daily use"
ai_assisted: true
role: "Ideation, product decisions, architecture calls, review loop"
built_with: "Claude Code, Codex"
platform: "Android 12+ · Kotlin · RemoteViews"
tags: [Kotlin, Android, RemoteViews, Widgets, AI-Assisted]
---

## The idea

I wanted the Nothing Phone's widget aesthetic — dark, dot-matrix, almost aggressively
sparse — with three surfaces I'd actually use every day.

| Widget | What it does |
|---|---|
| **Ringer** | One-tap cycle through ring / vibrate / silent, current mode drawn as a live orb. Turns red on silent. |
| **Steps** | Daily count against a goal you set in-app, drawn as a dot-matrix progress ring. |
| **Compass** | Live heading on a drawn dial. |

Each ships **compact and expanded layouts** and picks between them based on the actual slot
size — not a fixed 2×2 assumption.

## How it's built

Deliberately plain Android. No Compose, no Glance, no DI framework. The only dependency is
`androidx.appcompat`. Classic `RemoteViews`, with the visuals drawn onto bitmaps at render
time by a small canvas layer.

```
widget/
├── BaseNothingWidgetProvider     shared AppWidgetProvider behaviour
├── {Compass,Steps,RingerToggle}WidgetProvider
├── WidgetRenderCoordinator       decides what needs redrawing, and when
├── WidgetSizeResolver            slot dimensions → compact vs expanded
├── WidgetPresence                tracks which widgets are actually pinned
├── SensorServiceController       starts/stops the sensor stream on demand
└── renderers/                    one renderer per widget + WidgetArtFactory

service/WidgetSensorService       foreground service for live sensor data
util/                            CompassMath · AudioController · Haptics
```

## What I actually contributed

The code is AI-written. The two things that make it not-a-toy came out of review, not out
of the first draft:

- **The foreground service only runs when it has to.** The initial version kept a sensor
  service alive permanently — a constant battery tax for widgets the user might not even
  have added. I pushed for `WidgetPresence`: track what's actually pinned, and if no steps
  or compass widget exists, stop the service entirely.
- **Bitmap caching in the render path.** Sensor ticks arrive far faster than the display
  meaningfully changes, and the first pass allocated a fresh bitmap on every one of them.
  Redraws are now gated on progress moving by at least one dot (~1.6%) — enough to smooth
  out sensor noise without the ring feeling laggy.

Neither is a clever algorithm. Both are the kind of thing you only catch if you know what
a widget does to a phone's battery when nobody's watching — which is exactly the gap
between *code that compiles* and *code you'd keep installed*.

The renderer layer is split per widget specifically so adding a fourth surface stays a
small contained change rather than a refactor.

- **minSdk** 31 (Android 12) · **targetSdk** 35 · JDK 17 · Kotlin

Build steps and the full architecture notes are in the
[repository README](https://github.com/Yaksh-Patel/Nothings-Widget).

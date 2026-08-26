---
layout: project
title: "FocusFriction"
date: 2026-07-27
description: "An Android app that puts a deliberate cognitive speed bump between you and your distracting apps — and makes the puzzle harder the more times you've caved today."
github: "https://github.com/Yaksh-Patel/FocusFriction"
demo: ""
paper: ""
status: "Working on-device"
ai_assisted: true
role: "Ideation, product decisions, architecture calls, review loop"
built_with: "Claude Code, Codex"
platform: "Android · Expo SDK 57 · React Native 0.86 · Kotlin native modules"
tags: [React Native, Expo, Kotlin, Android, AI-Assisted]
---

## The idea

App blockers fail because blocking is binary — you either can't open the app, or you
disable the blocker and open it freely. Neither teaches you anything.

FocusFriction adds *friction* instead of a wall. You can always get through, but getting
through costs a few seconds of real cognitive effort — usually enough to notice you didn't
mean to open the app at all. And the cost **scales with your own behaviour**: 1–3 opens
today gets an easy puzzle, 4–5 a medium one, 6+ a hard one. Solve it, you get 10 minutes.
Bypass it, you get 3.

## How interception works

The decision is made **natively**, not in JavaScript — which turned out to be the whole
architectural crux of the project.

```
Target app opened (e.g. YouTube)
        │
        ▼
FocusAccessibilityService          TYPE_WINDOW_STATE_CHANGED
        │
        ▼
FocusPolicyRepository.shouldIntercept(packageId)
        ├── is protection enabled?
        ├── is this package monitored?
        ├── are we inside the active schedule window?
        └── is this package already unlocked?
        │
        ▼  (yes)
InterventionActivity  →  React Native intervention screen  →  puzzle
```

`FocusPolicyRepository` is a native singleton backed by `SharedPreferences`. That matters:
the accessibility service needs a **synchronous** answer the instant a window changes.
Routing that through the React Native bridge was too slow and too fragile, so the native
policy store became the single source of truth and JS mirrors it — not the reverse.

## What I actually contributed

The code is AI-written. The decisions weren't. Three that changed the outcome:

- **Moving the policy store native.** The first version asked JavaScript whether to
  intercept. It worked in testing and fell apart in practice — the bridge round-trip lost
  the race against the window change often enough to let apps through. Recognising *why*
  it was flaky, and that the fix was architectural rather than a tuning problem, was the
  single most valuable call I made on this project.
- **Deriving daily metrics instead of storing them.** The model's first pass kept mutable
  daily counters. They drifted out of sync with reality within a day. I had it replaced
  with an append-only event log that computes counts on read.
- **The excluded-packages guard.** Nothing stopped a bad policy from intercepting the
  launcher or Settings and bricking the phone until a reboot. I asked what happens if the
  user monitors their own launcher; the hardcoded exclusion set came out of that question.

That's the pattern I keep seeing: the AI writes competent code quickly, and the leverage
sits in knowing which competent-looking thing is going to fail in the real world.

## Structure

```
src/core/          appStore · settingsStore · taskStore
                   sessionManager · puzzleEngine · appStorage · secureStore
src/screens/       InterventionScreen · SetupScreen
src/components/    Home · AppSelector · Settings · InterceptOverlay

android/…/focusfriction/
                   FocusAccessibilityService · FocusPolicyRepository
                   InterventionActivity · InterventionModule · InstalledAppsModule
```

Android-only by design — the interception model has no iOS equivalent.

Full walkthrough and setup steps in the
[repository README](https://github.com/Yaksh-Patel/FocusFriction).

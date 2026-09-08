#!/usr/bin/env python3
"""
Generates the hand-drawn statistical-power sketches as inline SVG includes.

    python3 tools/gen_sketch.py _includes

Look we are after: colour pens on an eggshell sheet. Every curve is a real
Gaussian, then pushed through a turbulence displacement filter so the strokes
wobble the way a pen does. Text is left undisplaced -- a handwriting face
already reads as hand-made, and displacing glyphs just melts them.

Two things to know before editing:
  * The filters use filterUnits="userSpaceOnUse" with an explicit region. With
    the default objectBoundingBox units, any horizontal or vertical line has a
    zero-area bbox, the filter region collapses, and the stroke silently
    disappears -- which is what happened to the axis and the decision rule.
  * Arrowheads are one marker per pen colour rather than context-stroke, which
    is still uneven across browsers.
"""
import math

# ---- pens ----------------------------------------------------------------
PURPLE = "#7b52ab"   # the null distribution
GREEN  = "#2f8f57"   # the true-effect distribution
RED    = "#b4402c"   # the decision rule, and the error you agree to accept
INK    = "#4a5560"   # axis, ticks, neutral labels
INK_2  = "#7b8590"   # secondary annotation
BLUE   = "#2f6fa8"   # measurements and margin notes
GHOST  = "#a9a293"   # pencil trace of the version being changed away from
GHOST_2 = "#8b8474"
PAPER  = "#f5efdf"

MARKERS = {"b": BLUE, "g": GREEN, "r": RED, "i": INK, "h": GHOST, "p": PURPLE}


def gauss_pts(mu, sd, base, height, span=3.45, n=90):
    x0, x1 = mu - span * sd, mu + span * sd
    return [(x0 + (x1 - x0) * i / n,
             base - height * math.exp(-0.5 * ((x0 + (x1 - x0) * i / n - mu) / sd) ** 2))
            for i in range(n + 1)]


def polyline(pts):
    return "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def gauss_area(mu, sd, base, height, **kw):
    """Closed path -- the curve plus its baseline -- for clipping hatch fills."""
    pts = gauss_pts(mu, sd, base, height, **kw)
    return polyline(pts) + f" L {pts[-1][0]:.1f},{base:.1f} L {pts[0][0]:.1f},{base:.1f} Z"


def hatch(uid, x0, y0, x1, y1, step=9.0, color=GREEN, width=1.0, opacity=0.55):
    """45-degree pen hatching over a box; callers clip it to the real region."""
    out, c = [], x0 - (y1 - y0)
    while c <= x1:
        out.append(f'<line x1="{c:.1f}" y1="{y1:.1f}" x2="{c + (y1 - y0):.1f}" y2="{y0:.1f}"/>')
        c += step
    return (f'<g stroke="{color}" stroke-width="{width}" opacity="{opacity}" '
            f'filter="url(#{uid}-pen2)" stroke-linecap="round">' + "".join(out) + "</g>")


def defs(uid):
    """Filter region is explicit and generous: see the note in the docstring."""
    region = 'filterUnits="userSpaceOnUse" x="-240" y="-240" width="1440" height="1200"'
    marks = "".join(
        f'<marker id="{uid}-a{k}" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5.6" '
        f'markerHeight="5.6" orient="auto-start-reverse">'
        f'<path d="M 0.8,1.2 L 9,5 L 0.8,8.8" fill="none" stroke="{c}" stroke-width="1.7" '
        f'stroke-linecap="round" stroke-linejoin="round"/></marker>'
        for k, c in MARKERS.items())
    return f'''<defs>
  <filter id="{uid}-pen" {region} color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.021" numOctaves="3" seed="11" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="3.4" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="{uid}-pen2" {region} color-interpolation-filters="sRGB">
    <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="3" seed="41" result="n"/>
    <feDisplacementMap in="SourceGraphic" in2="n" scale="2.1" xChannelSelector="R" yChannelSelector="G"/>
  </filter>
  <filter id="{uid}-grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" stitchTiles="stitch" result="t"/>
    <feColorMatrix in="t" type="saturate" values="0"/>
  </filter>
  {marks}
</defs>'''


def paper(uid, w, h):
    return (f'<rect x="0" y="0" width="{w}" height="{h}" rx="3" fill="{PAPER}"/>'
            f'<rect x="0" y="0" width="{w}" height="{h}" filter="url(#{uid}-grain)" opacity="0.055" '
            f'style="mix-blend-mode:multiply"/>'
            f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="3" fill="none" '
            f'stroke="#d8cfb6" stroke-width="1"/>')


def hand(x, y, txt, color=INK, size=21, anchor="start", weight=600):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" font-family="Caveat, \'Bradley Hand\', cursive">{txt}</text>')


def stroke_g(uid, body, color, width=2.6, f="pen", opacity=1.0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<g fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity="{opacity}" filter="url(#{uid}-{f})"{d}>{body}</g>')


def double_stroke(uid, path, color, width=2.6):
    """A pen that went over the line twice, the second pass slightly off."""
    return (stroke_g(uid, f'<path d="{path}"/>', color, width, "pen")
            + stroke_g(uid, f'<path d="{path}" transform="translate(0.9,0.7)"/>',
                       color, width * 0.8, "pen2", 0.4))


SE_FORMULA = "SE = &#963;&#8730;<tspan dx=\"-7\">(2/n)</tspan>"


# =========================================================================
#  Figure 1 -- the main diagram
# =========================================================================
def main_figure():
    uid, W, H = "pw", 880, 578
    BASE, HGT, SD = 400.0, 232.0, 70.0
    MU0, MU1 = 300.0, 520.0
    CRIT = MU0 + 1.96 * SD          # the 5% decision rule, in SE units

    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="{uid}-t {uid}-d" class="sketch-svg">',
         f'<title id="{uid}-t">Two overlapping bell curves, hand-drawn on an eggshell sheet</title>',
         f'<desc id="{uid}-d">The horizontal axis is every difference-in-means the experiment '
         'could return. The left purple curve is the spread of results you would get if the '
         'treatment does nothing, centred on zero; the right green curve is the spread if it '
         'has its true effect. Both curves are the same width, and that width is the standard '
         'error, sigma times the square root of two over n. A dashed red line stands 1.96 '
         'standard errors right of zero: anything to the right of it gets called significant. '
         'The thin red-hatched sliver of the purple curve past that line is alpha, the false '
         'positives. The large green-hatched area of the right curve past the line is power. '
         'The part of the green curve left of the line is beta, the real effects that get missed.</desc>',
         defs(uid), paper(uid, W, H)]

    # -- clip regions: each curve's area, and the two sides of the rule -----
    s.append(f'''<clipPath id="{uid}-cNull"><path d="{gauss_area(MU0, SD, BASE, HGT)}"/></clipPath>
<clipPath id="{uid}-cReal"><path d="{gauss_area(MU1, SD, BASE, HGT)}"/></clipPath>
<clipPath id="{uid}-cRight"><rect x="{CRIT}" y="0" width="{W - CRIT}" height="{BASE}"/></clipPath>
<clipPath id="{uid}-cLeft"><rect x="0" y="0" width="{CRIT}" height="{BASE}"/></clipPath>''')

    # -- shaded regions: power, alpha, and the quiet beta ------------------
    s.append(f'<g clip-path="url(#{uid}-cReal)"><g clip-path="url(#{uid}-cRight)">'
             + hatch(uid, CRIT - 20, BASE - HGT, MU1 + 260, BASE, 10, GREEN, 1.15, 0.5) + '</g></g>')
    s.append(f'<g clip-path="url(#{uid}-cReal)"><g clip-path="url(#{uid}-cLeft)">'
             + hatch(uid, MU1 - 260, BASE - HGT, CRIT + 20, BASE, 14, GHOST, 1.0, 0.5) + '</g></g>')
    s.append(f'<g clip-path="url(#{uid}-cNull)"><g clip-path="url(#{uid}-cRight)">'
             + hatch(uid, CRIT - 20, BASE - HGT, MU0 + 250, BASE, 6, RED, 1.15, 0.8) + '</g></g>')

    # -- axis and ticks -----------------------------------------------------
    s.append(stroke_g(uid, f'<path d="M 52,{BASE} L 834,{BASE}" marker-end="url(#{uid}-ai)"/>', INK, 2.0))
    s.append(stroke_g(uid, f'<path d="M {MU0},{BASE-1} L {MU0},{BASE+11}"/>'
                           f'<path d="M {MU1},{BASE-1} L {MU1},{BASE+11}"/>', INK, 1.8))

    # -- the two curves -----------------------------------------------------
    s.append(double_stroke(uid, polyline(gauss_pts(MU0, SD, BASE, HGT)), PURPLE, 2.9))
    s.append(double_stroke(uid, polyline(gauss_pts(MU1, SD, BASE, HGT)), GREEN, 2.9))

    # -- the decision rule, with a leader up to its label -------------------
    s.append(stroke_g(uid, f'<path d="M {CRIT},{BASE+6} L {CRIT},98"/>', RED, 2.6, "pen", 1, "11 9"))
    s.append(stroke_g(uid, f'<path d="M {CRIT},94 C {CRIT+8},86 {CRIT+18},80 {CRIT+30},76"/>', RED, 1.6))
    s.append(hand(CRIT + 36, 50, "the decision rule", RED, 25))
    s.append(hand(CRIT + 36, 72, "anything right of here,", RED, 18, weight=500))
    s.append(hand(CRIT + 36, 90, "you call it significant", RED, 18, weight=500))

    # -- curve labels -------------------------------------------------------
    s.append(hand(190, 66, "if the null is true", PURPLE, 27, "middle"))
    s.append(hand(190, 88, "(the treatment does nothing)", PURPLE, 19, "middle", 500))
    s.append(stroke_g(uid, f'<path d="M 200,100 C 214,144 228,196 238,242" '
                           f'marker-end="url(#{uid}-ap)"/>', PURPLE, 1.7))
    s.append(hand(660, 208, "if the effect is real", GREEN, 27, "middle"))
    s.append(stroke_g(uid, f'<path d="M 618,216 C 600,228 596,236 592,246" '
                           f'marker-end="url(#{uid}-ag)"/>', GREEN, 1.7))

    # -- region callouts ----------------------------------------------------
    s.append(hand(CRIT + 66, 322, "POWER", GREEN, 31))
    s.append(hand(CRIT + 66, 345, "the real wins you actually catch", GREEN, 18, weight=500))
    s.append(hand(316, 296, "&#946;", GHOST_2, 31, "middle"))
    s.append(hand(316, 318, "the real effects", GHOST_2, 18, "middle", 500))
    s.append(hand(316, 336, "you miss", GHOST_2, 18, "middle", 500))
    s.append(stroke_g(uid, f'<path d="M 330,346 C 352,362 372,374 392,384" '
                           f'marker-end="url(#{uid}-ah)"/>', GHOST, 1.6))

    # -- below the axis, kept to strict rows so nothing collides ------------
    s.append(hand(MU0, 425, "0", INK, 22, "middle"))
    s.append(hand(MU0, 444, "no difference", INK_2, 18, "middle", 500))
    s.append(hand(MU1 + 14, 425, "the true effect", GREEN, 20))

    s.append(hand(474, 454, "&#945; &#8212; the false positives you agree to accept", RED, 20))
    s.append(stroke_g(uid, f'<path d="M 470,447 C 458,433 450,414 {CRIT+7},398" '
                           f'marker-end="url(#{uid}-ar)"/>', RED, 1.7))

    s.append(stroke_g(uid, f'<path d="M {MU0},486 L {CRIT},486" marker-start="url(#{uid}-ab)" '
                           f'marker-end="url(#{uid}-ab)"/>'
                           f'<path d="M {MU0},478 L {MU0},494"/><path d="M {CRIT},478 L {CRIT},494"/>', BLUE, 1.6))
    s.append(hand((MU0 + CRIT) / 2, 478, "1.96 &#215; SE", BLUE, 21, "middle"))

    # -- margin note: the one fact the whole picture hangs on ---------------
    s.append(hand(832, 512, "both curves are the same width &#8212;", BLUE, 22, "end"))
    s.append(hand(832, 544, f"and that width is {SE_FORMULA}", BLUE, 28, "end"))
    s.append(stroke_g(uid, '<path d="M 506,554 C 570,560 640,549 700,556 C 750,562 792,552 832,556"/>',
                      BLUE, 1.5, "pen2"))

    s.append(hand(250, 526, "every difference-in-means you could observe &#8594;", INK_2, 21, "middle", 500))

    s.append("</svg>")
    return "".join(s)


# =========================================================================
#  Figure 2 -- the four levers, as four small panels on one sheet
# =========================================================================
def levers_figure():
    uid, W, H = "lv", 880, 508
    PW, PH, ROW = 440, 242, 248
    s = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-labelledby="{uid}-t {uid}-d" class="sketch-svg">',
         f'<title id="{uid}-t">Four small sketches: what each lever does to the picture</title>',
         f'<desc id="{uid}-d">Four panels redraw the same two curves with one thing changed, '
         'leaving the previous version as a faint pencil trace. One: raising sample size '
         'narrows both curves and pulls the decision line in toward zero, so power rises. '
         'Two: a bigger true effect slides the right curve further right while both widths '
         'stay the same, so power rises. Three: raising alpha from 0.05 to 0.10 slides the '
         'decision line left from 1.96 to 1.645 standard errors, so power rises, but more of '
         'the null curve clears the line as well. Four: a noisier metric widens both curves '
         'and pushes the line further out, so the same true effect becomes less detectable.</desc>',
         defs(uid), paper(uid, W, H)]

    panels = [
        # title, note, verdict, verdict colour, sd, mu1, k, ghost sd, ghost mu1, ghost k
        ("sample size &#8593;", "n sits in the denominator of SE", "power &#8593;", GREEN,
         17.0, 208.0, 1.96, 27.0, 208.0, 1.96),
        ("effect size &#8593;", "same widths &#8212; they just separate", "power &#8593;", GREEN,
         27.0, 236.0, 1.96, 27.0, 190.0, 1.96),
        ("&#945;: 0.05 &#8594; 0.10", "the rule itself moves, not the curves", "power &#8593;, but&#8230;", RED,
         27.0, 208.0, 1.645, 27.0, 208.0, 1.96),
        ("variance &#8593;", "&#963; sits in the numerator of SE", "power &#8595;", RED,
         37.0, 208.0, 1.96, 27.0, 208.0, 1.96),
    ]

    for i, (title, note, verdict, vcol, sd, mu1, k, gsd, gmu1, gk) in enumerate(panels):
        ox, oy = 12 + (i % 2) * PW, 6 + (i // 2) * ROW
        base, hgt, mu0 = 196.0, 92.0, 118.0
        crit, gcrit = mu0 + k * sd, mu0 + gk * gsd
        s.append(f'<g transform="translate({ox},{oy})">')

        s.append(hand(20, 42, f"{i+1}. {title}", INK, 26))
        s.append(hand(20, 63, note, INK_2, 18, weight=500))
        s.append(hand(PW - 26, 42, verdict, vcol, 26, "end"))

        # the faint pencil trace of what we are changing away from
        s.append(stroke_g(uid, f'<path d="{polyline(gauss_pts(mu0, gsd, base, hgt))}"/>'
                               f'<path d="{polyline(gauss_pts(gmu1, gsd, base, hgt))}"/>',
                          GHOST, 1.9, "pen2", 0.6))
        s.append(stroke_g(uid, f'<path d="M {gcrit},{base+4} L {gcrit},100"/>',
                          GHOST, 1.6, "pen2", 0.6, "7 6"))

        # power and alpha regions of the new picture
        s.append(f'<clipPath id="{uid}-r{i}"><path d="{gauss_area(mu1, sd, base, hgt)}"/></clipPath>'
                 f'<clipPath id="{uid}-n{i}"><path d="{gauss_area(mu0, sd, base, hgt)}"/></clipPath>'
                 f'<clipPath id="{uid}-x{i}"><rect x="{crit}" y="0" width="{PW - crit}" height="{base}"/></clipPath>')
        s.append(f'<g clip-path="url(#{uid}-r{i})"><g clip-path="url(#{uid}-x{i})">'
                 + hatch(uid, crit - 14, base - hgt, mu1 + 150, base, 9, GREEN, 1.05, 0.5) + '</g></g>')
        s.append(f'<g clip-path="url(#{uid}-n{i})"><g clip-path="url(#{uid}-x{i})">'
                 + hatch(uid, crit - 14, base - hgt, mu0 + 140, base, 5, RED, 1.05, 0.85) + '</g></g>')

        # axis and the new curves
        s.append(stroke_g(uid, f'<path d="M 26,{base} L {PW-24},{base}"/>', INK, 1.8))
        s.append(double_stroke(uid, polyline(gauss_pts(mu0, sd, base, hgt)), PURPLE, 2.4))
        s.append(double_stroke(uid, polyline(gauss_pts(mu1, sd, base, hgt)), GREEN, 2.4))
        s.append(stroke_g(uid, f'<path d="M {crit},{base+4} L {crit},96"/>', RED, 2.2, "pen", 1, "9 7"))

        # the movement arrows -- what actually changed
        if i == 0:
            s.append(stroke_g(uid, f'<path d="M {mu0-50},116 L {mu0-20},116" marker-end="url(#{uid}-ab)"/>'
                                   f'<path d="M {mu0+50},116 L {mu0+20},116" marker-end="url(#{uid}-ab)"/>', BLUE, 1.6))
            s.append(hand(PW - 26, 86, "narrower curves, and the line comes in", BLUE, 19, "end"))
        elif i == 1:
            s.append(stroke_g(uid, f'<path d="M {gmu1+16},116 L {mu1-12},116" marker-end="url(#{uid}-ab)"/>', BLUE, 1.6))
            s.append(hand(PW - 26, 86, "the whole curve slides right", BLUE, 19, "end"))
        elif i == 2:
            s.append(stroke_g(uid, f'<path d="M {gcrit-4},116 L {crit+8},116" marker-end="url(#{uid}-ab)"/>', BLUE, 1.6))
            s.append(hand(PW - 26, 86, "1.96 SE &#8594; 1.645 SE", BLUE, 19, "end"))
            s.append(hand(PW - 26, 63, "&#8230; and more &#945; with it", RED, 18, "end", 500))
        else:
            s.append(stroke_g(uid, f'<path d="M {mu0-22},116 L {mu0-56},116" marker-end="url(#{uid}-ab)"/>'
                                   f'<path d="M {mu0+22},116 L {mu0+56},116" marker-end="url(#{uid}-ab)"/>', BLUE, 1.6))
            s.append(hand(PW - 26, 86, "both spread out, the line pushes away", BLUE, 19, "end"))

        s.append(hand(mu0, base + 22, "0", INK_2, 19, "middle"))
        s.append("</g>")

    # creases in the sheet, standing in for panel dividers
    s.append(stroke_g(uid, f'<path d="M {W/2},26 L {W/2},{H-24}"/>'
                           f'<path d="M 30,{ROW} L {W-30},{ROW}"/>', "#cfc5aa", 1.2, "pen2", 0.9))
    s.append("</svg>")
    return "".join(s)


HEADER = """{%- comment -%}
  Hand-drawn statistical-power sketch. GENERATED by tools/gen_sketch.py -- the
  curves are real Gaussians, so change the generator and re-run it rather than
  nudging coordinates in here:

      python3 tools/gen_sketch.py _includes

  Pens: purple = null, green = true effect, red = the decision rule and the error
  you accept, blue = measurements, pencil grey = the version being changed away from.
{%- endcomment -%}
"""

if __name__ == "__main__":
    import sys
    out = sys.argv[1]
    for name, fn in (("diagram-power-curves", main_figure), ("diagram-power-levers", levers_figure)):
        with open(f"{out}/{name}.html", "w") as f:
            f.write(HEADER + fn() + "\n")
    print("wrote includes to", out)

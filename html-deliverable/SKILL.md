---
name: html-deliverable
description: Produce polished, self-contained HTML pages as deliverables — explainers, implementation plans, code-review writeups, dashboards, design-option grids, and interactive editors (sliders, draggable cards, form editors with copy/export buttons). Builds on the prompt patterns from Anthropic's "unreasonable effectiveness of HTML" blog and enforces WCAG color contrast so text is always readable. Use when the user asks for an HTML page/file/artifact to explain, plan, review, compare, report, or interactively edit something — or whenever a visual HTML output would communicate better than plain markdown or terminal text.
---

# HTML Deliverable

Turn a request into a single, readable, self-contained HTML page. The premise (from the
[blog](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html)):
HTML is a high-bandwidth medium for plans, reviews, explainers, and small tools — far richer
than markdown, and cheap to produce. Pick the right *archetype*, fill it with real content,
and never ship unreadable contrast.

## Workflow

1. **Identify the archetype.** Match the request to one of the patterns in
   [PATTERNS.md](PATTERNS.md) (explainer, implementation plan, code review, design-option grid,
   report/research, interactive editor). Each has a ready-made structure and a recommended prompt
   shape. When the user is exploring and unsure, default to the **6-option grid** so they can choose.
2. **Plan the visual identity.** If the `artifact-design` skill is available, invoke it first for
   palette/type/layout calibration. Otherwise pick a 4–6 color palette + 2 type roles grounded in
   the subject — not the generic cream/serif/terracotta default.
3. **Write the page** to a `.html` file with real content (never lorem). Follow the Hard Rules below.
4. **Check contrast — required, not optional.** Run the checker on every text/background pair you
   used (see below). Fix anything below AA before showing the user. This is the step that most often
   gets skipped and produces "I can't read this."
5. **Deliver.** If publishing as an Artifact, write page content only (no `<html>/<head>/<body>` —
   those are added at publish time). Otherwise hand over the standalone file.

## Hard rules

- **Contrast (the #1 failure):** body text ≥ **4.5:1**, large text (≥24px / ≥18.66px bold) ≥ **3.0:1**,
  UI borders/icons ≥ **3.0:1**. Aim for AAA (7:1) on body text where you can. Muted greys are the usual
  offenders — a "subtle" `#8595a0` on white is only 3.09:1 and **fails**. Verify, don't eyeball.
- **Self-contained:** inline all CSS/JS; no external fonts/CDNs/images (Artifact CSP blocks them).
  Embed assets as data URIs. Use strong system font stacks rather than risking a silent webfont fallback.
- **Responsive:** relative units, flex/grid + `gap`, `max-width:100%` on media. Wide content (tables,
  code, diagrams) goes in its own `overflow-x:auto` container so the page body never scrolls sideways.
- **Real interactivity earns its keep:** copy/export buttons ("copy as Markdown/JSON/prompt"), live
  re-render, draggable cards, sliders — include them when the archetype calls for it (see PATTERNS.md).
- **Accessible & clean:** visible keyboard focus, `prefers-reduced-motion` guard on any animation,
  semantic structure, double-quoted attributes, every non-void element closed.

## Checking contrast

Run the bundled script on each pair (foreground, background). It exits non-zero if any pair fails AA,
so it can gate the deliverable:

```bash
# pairs as "fg/bg", or as alternating args; add --large for big/bold text
python3 scripts/contrast.py "#1f2d3a/#f4f6f7" "#5c6b76/#f4f6f7" "#9fb6c2/#13283c"
python3 scripts/contrast.py --large "#8595a0" "#ffffff"
```

When a pair fails: darken the foreground (or lighten the background) and re-run until it passes —
don't reach for a different hue, just push lightness until the ratio clears.

## Reference

- [PATTERNS.md](PATTERNS.md) — the page archetypes, their structures, and copy-ready prompt shapes
  drawn from the blog.
- `scripts/contrast.py` — WCAG contrast checker (deterministic; use it every time).

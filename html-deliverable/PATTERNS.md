# HTML Deliverable — Archetypes & Prompt Patterns

The six page archetypes from the "unreasonable effectiveness of HTML" blog. Each lists **when to
use it**, the **structure** to build, and a **prompt shape** you can lift verbatim or adapt. All
archetypes obey the Hard Rules in SKILL.md (contrast, self-contained, responsive).

---

## 1. Design-option grid (the default when the user is exploring)

**Use when** the user hasn't settled on a direction, or asks to "see options," or you're unsure
which treatment fits.

**Structure:** one HTML file, CSS grid of 6 cells. Each cell is a distinct mini-treatment varying
layout, tone, and density. Label each with the tradeoff it makes.

**Prompt shape:**
> "Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as
> a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's
> making."

---

## 2. Explainer / research synthesis

**Use when** teaching a codebase, concept, or system — onboarding docs, "explain this to me," learning.

**Structure:** hero thesis → diagram of the flow (SVG/HTML, not just prose) → 3–4 key code snippets,
annotated → a "gotchas" section. Navigation tabs or internal links if long. Information-dense but
hierarchical.

**Prompt shape:**
> "Read the relevant code and produce a single HTML explainer page: a diagram of the [X] flow, the
> 3–4 key code snippets annotated, and a 'gotchas' section."

---

## 3. Implementation plan / spec

**Use when** proposing how to build something before building it; handoff to a later session.

**Structure:** easy-to-digest sections, UI **mockups**, a **data-flow** diagram, and the **code
snippets** worth reviewing inline. Optimize for skim-then-deep-read.

**Prompt shape:**
> "Create a thorough implementation plan in an HTML file. Make some mockups, show data flow, and add
> important code snippets I might want to review. Make it easy to read and digest."

**Multi-file workflow:** explorations → mockups → this plan as a separate HTML doc → hand the
collected files to a fresh session for implementation; verification agents read all reference files.

---

## 4. Code-review / PR writeup

**Use when** explaining or reviewing a diff.

**Structure:** render the actual diff with **inline margin annotations**; **color-code findings by
severity** (use semantic colors distinct from the accent — and verify their contrast). Summary of
findings up top, detail below.

**Prompt shape:**
> "Help me review this PR by creating an HTML artifact that describes it. Render the actual diff with
> inline margin annotations, and color-code findings by severity."

---

## 5. Report / research / dashboard

**Use when** presenting findings, status, metrics, or a scorecard.

**Structure:** summary before detail; encode state in *form* (pill, chip, severity stripe), not just
number, so what needs attention reads at a glance. Tables get `overflow-x:auto` + `tabular-nums`.
Sparklines/charts get the same care as type (area fill, faint grid, emphasized endpoint).

**Prompt shape:**
> "Produce a single HTML report: summary scorecard at the top with status pills, then the detail in
> sortable/scannable tables. Color-code by status."

---

## 6. Interactive editor / tool (HTML + JS)

**Use when** the user wants to *try* things or *manipulate* data, not just read.

**Structures & prompt shapes — pick the one that fits:**

- **Parameter playground (sliders):**
  > "Create an HTML file with sliders and options to try different settings on this [animation/config].
  > Give me a copy button to copy the parameters that worked well."

- **Draggable cards (prioritization/kanban):**
  > "Make an HTML file with each [ticket] as a draggable card across Now / Next / Later / Cut columns.
  > Add a 'copy as Markdown' button that exports the final ordering."

- **Form-based config editor (with dependency awareness):**
  > "Build a form-based editor for this config. Group flags by area, show dependencies between them,
  > warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button."

- **Live template / prompt tuner (side-by-side):**
  > "Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, and
  > sample inputs on the right that re-render the filled template live."

**Common ingredient:** an **export/copy button** — "copy as JSON / prompt / Markdown / diff." Almost
every interactive deliverable should let the user get their result back out.

---

## Toolbox (techniques worth reaching for)

- **Density:** HTML tables, CSS-styled data, **SVG** diagrams/illustrations, syntax-highlighted code,
  workflow visualizations (SVG+HTML), spatial layouts (absolute positioning / canvas).
- **Readability:** clear visual hierarchy, navigation tabs, mobile-responsive layout, supporting
  illustrations, internal links for long docs.
- **Interaction:** export buttons, sliders/knobs, draggable cards, form editors with live preview,
  real-time template re-rendering.

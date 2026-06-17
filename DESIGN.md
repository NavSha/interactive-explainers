---
name: AI for Builders
description: Interactive guides for builders shipping AI products — editorial craft meets hands-on widgets
colors:
  warm-paper: "#FAF8F5"
  page-white: "#FFFFFF"
  ink: "#1A1A1A"
  quiet-gray: "#6B6B6B"
  hairline: "#E8E6E2"
  hairline-light: "#F0EEEA"
  code-wash: "#F3F0EC"
  agents-blue: "#2563EB"
  agents-wash: "#EFF6FF"
  cost-amber: "#D97706"
  cost-wash: "#FFFBEB"
  eval-green: "#059669"
  eval-wash: "#ECFDF5"
  context-violet: "#7C3AED"
  context-wash: "#F5F3FF"
  llm-slate: "#475569"
  llm-wash: "#F1F5F9"
  grounding-rose: "#E11D48"
  grounding-wash: "#FFF1F2"
  ux-indigo: "#4F46E5"
  ux-wash: "#EEF2FF"
  vibe-teal: "#0D9488"
  vibe-wash: "#F0FDFA"
typography:
  display:
    fontFamily: "Newsreader, Georgia, 'Times New Roman', serif"
    fontSize: "3rem"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Newsreader, Georgia, 'Times New Roman', serif"
    fontSize: "2.25rem"
    fontWeight: 600
    lineHeight: 1.25
  title:
    fontFamily: "Newsreader, Georgia, 'Times New Roman', serif"
    fontSize: "1.375rem"
    fontWeight: 600
    lineHeight: 1.25
  body:
    fontFamily: "Newsreader, Georgia, 'Times New Roman', serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.7
  ui:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 500
    lineHeight: 1.5
  label:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.08em"
  code:
    fontFamily: "'JetBrains Mono', 'SF Mono', 'Fira Code', monospace"
    fontSize: "0.9em"
rounded:
  control: "8px"
  surface: "12px"
  pill: "12px"
  code: "4px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "64px"
  section: "80px"
components:
  button-primary:
    backgroundColor: "{colors.agents-blue}"
    textColor: "#FFFFFF"
    typography: "{typography.ui}"
    rounded: "{rounded.control}"
    padding: "8px 16px"
  button-secondary:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.control}"
    padding: "8px 16px"
  widget:
    backgroundColor: "{colors.agents-wash}"
    rounded: "{rounded.surface}"
    padding: "32px"
  topic-card:
    backgroundColor: "{colors.page-white}"
    rounded: "{rounded.surface}"
  callout-insight:
    backgroundColor: "{colors.agents-wash}"
    textColor: "{colors.ink}"
    padding: "24px"
  chip:
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "2px 10px"
---

# Design System: AI for Builders

## 1. Overview

**Creative North Star: "The Builder's Field Guide"**

This is a crafted manual you take into the field — editorial authority in the prose, practical interactivity in the widgets, built to be used, not admired. The reading surface is a warm paper ground (#FAF8F5) carrying serif long-form text at a comfortable 760px measure; the working surfaces (widgets, quizzes, simulations) sit inside it as tinted panels where the reader stops reading and starts doing. The voice is a sharp practitioner explaining things over coffee: confident, a little playful (every article opens with a 4-bar rap-verse epigraph), never academic.

The system explicitly rejects corporate docs-site utility (GitBook/Docusaurus sidebar energy), AI-hype marketing aesthetics (purple glow, gradient excess), and textbook density. It is one publication with eight accents: each topic series carries its own saturated accent color, but the serif/sans typographic system, the paper ground, and the hairline-border surface logic keep the whole site reading as a single crafted object.

**Key Characteristics:**
- Serif prose for reading, sans for UI chrome and instruction, mono for code and tool-call data
- Warm paper ground; pure white panels; hairline borders define structure
- Eight per-topic accent colors used as identity, never as semantics
- Flat at rest — shadow appears only as a response to hover or focus
- Widgets are the argument: interactive panels are visually distinct "do" zones inside "read" flow
- Quietly tactile: 150ms ease-out transitions, 1px hover lifts, restrained feedback

## 2. Colors

A warm-neutral reading ground with one saturated accent per topic series — restrained on any single page, polychrome across the site.

### Primary
- **Topic Accents** — eight saturated hues, one per series, each with a matching pale wash for widget and callout backgrounds:
  - **Agents Blue** (#2563EB / wash #EFF6FF): Agents & Tool Use; also the site-wide default link and interaction color.
  - **Cost Amber** (#D97706 / wash #FFFBEB): Cost & Latency; doubles as the summary-callout accent.
  - **Eval Green** (#059669 / wash #ECFDF5): Evaluation & Testing; doubles as the Builder Tip callout and "correct" state.
  - **Context Violet** (#7C3AED / wash #F5F3FF): Context Windows & Memory; doubles as the analogy-callout accent.
  - **LLM Slate** (#475569 / wash #F1F5F9): How LLMs Work.
  - **Grounding Rose** (#E11D48 / wash #FFF1F2): Grounding & Guardrails.
  - **UX Indigo** (#4F46E5 / wash #EEF2FF): AI UX & Human-in-the-Loop.
  - **Vibe Teal** (#0D9488 / wash #F0FDFA): Vibe Coding.
- Each accent also has a 135° gradient variant used **only** in article-hero banners and topic-card banners — never in body content, buttons, or text.

### Neutral
- **Warm Paper** (#FAF8F5): the body background everywhere. The site's "page".
- **Page White** (#FFFFFF): raised panels — cards, chat areas, quiz cards, canvas wraps.
- **Ink** (#1A1A1A): all reading text and headings.
- **Quiet Gray** (#6B6B6B): secondary text — metadata, instructions, captions. UI-scale text only; never long-form body copy.
- **Hairline** (#E8E6E2) / **Hairline Light** (#F0EEEA): borders and dividers. Structure is drawn with these, not with shadows.
- **Code Wash** (#F3F0EC): inline code background and assistant chat bubbles.

### Named Rules
**The One Accent Per Page Rule.** A page lives inside one topic and uses that topic's accent for its links, widget labels, buttons, and hero. Accents never mix within a page (callout colors are the one sanctioned exception — they are a fixed semantic set).
**The Identity-Not-Semantics Rule.** Topic accents say "where you are," never "what this means." Meaning (correct/incorrect, warning) uses the fixed green/red feedback pair (#059669 / #DC2626) regardless of topic.
**The Gradient Quarantine Rule.** Gradients exist only in hero and card banners. A gradient on text, a button, or a background panel is forbidden.

## 3. Typography

**Display Font:** Newsreader (with Georgia fallback)
**Body Font:** Newsreader — the prose itself is serif
**UI Font:** Inter (with system-ui fallback)
**Mono Font:** JetBrains Mono (with SF Mono / Fira Code fallback)

**Character:** A bookish serif carries the authority and warmth of the writing; a neutral sans handles everything operational (buttons, labels, instructions, metadata); mono appears wherever the machine speaks (code, tool calls, token counts). The reader always knows which register they're in by the typeface alone.

### Hierarchy
- **Display** (600, 3rem, 1.25, -0.02em): article and page titles. Drops to 1.875rem at ≤480px.
- **Headline** (600, 2.25rem, 1.25): h2 section headings, paired with a faded serif section number.
- **Title** (600, 1.375–1.75rem, 1.25): h3 subheads, widget titles, part-list titles.
- **Body** (400, 1.125rem, 1.7): serif prose at a max 760px measure (~70ch). Leads are 1.375rem in Quiet Gray.
- **UI** (500, 0.875rem, 1.5): Inter — buttons, instructions, descriptions, nav, table cells.
- **Label** (600, 0.75rem, 0.08em tracking, uppercase): widget labels, callout labels, TOC title, table headers. The one sanctioned uppercase-tracked element family.
- **Code** (0.9em, JetBrains Mono): inline code on Code Wash, 4px radius; tool-call/result chat bubbles.

### Named Rules
**The Three Voices Rule.** Serif = the author reading to you. Sans = the interface talking to you. Mono = the machine output. Never swap voices: no serif buttons, no sans prose paragraphs, no mono as decoration.
**The Epigraph Rule.** Every article opens with an original 4-bar verse — centered, italic serif, Quiet Gray, line-height 2, under a 40px hairline tick. This is a deliberate brand system, not optional decoration.

## 4. Elevation

Flat by default. Structure is drawn with hairline borders (#E8E6E2) and background tints, not shadows. Shadow exists in exactly one role: a response to hover intent. Topic cards lift 4px and gain a soft, wide shadow; buttons lift 1px with a slight brightness shift. Nothing casts a shadow at rest.

### Shadow Vocabulary
- **Hover Lift** (`box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08)` + `transform: translateY(-4px)`): topic cards on hover only.
- **Button Lift** (`transform: translateY(-1px)` + `filter: brightness(1.1)`): primary buttons on hover; no box-shadow.

### Named Rules
**The Flat-By-Default Rule.** Surfaces are flat at rest. Shadow is a response to intent (hover, focus), never decoration. If a resting element has a shadow, it's a bug.

## 5. Components

Quietly tactile: subtle lift on hover, fast 150ms ease-out transitions, restrained color. The interactivity invites without shouting.

### Buttons
- **Shape:** gently rounded (8px radius), inline-flex with 8px gap for icons.
- **Primary:** topic accent background, white text, Inter 0.875rem/500, 8px 16px padding.
- **Hover:** brightness(1.1) + 1px lift, 150ms `cubic-bezier(0.16, 1, 0.3, 1)`.
- **Secondary:** Page White with hairline border; hover recolors border and text to the topic accent.
- **States:** `--active` fills with accent; `--correct` (#059669) and `--incorrect` (#DC2626) for quiz feedback; disabled at 40% opacity.

### Widgets (signature component)
- The site's defining pattern: an interactive panel between prose sections where the reader stops reading and starts doing.
- **Container:** topic wash background, 1px tinted border, 12px radius, 32px padding (16px at ≤480px), 40px vertical margin.
- **Anatomy:** uppercase Label in topic accent → serif Title → sans Instruction in Quiet Gray → the interactive body (canvas, chat, controls) → optional annotation.
- **Inner surfaces** (chat areas, quiz cards, canvas wraps): Page White, hairline border, 8px radius — a white "instrument" inside the tinted panel.

### Callouts
- Fixed four-type semantic set, each on its wash with a 4px accent edge and rounded right corners: **Insight** (Agents Blue), **Analogy** (Context Violet), **Builder Tip** (Eval Green), **Summary** (Cost Amber).
- Uppercase label in the accent, sans body in Ink. These keep their colors on every page regardless of topic — they are semantics, not identity.

### Cards / Containers
- **Topic cards:** Page White, hairline border, 12px radius, gradient banner (label + serif title + parts count in white) over a body with sans description and pill tags. Hover Lift per Elevation.
- **Part lists:** borderless rows with hairline dividers, mono part numbers in topic accent, serif titles; hover tints the row with the topic wash.

### Chips / Tags
- Pill-shaped (12px radius), 2px 10px padding, 0.75rem sans. Topic-tinted on cards; badge variants (accent-filled, white-outlined) in agent widgets.

### Tables
- "Tier table" pattern: uppercase tracked sans headers over a 2px hairline rule, generous 16px cell padding, hairline row dividers, topic-wash row hover. No outer border, no zebra striping.

### Navigation
- **Breadcrumbs:** small sans in Quiet Gray, accent on hover; white variant over hero gradients.
- **Article nav:** prev/next sans links across a top hairline; locked items at 50% opacity.
- **TOC:** uppercase tracked label over a serif-numbered list with faded numerals; links darken to accent on hover.

## 6. Do's and Don'ts

### Do:
- **Do** keep prose serif at the 760px measure with 1.7 line-height; the reading experience is the product.
- **Do** give every new series its own accent + wash pair and use it consistently across that series' hero, links, widgets, and buttons.
- **Do** make widgets keyboard-operable with a `prefers-reduced-motion` alternative for every animation — WCAG AA is the floor (body text ≥4.5:1).
- **Do** draw structure with hairline borders and background tints; reserve shadow for hover (The Flat-By-Default Rule).
- **Do** use the fixed callout set (Insight / Analogy / Builder Tip / Summary) with their fixed colors on every page.
- **Do** bump the `?v=N` cache-buster in every HTML file whenever `shared.css` changes.

### Don't:
- **Don't** drift toward **corporate docs sites** (GitBook / Docusaurus / ReadTheDocs sidebar-docs energy with no voice) — no persistent sidebars, no utility-first chrome.
- **Don't** touch **AI-hype landing page** aesthetics: no purple-glow gradients on text or buttons, no glassmorphism, no "unlock the power of AI" energy. Gradients stay quarantined in hero/card banners.
- **Don't** go **academic/textbook**: no dense citation blocks, no dry intimidating walls of text; keep the confident-conversational register.
- **Don't** use Quiet Gray (#6B6B6B) for long-form body copy or on tinted washes without checking 4.5:1 contrast — it is a UI-scale secondary color only.
- **Don't** mix topic accents within a page (callouts excepted), and never use an accent to carry meaning — color identifies, the green/red pair judges.
- **Don't** put shadows on resting surfaces, gradients on text, or serif type in buttons.
- **Don't** convey information by color alone — pair accents with labels, icons, or text.

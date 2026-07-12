---
type: reflect
generated: 2026-05-16
---

# Reflect — 2026-05-16 (first pass)

Run quarterly or on-demand. Covers: ranked backlog, stance audit, thinnest topic,
unexpected bridge, state of the site.

---

## 1. Top 5 planned articles (ranked by gap severity × reader interest)

### 1. Multi-agent orchestration (`agents`)
**Gap:** The site covers single-agent loops thoroughly but never addresses what
happens when you need agents to coordinate — supervisor/worker patterns, swarms,
handoffs between specialized agents. This is where real-world agent deployments
are heading and builders will face architecture decisions about it imminently.
**Reader interest:** High — anyone who's shipped a single agent immediately asks
"how do I compose them?"

### 2. Evaluating agents / multi-turn (`evaluation`)
**Gap:** Evals in Practice covers single-turn evaluation well, but agent
evaluation is fundamentally different — you're judging trajectories, not outputs.
No article currently helps a builder understand how to eval a 15-step agent workflow.
**Reader interest:** High — directly tied to the "should we ship this agent?" decision.

### 3. LLM-as-judge done right (`evaluation`)
**Gap:** The site mentions LLM-as-judge as a pattern but never unpacks it. This
is the fastest-growing eval approach and builders need to understand when it's valid,
when it's circular, and how to calibrate it.
**Reader interest:** High — practical, immediately actionable.

### 4. Context engineering (`context-windows`)
**Gap:** "Designing for Memory" covers the theory but there's no dedicated piece
on the craft of context engineering — prompt structure, chunking strategy,
what goes in system vs. user messages, managing context across turns. Vibe Coding
Part 2 touches this for code contexts, but the general concept deserves its own article.
**Reader interest:** Medium-high — this is the skill that separates good AI
product implementations from mediocre ones.

### 5. Streaming UX patterns (`ai-ux`)
**Gap:** Streaming appears in Cost & Latency as a performance technique and in
AI UX conceptually, but there's no article on the UX craft — skeleton screens,
progressive rendering, token-by-token vs. chunk reveals, handling errors mid-stream.
**Reader interest:** Medium-high — every builder shipping a chat interface needs this.

**Honorable mentions:** Graph RAG & structured retrieval (grounding), Trust
recovery after failure (ai-ux), Prompt caching & batching (cost-latency).

---

## 2. Stance audit

The site takes several strong positions. Assessment of each:

| Stance | Where | Still defensible? | Notes |
|---|---|---|---|
| "It's prediction all the way down" | llm-fundamentals | **Yes** — still the right mental model for builders, even as reasoning models add chain-of-thought. The underlying mechanism hasn't changed. | Could add nuance about reasoning models (o1/o3-style) in a future article. |
| "Hallucinations are confabulation by design, not a bug" | grounding | **Yes** — reinforced by continued industry experience. No model has "solved" hallucination; mitigation remains the answer. | No update needed. |
| "RAG isn't always the answer" | grounding | **Yes** — if anything, the industry has over-indexed on RAG. Fine-tuning, structured retrieval, and graph RAG are gaining traction as complements. | The planned Graph RAG article would strengthen this stance. |
| "HITL is the practical answer to unreliability" | ai-ux, agents | **Yes, but worth revisiting scope** — as models improve, the automation threshold shifts. The stance should acknowledge that HITL is a *current* practical answer, not necessarily permanent. | Consider a callout in the HITL article about how the threshold moves. |
| "The maintenance trap" in vibe coding | vibe-coding | **Yes** — still widely observed. AI-generated code that nobody understands remains a real risk. | No update needed. |
| "Tool-use reliability drops multiplicatively" | agents | **Yes** — compound failure in agent loops is well-documented. | Consider adding real-world numbers when available. |

**Verdict:** All stances hold. No urgent corrections needed. The biggest gap is
acknowledging reasoning models (o1/o3-style chain-of-thought) as a nuance to the
"prediction all the way down" thesis — not a contradiction, but worth addressing.

---

## 3. Thinnest topic

**By ratio:** All topics with 2 live articles are equally thin (llm-fundamentals,
cost-latency, evaluation, context-windows, ai-ux), but the *gap severity* varies.

**Winner: Evaluation & Testing** — 2 live, 4 planned, and the planned articles
(LLM-as-judge, human eval workflows, production evals, agent evaluation) are all
high-demand topics that builders actively search for. The current 2 articles set up the
framework but leave readers without actionable eval recipes.

**Runner-up: LLM Fundamentals** — 2 live, 4 planned. The planned articles
(tokenization, transformers, pre/post-training, open vs. closed) would complete
the foundation. Less urgent because the current 2 articles cover enough for
downstream topics to make sense.

**Orphan concept load:**
- Evaluation has 2 orphan concepts (non-determinism, prompt injection) — moderate.
- LLM Fundamentals has 5 orphan concepts (embedding, attention, inference, fine-tuning, RLHF) — heavier, but these are partially explained inline.

---

## 4. One unexpected bridge

**Vibe Coding ↔ Evaluation**

Not currently bridged in either topic map, but there's a strong connection: the
question "does this code work?" that vibe coders face is fundamentally an
evaluation question. A builder using Claude Code to build a feature needs to evaluate
AI-generated code the same way they'd evaluate any AI output — is it correct,
is it complete, does it handle edge cases?

This bridge could manifest as:
- A callout in Vibe Coding Part 3 (The Reality Check) linking to eval concepts
- A planned article on "evaluating AI-generated code" that lives in either topic
- A cross-reference in both topic maps

This connection would help readers who arrive via vibe coding (likely the most
accessible entry point) discover the evaluation series.

---

## 5. State of the site

The site is content-complete at its initial scope: 19 articles across 8 topics,
each with interactive widgets, reading progress, capstone quizzes, and consistent
design. The writing voice is established — confident, conversational, dry wit,
rich analogies — and the epigraph tradition (rap verses) gives each article a
distinctive personality. The wiki planning layer now tracks 27 planned articles,
6 themes, and 6 entities, giving the site a clear growth roadmap.

The biggest opportunity is depth, not breadth. The 8 topics cover the right
territory for "AI for Builders," but several (evaluation, LLM fundamentals, AI UX)
have only 2 articles each and leave readers wanting actionable follow-ups. The
next phase should prioritize the top 5 planned articles above, add the
vibe-coding ↔ evaluation bridge, and revisit stances as reasoning models mature.
The site's competitive advantage is its interactive, opinionated, builder-specific
angle — that should be protected as it grows.

---

## Log

- **2026-05-16** — First reflect pass. 19 live articles, 27 planned. All stances
  hold. Thinnest topic: Evaluation. Top priority: multi-agent orchestration.
  Unexpected bridge: vibe-coding ↔ evaluation.

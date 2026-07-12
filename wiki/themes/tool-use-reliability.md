---
type: theme
domains: [agents, evaluation]
first_seen: 2026-05-16
last_updated: 2026-05-16
---

## Summary

When agents call external tools, each call introduces a failure point — wrong parameters, API errors, misinterpreted responses. Compound failure across loops means reliability drops multiplicatively, not additively. The site's position: tool-use reliability is the central engineering challenge of agentic systems.

## Articles mentioning it

- [Tools & Function Calling](../../agents/tools.html)
- [Planning, Failure & Tradeoffs](../../agents/planning.html)
- [The Agent Loop](../../agents/agent-loop.html)
- [Evals in Practice](../../evaluation/evals-in-practice.html)

14 mentions across 4 articles.

## Builder takeaway

A 95% reliable tool called 5 times in a loop gives ~77% end-to-end reliability. Budget for retries, fallbacks, and human escalation in any multi-step agent workflow.

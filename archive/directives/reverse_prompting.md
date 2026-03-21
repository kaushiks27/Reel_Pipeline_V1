# Reverse Prompting — Directive

> Before starting ANY phase, ask 5 clarifying questions. Surface assumptions. Wait for answers. Then proceed.

## When to Apply
- Start of every pipeline phase (1–8)
- Any new non-trivial task
- Any task touching unfamiliar content or tools

## Question Format (for each question)
1. State the assumption you'd make if not asked
2. Ask the question
3. Explain why the answer matters

## Categories to Draw From
- **Scope:** What's in vs. out?
- **Tech choices:** Which tools/settings?
- **Edge cases:** What happens when things break?
- **Performance:** What quality bar / scale?
- **Integration:** What touches this?
- **UX:** What does the audience see?
- **Existing patterns:** Follow or diverge?

## Protocol
1. Generate exactly 5 questions, sorted by impact
2. Present to user
3. Wait for all answers before proceeding
4. If user says "just do it" → list assumptions and proceed
5. If user skips a question → use default assumption and note it

## Experience Accumulation
After each phase, record Q&A to `directives/experience/{domain}.md` for future reference, so future phases need fewer questions.

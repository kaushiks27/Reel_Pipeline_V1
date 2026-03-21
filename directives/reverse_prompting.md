# Reverse Prompting — Directive

> Source: `Reverse Prompting.md` (root)
> Status: Active

## Purpose

Before touching anything, ask the user exactly 5 clarifying questions that would most change your approach. Surface assumptions, let the user disambiguate, then build with high-quality context.

## When to Use

- Any task where you'd normally spend 10+ minutes writing a detailed spec
- Complex features with multiple valid approaches
- Tasks touching unfamiliar parts of the codebase
- Anything where getting it wrong means significant rework

## When NOT to Use

- Trivial tasks ("fix this typo", "add a log line")
- Tasks with extremely detailed specs already provided
- Urgent hotfixes where speed > perfection
- Follow-up tasks where questions were already answered

## Workflow

### Step 1 — Receive the task
Read the user's task. Do NOT start implementing.

### Step 2 — Check for experience docs
- Check `directives/experience/` for prior decisions
- Check `CLAUDE.md` / `AGENTS.md` for conventions
- Check existing code for patterns that answer questions implicitly
- This narrows questions to things NOT already answered.

### Step 3 — Generate 5 questions
Turn your silent assumptions into questions. Prioritize by impact.

**Categories:**
- **Scope** — what's in vs out?
- **Tech choices** — which tools/patterns?
- **Edge cases** — what happens when things break?
- **Performance** — what scale?
- **Integration** — what touches this?
- **UX** — what does the user see?
- **Existing patterns** — follow or diverge?

**Question format (for each):**
1. State the assumption you'd make if not asked
2. Ask the question
3. Explain why the answer matters

```
Q1 (highest impact): Should this be X or Y?
My default assumption: X, because [reason].
Why it matters: Y would require [completely different approach].
```

### Step 4 — Wait for answers
Do NOT proceed until all 5 are answered. If user skips one → use default assumption and note it.

### Step 5 — Record answers
Append Q&A to `directives/experience/{domain}.md`:

```markdown
## {Task Name} — Decisions ({date})

Q: {question}
A: {user's answer}
Rationale: {why this matters for future tasks}
```

### Step 6 — Proceed with implementation
Reference user's answers as requirements. If a new assumption surfaces during implementation → pause and ask, don't silently decide.

## Accumulated Experience Flywheel

For repeat domains:
1. Read `directives/experience/{domain}.md` for past decisions
2. Ask 5 questions NOT already answered by experience doc
3. After answers, append to experience doc
4. Then implement

Each task adds context → future tasks need fewer questions → better output.

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| question_count | 5 | Questions to ask (3–7 range) |
| experience_doc | none | Path to experience doc |
| priority_order | impact | Sort by implementation impact |

## Edge Cases & Learnings

- **User says "just do it"**: Respect it. List assumptions as a comment, proceed.
- **All questions answered by context**: Skip to implementation. Note you reviewed and found no ambiguities.
- **User answers are contradictory**: Flag the contradiction, ask one follow-up.
- **Task changes after questions**: Re-assess answers, ask 1–2 new questions if scope shifted.

---

*Self-annealing: append new learnings below as they are discovered.*

# Prompt Contracts — Directive

> Source: `Prompt Contracts.md` (root)
> Status: Active

## Purpose

Before implementation, define a 4-part contract: **GOAL**, **CONSTRAINTS**, **FORMAT**, **FAILURE**. Treat it as an engineering spec with zero ambiguity about what "done" means.

## When to Use

- Infrastructure code (rate limiters, caches, queues)
- API endpoints and services
- Anything hard to fix later
- Tasks where quality > speed
- Preventing "it technically works but…" outcomes

## When NOT to Use

- Quick prototypes ("just get something working")
- Exploratory tasks where requirements are still forming
- Trivial changes where a contract would be more text than the code itself

## Workflow

### Step 1 — Receive the task
- If the user provides a contract → parse it into 4 sections, go to Step 3.
- If the user provides a plain task → help convert it (Step 2).

### Step 2 — Generate the contract

```markdown
## Contract

GOAL: [Measurable success metric]

CONSTRAINTS:
- [Hard limit 1]
- [Hard limit 2]
- [Hard limit 3]

FORMAT:
- [Exact output shape — files, structure]
- [File naming and organization]
- [Includes — types, tests, docs]

FAILURE (any of these = not done):
- [Failure condition 1]
- [Failure condition 2]
- [Edge case that must be handled]
- [Quality bar that must be met]
```

**GOAL tips:** Include a number. Be specific. Define user-visible outcome.
**CONSTRAINTS tips:** Only hard limits — non-negotiable. Tech, scope, compatibility.
**FORMAT tips:** Exact file structure. What to include/exclude.
**FAILURE tips:** Think "technically works but actually wrong." Missing edge cases, performance misses, silent failures, incomplete handling, over-engineering.

Present the draft to the user for approval before proceeding.

### Step 3 — Validate the contract
- **Complete** — all 4 sections filled
- **Consistent** — CONSTRAINTS don't contradict GOAL
- **Testable** — every FAILURE condition can be mechanically verified
- **Scoped** — GOAL is achievable within CONSTRAINTS

If ambiguous → ask the user.

### Step 4 — Implement against the contract
- GOAL = what you optimize for
- CONSTRAINTS = boundaries you cannot cross
- FORMAT = exact output shape
- FAILURE = conditions you must actively prevent

Mentally check each FAILURE condition as you build.

### Step 5 — Self-verify against FAILURE conditions

```markdown
## Contract Verification

- [ ] FAILURE 1: {condition} → VERIFIED: {how}
- [ ] FAILURE 2: {condition} → VERIFIED: {how}
- [ ] GOAL metric met: {evidence}
- [ ] All CONSTRAINTS respected: {confirmation}
- [ ] FORMAT matches spec: {confirmation}
```

If any FAILURE condition is violated → fix before delivering.

### Step 6 — Deliver with contract status

```
Contract status: ALL PASS

GOAL: ✓ {evidence}
CONSTRAINTS: ✓ {all respected}
FORMAT: ✓ {matches spec}
FAILURE conditions: ✓ {all verified}
```

If any failed:
```
Contract status: 1 FAILURE

FAILURE conditions: 1 of N failed
  - FAILED: "{condition}" — {actual result}
  - Reason: {why}
  - Options: {what could fix it}
```

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| verify | true | Self-verify before delivering |
| strict | true | Fail if any FAILURE condition triggered |
| template | standard | standard / minimal / detailed |

## Edge Cases & Learnings

- **Incomplete contract from user**: Fill missing sections with reasonable defaults, confirm with user.
- **FAILURE conflicts with GOAL**: Flag contradiction, ask which takes priority.
- **Can't verify a FAILURE condition**: Mark "UNVERIFIABLE", explain why, suggest manual verification.
- **Contract is overkill**: Say so. Suggest GOAL + FAILURE only minimal version.

---

*Self-annealing: append new learnings below as they are discovered.*

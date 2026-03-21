# Prompt Contracts — Directive

> Before implementing any phase, define a 4-part contract: GOAL, CONSTRAINTS, FORMAT, FAILURE.

## When to Apply
- Every pipeline phase (1–8)
- Any new execution script
- Any task where quality matters more than speed

## Contract Template

```markdown
## Contract: [Phase / Task Name]

GOAL: [Measurable success criteria]

CONSTRAINTS:
- [Hard limit 1]
- [Hard limit 2]
- [Hard limit 3]

FORMAT:
- [Exact output shape/files]
- [Naming conventions]
- [What to include]
- [For manual tasks: exact copy-paste prompts grounded in coursework, not summaries]
- [For manual tasks: exact tool settings per directives/tool_settings.md — aspect ratio, resolution, image count, etc.]

FAILURE (any = not done):
- [Failure condition 1]
- [Failure condition 2]
- [Edge case to handle]
- [Quality bar to meet]
```

## Verification Checklist
Before delivering, run through every FAILURE condition:
```
- [ ] FAILURE 1: {condition} → VERIFIED
- [ ] FAILURE 2: {condition} → VERIFIED
- [ ] GOAL metric met
- [ ] All CONSTRAINTS respected
- [ ] FORMAT matches spec
```

## Delivery Format
```
Contract status: ALL PASS / N FAILURE(s)
GOAL: ✓/✗
CONSTRAINTS: ✓/✗
FORMAT: ✓/✗
FAILURE conditions: ✓/✗ (N of M passed)
```

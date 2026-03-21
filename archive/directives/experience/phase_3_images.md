# Experience — Phase 3 Image Creation

## Reverse Prompting Q&A (March 19, 2026)

Phase 3 reverse prompting was addressed through Phase 1 and 2 decisions:
- Visual style: Animated Pixar-adjacent (Phase 1 Q&A)
- Framing: Medium close-up for anchors (Phase 2 Q&A, grounded in Lesson 22)
- Camera techniques: 7 approved techniques (Phase 2 Q&A, grounded in Lesson 33)
- All carry forward into Phase 3 without new questions needed.

## Key Decisions
- 12 prompts written — 5 ANCHOR + 7 B-ROLL
- Anchor scenes use `lola_animated_reference.png` as @ reference
- B-roll scenes use NO reference (different characters)
- All prompts follow the `directives/animated_prompt_construction.md` 6-section structure
- Dense paragraph style adapted from Lesson 23 Prompt Bank
- Safety clauses appended to every prompt per Learnings Report

## Learnings (March 19, 2026)

1. **@ Element creation works** — uploading animated ref twice + description successfully locked Lola's face across anchors
2. **File format mismatch causes upload failures** — original `lola_animated_reference.png` was actually a JPEG saved with .png extension. Nanobanana PRO rejected it. Fix: use `sips -s format png` to convert properly. Added `lola_ref_1.png` and `lola_ref_2.png` (slightly cropped variant) as true PNGs
3. **Nanobanana PRO output is 768×1376** at 1K resolution with 9:16 ratio — this is the base resolution that Phase 5 will upscale
4. **Mixed output formats** — tool outputs both PNG and JPEG depending on the generation. Not an issue for pipeline but worth noting
5. **Consistency check passed** — Lola looks consistent across all 5 anchor scenes when @ element is used correctly

# Client Video Production — Directive

> Type: **Project-specific SOP**
> Client: TeenCare (Reels Factory)
> Status: **ACTIVE**
> **⚠️ MASTER RULES**: See `directives/video_pipeline_master.md` for ALL non-negotiable rules. That file takes precedence.

## Project Summary

Produce a demo video for a freelance job application: "AI Video Automation Engineer — Short-Form Content Pipeline (Reels Factory)". The client wants 6-10 vertical videos/day for Filipino parenting education content.

## Reference Video Pattern (Codified)

After analyzing the reference video in detail, here is the codified pattern:

### Video Structure Pattern
```
HOOK (4-5s) → LISTICLE RULES (5-8 items × 5-7s each) → CTA (3-4s) → END CARD (2-3s)
```

### Visual Pattern
- **Anchor character**: AI-generated avatar in a static setting (chair, warm lighting, cozy room)
- **B-roll cutaways**: Animated illustrations showing each rule in action
- **Intercut pacing**: Anchor → B-roll → Anchor → B-roll (very fast cuts, ~1-2s average scene duration)
- **Art style**: Concept-animated (NOT photorealistic) — warm, clean, consistent palette
- **Text overlays**: Rule number + text on every scene, plus a keyword takeaway in quotes

### Audio Pattern
- Single AI voiceover narration (warm, educational, steady pace)
- Gentle background music (low volume)
- No hard SFX (keeps the tone calm and educational)

### Key Learnings for This Genre
1. **Cut fast** — the reference has 51 scene changes in 50 seconds. Audiences on Reels/TikTok expect rapid visual changes.
2. **Text overlays are essential** — every rule needs visible text. Many viewers watch without sound.
3. **Cultural adaptation matters** — the client specifically wants Filipino visual context (characters, clothing, style).
4. **Consistent art style > photorealism** — for educational content, concept-animated style is warmer and more approachable.
5. **Script drives everything** — the voiceover timing dictates all cuts, so script must be finalized BEFORE image creation.
6. **Anchor character reuse** — the same character appears in 25+ of 51 scenes. Character consistency is critical.
7. **B-roll illustrates, doesn't duplicate** — each B-roll scene shows the rule in action, not just the character repeating it.

## Rules for This Project
0. **⚠️ MANDATORY PRE-EXECUTION CHECK**: Before executing ANY task (writing a prompt, choosing a tool, generating an image, editing a clip, making any creative decision), you MUST first consult the relevant expert guideline in `05_Video_Pipeline_2/Video_Expert/`. No exceptions. Refer to `video_expert_baseline.md` for the lookup table of which file to consult for which decision type.
1. Follow the 8-step workflow exactly (per `video_expert_baseline.md`)
2. Use Nanobanana PRO for image generation (best for character consistency in animated style)
3. Use Kling 3.0 for video generation (supports animated style well)
4. Use ElevenLabs for voiceover (best quality + Filipino accent options)
5. Script must be finalized and timed BEFORE any image generation begins
6. All images must be in matching art style — no mixing photorealistic and cartoon

---

*Self-annealing: append new learnings below as they are discovered during execution.*

### Learning 1: ChatGPT `generate_image` has NO aspect ratio control (2026-03-20)
- The built-in ChatGPT image generation tool always outputs 1:1 (square) images
- Even explicit prompts like "9:16 vertical", "1080x1920", "TALL PORTRAIT" do not change the output ratio
- **Workaround**: Use Nanobanana PRO (Higgsfield API) which supports native `"aspect_ratio": "9:16"` in the API payload
- **Alternative**: Generate square with ChatGPT, then crop/resize in post-production (Canva or script)
- **Verdict for this project**: Prefer Nanobanana PRO for production images since it delivers native 9:16

### Learning 2: Always validate against coursework checklist BEFORE marking a step done (2026-03-20)
- Step 2 audit caught 3 gaps (camera angles, vibe brainstorm, refinement pass)
- Rule: after completing any step, cross-check against the coursework checklist before moving on

### Learning 3: Character consistency via reference images (2026-03-20)
- ChatGPT: pass reference images via the `ImagePaths` parameter + begin prompt with "same face, same hair, same blouse"
- Nanobanana PRO: use `reference_image` field in API payload (base64-encoded). If 422, falls back to prompt-only
- Both tools maintain good consistency when character description is LOCKED and copy-pasted verbatim


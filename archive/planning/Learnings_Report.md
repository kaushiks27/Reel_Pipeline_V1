# Learnings Report — Reel AI Video Pipeline

## What to Do & What Not to Do (Based on March 18, 2026 Work)

> This report distills every insight, mistake, and pattern discovered during yesterday's intensive pipeline build. Use it as a design checklist for Phase 2.

---

## Table of Contents

1. [NSFW Content Safety — The Biggest Lesson](#1-nsfw-content-safety--the-biggest-lesson)
2. [Topic Selection — v1 vs v2 Evolution](#2-topic-selection--v1-vs-v2-evolution)
3. [Prompt Engineering Patterns](#3-prompt-engineering-patterns)
4. [API Integration — What Worked, What Broke](#4-api-integration--what-worked-what-broke)
5. [Two-Stage Lip-Sync Pipeline](#5-two-stage-lip-sync-pipeline)
6. [Quality Gates — Programmatic Trust](#6-quality-gates--programmatic-trust)
7. [Pipeline Architecture Decisions](#7-pipeline-architecture-decisions)
8. [3-Layer Architecture Compliance](#8-3-layer-architecture-compliance)
9. [Prompt Contracts & Reverse Prompting](#9-prompt-contracts--reverse-prompting)
10. [Scene Decomposition Tool Insights](#10-scene-decomposition-tool-insights)
11. [Automation vs Manual Trade-offs](#11-automation-vs-manual-trade-offs)
12. [Cost & Performance Benchmarks](#12-cost--performance-benchmarks)
13. [Next Phase Recommendations](#13-next-phase-recommendations)

---

## 1. NSFW Content Safety — The Biggest Lesson

### ❌ What NOT to Do

The v1 report used a topic ("5 Words That Hurt Your Child More Than You Think") that depicted **negative, distressing child scenarios**: children looking hurt, defeated, crying, isolated, standing alone in corners. This triggers NSFW/content-safety flags on **every major AI image generator** (Nanobanana PRO, Midjourney, DALL-E, etc.).

**Specific b-roll scenes that would get flagged:**
- "Younger child looks hurt" — child distress
- "Child with head down, defeated posture" — emotional harm
- "Child standing alone in corner, hugging herself" — isolation/neglect
- "A single tear forms but doesn't fall" — child crying
- "Child's hand slowly lowering, deflated expression" — hopelessness

> **Rule: Any scene showing a child in distress, sadness, isolation, fear, or emotional pain WILL be flagged by AI safety systems.**

### ✅ What TO Do

The v2 report completely pivoted to a positive topic ("5 Simple Habits That Raise Confident Filipino Kids") where every B-roll scene depicts **happy, joyful, empowered children**:

- Family laughing together at dinner
- Girl proudly choosing her own outfit, smiling
- Mother giving thumbs-up to son at homework desk, both beaming
- Father and children playing basketball, everyone laughing
- Mother and daughter talking on a bench, both smiling

**NSFW-Safe Prompt Guardrails (apply to ALL future content):**

| Rule | Rationale |
|------|-----------|
| All characters fully clothed in age-appropriate attire | Prevents body-related flags |
| All children shown in **positive, happy** activities | Prevents emotional distress flags |
| All settings bright, well-lit, and safe | Dark/dim settings trigger "threatening environment" filters |
| No conflict, distress, tears, isolation | These are the most common trigger words |
| All adults in nurturing, supportive roles | "Angry parent" or "neglectful adult" gets flagged |
| No physical contact beyond natural family affection | Prevents inappropriate contact flags |

### Design Principle for Next Phase

> **Choose topics where EVERY scene naturally produces positive imagery.** If any single scene in the shot list requires depicting a negative emotion, **change the topic**. Don't try to "work around" safety filters — redesign the content to not need them.

---

## 2. Topic Selection — v1 vs v2 Evolution

### What Changed and Why

| Aspect | v1 (What Not to Do) | v2 (What to Do) |
|--------|---------------------|-----------------|
| **Topic** | "5 Words That Hurt Your Child" | "5 Simple Habits That Raise Confident Kids" |
| **Emotional frame** | Guilt, fear, shame | Empowerment, warmth, action |
| **B-roll scenes** | Children in distress | Children in joyful moments |
| **NSFW risk** | HIGH — every scene has distress | ZERO — every scene is positive |
| **Scroll-stop mechanism** | Guilt/curiosity | Promise/aspiration |
| **Actionability** | "Here's what you're doing wrong" | "Here's what you can start today" |

### Topic Selection Checklist for Next Phase

Before accepting any topic, run this mental filter:

1. ✅ Can every B-roll scene show **only positive, happy imagery**?
2. ✅ Does the topic frame advice as **"do this"** (not "stop doing that")?
3. ✅ Are there **zero scenes** requiring children in distress, fear, sadness?
4. ✅ Will the hook work through **aspiration** (not guilt)?
5. ✅ Is the content culturally specific enough to resonate (Filipino family context)?

### Approved Topic Patterns

These topic formats are inherently NSFW-safe:
- "X Habits That Build Confident Kids"
- "X Fun Ways to Bond With Your Child"
- "X Morning Routines That Set Your Child Up for a Great Day"
- "X Life Skills Every Child Should Learn by Age Y"
- "X Filipino Family Traditions That Build Strong Kids"
- "X Outdoor Games That Teach Kids Teamwork"

### Topic Patterns to AVOID

These formats inevitably require negative B-roll:
- "X Words That Hurt Your Child"
- "X Mistakes Parents Make"
- "X Signs Your Child Is Stressed"
- "X Things That Make Your Child Afraid"
- "X Reasons Your Child Lies"

---

## 3. Prompt Engineering Patterns

### ✅ Do: Use the 6-Layer Prompt Framework (Lesson 11)

Every prompt — for scripts, images, video motion — follows this structure:

```
1. PURPOSE   → What you want
2. ROLE      → Who the AI should be
3. STRUCTURE → Exact format of output
4. STYLE     → Tone, voice, aesthetic
5. DETAILS   → Specifics (word count, color palette, camera angle)
6. EXAMPLE   → Optional reference output
```

### ✅ Do: Use the Kling 4-Field Prompt Structure (Lesson 36)

For all video motion prompts:

```
Shot:    [Type and duration]
Details: [What's happening in the scene]
Camera:  [Movement, angle, lens]
Mood:    [Emotional tone, lighting, style]
```

### ✅ Do: Include NSFW-Safety Clauses in Every Image Prompt

Append these to every B-roll image prompt:
```
All characters are fully clothed in age-appropriate attire.
Setting is bright, well-lit, and family-friendly.
Emotional tone: [positive emotion]. No conflict, no distress.
```

### ❌ Don't: Use Speech/Talking References in Veo 3.1 Prompts

**Critical Discovery:** Veo 3.1's audio safety filter aggressively blocks any prompt that mentions speech, talking, lips moving, or dialogue. This includes seemingly innocent phrases like:
- "grandmother speaking to camera" → BLOCKED
- "mouth slightly open as if talking" → BLOCKED
- "lip movement" → BLOCKED

**Fix:** Use only clean, visual-motion prompts for Veo:
```python
# WRONG — will trigger safety filter
"Grandmother speaking warmly to camera, lips moving naturally"

# RIGHT — clean motion only
"Elderly woman sitting in warm living room. Gentle nod. Soft warm lamp light. Cinematic interior."
```

Then handle lip-sync separately with Kling's lip-sync API in post-processing.

### ✅ Do: Lock Character Identity with Reference Upload (Lesson 20)

The two-phase approach is critical for consistency:
1. **Phase A**: Generate the first anchor image WITHOUT reference — this establishes the base face
2. **Phase B**: Upload Phase A result as reference, then pass it to ALL subsequent generations

```python
# Phase A: No reference
image_data = generate_image(prompt)
# Phase B: Lock identity
reference_url = upload_reference_image(phase_a_image)
image_data = generate_image(prompt, reference_image_url=reference_url)
```

---

## 4. API Integration — What Worked, What Broke

### API Architecture Summary

| API | Role | Status | Learnings |
|-----|------|--------|-----------|
| **OpenAI GPT-5.4** | Script + scene gen | ✅ Works | Needs structured JSON output + word count validation |
| **Higgsfield Nanobanana PRO** | Image generation | ✅ Works | Uses `Key {id}:{secret}` auth, async polling, Soul ID for consistency |
| **Higgsfield DoP** | Fallback video gen | ✅ Works | Same auth pattern, used as fallback for both anchor + B-roll |
| **ElevenLabs** | Voiceover | ✅ Works | `eleven_multilingual_v2` model, needs voice ID in `.env` |
| **OpenAI Whisper-1** | Timestamps | ✅ Works | Word-level timestamps, essential for caption sync |
| **Google Veo 3.1** | Anchor motion | ⚠️ Partial | Safety filter blocks speech prompts, needs clean prompts |
| **Kling 3.0** | B-roll video | ✅ Works | JWT auth, image-to-video, pro mode |
| **Kling Lip-Sync** | Post-processing | ✅ Works | Needs public URLs (catbox.moe upload), audio2video mode |

### ✅ Do: Always Implement Retry with Exponential Backoff

Every API call wraps in this pattern:
```python
@retry(max_retries=3, base_delay=5.0)
def api_call():
    # API-specific logic
```

### ✅ Do: Always Use Async Polling for Video Generation

All video APIs (Veo, Kling, Higgsfield) use async patterns:
1. Submit job → get `task_id` / `operation_name`
2. Poll every 5-10 seconds
3. Handle timeout (15-20 min max)
4. Handle `failed` / `error` / `nsfw` statuses

### ✅ Do: Implement Fallback Chains

Every scene has a fallback path:
- Anchor: Veo 3.1 → Kling lip-sync → **Higgsfield DoP** (fallback)
- B-Roll: Kling 3.0 → **Higgsfield DoP** (fallback)

### ❌ Don't: Hardcode API Keys

All keys live in `.env` and are loaded via `get_env()`:
```python
GOOGLE_AI_STUDIO_API_KEY=...
KLING_ACCESS_KEY=...
KLING_SECRET_KEY=...
HIGGSFIELD_API_KEY=...
HIGGSFIELD_API_SECRET=...
ELEVENLABS_API_KEY=...
ELEVENLABS_VOICE_ID=...
OPENAI_API_KEY=...
```

### ❌ Don't: Assume API Response Shapes Are Stable

Veo 3.1 has multiple response formats depending on API version:
- `generateVideoResponse.generatedSamples[0].video.uri` (primary)
- `generatedVideos[0].video.uri` (older)
- `videos[0].uri` (legacy)

Always implement multiple response path parsers with fallback logic.

---

## 5. Two-Stage Lip-Sync Pipeline

### The Problem

Veo 3.1 cannot do lip-sync directly because its safety filter blocks any prompt mentioning speech or talking. But we need realistic lip movement for anchor scenes.

### The Solution: Two-Stage Pipeline

```
Stage 1: Veo 3.1 → Generate clean face motion (no speech)
Stage 2: FFmpeg   → Strip Veo's auto-generated audio
Stage 3: Kling    → Lip-sync muted video + per-scene audio segment
```

### Key Implementation Details

1. **Audio segment extraction**: Use FFmpeg to cut the exact audio segment for each scene from the full voiceover
2. **File hosting**: Kling lip-sync needs **public URLs** — use catbox.moe for temporary file hosting
3. **Padding**: Add 0.5s padding after each audio segment for natural finish
4. **Cleanup**: Delete temp files (audio segments, raw Veo output, silent video) after processing

### ❌ Don't

- Don't try to make Veo do lip-sync directly — it will fail silently or get blocked
- Don't forget to strip Veo's auto-generated audio before lip-sync
- Don't use private/localhost URLs for Kling — it needs publicly accessible files

---

## 6. Quality Gates — Programmatic Trust

### ✅ Do: Validate After Every Pipeline Step

The pipeline has **8 quality gates** that automatically halt on failure:

| Gate | Validates | Key Checks |
|------|-----------|------------|
| Gate 1: Script | Word count, structure | 70-140 words, has HOOK+BODY+CTA, ≥3 rules |
| Gate 2: Scene Plan | Completeness | ≥10 scenes, has ANCHOR+B_ROLL, 25-40s duration |
| Gate 3: Anchor Images | Image quality | File exists, >10KB, ≥512x512, loadable |
| Gate 4: B-Roll Images | Image quality | Same as Gate 3 |
| Gate 5: Upscaled | Resolution | 1080×1920 target |
| Gate 6: Audio | Voiceover | File exists, >50KB, 15-90s duration |
| Gate 7: Video Clips | Per-clip quality | File exists, >50KB, >0.5s, valid video |
| Gate 8: Final Video | Full package | 1080×1920, H.264+AAC, >1MB, 25-90s, both streams |

### ✅ Do: Save QC Reports as JSON

Every gate saves a `qc_{step_name}.json` file for post-mortem analysis:
```python
save_json(report, run_dir / f"qc_{step_name}.json")
```

### ✅ Do: Use Wide Tolerances for LLM Outputs

LLM outputs are variable. Use wider tolerance bands:
- Word count target is 90-110, but **gate passes** at 70-140
- Duration target is 30s, but **gate passes** at 25-40s

### ❌ Don't: Hard-Fail on Non-Critical Errors

For video clips, the pipeline **warns but continues** if some clips fail:
```python
if not all_ok:
    log.warning("⚠ Some video clips failed — continuing with available clips")
    config["quality_gates"]["step7"] = "PARTIAL"  # Not "FAILED"
```

---

## 7. Pipeline Architecture Decisions

### ✅ Do: Support Resumable Runs

The `--skip` and `--run-dir` flags allow resuming from any step:
```bash
python execution/run_pipeline.py --topic "..." --skip 1 2 3 --run-dir .tmp/20260318_225925_...
```

Every intermediate output is saved to the run directory, so no work is lost on failure.

### ✅ Do: Use Timestamped Run Folders

Each run creates a unique folder: `.tmp/{timestamp}_{topic_slug}/`
This prevents overwriting previous runs and enables comparison.

### ✅ Do: Print Model Summary at Pipeline Start

```
┌──────────────────────────────────────────────────────────┐
│                    MODEL SELECTION                        │
├──────────────┬───────────────────────────────────────────┤
│ Script Gen   │ OpenAI GPT-5.4 (flagship)                │
│ Anchor Imgs  │ Higgsfield Nanobanana PRO + Soul ID      │
│ Lip-Sync Vid │ Google Veo 3.1 → Kling lip-sync          │
│ B-Roll Video │ Kling 3.0 Pro                            │
│ Assembly     │ FFmpeg H.264/AAC local                   │
└──────────────┴───────────────────────────────────────────┘
```

This makes debugging easier — you always know exactly which models were used.

### ✅ Do: Save Pipeline Config as JSON

Save the full config (topic, models, completed steps, gate results, timing) to `pipeline_config.json` and update it after every step.

---

## 8. 3-Layer Architecture Compliance

### ✅ Do: Maintain the Directive → Orchestration → Execution Split

| Layer | Files | Purpose |
|-------|-------|---------|
| **Directive** | `directives/generate_reel.md` | SOP: what to run, inputs, outputs, edge cases |
| **Orchestration** | AI agent (you) | Decision-making, error handling, routing |
| **Execution** | `execution/*.py` (11 scripts) | Deterministic Python: API calls, file I/O, validation |

### ✅ Do: Update Directives When You Learn Something New

The directive (`generate_reel.md`) was updated with:
- The `--skip` flag for resuming partial runs
- Edge cases (API rate limits, partial failure, word count drift)
- One-time setup requirements

### ❌ Don't: Let the Agent Do Execution Work Directly

The agent should never make API calls directly. It reads the directive, determines inputs, and runs the script:
```bash
python execution/run_pipeline.py --topic "..."
```

### Script Inventory (for reference)

| Script | Size | Purpose |
|--------|------|---------|
| `run_pipeline.py` | 17KB | Main orchestrator |
| `step1_script_gen.py` | 5KB | ChatGPT script generation |
| `step2_scene_plan.py` | 6KB | Scene planning + shot list |
| `step3_anchor_images.py` | 12KB | Higgsfield anchor images + Soul ID |
| `step4_broll_images.py` | 11KB | Higgsfield B-roll images |
| `step5_upscale.py` | 5KB | Pillow Lanczos upscaling |
| `step6_voiceover.py` | 7KB | ElevenLabs + Whisper timestamps |
| `step7_video_gen.py` | 30KB | Veo 3.1 + Kling + Higgsfield fallback |
| `step8_assembly.py` | 18KB | FFmpeg final assembly |
| `quality_gates.py` | 16KB | 8 validation gates |
| `utils.py` | 6KB | Shared utilities |

---

## 9. Prompt Contracts & Reverse Prompting

### ✅ Do: Use Prompt Contracts for Critical Steps

The 4-part contract pattern prevents ambiguity:

```
GOAL:        [Measurable success metric]
CONSTRAINTS: [Hard limits — non-negotiable]
FORMAT:      [Exact output shape]
FAILURE:     [Explicit conditions that mean "not done"]
```

**Key insight:** The FAILURE clause is the most important part. It prevents the agent from rationalizing shortcuts.

### ✅ Do: Self-Verify Against Failure Conditions

Before delivering, run through every FAILURE condition as a checklist:
```
✓ Pipeline completes without crash
✓ All frames present in JSON
✓ Word-level timestamps present
✓ JSON is valid
✓ Zero empty fields
✓ API key loaded from .env
✓ Retry/backoff implemented
```

### ✅ Do: Use Reverse Prompting Before Starting Complex Tasks

Ask 5 clarifying questions before building:
1. State your assumption
2. Ask the question
3. Explain why the answer matters

This prevents the most expensive failure: **confidently building the wrong thing**.

---

## 10. Scene Decomposition Tool Insights

### From the Video Analysis Pipeline (04_Video_Analyzer)

A separate pipeline was built to analyze existing videos frame-by-frame. Key learnings:

| Metric | Value |
|--------|-------|
| Total processing time | 96.2 minutes for 50s video |
| Frames analyzed | 1496/1496 (100%) |
| Batch size | 10 frames per API call |
| Total API calls | ~150 (batched from 1496) |
| Scenes detected | 51 |
| Words transcribed | 111 (word-level timestamps) |

### ✅ Do: Batch API Calls

Sending 1496 individual frames = 1496 API calls. Batching 10 frames per call = 150 calls. **10x cost reduction.**

### ✅ Do: Save Per-Batch Partial Results

Write partial results to `.tmp/` after each batch. If the pipeline crashes at batch 80, you don't lose batches 1-79.

### ✅ Do: Use Gemini for Both Vision AND Audio

Since FFmpeg wasn't available in the analysis environment, Gemini's native video understanding was used for both frame analysis AND audio transcription. This eliminated a dependency but meant transcription quality depends on Gemini's capabilities.

### ❌ Don't: Forget Python 3.8 Compatibility

When targeting systems with older Python:
- No f-string `=` debugging (e.g., `f"{x=}"`)
- No walrus operators in comprehensions
- No `match` statements
- Use `Dict, List, Optional` from `typing` (not built-in generics)

---

## 11. Automation vs Manual Trade-offs

### What's Fully Automated

| Step | Automated? | Notes |
|------|-----------|-------|
| Script generation | ✅ Yes | ChatGPT API with template |
| Scene planning | ✅ Yes | ChatGPT API with structure template |
| Anchor image generation | ✅ Yes | Higgsfield API with Soul ID |
| B-roll image generation | ✅ Yes | Higgsfield API |
| Upscaling | ✅ Yes | Pillow Lanczos |
| Voiceover | ✅ Yes | ElevenLabs API |
| Timestamp extraction | ✅ Yes | Whisper API |
| Video clip generation | ✅ Yes | Veo + Kling + Higgsfield |
| Final assembly | ✅ Yes | FFmpeg |

### What Remains Manual (Quality Gates)

| Manual Step | Time | Why It's Manual |
|-------------|------|-----------------|
| Review B-roll for AI artifacts | ~30s/image | Extra fingers, text glitches, style inconsistency |
| Listen to voiceover | ~30s | Filipino pronunciation, pacing, tone |
| Final video QC | ~30s | Overall flow, timing, caption sync |
| **Total per video** | **~2-3 min** | |

### Coursework Deviations (Flagged)

Three areas deviate from the coursework:

| Deviation | Coursework Recommendation | Our Choice | Rationale |
|-----------|--------------------------|------------|-----------|
| FFmpeg for assembly | CapCut (Lesson 47) | FFmpeg + Python | Batch automation for 6-10 videos/day |
| Whisper for captions | CapCut auto-captions | Whisper API | Programmatic caption sync |
| Python orchestration | Manual tool-by-tool | `run_pipeline.py` | End-to-end automation |

---

## 12. Cost & Performance Benchmarks

### Monthly Cost Estimate

| Service | Cost |
|---------|------|
| Nanobanana PRO (via Higgsfield) | ~$20/mo |
| ElevenLabs Creator | ~$22/mo |
| Kling AI Pro | ~$10/mo |
| ChatGPT Plus | ~$20/mo |
| Veo 3.1 (Google AI Studio) | Free tier or ~$20/mo |
| Pixabay | Free |
| FFmpeg/Python | Free |
| **Total** | **~$92/mo** |

### Per-Video Timing Targets

| Phase | Time |
|-------|------|
| Compute/generation | ~5 min |
| Manual QC | ~2-3 min |
| **Total** | **~8 min/video** |

### Daily Capacity

At 8 min/video: **6-10 videos/day** in under 1 hour of active work.

---

## 13. Next Phase Recommendations

### Priority 1: Content Safety Layer

Build an automated NSFW pre-check into the pipeline:
- Before generating images, scan the image prompt for distress-triggering keywords
- Maintain a blocklist: `["hurt", "sad", "crying", "alone", "scared", "angry", "defeated", "guilt"]`
- If any B-roll prompt contains blocklisted words → reject and regenerate with positive framing

### Priority 2: End-to-End Test Run

Run the full pipeline end-to-end on 3-5 topics from the approved list. Measure:
- Success rate per step
- Total compute time
- API cost per video
- Quality gate pass/fail rates

### Priority 3: Voice Blueprint Consistency

ElevenLabs voice settings need to be locked for the Lola character:
- Stability: 65-70%
- Clarity + Similarity: 75%
- Style: 30%
- Speed: Slightly slower than default

Clone or select a voice with Filipino-English accent and save the `ELEVENLABS_VOICE_ID`.

### Priority 4: Asset One-Time Setup

These need to be created once before the pipeline can run:
- [ ] Lola reference images → `assets/lola_reference.png`
- [ ] End card design → `assets/end_card.png`
- [ ] Background music → `assets/bg_music.mp3`
- [ ] ElevenLabs voice profile → `ELEVENLABS_VOICE_ID` in `.env`

### Priority 5: Monitoring & Observability

Add to the pipeline:
- Per-step timing logs (which step is the bottleneck?)
- API cost tracking (how much does each video cost?)
- Failure rate dashboard (which API fails most often?)
- A/B testing for prompt variations

---

## Summary: The 10 Commandments

1. **Choose only positive topics** — if any scene requires child distress, reject the topic
2. **Never reference speech in Veo prompts** — use clean motion, lip-sync in post-processing
3. **Lock character identity** — Phase A (establish face) → Phase B (reference lock)
4. **Batch API calls** — 10x cost reduction vs 1:1
5. **Quality gate after every step** — halt on failure, warn on partial
6. **Save all intermediates** — every step writes to the run folder for resumability
7. **Implement fallback chains** — Veo → Kling → Higgsfield
8. **Use Prompt Contracts** — GOAL + CONSTRAINTS + FORMAT + FAILURE
9. **Keep directives alive** — update SOPs with every new edge case discovered
10. **Never hardcode keys** — everything in `.env`, loaded via `get_env()`

---

*Report generated: March 19, 2026*
*Based on work from: March 18, 2026*
*Workspace: `05_Video_Pipeline`*

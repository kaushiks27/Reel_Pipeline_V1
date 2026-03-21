# Video Pipeline — Execution Log

> Purpose: **Granular log of every step and action taken** during manual video production. This will become the blueprint for designing the automated pipeline.
> Status: **ACTIVE — UPDATE AFTER EVERY ACTION**

---

## Step 1: Concept & Planning ✅

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|
| 1.1 | Selected topic | Manual decision | Client brief + reference video analysis | "3 Things to Say to Your Child Every Day" | — | 3 rules, not 5 — client requested shorter |
| 1.2 | Defined audience | Manual decision | Client brief (TeenCare fanpage) | Filipino parents on FB/IG/TikTok | — | — |
| 1.3 | Set format specs | Manual decision | Client brief + reference video | 9:16 vertical, 30s max, concept-animated | — | Reference was 50s but client wants 30s |
| 1.4 | Chose art style | Manual decision + reference analysis | Reference video scene decomposition | Concept-animated (NOT photorealistic) | — | Warmer, more approachable for educational content |
| 1.5 | Outlined scene structure | Manual | Topic + format | 9 scene cuts: hook → 3×(anchor+B-roll) → CTA → end card | — | Mirrors reference video pattern |

## Step 2: Scriptwriting & Voice Planning ✅

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|
| 2.1 | Wrote narration script | Manual (coursework ref: `11_how_to_write_prompts.md`) | Scene structure + topic | 55-word script with pause markers | — | `...` for natural pauses per `41_Consistent_Character_Voices_in_Veo_3.1.md` |
| 2.2 | Defined voice blueprint | Manual (coursework ref: `41_Consistent_Character_Voices_in_Veo_3.1.md`) | Character profile | `"subtle Filipino accent, warm maternal tone, medium pace, gentle authority..."` | — | LOCKED — copy-paste verbatim, never modify |
| 2.3 | Timed each segment | Manual | Script word count + target pace (~2 wps) | 9-clip timing map: hook(4s) + 3 rules(6-7s each) + CTA(3s) + end(3s) = 30s | — | — |
| 2.4 | Specified camera angles | Manual (coursework ref: `33_KlingCameraPDF.pdf.md`) | Scene descriptions | Camera angle, shot type per scene (medium, MCU, low angle) | — | Gap caught during audit |
| 2.5 | Specified lighting | Manual (coursework ref: `21_Making_Your_Avatar_More_Realistic.md`) | Scene descriptions | Warm lamplight (anchor), natural daylight (B-roll) | — | Gap caught during audit |
| 2.6 | Brainstormed vibe | Manual (coursework ref: `54_AI_Video_Creation_Workflow.md`) | Reference video feel | "Warm friend sharing a secret over coffee, never preachy" | — | Gap caught during audit |
| 2.7 | Refinement pass | Manual | Full script review | No changes needed — structure validated | — | Gap caught during audit |
| 2.8 | Validated against coursework checklist | Manual | `54_AI_Video_Creation_Workflow.md` Step 2 checklist | 10/10 items checked | — | Self-annealing: always audit before marking done |

## Step 3: Image Creation *(IN PROGRESS — character freeze)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|
| 3.1 | Consulted coursework (Rule 0) | Manual | `16_Nano_banana.md`, `21_Making_Your_Avatar_More_Realistic.md` | Confirmed concept-animated style, character consistency approach | — | Avoid photorealism triggers for this style |
| 3.2 | Found existing Higgsfield script | grep_search | `03_Video_Challenge/execution/` | `generate_echoes_nanobanana.py` — proven API pattern | — | Reuse don't reinvent |
| 3.3 | Created character gen script | Manual | API pattern + character prompts | `execution/generate_character_options.py` | — | 5 prompts with locked character base + varied expressions |
| 3.4 | Defined character base description | Manual (coursework ref) | Filipino market needs + concept-animated style | Filipina woman, mid-30s, shoulder-length black hair, coral floral blouse, warm brown skin | — | LOCKED — reuse across all prompts |
| 3.5 | Generated 5 ChatGPT images | ChatGPT (generate_image) | 5 prompts with same character base | 5 images: warm smile, speaking, thoughtful, hands together, close-up | — | All concept-animated, consistent palette |
| 3.6 | Generated 5 Nanobanana PRO images | Higgsfield API (`generate_character_options.py`) | Same 5 prompts | 5 images saved to `assets/character_freeze/nanobanana_pro/` | ~5min | All 5/5 succeeded |
| 3.7 | Prepared review artifact | Manual | All 10 images | `character_freeze_review.md` with carousels | — | Awaiting user selection |
| 3.8 | **Character frozen** | User decision | 10 options reviewed | **C3 (thoughtful) + C4 (hands together)** — frozen as anchor references | — | Both from ChatGPT |
| 3.9 | Extracted locked character description | Manual | C3 + C4 images | Filipina, mid-30s, black hair center-part, coral-pink floral blouse, green armchair, gold studs | — | VERBATIM in every anchor prompt |
| 3.10 | Extracted locked background description | Manual | C3 + C4 images | Wood-paneled walls, bookshelf, family photos, ceramic lamp, pothos, monstera, tribal pillows | — | VERBATIM in every anchor prompt |
| 3.11 | Consulted coursework for prompts | Manual | `22_UGC_Avatar_Prompt_Vault.md`, `23_Prompt_Bank.md` | Dense paragraph format, detailed scene descriptions, style/lighting specifics | — | Rule 0 check |
| 3.12 | Wrote 6 scene prompts | Manual | Scene breakdown + frozen refs | `assets/step3_scene_prompts.md`: 3 anchor + 3 B-roll prompts | — | Approved by user |
| 3.13 | Generated 3 ChatGPT anchor images | ChatGPT (generate_image) + ref images C3/C4 | 3 anchor prompts | A1 (hook), A2 (speaking), A3 (CTA) — **1:1 ratio** (tool limitation) | — | ⚠️ No 9:16 control in ChatGPT tool |
| 3.14 | Generated 3 Nanobanana PRO anchor images | Higgsfield API (`generate_anchor_scenes.py`) + ref image | Same 3 prompts | A1, A2, A3 — **native 9:16** | ~3min | All 3/3 succeeded |
| 3.15 | **LEARNING**: ChatGPT has no aspect ratio control | Self-annealing | Failed 9:16 attempt | Added to `client_video_production.md` learnings | — | Use Nanobanana PRO for production 9:16 images |
| 3.16 | Prepared anchor review artifact | Manual | All 6 images | Review for user selection | — | — |
| 3.17 | Regenerated ChatGPT anchors via OpenAI API | `generate_anchor_chatgpt.py` (DALL-E 3) | Same prompts, `size: 1024x1792` | 3 images in native 9:16 | ~90s | API supports exact size unlike ChatGPT tool |
| 3.18 | Resized ChatGPT anchors to 1080×1920 | PIL/Pillow (Python) | 1024×1792 images | 3 images at 1080×1920 | — | User requested exact resolution |
| 3.19 | Generated B-roll images | `generate_broll_chatgpt.py` (DALL-E 3) | 9 prompts (3 scenes × 3 variants) | **3/9 succeeded** — 6 blocked by content filter | — | DALL-E 3 blocks parent-child interaction prompts |
| 3.20 | **LEARNING**: DALL-E 3 content filter blocks child scenes | Self-annealing | 6/9 B-roll prompts blocked | Use Nanobanana PRO for child-related B-roll | — | Logged in directives |

## Step 6: Video Prompt Engineering *(COMPLETE — awaiting approval)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|
| 6.1 | Consulted coursework (Rule 0) | Manual | `33_KlingCameraPDF.pdf.md`, `36_Kling_3.0_UPDATE_2026.md`, `41_Consistent_Character_Voices_in_Veo_3.1.md` | Camera movement catalog, shot structure, voice blueprint locking | — | Key: start with camera angle, use Shot/Details/Camera/Mood |
| 6.2 | Wrote video prompts for all 6 scenes | Manual | Scene breakdown + script + coursework | `assets/step6_video_prompts.md`: 3 anchor + 3 B-roll Veo 3.1 prompts | — | Lip-sync dialogue, voice blueprint locked, `...` pauses |
| 6.3 | Updated for Veo 3.1 + lip-sync | Manual (user feedback) | User specified Veo 3.1 with lip-sync | Added lip-sync directives, confirmed dialogue format | — | Dialogue = character spoken words, not narration |

## Step 4: Image Editing *(PENDING)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|

## Step 5: Upscaling *(PENDING)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|

## Step 6: Video Generation *(PENDING)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|

## Step 7: Sound & Voiceover *(PENDING)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|

## Step 8: Final Assembly *(PENDING)*

| # | Action | Tool | Input | Output | Time | Notes |
|---|--------|------|-------|--------|------|-------|

---

*Every action goes here. No action too small. This is the automation blueprint.*

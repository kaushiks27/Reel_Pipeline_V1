# Tool Settings — Directive

> Every manual task must specify the exact tool settings. These are the locked defaults per tool.

## Nanobanana PRO (via Higgsfield)

**Source:** Lesson 20, Lesson 72, Phase 0 Setup

### Settings for Character Reference Images (one-time)

| Setting | Value | Rationale |
|---------|-------|-----------|
| Model | Nano Banana Pro | Locked tool (Lesson 54) |
| Aspect Ratio | **3:4** | Portrait orientation — captures face and upper body for character locking |
| Resolution | **1K** | Sufficient base; upscaled in Phase 5 |
| Image Count | **4** | Generate 4, pick the most realistic (Lesson 20: "review all outputs") |
| Reference (@) | **Empty** for first gen | Lesson 20, Step 4: "Leave reference empty for FIRST generation only" |
| Extra Free Gens | **ON** | Maximize selection options |
| Draw | **OFF** | Not needed for photo-realistic generation |

### Creating a Named @ Element (REQUIRED before scene generation)

The **@** button in Nanobanana PRO opens a **"New element"** dialog. This creates a named, reusable character reference.

**Steps:**
1. Click **@** → "New element" window opens
2. **Upload images:** Min 2 required — upload the **animated** reference image **twice**
3. **Element name:** Character name (e.g., `Lola`)
4. **Category:** Leave as `Auto`
5. **Description:** Key physical features of the character
6. Click **Create**

**Then in prompts:** Type `@Lola` (or `@ElementName`) to reference the character.

> ⚠️ **CRITICAL LEARNING:** Always upload images that match the target output style.
> - For **animated** output → upload only **animated** reference images
> - For **photorealistic** output → upload only **photorealistic** reference images
> - Mixing styles (e.g., uploading a photorealistic reference when you want animated output) may pull the output toward the wrong style.

### Settings for Scene Images (Phase 3 — per video)

| Setting | Value | Rationale |
|---------|-------|-----------|
| Model | Nano Banana Pro | Locked tool (Lesson 54) |
| Aspect Ratio | **9:16** | Target output: 1080×1920 vertical (Lesson 67) |
| Resolution | **1K** | Base resolution; upscaled in Phase 5 |
| Image Count | **4** | Generate 4, pick the best per scene |
| Reference (@) | **Type `@Lola` in prompt** for ANCHOR scenes, **omit** for B-ROLL | Anchor = keep Lola's face; B-roll = different characters |
| Extra Free Gens | **ON** | Maximize selection options |
| Draw | **OFF** | Not needed |

> **Key differences:** Reference images use **3:4** (portrait). Scene images use **9:16** (video frame). ANCHOR scenes include `@Lola`, B-ROLL scenes do NOT.

---

## ElevenLabs

**Source:** Lesson 41, Lesson 49, Phase 0 Setup

| Setting | Value |
|---------|-------|
| Model | `eleven_multilingual_v2` |
| Stability | 65–70% |
| Clarity + Similarity | 75% |
| Style | 30% |
| Speed | Slightly slower than default |
| Voice | Filipino-English accent (to be selected) |

---

## Kling 3.0 (B-Roll Video)

**Source:** Lesson 34, Lesson 36
**Verified settings from Kling UI (March 19, 2026):**

| Setting | Value | Notes |
|---------|-------|-------|
| Model | **VIDEO 3.0** | Latest version — "Enhanced Native Audio, Improved Element Consistency, Multi-Shot Storytelling" |
| Mode | **Image-to-Video** | Upload upscaled image as start frame |
| Quality | **Standard** (bottom-left toggle) | Switch to Pro if quality is poor |
| Resolution | **1080p** | Matches our upscaled images |
| Duration | **5s** | Minimum available — trim to target in CapCut |
| Aspect Ratio | **9:16** | ⚠️ Default is 16:9 — MUST change to 9:16 (vertical) |
| Count | **1** | One clip per scene |
| Native Audio | **ON** | Leave on — can mute in CapCut if not needed |
| Prompt structure | 4-Field: Shot / Details / Camera / Mood (Lesson 36) |

> ⚠️ **CRITICAL:** Kling defaults to **16:9** — always verify aspect ratio is **9:16** before generating.

---

## Veo 3.1 (Anchor Motion)

**Source:** Lesson 41, Learnings Report §3
**Verified settings from Google AI Studio UI (March 19, 2026):**

| Setting | Value | Notes |
|---------|-------|-------|
| Model | **Veo 3.1** | via Google AI Studio → Playground |
| Number of results | **1** | One clip per scene |
| Aspect ratio | **9:16** | Vertical format |
| Video duration | **8s** | Minimum available — trim to target in CapCut |
| Frame rate | **24 fps** | Cinematic standard |
| Output resolution | **720p** (max available) | Source image is 1080p, Veo downscales |
| Negative prompt | `photorealistic, dark, cinematic, anime, manga, blurry, distorted face, extra fingers` |
| Prompt format | `[Lola speaks]: "dialogue"` + voice blueprint |
| Fallback | If safety filter blocks → generate silent motion → ElevenLabs voiceover in Phase 7 |

> ⚠️ **Veo does not support uploading images with children** — only use for ANCHOR scenes (Lola only). B-roll goes to Kling.
> ⚠️ **Veo max resolution is 720p** — lower than Kling's 1080p. Final upscaling happens in CapCut export.

---

## CapCut (Final Editing)

**Source:** Lesson 47, Lesson 67

| Setting | Value |
|---------|-------|
| Aspect Ratio | 9:16 |
| Resolution | 1080×1920 |
| Duration target | 30–50 seconds |
| Captions | CapCut auto-captions (not Whisper) |

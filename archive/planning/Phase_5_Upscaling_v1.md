# PHASE 5 — UPSCALING

> Coursework Reference: Step 5 — "Gigapixel 8 / Midjourney upscale / Bigjpg / Nanobanana PRO for Upscaling" (Lesson 54)
> Feed this prompt to the agent after Phase 4 is approved.

---

## WHAT THIS PHASE DOES

Upscale all edited images to the target resolution before they go to video generation.

**Source (Lesson 54, Step 5 — exact coursework instructions):**
- Make sure your base image is clean, well-lit, and ready to upscale
- Choose the best version of your AI-generated image
- Avoid blurry, overly compressed, or poorly lit images
- Crop or clean it slightly if needed

---

## INSTRUCTIONS FOR THE AGENT

### Step 5.1 — Pre-Upscale Quality Check

Before upscaling, verify each image is ready:

```
PRE-UPSCALE CHECKLIST (for each image):
□ Image is clean — no remaining AI artifacts (these get WORSE when upscaled)
□ Image is well-lit — not too dark, not blown out
□ Image is the best version — you picked the right one in Phase 3
□ Image is not blurry or overly compressed
□ Image has been edited in Canva (Phase 4 complete)
□ Any needed cropping has been done BEFORE upscaling

If ANY image fails this check → go back to Phase 4 and fix it first.
Upscaling a bad image just gives you a bigger bad image.
```

### Step 5.2 — Choose Upscaling Tool

**Source:** Lesson 54, Step 5 — the coursework lists these options in order:

```
UPSCALING TOOL PRIORITY:
1. Gigapixel 8 (best quality — desktop app)
2. Midjourney upscale (if image was generated in Midjourney)
3. Bigjpg (free online alternative)
4. Nanobanana PRO (built-in upscale if available)

Choose based on what you have access to.
```

### Step 5.3 — Upscaling Settings

```
TARGET SPECIFICATIONS:
- Target resolution: 1080×1920 (9:16 vertical)
- If source image is smaller: upscale to at least 1080px wide
- If source image is already 1080×1920 or larger: no upscale needed
- Upscale factor: 2x or 4x depending on source size
- Quality setting: Maximum / Best Quality
- Noise reduction: Light (preserve natural texture, don't over-smooth)
- Sharpening: Light to Medium (avoid over-sharpening — it looks AI-generated)

CRITICAL: Do NOT over-process. The goal is higher resolution while keeping
the natural, photorealistic look from Phases 3-4.
```

### Step 5.4 — Scene-by-Scene Upscale Loop

```
FOR each edited image from Phase 4:

  1. CHECK if it meets the pre-upscale quality criteria (Step 5.1)

  2. UPSCALE using the chosen tool and settings from Steps 5.2-5.3

  3. VERIFY the upscaled result:
     □ Resolution is at least 1080×1920
     □ Image is sharp but not over-sharpened
     □ Skin still looks natural (not plasticky from over-smoothing)
     □ No new artifacts introduced by the upscaling process
     □ Colors and warmth are preserved from Phase 4 edits
     □ File size is reasonable (not corrupted or empty)

  4. SAVE upscaled image as: scene_[NUMBER]_[TYPE]_upscaled.png

  5. PRESENT result to human — show before and after if possible

  6. WAIT FOR APPROVAL:
     - "APPROVED" → move to next image
     - "REDO" → try different upscale settings
     - "SKIP" → use the pre-upscale version instead
```

---

## QUALITY GATE — PHASE 5

Before moving to Phase 6:

```
PHASE 5 DELIVERABLES:
1. ✅ All scene images upscaled to at least 1080×1920
2. ✅ No new artifacts introduced by upscaling
3. ✅ Natural photorealistic quality preserved
4. ✅ Files saved as scene_[NUMBER]_[TYPE]_upscaled.png
5. ✅ Human has approved all upscaled images
```

Wait for "APPROVED" before proceeding to Phase 6.

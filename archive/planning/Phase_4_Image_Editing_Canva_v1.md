# PHASE 4 — IMAGE EDITING WITH CANVA

> Coursework Reference: Step 4 — "Canva for Image Editing" (Lesson 54)
> Feed this prompt to the agent after Phase 3 is approved.

---

## WHAT THIS PHASE DOES

Edit and touch up the generated images using Canva before they go to video generation.

**Source (Lesson 54, Step 4 — exact coursework instructions):**
- Use Canva to remove any unwanted objects from your generated images
- Add new objects to images
- Add logos, branding
- Change lighting, brightness, tone using Canva 'Adjust' feature
- Overall edit the images to suit your needs more

---

## INSTRUCTIONS FOR THE AGENT

### Step 4.1 — Prepare the Edit Checklist

For each approved image from Phase 3, the agent should provide specific editing guidance for you to execute in Canva.

**Prompt to use:**

```
PURPOSE: Review each approved scene image and create a Canva editing checklist.

ROLE: Act as a photo editor preparing images for a professional short-form video.

STRUCTURE: For each image, provide:
- Scene number
- REMOVE: List any unwanted objects, AI artifacts, text glitches, extra fingers, or inconsistencies to remove using Canva's Magic Eraser or background remover
- ADD: List any objects to add (if needed) — logos, branding elements, text overlays
- ADJUST: Specific Canva 'Adjust' settings to apply:
  * Brightness (increase/decrease and by roughly how much)
  * Contrast
  * Saturation (keep natural — avoid oversaturation per Lesson 72)
  * Warmth (lean warm for family content)
  * Tint
  * Highlights / Shadows
- LIGHTING: Does the lighting need correction? Match to the vibe definition from Phase 2 (warm, natural daylight)
- BRANDING: Should any branding element be added to this specific scene?

STYLE: Be specific. "Increase warmth by 10-15%" not "make it warmer."

DETAILS:
- Goal is to make each image look like a REAL photograph, not AI-generated
- Reference the color/tone guidance from Lesson 72: "natural color grading, muted tones, cinematic color balance, realistic contrast"
- Avoid oversaturation — keep colors natural and earthy
- All edits should maintain the warm, family-friendly vibe
```

### Step 4.2 — Scene-by-Scene Edit Guidance

**Follow this loop for EVERY scene image:**

```
FOR each approved image from Phase 3:

  1. ANALYZE the image for:
     □ AI artifacts (extra fingers, warped text, impossible geometry)
     □ Lighting consistency with the rest of the set
     □ Color temperature match (all images should feel warm)
     □ Any unwanted objects or distractions
     □ Skin quality — does it look natural or plasticky?

  2. PROVIDE CANVA INSTRUCTIONS:
     - Specific Canva tools to use:
       * Magic Eraser → for removing AI artifacts
       * Background Remover → if background needs replacing
       * Adjust panel → brightness, contrast, warmth, saturation
       * Filters → only if needed for consistency (use "subtle" filters)
     - Exact values or ranges for adjustments

  3. PRESENT TO HUMAN:
     Show:
     - Scene number
     - Original image (from Phase 3)
     - List of suggested edits
     - Expected result description

  4. WAIT FOR CONFIRMATION:
     - "DONE" → you've made the edits in Canva, move to next image
     - "SKIP" → no edits needed for this image
     - "HELP" → you need more specific guidance

  NOTE: The human executes the Canva edits manually.
  The agent's job is to DIRECT the edits, not execute them.
```

### Step 4.3 — Batch Consistency Review

After all individual edits are done, do a final visual consistency pass:

```
CONSISTENCY CHECK (POST-EDIT):
□ All images have similar brightness levels
□ All images have matching color temperature (warm)
□ All images have consistent contrast
□ No image looks noticeably different from the others
□ The set looks like frames from the same video
□ If any image stands out, recommend specific adjustment values to bring it in line
```

---

## QUALITY GATE — PHASE 4

Before moving to Phase 5:

```
PHASE 4 DELIVERABLES:
1. ✅ Editing checklist provided for every scene image
2. ✅ All AI artifacts identified and marked for removal
3. ✅ Canva Adjust values specified for each image
4. ✅ Post-edit consistency check passed
5. ✅ All images look like they belong in the same video
6. ✅ Human has confirmed all edits are complete in Canva
```

Wait for "APPROVED" before proceeding to Phase 5.

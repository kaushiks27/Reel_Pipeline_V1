# PHASE 3 — IMAGE CREATION (SCENE-BY-SCENE)

> Coursework Reference: Step 3 — "ChatGPT and Midjourney/Nanobanana PRO for Image Creation" (Lesson 54)
> Feed this prompt to the agent after Phase 2 is approved.

---

## WHAT THIS PHASE DOES

Generate images for every scene in the shot list — one scene at a time, with human approval between each.

**Source (Lesson 54, Step 3 — exact coursework instructions):**
- Ask ChatGPT to write detailed prompts per scene (camera angle, lighting, emotion)
- Decide on POV (first-person or cinematic third-person)
- Consider visual consistency (hands, outfits, backgrounds, characters)
- Use character reference for consistency
- Put the prompts into Nanobanana PRO and generate images

---

## INSTRUCTIONS FOR THE AGENT

### Step 3.1 — Establish Anchor Character (First Generation)

**Source:** Lesson 20 — Beginner Workflow for Avatars, Steps 1-6

For the FIRST anchor scene image only:

```
ANCHOR CHARACTER ESTABLISHMENT PROTOCOL:

1. If this is the FIRST time generating Lola:
   - Use the prompt WITHOUT any reference image (Lesson 20, Step 4)
   - Goal: Find a face and look that works
   - Generate, review, pick the most realistic output
   - Download it — this becomes the reference image

2. If Lola's reference already exists (from Phase 0):
   - Upload the reference image BEFORE generating (Lesson 20, Step 6)
   - This locks the character identity
   - Use the reference for ALL subsequent anchor scene generations
```

> "These reference images tell NanoBanana PRO: 'Keep generating this same person.' This is what creates character consistency." — Lesson 20

### Step 3.2 — Generate Image Prompts (Using ChatGPT)

**Source:** Lesson 54, Step 3 — "Ask ChatGPT to write detailed prompts per scene"

For EACH scene in the shot list from Phase 2, generate a detailed image prompt.

**Prompt template for ANCHOR scenes (Lola talking to camera):**

```
PURPOSE: Write a Nanobanana PRO image prompt for an anchor scene where the character is facing the camera.

ROLE: Act as a world-class AI image prompt engineer.

STRUCTURE: The prompt must include ALL of the following elements:
1. Subject description (Lola — 55-60 year old Filipino grandmother)
2. Camera angle: [FROM PHASE 2 SCENE PLAN]
3. Lens specification: [35mm / 50mm / 85mm]
4. Lighting: [natural daylight / soft window light / warm lamp light]
5. Setting: [FROM PHASE 2 SCENE PLAN]
6. Expression and body language: [FROM PHASE 2 EMOTIONAL TONE]
7. Clothing: modest, age-appropriate Filipino everyday wear
8. Photorealism triggers (from Lesson 72):
   - "ultra-realistic" or "photorealistic"
   - "visible pores, skin micro-details, slight imperfections"
   - "natural bokeh, shallow depth of field"
   - "realistic shadows"
9. Negative prompts: "No cartoon style, no CGI, no 3D render, no plastic skin"
10. NSFW safety clause: "All characters fully clothed in age-appropriate attire. Setting is bright, well-lit, and family-friendly. Emotional tone: [positive emotion]. No conflict, no distress."

STYLE: Write the prompt as a single dense paragraph, like the examples in the UGC Avatar Prompt Vault (Lesson 22).

DETAILS:
- Vertical composition (9:16 aspect ratio)
- The character should look natural, not posed
- "UGC TikTok aesthetic" or "influencer content style" depending on scene
- Include camera/lens language to make it look like a real photo
```

**Prompt template for B-ROLL scenes (illustrative visuals):**

```
PURPOSE: Write a Nanobanana PRO image prompt for a B-roll scene illustrating: "[VISUAL DESCRIPTION FROM PHASE 2]"

ROLE: Act as a world-class AI image prompt engineer.

STRUCTURE: The prompt must include ALL of the following:
1. Scene description: [FROM PHASE 2 VISUAL DESCRIPTION]
2. Camera angle: [FROM PHASE 2 SCENE PLAN]
3. Lens specification: [35mm / 50mm]
4. Lighting: natural daylight or warm indoor lighting
5. Setting: Filipino home/school/outdoor environment
6. Characters: Filipino family members in positive interaction
7. Photorealism triggers (from Lesson 72):
   - "ultra-realistic cinematic photography"
   - "true-to-life textures"
   - "natural imperfections"
   - "realistic skin / materials / surfaces"
8. Camera language (from Lesson 72):
   - "shot on a [35mm/50mm] lens"
   - "shallow depth of field"
   - "natural bokeh"
9. Lighting language (from Lesson 72):
   - "natural light" or "soft window light"
   - "realistic shadows"
   - NO "neon glow", "magical light", "fantasy lighting"
10. Texture details (from Lesson 72):
    - "visible pores, fabric grain, skin micro-details"
    - "slight imperfections"
11. Color/tone (from Lesson 72):
    - "natural color grading, muted tones, cinematic color balance"
12. Negative prompts: "No cartoon style, no CGI, no 3D render, no plastic skin, no unrealistic lighting"
13. NSFW safety clause (MANDATORY — from Learnings Report):
    "All characters are fully clothed in age-appropriate attire. Setting is bright, well-lit, and family-friendly. Emotional tone: [positive emotion]. No conflict, no distress."

STYLE: Single dense paragraph. Reference the style of the Prompt Bank (Lesson 23) and UGC Avatar Prompt Vault (Lesson 22).
```

### Step 3.3 — Scene-by-Scene Generation Loop

**CRITICAL: Follow this loop for EVERY scene. Do not batch.**

```
FOR each scene in the Phase 2 shot list:

  1. GENERATE THE PROMPT
     - Use the appropriate template (ANCHOR or B_ROLL) from Step 3.2
     - Include the specific camera angle, lighting, and emotional tone from Phase 2

  2. GENERATE THE IMAGE
     - Tool: Nanobanana PRO (via Higgsfield)
     - For ANCHOR scenes: upload Lola's reference image (Lesson 20, Step 6)
     - For B_ROLL scenes: no reference needed (unless same character appears)

  3. PRESENT TO HUMAN
     Show:
     - Scene number and type (ANCHOR / B_ROLL)
     - The exact prompt used
     - The generated image
     - Self-assessment:
       □ Does it match the visual description from Phase 2?
       □ Is it photorealistic (not cartoon/CGI)?
       □ Is the lighting natural and warm?
       □ Are all characters clothed appropriately?
       □ Is the emotional tone positive?
       □ For ANCHOR: does Lola's face match the reference?
       □ No AI artifacts (extra fingers, text glitches, style inconsistency)?

  4. WAIT FOR APPROVAL
     - "APPROVED" → save image, move to next scene
     - "REDO" + feedback → regenerate with adjusted prompt
     - "SKIP" → mark as TODO, move to next scene

  5. SAVE
     - Save approved image as: scene_[NUMBER]_[TYPE].png
     - Example: scene_01_anchor.png, scene_02_broll.png
```

### Step 3.4 — Visual Consistency Check

**Source:** Lesson 54, Step 3 — "Consider visual consistency (hands, outfits, backgrounds, characters)"

After every 3-4 scenes, do a consistency review:

```
CONSISTENCY CHECK:
□ Lola's face is consistent across all anchor scenes (same reference used)
□ Lola's clothing is the same in all anchor scenes
□ Lighting style is consistent (all natural/warm, no sudden changes)
□ Color palette is consistent (warm tones throughout)
□ Filipino cultural elements are present and accurate
□ All settings feel like they belong in the same video
```

If inconsistency is found, flag it and offer to regenerate the inconsistent scene.

---

## QUALITY GATE — PHASE 3

Before moving to Phase 4, present:

```
PHASE 3 DELIVERABLES:
1. ✅ One approved image per scene (10-15 images total)
2. ✅ All ANCHOR images use the same Lola reference
3. ✅ All images pass the NSFW safety check
4. ✅ All images are photorealistic (no cartoon/CGI)
5. ✅ Visual consistency verified across all scenes
6. ✅ Files saved as scene_[NUMBER]_[TYPE].png
7. ✅ The exact prompt used for each image is documented
```

Present a gallery of all approved images in scene order. Wait for final "APPROVED" before Phase 4.

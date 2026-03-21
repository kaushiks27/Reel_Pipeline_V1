# PHASE 6 — AI VIDEO GENERATION (SCENE-BY-SCENE)

> Coursework Reference: Step 6 — "Kling / Veo 3 / Higgsfield for AI Video Generation" (Lesson 54)
> Feed this prompt to the agent after Phase 5 is approved.

---

## WHAT THIS PHASE DOES

Animate the upscaled images into video clips — one scene at a time, with human approval between each.

**Source (Lesson 54, Step 6 — exact coursework instructions):**
- Animate your images using Kling or Higgsfield or Google Veo 3
- Add any camera movement you like (dolly, zoom, tilt, pan)
- Match visuals to your script timing
- Add subtle motion, muted colours to each prompt on Kling

---

## TOOL SELECTION PER SCENE TYPE

**Source:** Lesson 53 — 8 Step Workflow (simplified avatar workflow):
"ChatGPT for prompts → Nanobanana PRO for images → Veo 3.1 for lip-sync or Kling for B-roll"

```
TOOL ROUTING:
- ANCHOR scenes (Lola talking to camera) → Veo 3.1 for lip-sync
- B_ROLL scenes (illustrative visuals)    → Kling 3.0 for motion

If Veo 3.1 fails (safety filter, etc.) → fallback to Kling 3.0 image-to-video
If Kling 3.0 fails → fallback to Higgsfield DoP
```

---

## INSTRUCTIONS FOR THE AGENT

### Step 6.1 — Write Video Motion Prompts

**Source:** Lesson 36 — Kling 3.0 UPDATE 2026

"This model works best if you upload the start image to ChatGPT and ask for detailed shot prompts."

**For Kling B-Roll scenes, use the 4-Field Prompt Structure (from Lesson 36):**

```
Shot:    [Type and duration — e.g., "Tight cinematic close-up, 3 seconds"]
Details: [What's happening in the scene — specific actions, textures, particles]
Camera:  [Movement and lens — from the Kling Camera Movement Toolkit, Lesson 33]
Mood:    [Emotional tone, lighting style, color palette]
```

**Example B-Roll prompt (from Lesson 36 style):**

```
Shot: Medium close-up, 3 seconds
Details: Filipino mother giving thumbs-up to son at homework desk, both beaming with pride. Warm lamp light illuminating the desk. Pencils and notebooks visible. Natural fabric textures on clothing.
Camera: Slow dolly in, 50mm lens, shallow depth of field
Mood: Warm pride, golden hour interior light, soft family warmth
```

**For Veo 3.1 Anchor scenes (lip-sync), use this structure (from Lesson 41):**

```
IMPORTANT RULES FOR VEO 3.1 PROMPTS (from Learnings Report, Section 3):
- NEVER reference speech, talking, lips moving, or dialogue in the visual prompt
- Veo's safety filter BLOCKS any mention of mouth movement
- Instead: describe clean face motion only — nods, expressions, eye movement
- Handle lip-sync separately (Veo generates the voice from the voice blueprint)

CORRECT VEO PROMPT FORMAT:
"[Visual description of Lola in the setting]. [Subtle natural movement — gentle nod,
warm expression, eyes engaging camera]. [Lighting description]. [Camera movement].
[Lola speaks]: '[EXACT DIALOGUE LINE with ... pauses]'
[Voice blueprint — copy-paste from Phase 0]: 'speaks with a subtle Filipino accent,
warm and nurturing tone, medium pace with natural pauses between ideas. voice carries
gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.'"
```

**Voice Blueprint Rules (from Lesson 41):**
- Copy-paste the EXACT same voice description into every Veo prompt — never change it
- Keep dialogue lines SHORT — Veo clips are ~8 seconds max
- Add "..." for natural pauses: "Rule one... greet people politely."
- The accent limits Veo's voice pool — this HELPS consistency
- Add punctuation generously — it gives the prompt rhythm

### Step 6.2 — Camera Movement Selection

**Source:** Lesson 33 — Kling AI Cinematic Camera Movement Toolkit

"IMPORTANT: Always start your prompt with the camera angle and build from there. Always create your images in a way that will complement the camera movement you have in mind."

Select camera movements that match each scene's emotional purpose:

```
CAMERA MOVEMENT GUIDE (from Lesson 33):

For EMOTIONAL INTENSITY (rule reveal, key moment):
→ Slow Dolly In — "cinematic slow dolly in toward [subject]"
→ Push-In Zoom on Face — "slow cinematic zoom in on [subject's] face"

For ESTABLISHING / CONTEXT:
→ Wide Static Shot — "wide static camera watching [action] in foreground"
→ Slow Pan Right — "slow pan right across [setting]"

For FOLLOWING ACTION:
→ Medium Tracking Shot — "medium tracking shot moving parallel to [subject]"
→ Smooth Tracking Behind — "camera smoothly tracking behind [subject]"

For REVEAL / SURPRISE:
→ Pull-Out Environmental Reveal — "starts on close-up, slowly pulls out to reveal [environment]"
→ Crane Shot Up — "crane shot rising above [subject], revealing [surroundings]"

For INTIMACY / CONNECTION:
→ Over-the-Shoulder — "over-the-shoulder shot of [subject]"
→ Close-Up with shallow depth — "tight close-up, shallow depth of field"

For B-ROLL DYNAMISM:
→ Subtle handheld — "slight camera shake, handheld feel"
→ Slow orbit — "camera slowly orbits around [subject]"
```

### Step 6.3 — Scene-by-Scene Video Generation Loop

**CRITICAL: One scene at a time. Generate, approve, then next.**

```
FOR each upscaled image from Phase 5:

  1. DETERMINE TOOL:
     - ANCHOR scene → Veo 3.1
     - B_ROLL scene → Kling 3.0

  2. WRITE THE VIDEO PROMPT:
     - For Kling: Use the 4-Field structure (Shot/Details/Camera/Mood)
     - For Veo: Use the voice blueprint format from Step 6.1
     - Camera movement from Step 6.2, matched to scene emotion
     - Duration: match the scene duration from Phase 2 (2-5 seconds)

  3. UPLOAD THE IMAGE:
     - Upload the upscaled image from Phase 5 as the start frame
     - For Kling: use image-to-video mode
     - For Veo: use image-to-video with voice prompt

  4. GENERATE THE VIDEO CLIP

  5. PRESENT TO HUMAN:
     Show:
     - Scene number and type
     - The exact prompt used
     - The generated video clip
     - Self-assessment:
       □ Does the motion look natural (not jerky or robotic)?
       □ Does the camera movement match what was requested?
       □ Does the clip duration match the target from Phase 2?
       □ For ANCHOR: does Lola's lip movement sync with the voice?
       □ For ANCHOR: does the voice match the blueprint (accent, tone, pace)?
       □ For B_ROLL: is the motion subtle and cinematic (not chaotic)?
       □ Are there any video artifacts (morphing faces, warping objects)?
       □ Does the lighting remain consistent with the source image?

  6. WAIT FOR APPROVAL:
     - "APPROVED" → save video clip, move to next scene
     - "REDO" + feedback → regenerate with adjusted prompt
     - "SKIP" → mark as TODO, move to next scene

  7. SAVE:
     - Save approved clip as: scene_[NUMBER]_[TYPE]_video.mp4
     - Example: scene_01_anchor_video.mp4
```

### Step 6.4 — Veo 3.1 Troubleshooting

**Source:** Learnings Report, Sections 3 and 5

If Veo 3.1 blocks a prompt:

```
VEO SAFETY FILTER WORKAROUND:
1. Remove ALL references to speech, talking, lips, dialogue from the visual prompt
2. Use only clean motion descriptions: "gentle nod", "warm expression", "eyes engaging camera"
3. If still blocked: Try the two-stage pipeline:
   - Stage 1: Generate clean face motion in Veo (no speech)
   - Stage 2: Strip Veo's auto-generated audio
   - Stage 3: Add lip-sync separately using Kling lip-sync API

FALLBACK CHAIN:
Veo 3.1 → Kling 3.0 image-to-video → Higgsfield DoP
```

### Step 6.5 — Motion Quality Guidelines

**Source:** Lesson 54, Step 6 — "Add subtle motion, muted colours to each prompt on Kling"

```
MOTION RULES:
- Keep motion SUBTLE for most scenes — small movements, gentle camera drift
- Avoid extreme camera movements unless the scene demands it
- B-roll should feel like watching a real moment unfold, not an action sequence
- Match the warm, nurturing vibe — no fast cuts, no shaky-cam chaos
- Muted colors in the prompt help Kling produce more cinematic output
- Duration must match Phase 2 scene timing (usually 2-5 seconds per clip)
```

---

## QUALITY GATE — PHASE 6

Before moving to Phase 7:

```
PHASE 6 DELIVERABLES:
1. ✅ One approved video clip per scene (10-15 clips total)
2. ✅ All ANCHOR clips have lip-sync matching the script dialogue
3. ✅ All ANCHOR clips use the same voice (voice blueprint consistency)
4. ✅ All B_ROLL clips have natural, subtle motion
5. ✅ Camera movements match what was planned in Phase 2
6. ✅ Clip durations match Phase 2 scene timing
7. ✅ No video artifacts (morphing, warping, glitching)
8. ✅ Files saved as scene_[NUMBER]_[TYPE]_video.mp4
9. ✅ The exact prompt used for each video is documented
```

Present all clips in scene order for a final review. Wait for "APPROVED" before Phase 7.

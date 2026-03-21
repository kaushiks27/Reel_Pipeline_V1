# Phase 0 — Manual Tasks (with Exact Prompts)

> Complete these 3 tasks, then tell me you're done. We move to Phase 1.

---

## Task 1: Create Lola Reference Image

**Tool:** Nanobanana PRO (via Higgsfield)
**Source:** Lesson 20, Lesson 22, Lesson 72

### Step-by-Step

**Set these in the Nanobanana PRO toolbar FIRST:**

| Setting | Set To | How |
|---------|--------|-----|
| Model | **Nano Banana Pro** | Already selected |
| Aspect Ratio | **3:4** | Click the ratio button — 3:4 for reference portrait |
| Resolution | **1K** | Already set |
| Image Count | **4** | Use the **+** button until it shows 4/4 |
| Reference (@) | **Empty** | Do NOT click @ — leave empty for first gen |
| Extra Free Gens | **ON** (green) | Toggle should be green |
| Draw | **OFF** | Do not enable |

**Then follow these steps:**

1. Open Nanobanana PRO in Higgsfield
2. **Leave the reference image section empty** (first generation only — Lesson 20, Step 4)
3. Paste the prompt below into the prompt box
4. Click **Generate**
5. Review outputs → pick the most realistic face
6. Download it
7. Upload it back as a **character reference** for ALL future generations (Lesson 20, Step 6)
8. Save the final file as `assets/lola_reference.png` in the workspace

### Exact Prompt (copy-paste this)

```
Ultra-realistic, true-to-life cinematic portrait of a 55-60 year old Filipino grandmother, warm and nurturing expression, natural beauty. She has medium-deep warm brown skin with visible natural skin texture, faint age spots on cheeks, slight crow's feet around eyes, visible pores across T-zone, skin micro-details and slight imperfections that make the portrait feel authentic. Soft wrinkles around the eyes and mouth from a lifetime of smiling. Hair is black with natural grey streaks, neatly pulled back in a low bun with tiny loose strands near the temples.

She is wearing a modest, clean, light-colored Filipino everyday blouse with visible fabric grain and natural wrinkles in the cloth. Small pearl stud earrings with realistic metallic reflections. Her expression is a warm, welcoming, genuine smile — gentle authority and maternal warmth, like she's about to share life advice with her grandchildren.

Shot on a 50mm portrait lens at f/2.0, shallow depth of field with creamy warm background bokeh. Soft natural window light entering from camera-left, creating gentle highlights on cheekbones and realistic shadow falloff under chin and jawline. Warm ambient light (5200K) with natural color grading, realistic contrast, muted earthy tones. Subtle film grain and sensor noise in shadows for organic realism.

Setting is a bright, well-lit Filipino home interior — warm wooden furniture softly blurred in background, natural daylight streaming through windows. Foreground/background separation. Vertical 9:16 framing.

Surfaces show real-world micro-texture: visible skin pores, natural fabric grain, realistic surface detail. High dynamic range, highlights roll off smoothly with no clipping, blacks retain detail. Clean but not overly polished.

No cartoon style, no CGI, no 3D render, no game engine, no plastic skin, no unrealistic lighting, no text, no logo, no watermark. No over-smoothing, no artificial glow. All characters fully clothed in age-appropriate attire. Setting is bright, well-lit, and family-friendly. Emotional tone: warm, nurturing. No conflict, no distress.
```

### Why This Prompt Works (Lesson 72 Categories Used)

| Category | Triggers Used |
|----------|--------------|
| 1. Core Photorealism | "ultra-realistic", "true-to-life", "natural imperfections", "authentic" |
| 2. Camera & Lens | "50mm portrait lens", "f/2.0", "shallow depth of field", "creamy bokeh" |
| 3. Lighting | "soft natural window light", "warm ambient light (5200K)", "realistic shadow falloff" |
| 4. Texture & Detail | "visible pores", "skin micro-details", "fabric grain", "slight imperfections" |
| 5. Color & Tone | "natural color grading", "muted earthy tones", "realistic contrast" |
| 6. Composition | "foreground/background separation", "vertical 9:16 framing" |
| 7. Grain & Quality | "subtle film grain", "sensor noise in shadows", "clean but not overly polished" |
| 8. Negatives | "no cartoon", "no CGI", "no 3D render", "no plastic skin", "no unrealistic lighting" |

### If the first result isn't realistic enough

Ask ChatGPT: *"This doesn't look real enough to me, can we add some more detail to the prompt?"* (Lesson 72 tip)

### Done when:
- [ ] `assets/lola_reference.png` exists in workspace
- [ ] Image uploaded as character reference in Higgsfield for future use
- [ ] Face looks realistic — check: visible pores, natural lighting, no plastic skin

---

## Task 2: Configure & Test Lola's Voice in ElevenLabs

**Tool:** ElevenLabs
**Source:** Lesson 41, Phase 0 Setup
**Voice ID:** `YNTPwYwh85yYASHOSs7H` ✅ (already saved to `.env`)

### Step-by-Step (beginner walkthrough)

**Step 1 — Open ElevenLabs**
1. Go to [elevenlabs.io](https://elevenlabs.io) in your browser
2. Sign in with your account (or sign up if you haven't yet)
3. You'll land on the main dashboard

**Step 2 — Go to Text to Speech**
1. In the left sidebar, click **"Text to Speech"** (it has a speaker icon)
2. You'll see a big text box in the center — this is where you type what the voice will say

**Step 3 — Select the voice**
1. Near the top of the text box, you'll see a voice name (it might say "Rachel" or some default voice)
2. Click on that voice name — a dropdown/panel will open
3. Click **"Add Voice"** or search in the voice library
4. In the search bar, paste this Voice ID: `YNTPwYwh85yYASHOSs7H`
   - Or if search by ID isn't available, browse until you find the voice you liked
5. Click the voice to select it — it should now show as the active voice

**Step 4 — Select the model**
1. Look for a **"Model"** dropdown (usually near the voice selector or in settings)
2. Click it and select: **`Eleven Multilingual v2`**
   - This is important — it handles accents much better than the default English model

**Step 5 — Adjust voice settings**
1. Look for a **"Voice Settings"** panel (sometimes you need to click a gear ⚙️ icon or "Settings" link near the voice selector)
2. You'll see slider controls. Set them to:

| Slider | Set To | What to look for |
|--------|--------|------------------|
| **Stability** | **67%** (middle of 65–70) | Drag the slider to about ⅔ from left |
| **Clarity + Similarity Enhancement** | **75%** | Drag to about ¾ from left |
| **Style Exaggeration** | **30%** | Drag to about ⅓ from left |
| **Speaker Boost** | **OFF** | Make sure this toggle is off |

> 💡 **Tip:** If you don't see all sliders, look for an "Advanced" or "Show more" link.

**Step 6 — Test with Line 1**
1. In the big text box, delete any existing text
2. Copy-paste this exactly:
```
Rule one... greet people politely. When your child sees you greet others with warmth... they learn respect without you saying a word.
```
3. Click the **"Generate"** button (or play ▶️ button)
4. Listen to the output. Ask yourself:
   - Does it sound warm and maternal? ✅
   - Does it pause naturally at the `...` marks? ✅
   - Does it sound like a real person, not a robot? ✅

**Step 7 — Test with Line 2**
1. Clear the text box, paste:
```
Start small. One habit... just one... can change everything.
```
2. Generate and listen. This line should be under 8 seconds (important for Veo 3.1 lip-sync later)

**Step 8 — Test with Line 3**
1. Clear the text box, paste:
```
Try this tonight... and watch what happens.
```
2. Generate and listen. This is the CTA (call-to-action) style — should feel convincing but gentle

**Step 9 — Adjust if needed**
- If the voice sounds **too robotic/flat**: increase Style to 35–40%
- If the voice sounds **too dramatic/theatrical**: decrease Style to 20–25%
- If the voice **rushes through pauses**: increase Stability to 70–75%
- If the voice sounds **monotone**: decrease Stability to 60%

**Step 10 — Lock these settings**
Once you're happy with how the 3 test lines sound:
1. **Don't change these settings again** — they're locked for the Lola character
2. The Voice ID is already saved in your `.env` file ✅

### Exact Voice Blueprint (copy-paste into every Veo prompt)

This is the text description you'll paste into Veo 3.1 prompts (not ElevenLabs — this is for video generation):
```
speaks with a subtle Filipino accent, gentle rhythm, soft welcoming tone. speech flows smoothly with small pauses that feel natural and reassuring. warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

### Fallback if voice drifts later (Lesson 41)

If voices become inconsistent across videos:
1. Go to [ElevenLabs Voice Changer](https://elevenlabs.io/app/speech-synthesis/speech-to-speech)
2. Click the **"Voice Changer"** tab in the left sidebar
3. Select the same voice you chose above
4. Upload the video file that has the drifted voice
5. Click **Generate** — it will re-voice the entire video with the locked voice

### Done when:
- [x] Voice ID saved to `.env` ✅
- [ ] Voice settings configured (Stability 67%, Clarity 75%, Style 30%)
- [ ] All 3 test lines generated and sound warm/natural
- [ ] You're happy with how Lola sounds

---

## Task 3: Fill in Remaining API Keys

**File:** `.env` in the workspace root

Open `.env` and fill in the values you have:

```
OPENAI_API_KEY=           ← your OpenAI key
GOOGLE_AI_STUDIO_API_KEY= ← your Google AI Studio key
KLING_ACCESS_KEY=         ← your Kling access key
KLING_SECRET_KEY=         ← your Kling secret key
HIGGSFIELD_API_KEY=       ← your Higgsfield key
HIGGSFIELD_API_SECRET=    ← your Higgsfield secret
```

Already saved:
- [x] `ELEVENLABS_API_KEY` ✅

### Done when:
- [ ] All keys you have are filled in

---

## Summary

| # | Task | Time Est. | Key Source |
|---|------|-----------|-----------|
| 1 | Create Lola reference image | ~15 min | Lessons 20, 22, 72 |
| 2 | Choose & test Lola's voice | ~10 min | Lesson 41 |
| 3 | Fill in API keys | ~2 min | Learnings Report §4 |

**When all 3 are done, tell me and we move to Phase 1.**

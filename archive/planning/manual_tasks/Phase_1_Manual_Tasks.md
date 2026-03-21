# Phase 1 — Manual Tasks

> Complete this before we begin Phase 2.

---

## Task 1: Create Animated Lola Reference Image

**Tool:** Nanobanana PRO (via Higgsfield)
**Source:** Lesson 20, Client Brief (animated style)

### Why This Is Needed
The existing `assets/lola_reference.png` is **photorealistic**. The client brief requires **soft Pixar-adjacent animated illustrations**. We need a new Lola reference in the animated style so all future images are consistent.

### Set these in the Nanobanana PRO toolbar FIRST:

| Setting | Set To | How |
|---------|--------|-----|
| Model | **Nano Banana Pro** | Already selected |
| Aspect Ratio | **3:4** | Click the ratio button — 3:4 for reference portrait |
| Resolution | **1K** | Already set |
| Image Count | **4** | Use the **+** button until it shows 4/4 |
| Reference (@) | **Upload your existing `lola_reference.png`** | Click **@** → select `assets/lola_reference.png` from your computer. This tells the tool to keep the same face identity but render in the new style |
| Extra Free Gens | **ON** (green) | Toggle should be green |
| Draw | **OFF** | Do not enable |

> **💡 Key difference from Phase 0:** This time you ARE uploading the photorealistic Lola as a reference. The tool will use her face structure but apply the animated style from the prompt. This creates consistency between the two versions.

### Then follow these steps:

1. Open Nanobanana PRO in Higgsfield
2. Make sure the existing `lola_reference.png` is uploaded via the **@** button
3. Paste the prompt below into the prompt box
4. Click **Generate**
5. Review 4 outputs → pick the one that:
   - Looks most like a warm Pixar/Disney-adjacent character
   - Has the same face identity as the original Lola
   - Feels bright, warm, and approachable (NOT photorealistic)
6. Download it
7. Save it as `assets/lola_animated_reference.png` in the workspace
8. **Upload this new animated image back into the @ reference** for ALL future scene generations
9. **Keep the old `lola_reference.png`** — don't delete it (useful as identity backup)

### Exact Prompt (copy-paste this)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character, Pixar-adjacent 3D illustration style. Expressive, kind face with warm brown skin, gentle smile lines around her eyes, black hair with natural grey streaks pulled back in a neat low bun. She has a warm, welcoming, genuine smile — the kind of grandmother who always has good advice and a warm hug.

She is wearing a modest, clean, light-colored Filipino everyday blouse — simple and culturally appropriate. Small pearl stud earrings. Her expression radiates gentle authority and maternal warmth, like she's about to share wisdom with her grandchildren.

Setting is a bright, warm-lit Filipino home interior — wooden furniture, warm lighting streaming through windows, potted plants, family photos on the wall. The atmosphere is cozy, inviting, and distinctly Filipino.

Art style: soft 3D animated illustration, warm color palette, smooth rounded features, expressive cartoon-proportioned eyes, bright natural lighting, pastel and earthy warm tones. Similar to Pixar or Disney short film character design. Clean line work, soft shadows, gentle ambient occlusion.

Vertical 9:16 framing, character centered, upper body and face visible, facing camera directly, eye contact with viewer.

NOT photorealistic. NOT dark or cinematic. NOT anime or manga style. NOT flat 2D. NOT creepy or uncanny valley. Warm, bright, family-friendly, approachable, culturally Filipino.
```

### How This Prompt Is Built (Coursework Grounding)

This is a **new prompt** built by adapting the Lesson 22 + Lesson 72 structure for animated style. Here's how each section maps:

**Lesson 22 structural pattern adapted (compare to UGC Avatar Prompt Vault):**

| Prompt Section | Lesson 22 Pattern | What We Changed for Animated Style |
|---------------|-------------------|------------------------------------|
| Line 1: Subject description | "Ultra-realistic 25-year-old influencer woman..." | → "Warm, soft animated illustration of a 55-60 year old Filipino grandmother" |
| Line 2: Clothing & accessories | "wearing a fitted sheer black top, gold hoop earrings..." | → "modest Filipino everyday blouse, small pearl stud earrings" |
| Line 3: Setting & environment | "luxury hotel bathroom, marble walls..." | → "bright Filipino home interior, wooden furniture, potted plants" |
| Line 4: Art style & rendering | "hyper-realistic, DSLR-level detail, 4K realism" | → "soft 3D animated illustration, Pixar, warm color palette, smooth rounded features" |
| Line 5: Framing & composition | "vertical TikTok-style composition" | → "Vertical 9:16, character centered, facing camera, eye contact" |
| Line 6: Negatives | "no cartoon style, no CGI, no 3D render" | → **INVERTED**: "NOT photorealistic, NOT dark, NOT anime" (we WANT stylized) |

**Lesson 72 categories adapted for animation:**

| Lesson 72 Category | Photorealistic Trigger (original) | Animated Equivalent (used here) |
|--------------------|----------------------------------|--------------------------------|
| 1. Core Style | "ultra-realistic, photorealistic" | "soft animated illustration, Pixar-adjacent" |
| 2. Camera & Lens | "50mm lens, shallow DoF, bokeh" | "character centered, upper body visible, eye contact" |
| 3. Lighting | "soft natural window light, warm ambient 5200K" | "bright natural lighting, warm lighting through windows" |
| 4. Texture & Detail | "visible pores, skin micro-details" | "smooth rounded features, gentle smile lines, expressive eyes" |
| 5. Color & Tone | "natural color grading, muted earthy tones" | "warm color palette, pastel and earthy warm tones" |
| 6. Composition | "foreground/background separation, vertical framing" | "vertical 9:16, character centered, cozy interior backdrop" |
| 7. Quality & Finish | "subtle film grain, clean but not overly polished" | "clean line work, soft shadows, gentle ambient occlusion" |
| 8. Negatives | "no cartoon, no CGI, no 3D render" | "NOT photorealistic, NOT dark, NOT anime, NOT flat 2D" |

### If the first result isn't quite right

**Problem → Fix:**
- Too photorealistic → Add "more stylized, more cartoon-like, rounder features" to the prompt
- Too childish/cartoony → Add "mature illustration, elegant character design, subtle stylization"
- Wrong skin tone → Specify "warm medium-brown Filipino skin tone, not pale, not dark"
- Face doesn't match original Lola → Make sure the **@ reference** is uploaded with the original photorealistic image
- Or ask ChatGPT: *"Make this prompt more Pixar-like and less photorealistic"*

### Done when:
- [ ] `assets/lola_animated_reference.png` exists in the workspace
- [ ] Image looks like a warm Pixar-adjacent animated grandmother
- [ ] Face is recognizably the same person as the original Lola (similar features)
- [ ] Uploaded as the new **@ reference** in Nanobanana PRO for future generations

---

## Summary

| # | Task | Time Est. |
|---|------|-----------|
| 1 | Create animated Lola reference | ~10 min |

**When done, tell me and we proceed to Phase 2: Script & Voice Planning.**

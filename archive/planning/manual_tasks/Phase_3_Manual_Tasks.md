# Phase 3 — Manual Tasks: Image Creation (12 Scenes)

> Generate one image per scene in Nanobanana PRO. Follow the order below.
> After generating all 12, tell me and we'll review together before Phase 4.

---

## Before You Start

### Step 0 — Create the @Lola Element (Do This ONCE)

Before generating any scenes, you need to create a named character element for Lola. This is how Nanobanana PRO keeps her face consistent across all anchor scenes.

1. Click the **@** button in the toolbar
2. You'll see the **"New element"** window
3. Fill in:

| Field | Set To |
|-------|--------|
| **Upload images** | Click **+** → upload `assets/lola_animated_reference.png` **twice** (the tool requires min 2 images — upload the same animated image two times) |
| **Element name** | `Lola` |
| **Category** | Leave as **Auto** |
| **Description** | `55-60 year old Filipino grandmother, warm brown skin, gentle smile lines, black hair with grey streaks in a low bun, pearl stud earrings, modest light-colored Filipino blouse, warm welcoming expression, Pixar-adjacent animated style` |

4. Click **Create**

> 💡 **Why upload the animated image twice (not the photorealistic one)?** If you upload the photorealistic Lola, the tool may pull output toward photorealism. We want purely animated output, so give it only animated references. The style is controlled by both the reference AND the prompt.

Now when writing prompts, type **`@Lola`** in the prompt box and the tool will reference this element.

---

### Tool Settings — Lock These FIRST

**For ALL ANCHOR scenes (Lola talking to camera):**

| Setting | Set To | Why |
|---------|--------|-----|
| Model | **Nano Banana Pro** | Locked tool |
| Aspect Ratio | **9:16** | Video frame format |
| Resolution | **1K** | Upscaled in Phase 5 |
| Image Count | **4** | Pick the best from 4 |
| Reference (@) | **Type `@Lola` in the prompt** | This references the element you created in Step 0 |
| Extra Free Gens | **ON** (green) | More options |
| Draw | **OFF** | Not needed |

**For ALL B-ROLL scenes (family illustrations):**

| Setting | Set To | Why |
|---------|--------|-----|
| Model | **Nano Banana Pro** | Locked tool |
| Aspect Ratio | **9:16** | Video frame format |
| Resolution | **1K** | Upscaled in Phase 5 |
| Image Count | **4** | Pick the best from 4 |
| Reference (@) | **Do NOT type @Lola** | B-roll scenes have different characters — no reference needed |
| Extra Free Gens | **ON** (green) | More options |
| Draw | **OFF** | Not needed |

> ⚠️ **Key rule:** Include `@Lola` in the prompt for ANCHOR scenes. Do NOT include it for B-ROLL scenes (otherwise all characters will look like Lola).

### How to Pick the Best Image

For each generation of 4, pick the one that:
- ✅ Looks most like a warm Pixar/Disney-adjacent animated illustration
- ✅ Is bright and warm — NOT dark or cinematic
- ✅ Has the right Filipino cultural markers (clothing, setting, skin tone)
- ✅ For ANCHOR scenes: Lola's face matches the reference
- ✅ Composition matches 9:16 vertical format
- ❌ NO photorealistic images — reject any that look like photos
- ❌ NO anime/manga style — reject any that look like Japanese animation

### File Naming

Save each image as:
```
assets/scenes/scene_01_anchor.png
assets/scenes/scene_02_anchor.png
assets/scenes/scene_03_broll.png
...
```

Create the `assets/scenes/` folder first.

---

## Scene 1 — HOOK (ANCHOR)

**Type:** ANCHOR (upload Lola reference)
**Duration:** 3 seconds
**Voiceover:** "Want your child to grow up respectful? Start with these three."
**Camera:** Slow dolly in (Lesson 33 #2)
**Save as:** `assets/scenes/scene_01_anchor.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character (Lola), Pixar-adjacent 3D illustration style. Medium close-up framing showing face and shoulders, facing camera directly with warm welcoming eye contact. She has warm brown skin, gentle smile lines, black hair with grey streaks in a neat low bun, small pearl stud earrings, wearing a modest light-colored Filipino everyday blouse.

She is sitting in a bright, warm-lit Filipino living room — wooden furniture, warm daylight streaming through windows, potted plants, family photos on the wall. Her expression is inviting and confident, the look of someone about to share important wisdom. Slight warm smile, eyebrows gently raised.

Art style: soft 3D animated illustration, warm golden color palette, smooth rounded features, expressive cartoon-proportioned eyes, bright natural lighting, pastel and earthy warm tones, Pixar or Disney short film character design. Clean line work, soft shadows, gentle ambient occlusion.

Vertical 9:16 framing, character centered, upper body visible, facing camera directly. Composition designed for slow dolly-in camera movement — leave space around the subject.

NOT photorealistic. NOT dark or cinematic. NOT anime or manga style. NOT flat 2D. Warm, bright, family-friendly, approachable, culturally Filipino. All characters fully clothed in age-appropriate attire. Setting bright, well-lit, and family-friendly. Emotional tone: warm invitation.
```

---

## Scene 2 — Habit 1 Intro (ANCHOR)

**Type:** ANCHOR (upload Lola reference)
**Duration:** 2.5 seconds
**Voiceover:** "Rule one... greet people politely."
**Camera:** Static locked (Lesson 33 #16)
**Save as:** `assets/scenes/scene_02_anchor.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character (Lola), Pixar-adjacent 3D illustration style. Medium close-up, face and shoulders, facing camera with gentle authoritative expression. She is speaking, mouth slightly open, one hand raised in a calm teaching gesture. Warm brown skin, gentle smile lines, black hair with grey streaks in low bun, pearl stud earrings, modest Filipino blouse.

Same bright Filipino living room — wooden furniture, warm window light, potted plants. Her expression shows calm wisdom, like a teacher beginning a lesson. Slight head nod, gentle authority.

Art style: soft 3D animated illustration, warm golden tones, smooth rounded features, expressive eyes, bright natural lighting, Pixar character design. Clean line work, soft shadows.

Vertical 9:16 framing, character centered, static composition designed for locked camera — subject fills center frame.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly, culturally Filipino. All characters fully clothed. Emotional tone: gentle authority.
```

---

## Scene 3 — Mano Po (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "When your child sees you do 'mano po' to your elders..."
**Camera:** Static wide with foreground movement (Lesson 33 #16)
**Save as:** `assets/scenes/scene_03_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a young Filipino child (age 7-8) performing "mano po" — gently pressing an elderly grandmother's hand to their forehead in a sign of respect. Pixar-adjacent 3D illustration style. Both characters smiling warmly, genuine affection between them. The grandmother sits in a wooden chair, the child stands beside her, leaning in respectfully.

Setting is a bright Filipino home interior — warm wooden furniture, tiled floor, warm daylight streaming through open windows, potted plants on windowsills, santo figure on a shelf. The room feels lived-in, cozy, distinctly Filipino.

Both characters have warm medium-brown Filipino skin tones, culturally appropriate everyday clothing. The grandmother wears a house dress, the child wears a school uniform or casual play clothes. Expressions are joyful and tender.

Art style: soft 3D animated illustration, warm golden color palette, smooth rounded features, expressive eyes, bright natural lighting, pastel earthy tones, Pixar short film quality. Clean line work, soft shadows, gentle ambient occlusion.

Wide static composition in vertical 9:16 framing, both characters visible full body, room environment establishing the Filipino home setting. Designed for static camera with foreground character movement.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed in age-appropriate attire. Setting bright and well-lit. Emotional tone: family warmth, tradition, respect. No conflict, no distress.
```

---

## Scene 4 — Greeting Neighbor (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "...they learn respect... without you saying a word."
**Camera:** Medium tracking alongside (Lesson 33 #22)
**Save as:** `assets/scenes/scene_04_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a young Filipino child (age 7-8) cheerfully waving "hello" to an elderly neighbor standing at a gate. Pixar-adjacent 3D illustration style. The child's face is bright and happy, a natural genuine smile. The neighbor waves back warmly.

Setting is a sunny Filipino barangay street — a modest concrete fence with an iron gate, tropical plants and flowers, bright morning sunshine, a mango tree nearby, clean narrow street. The atmosphere is warm, neighborly, distinctly Filipino residential.

Both characters have warm medium-brown Filipino skin tones. The child wears casual play clothes. The neighbor wears a comfortable house dress or polo shirt. Natural, everyday clothing.

Art style: soft 3D animated illustration, warm golden-green color palette reflecting morning sunlight and tropical greenery, smooth rounded features, expressive cartoon eyes, bright natural outdoor lighting, Pixar quality. Clean line work, soft shadows.

Vertical 9:16 framing, medium shot showing the child in the foreground and neighbor at the gate. Composition designed for medium tracking shot alongside the child — sense of forward movement.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed. Emotional tone: joy, natural respect, community warmth. No conflict, no distress.
```

---

## Scene 5 — Habit 2 Intro (ANCHOR)

**Type:** ANCHOR (upload Lola reference)
**Duration:** 2.5 seconds
**Voiceover:** "Two... say 'thank you' at the dinner table."
**Camera:** Static locked (Lesson 33 #16)
**Save as:** `assets/scenes/scene_05_anchor.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character (Lola), Pixar-adjacent 3D illustration style. Medium close-up, face and shoulders, facing camera. She is speaking mid-sentence, warm expression, two fingers raised gently to indicate "rule two." Warm brown skin, smile lines, black hair with grey streaks in low bun, pearl earrings, modest Filipino blouse.

Same bright Filipino living room as previous anchor scenes. Warm window light, wooden furniture, potted plants. Consistent setting.

Art style: soft 3D animated illustration, warm golden tones, smooth rounded features, expressive eyes, bright lighting, Pixar design. Clean line work, soft shadows.

Vertical 9:16 framing, character centered, static composition for locked camera.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. Emotional tone: calm wisdom.
```

---

## Scene 6 — Family Dinner (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "A small word... repeated every day..."
**Camera:** Slow pan right (Lesson 33 #9)
**Save as:** `assets/scenes/scene_06_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a Filipino family eating dinner together at a wooden dining table. Pixar-adjacent 3D illustration style. A young child (age 7-8) is saying "Salamat, Nanay" (thank you, Mom) with a sweet smile as the mother serves rice and ulam (Filipino home-cooked dishes). The father sits nearby, smiling proudly. Dishes on the table include a pot of rice, a viand dish, a soup bowl — typical Filipino family dinner.

Setting is a bright, warm Filipino kitchen-dining area — warm overhead light, wooden table and chairs, a window showing early evening sky, simple but cozy. The table has a plastic tablecloth or a woven placemat. The atmosphere is warm, communal, family bonding.

All characters have warm medium-brown Filipino skin tones, wearing everyday comfortable home clothes. Natural, unpretentious.

Art style: soft 3D animated illustration, warm amber-golden color palette reflecting dinnertime warm lighting, smooth rounded features, expressive eyes, bright warm indoor lighting, Pixar quality. Clean line work, soft shadows.

Wide composition in vertical 9:16 framing showing the family at the table. Designed for slow pan right — the composition extends horizontally so panning reveals more of the family and table.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed. Emotional tone: gratitude, togetherness, family warmth. No conflict, no distress.
```

---

## Scene 7 — Clearing Table (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "...becomes a lifetime habit."
**Camera:** Over-the-shoulder (Lesson 33 #5)
**Save as:** `assets/scenes/scene_07_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration showing a young Filipino child (age 7-8) carefully carrying plates from the dining table to the kitchen sink, stepping carefully and concentrating. Pixar-adjacent 3D illustration style. In the background, the mother watches with a proud, tender smile, arms loosely crossed, leaning against the doorframe.

Setting is the same Filipino home kitchen — clean tiles, wooden cabinets, warm lighting. The child walks from the table toward the sink. The mother's expression is pure pride and affection.

Both characters have warm medium-brown Filipino skin tones, home clothes. The child looks focused and helpful, a small sense of responsibility on their face.

Art style: soft 3D animated illustration, warm golden tones, smooth features, expressive eyes, warm indoor lighting, Pixar quality. Clean line work, soft shadows.

Vertical 9:16 framing, over-the-shoulder composition — camera is positioned behind the mother looking past her shoulder toward the child carrying plates. The mother is in foreground (partial, shoulder/head visible), child is the focal point in mid-ground.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed. Emotional tone: pride, nurturing, responsibility. No conflict, no distress.
```

---

## Scene 8 — Habit 3 Intro (ANCHOR)

**Type:** ANCHOR (upload Lola reference)
**Duration:** 2.5 seconds
**Voiceover:** "Three... let them help around the house."
**Camera:** Static locked (Lesson 33 #16)
**Save as:** `assets/scenes/scene_08_anchor.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character (Lola), Pixar-adjacent 3D illustration style. Medium close-up, face and shoulders, facing camera. She is speaking, encouraging expression, three fingers raised gently to indicate "rule three." Warm, confident smile. Warm brown skin, smile lines, black hair with grey streaks in low bun, pearl earrings, modest Filipino blouse.

Same bright Filipino living room. Warm window light, wooden furniture, consistent setting with previous anchor scenes.

Art style: soft 3D animated illustration, warm golden tones, smooth rounded features, expressive eyes, bright lighting, Pixar design. Clean line work, soft shadows.

Vertical 9:16 framing, character centered, static composition for locked camera.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. Emotional tone: encouraging, warm.
```

---

## Scene 9 — Watering Plants (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "When they help... they feel responsible."
**Camera:** Static wide with foreground movement (Lesson 33 #16)
**Save as:** `assets/scenes/scene_09_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a young Filipino child (age 7-8) happily watering potted plants in a small Filipino home garden. Pixar-adjacent 3D illustration style. The child holds a plastic watering can, carefully pouring water on leafy plants and herbs in clay pots. Their expression is cheerful and focused, enjoying the simple task.

Setting is a bright Filipino home garden or small yard — concrete pathway, potted plants arranged along a wall, tropical flowers (sampaguita, bougainvillea), morning sunshine, green leaves glistening. A simple clothesline or a wooden fence in the background. Distinctly Filipino residential garden.

The child has warm medium-brown Filipino skin, wearing casual play clothes (shorts and t-shirt), barefoot or wearing tsinelas (flip-flops).

Art style: soft 3D animated illustration, warm green-golden color palette reflecting morning sunshine through tropical plants, smooth rounded features, expressive eyes, bright outdoor natural lighting, Pixar quality. Clean line work, soft shadows, dappled sunlight through leaves.

Wide composition in vertical 9:16 framing, child in center of frame surrounded by plants. Static camera with the child moving through the garden, watering different pots.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed. Emotional tone: independence, growth, joy. No conflict, no distress.
```

---

## Scene 10 — Family Chores Together (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 3.5 seconds
**Voiceover:** "And a responsible child... is a respectful child."
**Camera:** Medium tracking alongside (Lesson 33 #22)
**Save as:** `assets/scenes/scene_10_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a Filipino family doing chores together in their home or yard. Pixar-adjacent 3D illustration style. A father and young child (age 7-8) sweep the yard together with walis tambo (Filipino broom), while the mother hangs laundry on a clothesline nearby. Everyone is smiling, talking, enjoying the work as a team. The child mimics the father's sweeping motion.

Setting is a bright Filipino home yard — concrete ground, simple fence, clothesline with colorful clothes, tropical plants, morning sunshine. Neighboring houses visible in background. The atmosphere is warm, communal, and active.

All characters have warm medium-brown Filipino skin tones, wearing casual comfortable home clothes. Father in a t-shirt and shorts, mother in a house dress, child in play clothes.

Art style: soft 3D animated illustration, warm golden-green color palette, smooth rounded features, expressive eyes, bright morning outdoor lighting, Pixar quality. Clean line work, soft shadows.

Vertical 9:16 framing, family spread across the frame with the child and father in center. Composition designed for medium tracking shot alongside — sense of lateral movement past the family.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. All characters fully clothed. Emotional tone: teamwork, family bond, responsibility. No conflict, no distress.
```

---

## Scene 11 — CTA / Closing (ANCHOR)

**Type:** ANCHOR (upload Lola reference)
**Duration:** 3 seconds
**Voiceover:** "Try just one tonight... and watch what happens."
**Camera:** Push-in zoom (Lesson 33 #12)
**Save as:** `assets/scenes/scene_11_anchor.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a 55-60 year old Filipino grandmother character (Lola), Pixar-adjacent 3D illustration style. Medium close-up becoming closer — face filling more of the frame. She faces camera with a warm, personal, knowing smile, like she's sharing a secret with a close friend. Gentle nod. Her eyes are kind and confident, direct eye contact. Warm brown skin, smile lines, black hair with grey streaks in low bun, pearl earrings, modest Filipino blouse.

Same bright Filipino living room, warm window light. The lighting feels slightly warmer and more intimate than previous anchor scenes — golden hour quality.

Art style: soft 3D animated illustration, warm golden tones, smooth rounded features, expressive eyes, warm intimate lighting, Pixar design. Clean line work, soft shadows.

Vertical 9:16 framing, character centered but closer than previous anchor shots — more intimate. Composition designed for push-in zoom — some space around the character that the camera can zoom into.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. Emotional tone: warm confidence, personal connection, gentle encouragement.
```

---

## Scene 12 — End Card (B-ROLL)

**Type:** B-ROLL (remove Lola reference)
**Duration:** 2 seconds
**Voiceover:** "Follow for more."
**Camera:** Static (Lesson 33 #16)
**Save as:** `assets/scenes/scene_12_broll.png`

### Exact Prompt (copy-paste)

```
Warm, soft animated illustration of a cozy Filipino home scene — an empty living room warmly lit with golden afternoon light streaming through windows. Pixar-adjacent 3D illustration style. Wooden furniture, family photos on the wall, a bookshelf with children's books, potted plants. The room feels inviting and lived-in, waiting for the family to return.

The center of the image has clean open space suitable for overlaying text ("Follow for more parenting tips from Lola"). The warm golden light creates a natural spotlight in the center.

Art style: soft 3D animated illustration, warm golden color palette, smooth textures, bright natural lighting, Pixar quality. Clean line work, soft ambient lighting.

Vertical 9:16 framing, room centered, plenty of clear space in the middle and lower third for text overlay.

NOT photorealistic. NOT dark. NOT anime. Warm, bright, family-friendly. No characters needed. Emotional tone: welcoming closure, warmth.
```

---

## After All 12 Are Done

### Consistency Check (do this yourself before telling me)

Look at all 12 images side by side and check:
- [ ] Lola looks the same across scenes 1, 2, 5, 8, 11 (same face, same clothing)
- [ ] All images are in the same animated style (no photorealistic ones mixed in)
- [ ] Color palette is consistent (warm golden tones throughout)
- [ ] Filipino cultural markers are present (homes, clothing, settings, food)
- [ ] All scenes are bright and warm — no dark or moody images

### If any image doesn't match:
- Regenerate it with the same prompt
- If Lola's face drifts: make sure the @ reference is uploaded
- If style is wrong: check you haven't left photorealistic triggers in the prompt

### Done When:
- [ ] All 12 images saved in `assets/scenes/`
- [ ] Consistency check passed
- [ ] Tell me "done" and we move to Phase 4

---

## Summary

| Scene | Type | Description | File |
|-------|------|-------------|------|
| 1 | ANCHOR | Hook — Lola in living room | `scene_01_anchor.png` |
| 2 | ANCHOR | Habit 1 intro | `scene_02_anchor.png` |
| 3 | B-ROLL | Mano po | `scene_03_broll.png` |
| 4 | B-ROLL | Greeting neighbor | `scene_04_broll.png` |
| 5 | ANCHOR | Habit 2 intro | `scene_05_anchor.png` |
| 6 | B-ROLL | Family dinner | `scene_06_broll.png` |
| 7 | B-ROLL | Clearing table | `scene_07_broll.png` |
| 8 | ANCHOR | Habit 3 intro | `scene_08_anchor.png` |
| 9 | B-ROLL | Watering plants | `scene_09_broll.png` |
| 10 | B-ROLL | Family chores | `scene_10_broll.png` |
| 11 | ANCHOR | CTA closing | `scene_11_anchor.png` |
| 12 | B-ROLL | End card | `scene_12_broll.png` |

**Estimated time: ~45 minutes (12 generations × ~3-4 min each)**

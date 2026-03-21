# Phase 6 — Manual Tasks: AI Video Generation (12 Scenes)

> Animate each upscaled image into a short video clip.
> One scene at a time → generate → review → next.

---

## Before You Start

### Tool Routing

| Scene Type | Tool | Why |
|------------|------|-----|
| **ANCHOR** (Lola talking) | **Veo 3.1** (Google AI Studio) | Lip-sync + voice generation |
| **B-ROLL** (family scenes) | **Kling 3.0** | Image-to-video motion |

### Veo 3.1 Setup (for ANCHOR scenes)

1. Go to **Google AI Studio** → Veo 3.1
2. Select **Image-to-Video** mode
3. Upload the upscaled image from `assets/scenes/upscaled/`
4. Paste the prompt (includes dialogue + voice blueprint)
5. Generate → download → save

### Kling 3.0 Setup (for B-ROLL scenes)

1. Go to **Kling** → Image-to-Video
2. Select **Pro mode**
3. Upload the upscaled image from `assets/scenes/upscaled/`
4. Paste the 4-field prompt
5. Generate → download → save

### File Naming

Save each video clip as:
```
assets/video_clips/scene_01_anchor_video.mp4
assets/video_clips/scene_02_anchor_video.mp4
assets/video_clips/scene_03_broll_video.mp4
...
```

Create the `assets/video_clips/` folder first.

### Voice Blueprint (copy into EVERY Veo prompt)

```
speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

---

## Scene 1 — HOOK (ANCHOR → Veo 3.1)

**Upload:** `assets/scenes/upscaled/scene_01_anchor_upscaled.png`
**Duration target:** 3 seconds
**Save as:** `assets/video_clips/scene_01_anchor_video.mp4`

### Exact Prompt (copy-paste into Veo 3.1)

```
Warm animated Filipino grandmother (Lola) sitting in a bright living room, medium close-up framing, facing camera directly. Gentle warm smile, soft eyebrow raise, slight forward lean — inviting the viewer in. Warm golden daylight streams through windows. Subtle head movement, eyes engaging camera with confidence. Slow dolly in toward her face.

[Lola speaks]: "Want your child to grow up respectful?... Start with these three."

Voice blueprint: speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

> ⚠️ If Veo blocks this prompt: remove the `[Lola speaks]` line, generate clean motion only, and we'll add voiceover separately in Phase 7.

---

## Scene 2 — Habit 1 Intro (ANCHOR → Veo 3.1)

**Upload:** `assets/scenes/upscaled/scene_02_anchor_upscaled.png`
**Duration target:** 2.5 seconds
**Save as:** `assets/video_clips/scene_02_anchor_video.mp4`

### Exact Prompt (copy-paste into Veo 3.1)

```
Warm animated Filipino grandmother (Lola), medium close-up, facing camera. She speaks with gentle authority, slight head nod, one hand raised in a calm teaching gesture. Static camera, locked frame. Same bright living room, warm window light.

[Lola speaks]: "Rule one... greet people politely."

Voice blueprint: speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

---

## Scene 3 — Mano Po (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_03_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_03_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Wide static shot, 3.5 seconds
Details: Young animated Filipino child performs "mano po" — gently presses elderly grandmother's hand to their forehead. Both characters smile warmly. Grandmother seated in wooden chair, child standing beside her. Subtle hand movement, child's head bowing gently forward. Bright Filipino home interior, warm daylight through open windows, potted plants, tiled floor.
Camera: Static wide camera, foreground character movement only — child's gentle bowing motion.
Mood: Family warmth, tradition, soft golden light, gentle reverence. Muted warm tones, subtle motion.
```

---

## Scene 4 — Greeting Neighbor (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_04_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_04_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Medium tracking shot, 3.5 seconds
Details: Young animated Filipino child cheerfully waves hello to an elderly neighbor at a gate. The child walks forward along a sunny barangay street. Neighbor waves back. Tropical plants, bright morning sunshine, mango tree nearby. Subtle walking motion, arm waving gently.
Camera: Medium tracking shot moving alongside the child — smooth lateral movement following the child's direction of walking.
Mood: Joy, community warmth, bright morning light, muted green and golden tones. Natural neighborly interaction.
```

---

## Scene 5 — Habit 2 Intro (ANCHOR → Veo 3.1)

**Upload:** `assets/scenes/upscaled/scene_05_anchor_upscaled.png`
**Duration target:** 2.5 seconds
**Save as:** `assets/video_clips/scene_05_anchor_video.mp4`

### Exact Prompt (copy-paste into Veo 3.1)

```
Warm animated Filipino grandmother (Lola), medium close-up, facing camera. She speaks calmly, two fingers raised to indicate "rule two." Warm expression, gentle nod. Static camera, locked frame. Same bright living room.

[Lola speaks]: "Two... say 'thank you' at the dinner table."

Voice blueprint: speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

---

## Scene 6 — Family Dinner (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_06_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_06_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Wide composition with slow pan, 3.5 seconds
Details: Animated Filipino family at dinner table — mother serves rice from a pot, child reaches forward with bowl, father sits nearby smiling. Warm overhead light illuminates the table. Filipino home-cooked dishes visible: rice pot, fried fish, soup bowl, plastic tablecloth on wooden table. Subtle serving motion, child's arm extending.
Camera: Slow pan right across the dinner table — smooth, gentle horizontal movement revealing more of the family scene.
Mood: Gratitude, family togetherness, warm amber-golden dinnertime lighting. Muted warm tones, cozy intimacy.
```

---

## Scene 7 — Clearing Table (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_07_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_07_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Over-the-shoulder composition, 3.5 seconds
Details: Young animated Filipino child carefully carries plates from dining table toward kitchen sink, stepping carefully. Mother watches from the doorframe in the background with a proud, tender smile. Child's walking motion is gentle and focused. Filipino home kitchen — clean tiles, wooden cabinets, warm interior lighting.
Camera: Over-the-shoulder shot from behind the mother — she is in foreground (partial shoulder/head), child walks away carrying plates in mid-ground.
Mood: Pride, nurturing, responsibility. Warm golden indoor light, muted tones. Gentle, slow movement.
```

---

## Scene 8 — Habit 3 Intro (ANCHOR → Veo 3.1)

**Upload:** `assets/scenes/upscaled/scene_08_anchor_upscaled.png`
**Duration target:** 2.5 seconds
**Save as:** `assets/video_clips/scene_08_anchor_video.mp4`

### Exact Prompt (copy-paste into Veo 3.1)

```
Warm animated Filipino grandmother (Lola), medium close-up, facing camera. She speaks with encouraging expression, three fingers raised to indicate "rule three." Warm confident smile, slight nod. Static camera, locked frame. Same bright living room.

[Lola speaks]: "Three... let them help around the house."

Voice blueprint: speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

---

## Scene 9 — Watering Plants (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_09_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_09_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Wide static shot, 3.5 seconds
Details: Young animated Filipino child happily waters potted plants with a blue plastic watering can in a small home garden. Water pours gently from the can onto leafy herbs in clay pots. Child's expression is cheerful and focused. Bright morning sunshine, tropical flowers (bougainvillea), wooden fence, clothesline in background. Tsinelas (flip-flops) on feet.
Camera: Static wide camera — the child's watering motion provides all movement. Dappled sunlight through leaves creates subtle light play.
Mood: Independence, joy, growth. Bright green-golden morning light, warm outdoor tones. Peaceful, natural.
```

---

## Scene 10 — Family Chores (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_10_broll_upscaled.png`
**Duration target:** 3.5 seconds
**Save as:** `assets/video_clips/scene_10_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Medium tracking shot, 3.5 seconds
Details: Animated Filipino family doing chores together in their yard. Father and young child sweep the yard with walis tambo (Filipino broom), child mimics the sweeping motion. Mother hangs laundry on a clothesline nearby. Everyone smiles, enjoying teamwork. Bright morning sunshine, concrete ground, simple fence, colorful clothes on the line.
Camera: Medium tracking shot moving alongside the family — smooth lateral movement past the sweeping action.
Mood: Teamwork, family bond, responsibility. Warm golden-green morning light, muted tones. Active but calm.
```

---

## Scene 11 — CTA / Closing (ANCHOR → Veo 3.1)

**Upload:** `assets/scenes/upscaled/scene_11_anchor_upscaled.png`
**Duration target:** 3 seconds
**Save as:** `assets/video_clips/scene_11_anchor_video.mp4`

### Exact Prompt (copy-paste into Veo 3.1)

```
Warm animated Filipino grandmother (Lola), medium close-up, facing camera. Warm personal knowing smile, gentle nod, direct eye contact — like sharing a secret with a friend. Slightly warmer golden light than previous scenes. Push-in zoom — camera slowly moves closer to her face throughout the clip.

[Lola speaks]: "Try just one tonight... and watch what happens."

Voice blueprint: speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply.
```

---

## Scene 12 — End Card (B-ROLL → Kling 3.0)

**Upload:** `assets/scenes/upscaled/scene_12_broll_upscaled.png`
**Duration target:** 2 seconds
**Save as:** `assets/video_clips/scene_12_broll_video.mp4`

### Exact Prompt (copy-paste into Kling 3.0)

```
Shot: Static hold, 2 seconds
Details: Cozy animated Filipino living room — warm golden afternoon light streams through windows, casting soft shadows across the floor. Wooden furniture, family photos on walls, bookshelf with colorful books, potted plants. The room feels lived-in and inviting. Very subtle ambient light movement — dust particles catching sunlight, slight curtain sway from a breeze.
Camera: Static camera, no movement — held frame.
Mood: Welcoming closure, warmth, contentment. Golden ambient light, muted earthy tones. Peaceful, still.
```

---

## Troubleshooting

### If Veo 3.1 blocks a prompt:

1. **Remove** the `[Lola speaks]` line entirely
2. **Remove** the voice blueprint
3. Generate **motion only** — Lola nodding, smiling, gesturing
4. Download the silent video
5. We'll add the voiceover separately in Phase 7 (ElevenLabs)
6. Record which scenes needed this workaround

### If Kling produces jerky/chaotic motion:

1. Add "very subtle motion" or "minimal movement" to the prompt
2. Reduce the described action — less movement = more stable
3. Try regenerating — Kling output varies between runs

### If motion doesn't match the camera described:

1. Delete the failed generation
2. Try simpler camera language: "static camera" instead of complex moves
3. Generate again

---

## After All 12 Clips Are Done

### Consistency Check

- [ ] All clips match the same animated style (no weird style shifts mid-video)
- [ ] ANCHOR clips: Lola's voice sounds the same across scenes 1, 2, 5, 8, 11
- [ ] B-ROLL clips: motion is subtle and cinematic, not chaotic
- [ ] Clip durations roughly match targets (±1 second is fine)
- [ ] No morphing faces, warping objects, or video glitches

### Save Format

| What | Where |
|------|-------|
| All video clips | `assets/video_clips/scene_XX_type_video.mp4` |
| Document any Veo workarounds | Note which scenes needed the fallback |

---

## Summary

| Scene | Type | Tool | Duration | File |
|-------|------|------|----------|------|
| 1 | ANCHOR | Veo 3.1 | 3s | `scene_01_anchor_video.mp4` |
| 2 | ANCHOR | Veo 3.1 | 2.5s | `scene_02_anchor_video.mp4` |
| 3 | B-ROLL | Kling 3.0 | 3.5s | `scene_03_broll_video.mp4` |
| 4 | B-ROLL | Kling 3.0 | 3.5s | `scene_04_broll_video.mp4` |
| 5 | ANCHOR | Veo 3.1 | 2.5s | `scene_05_anchor_video.mp4` |
| 6 | B-ROLL | Kling 3.0 | 3.5s | `scene_06_broll_video.mp4` |
| 7 | B-ROLL | Kling 3.0 | 3.5s | `scene_07_broll_video.mp4` |
| 8 | ANCHOR | Veo 3.1 | 2.5s | `scene_08_anchor_video.mp4` |
| 9 | B-ROLL | Kling 3.0 | 3.5s | `scene_09_broll_video.mp4` |
| 10 | B-ROLL | Kling 3.0 | 3.5s | `scene_10_broll_video.mp4` |
| 11 | ANCHOR | Veo 3.1 | 3s | `scene_11_anchor_video.mp4` |
| 12 | B-ROLL | Kling 3.0 | 2s | `scene_12_broll_video.mp4` |

**Estimated time: ~60-90 minutes (12 generations + review time)**

**When done, tell me and we proceed to Phase 7: Voiceover & Audio.**

# Phase 7 — Manual Tasks: Sound Effects & Background Music

> Layer SFX and background music onto the video clips.
> Veo 3.1 SUCCESSFULLY generated voice + lip-sync on all anchor clips — no ElevenLabs voiceover needed.

---

## Before You Start

### What's Changed

Veo 3.1 generated working voice + lip-sync on all 5 anchor clips (Scenes 1, 2, 5, 8, 11). This means:

- ✅ **KEEP** Veo's native audio on anchor clips — it's already perfectly lip-synced
- ❌ **DO NOT** add a separate ElevenLabs voiceover — it will desync from the lip movements
- ✅ **ADD** background music — generate via ElevenLabs SFX (or grab from Pixabay)
- ✅ **ADD** 2-3 subtle SFX for transitions — optional polish

### Lip-Sync Protection Strategy

> [!IMPORTANT]
> **The #1 rule for Phase 7 and Phase 8:** Never replace or modify the audio on anchor clips.
> In CapCut, the Veo-generated clips go on the timeline as-is (video + audio together).
> Background music and SFX go on **separate audio tracks below** — never on the same track as the anchor audio.

### What You Need

| Asset | Source | Status |
|-------|--------|--------|
| 12 video clips | `assets/video_clips/` | ✅ Phase 6 complete |
| ElevenLabs account | [elevenlabs.io](https://elevenlabs.io) | For BGM + SFX generation |

### Create the Audio Folder

```
assets/audio/
```
*(Already created — just add files here)*

---

## Step 7.1 — Organize What You Already Have

### Audio Status per Scene

| Scene | Type | Veo Voice + Lip-Sync | What to Add |
|-------|------|---------------------|-------------|
| 1 | ANCHOR | ✅ Has voice + lip-sync | BG music (low volume) |
| 2 | ANCHOR | ✅ Has voice + lip-sync | BG music + rule chime SFX |
| 3 | B-ROLL | No voice (visual only) | BG music |
| 4 | B-ROLL | No voice (visual only) | BG music |
| 5 | ANCHOR | ✅ Has voice + lip-sync | BG music + rule chime SFX |
| 6 | B-ROLL | No voice (visual only) | BG music |
| 7 | B-ROLL | No voice (visual only) | BG music |
| 8 | ANCHOR | ✅ Has voice + lip-sync | BG music + rule chime SFX |
| 9 | B-ROLL | No voice (visual only) | BG music |
| 10 | B-ROLL | No voice (visual only) | BG music |
| 11 | ANCHOR | ✅ Has voice + lip-sync | BG music |
| 12 | B-ROLL | No voice (visual only) | BG music |

**Key takeaway:** The voiceover is DONE — Veo handled it. Phase 7 is only about SFX + music.

---

## Step 7.2 — Generate Background Music (ElevenLabs SFX)

### Click-by-Click Instructions

1. Go to **[elevenlabs.io/app/sound-effects](https://elevenlabs.io/app/sound-effects)**
2. Set the **duration** to the maximum available (we need ~30-45 seconds)
3. Try the prompts below — generate 2-3 options and pick the best one

### Prompt Option A (Recommended — Warm Acoustic)

```
Soft warm acoustic guitar melody with gentle piano accompaniment. Uplifting and calming instrumental music. Family-friendly, nurturing feel. Warm golden-hour mood. No drums, no bass, no vocals. Gentle and positive. Loopable background music suitable for a heartwarming family video. 30 seconds.
```

### Prompt Option B (Gentle Piano)

```
Gentle piano melody with soft strings in the background. Warm, nurturing, and uplifting instrumental. Like background music for a heartwarming family moment. Calm and peaceful, slightly emotional. No drums, no vocals, no bass drops. Clean and simple. 30 seconds.
```

### Prompt Option C (Ukulele — Filipino-friendly vibe)

```
Soft ukulele playing a gentle, happy melody. Light and warm acoustic feel. Family-friendly background music for a parenting video. Positive and calming with a subtle tropical warmth. No vocals, no heavy instruments. Simple and loopable. 30 seconds.
```

### How to Pick the Best One

- **Generate all 3 prompts** (or at least 2)
- **Play each one** while imagining Lola's voice speaking over it
- Pick the one that:
  - [ ] Sits quietly in the background without demanding attention
  - [ ] Feels warm and family-friendly
  - [ ] **No lyrics** — purely instrumental
  - [ ] Doesn't have sudden volume spikes or dramatic changes
  - [ ] Would loop cleanly if needed (no abrupt endings)

### If ElevenLabs Doesn't Sound Right

**Fallback: Pixabay** (free, royalty-free library)

1. Go to **[pixabay.com/music/](https://pixabay.com/music/)**
2. Search: `gentle family`, `warm inspirational`, `soft acoustic`, or `calm positive`
3. Preview tracks → pick one that fits → download

### Save the BGM

Download your chosen track and save as:
```
assets/audio/bgm_track.mp3
```

### Quality Check

- [ ] Track is **30-60 seconds** long (or loops cleanly for our ~36s video)
- [ ] **No lyrics** — instrumental only
- [ ] Feels **warm and soft** — won't compete with Lola's voice
- [ ] No sudden volume changes or dramatic moments

---

## Step 7.3 — Generate Sound Effects (ElevenLabs SFX)

These are optional polish. Only 2 SFX recommended — keep it minimal.

### Click-by-Click Instructions

1. Go to **[elevenlabs.io/app/sound-effects](https://elevenlabs.io/app/sound-effects)**
2. Generate each SFX below one at a time:

### SFX 1: Transition Whoosh

**Paste this prompt:**
```
Soft gentle whoosh sound, like a warm breeze passing by. Very subtle, not dramatic. Short duration, about 1 second. Smooth and calming.
```

- Click **Generate** → listen → it should feel like a gentle page turn
- Download → save as: `assets/audio/sfx_transition_whoosh.mp3`

### SFX 2: Rule Chime

**Paste this prompt:**
```
Soft warm notification chime, like a gentle bell or a soft xylophone note. Single note, pleasant and uplifting. Very short, about 0.5 seconds. Family-friendly and calming.
```

- Click **Generate** → listen → it should be a warm "ding" for each new rule
- Download → save as: `assets/audio/sfx_rule_chime.mp3`

### Quality Check

- [ ] Whoosh is **subtle** — not dramatic or sci-fi
- [ ] Chime is **pleasant** — not harsh or startling
- [ ] Neither would overpower Lola's voice if played simultaneously

---

## Step 7.4 — Compile & Organize Audio Assets

### Final Folder Structure

```
assets/audio/
├── bgm_track.mp3               ← Your background music
├── sfx_transition_whoosh.mp3    ← Gentle transition whoosh
└── sfx_rule_chime.mp3           ← Rule intro chime
```

### Volume Hierarchy (for CapCut Phase 8)

| Layer | Volume | Notes |
|-------|--------|-------|
| **Veo anchor audio** | 100% | Primary — already on the video clips, DO NOT touch |
| **Sound effects** | 15-25% | Subtle support |
| **Background music** | 10-15% | Very low — must sit behind Lola's voice without competing |

> [!CAUTION]
> During B-roll scenes (no voice), you can raise the music volume slightly (20-25%) since there's no voice to compete with. Drop it back to 10-15% when anchor clips play. This is called **ducking** and CapCut makes it easy — covered in Phase 8.

---

## CapCut Lip-Sync Protection (Preview for Phase 8)

Here's exactly how to preserve the lip-sync in CapCut:

1. **Import each video clip** onto the main video track — this brings both the video AND Veo's audio together
2. **Never unlink** the video and audio on anchor clips — they must stay bonded
3. **Add background music** on a **separate audio track** (Audio Track 2) — drag it below the video track
4. **Add SFX** on yet **another audio track** (Audio Track 3)
5. **Lower the music volume** to 10-15% globally, then slightly raise during B-roll gaps
6. The result: Veo's voice plays perfectly synced on anchor clips, with music and SFX layered underneath

```
Timeline Layout (CapCut):
─────────────────────────────────────────────────
Track 1 (Video): [Scene 1][Scene 2][Scene 3]...   ← clips with Veo audio attached
Track 2 (Audio): [═══ Background Music ═══════]   ← continuous, low volume
Track 3 (Audio): [chime]    [chime]    [chime]     ← SFX at transition points
─────────────────────────────────────────────────
```

---

## Quality Gate — Phase 7

Before moving to Phase 8:

- [ ] Background music track saved in `assets/audio/`
- [ ] At least 1-2 SFX files generated and saved
- [ ] All files play without errors
- [ ] Confirmed: **Veo anchor clips will NOT have their audio replaced** in Phase 8

---

## Summary

| Step | Task | Tool | Output |
|------|------|------|--------|
| 7.1 | Audit audio status | Manual review | Confirmed Veo voice works |
| 7.2 | Save BG music | File management | `bgm_track.mp3` |
| 7.3 | Generate SFX | ElevenLabs SFX | `sfx_*.mp3` |
| 7.4 | Compile & organize | File management | `assets/audio/` complete |

**Estimated time: ~15-20 minutes** (much simpler since Veo handled voiceover!)

**When done, tell me and we proceed to Phase 8: Editing (CapCut).**

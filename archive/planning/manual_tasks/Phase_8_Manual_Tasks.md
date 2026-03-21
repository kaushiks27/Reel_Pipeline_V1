# Phase 8 — Manual Tasks: Final Video Editing (CapCut)

> Assemble the final video from all assets: 12 video clips, SFX, and background music.
> Veo's voice + lip-sync is already on the anchor clips — protect it.

---

## Before You Start

### What You Need

| Asset | Location | Count |
|-------|----------|-------|
| Video clips | `assets/video_clips/` | 12 files |
| Background music | `assets/audio/bgm_track.mp3` | 1 file |
| SFX (whoosh) | `assets/audio/sfx_transition_whoosh.mp3` | 1 file |
| SFX (chime) | `assets/audio/sfx_rule_chime.mp3` | 1 file |
| CapCut installed | Desktop or mobile | ✅ |

### ⚠️ THE #1 RULE — Lip-Sync Protection

> [!CAUTION]
> **NEVER unlink, mute, or replace the audio on anchor clips (Scenes 1, 2, 5, 8, 11).**
> Veo generated perfectly synced voice + lip-sync. If you detach the audio, it will desync permanently.
> Background music and SFX go on **separate tracks below** — never on the video track.

---

## Step 8.1 — Create New CapCut Project

### Click-by-Click

1. Open **CapCut** (desktop version recommended for precision)
2. Click **New Project**
3. Set project settings:

   | Setting | Value | Where to Find |
   |---------|-------|---------------|
   | **Aspect Ratio** | **9:16** (vertical) | Usually prompted at project creation, or under Project Settings |
   | **Resolution** | **1080×1920** | Project Settings → Resolution |
   | **Frame Rate** | **30 fps** | Project Settings → Frame Rate |

4. Don't change these settings later — they're locked for TikTok/Reels/Shorts

---

## Step 8.2 — Import All Assets

### Click-by-Click

1. Click **Import** (or drag files into the media panel)
2. Import all **12 video clips** from `assets/video_clips/`:
   ```
   scene_01_anchor_video.mp4
   scene_02_anchor_video.mp4
   scene_03_broll_video.mp4
   scene_04_broll_video.mp4
   scene_05_anchor_video.mp4
   scene_06_broll_video.mp4
   scene_07_broll_video.mp4
   scene_08_anchor_video.mp4
   scene_09_broll_video.mp4
   scene_10_broll_video.mp4
   scene_11_anchor_video.mp4
   scene_12_broll_video.mp4
   ```
3. Import all **audio files** from `assets/audio/`:
   ```
   bgm_track.mp3
   sfx_transition_whoosh.mp3
   sfx_rule_chime.mp3
   ```
4. You should see all 15 files in your media panel

---

## Step 8.3 — Arrange Clips on the Timeline

This is the most important step. Follow this exact order:

### 8.3a — Place Video Clips (Track 1)

Drag each clip onto the **main video track** in scene order (1 through 12):

| Order | File | Duration Target | Scene Content |
|-------|------|-----------------|---------------|
| 1 | `scene_01_anchor_video.mp4` | ~3s | HOOK — Lola: "Want your child to grow up respectful?" |
| 2 | `scene_02_anchor_video.mp4` | ~2.5s | Lola: "Rule one... greet people politely" |
| 3 | `scene_03_broll_video.mp4` | ~3.5s | Mano Po illustration |
| 4 | `scene_04_broll_video.mp4` | ~3.5s | Greeting neighbor |
| 5 | `scene_05_anchor_video.mp4` | ~2.5s | Lola: "Two... say thank you at the dinner table" |
| 6 | `scene_06_broll_video.mp4` | ~3.5s | Family dinner |
| 7 | `scene_07_broll_video.mp4` | ~3.5s | Clearing table |
| 8 | `scene_08_anchor_video.mp4` | ~2.5s | Lola: "Three... let them help around the house" |
| 9 | `scene_09_broll_video.mp4` | ~3.5s | Watering plants |
| 10 | `scene_10_broll_video.mp4` | ~3.5s | Family chores |
| 11 | `scene_11_anchor_video.mp4` | ~3s | CTA — Lola: "Try just one tonight..." |
| 12 | `scene_12_broll_video.mp4` | ~2s | End card — ambient room |

**Total: ~36.5 seconds**

> **Important:** When you drag a video clip onto the timeline, CapCut imports both the video AND the audio together (linked). **Do NOT unlink them** — especially on anchor clips where Veo's voice is synced.

### 8.3b — Trim Each Clip to Target Duration

Each clip from Veo/Kling may be longer than needed (Veo clips are 8s, Kling clips are 5s). Trim them:

1. **Click on a clip** on the timeline
2. **Hover over the right edge** — the cursor changes to a trim icon (↔)
3. **Drag the right edge left** to shorten the clip to the target duration
4. **Repeat** for every clip

**Trimming tips:**
- Trim from the END of each clip (the beginning usually has the best content)
- For anchor clips: listen first and trim so Lola's full sentence is included, don't cut her off mid-word
- For B-roll clips: find the moment with the most pleasing motion and keep that section
- Don't worry about being exact to the second — ±0.5s is fine

### 8.3c — Place Background Music (Track 2)

1. Drag `bgm_track.mp3` onto the **audio track below** the video track
2. Stretch or trim it to span the full video length (Scene 1 through Scene 12)
3. If the track is shorter than the video, you can:
   - **Duplicate it** — copy/paste to extend
   - **Loop it** — CapCut may have a loop option
4. **Lower the volume**:
   - Click on the music track on the timeline
   - Find the **Volume** slider (usually in the right-side panel)
   - Set to **10-15%** — this is a bed, not a featured element
5. **Add fade in/out**:
   - Fade in: **2 seconds** at the start
   - Fade out: **3 seconds** at the end
   - Look for "Fade" in the audio settings panel when the track is selected

### 8.3d — Place SFX (Track 3)

1. Drag SFX onto a **third audio track** (below the music track)
2. Position them at specific moments:

| SFX | When to Place | How Many |
|-----|---------------|----------|
| `sfx_rule_chime.mp3` | At the START of Scenes 2, 5, 8 (each new rule intro) | 3 times |
| `sfx_transition_whoosh.mp3` | Between anchor → B-roll transitions (e.g., between Scene 2 and 3, Scene 5 and 6, Scene 8 and 9) | 3 times |

3. **Set SFX volume** to **15-25%** — subtle enough to be felt, not noticed

### Your Timeline Should Look Like This

```
─────────────────────────────────────────────────────────────────────
Track 1 (Video):  [Sc.1][Sc.2][Sc.3][Sc.4][Sc.5][Sc.6][Sc.7][Sc.8][Sc.9][Sc.10][Sc.11][Sc.12]
                   ↑ Veo audio attached to anchor clips (1,2,5,8,11)

Track 2 (Music):  [═══════════ bgm_track.mp3 (10-15% volume) ═══════════════════════]
                   ↑ fade in 2s                                          fade out 3s ↑

Track 3 (SFX):       [♪]           [♪]                 [♪]        [swoosh][swoosh][swoosh]
                   chimes at        chimes at           chimes at    between anchor→broll
                   scene 2          scene 5             scene 8
─────────────────────────────────────────────────────────────────────
```

---

## Step 8.4 — Audio Ducking (Volume Balancing)

**What is ducking?** Automatically lowering the music volume when voice is playing, and raising it during silent B-roll scenes.

### Manual Ducking (if CapCut doesn't have auto-duck)

1. **Split the music track** at each anchor clip boundary:
   - Place the playhead at the start of Scene 1 → right-click music → **Split**
   - Repeat at the end of Scene 1, start of Scene 2, end of Scene 2, etc.
   - You'll end up with multiple music segments
2. **Lower volume during anchor clips** (Scenes 1, 2, 5, 8, 11):
   - Select the music segment under each anchor clip
   - Set volume to **8-10%** (very quiet — Lola's voice is primary)
3. **Raise volume during B-roll clips** (Scenes 3, 4, 6, 7, 9, 10, 12):
   - Select the music segment under each B-roll clip
   - Set volume to **20-25%** (a bit louder since there's no competing voice)

### Auto Ducking (if CapCut supports it)

Some CapCut versions have "Auto Lower Music Volume" or similar:
1. Select the music track
2. Look for **"Ducking"** or **"Auto Volume"** in the audio panel
3. Enable it — CapCut will automatically lower music when it detects voice on other tracks

---

## Step 8.5 — Transitions

### Rules (from Lesson 54)

- **Between most scenes:** Quick **hard cut** (no transition) — keeps pacing fast for social media
- **Between anchor → B-roll:** Quick **dissolve** (0.2-0.3 seconds) — smooth shift
- **Between rules/sections:** Optional subtle **swipe** (0.2 seconds)
- **NEVER use:** Flashy transitions (star wipe, spinning, glitch, etc.)
- **Be consistent:** Pick 1-2 transition types and stick with them

### Click-by-Click

1. Click the **gap between two clips** on the timeline
2. CapCut will show a **Transitions** panel
3. Select **"Dissolve"** or **"Cross Dissolve"**
4. Set duration to **0.2-0.3 seconds**
5. Apply at these transition points:
   - Scene 2 → Scene 3 (anchor → B-roll)
   - Scene 4 → Scene 5 (B-roll → anchor)
   - Scene 5 → Scene 6 (anchor → B-roll)
   - Scene 7 → Scene 8 (B-roll → anchor)
   - Scene 8 → Scene 9 (anchor → B-roll)
   - Scene 10 → Scene 11 (B-roll → anchor)
6. Leave hard cuts at: Scene 1→2, Scene 3→4, Scene 6→7, Scene 9→10, Scene 11→12

---

## Step 8.6 — Add Captions / Subtitles

### Why Captions Matter
- 80%+ of social media videos are watched on mute initially
- Captions are what makes someone **unmute** and engage
- CapCut's auto-captions are good enough for this

### Click-by-Click

1. Go to **Text** → **Auto Captions** (or "Auto Lyrics" depending on CapCut version)
2. Select the language: **English**
3. Click **Generate** — CapCut will transcribe the Veo audio on anchor clips
4. **Review every caption** — fix any typos or misheard words
5. Match captions to the script:
   - Scene 1: "Want your child to grow up respectful?... Start with these three."
   - Scene 2: "Rule one... greet people politely."
   - Scene 5: "Two... say 'thank you' at the dinner table."
   - Scene 8: "Three... let them help around the house."
   - Scene 11: "Try just one tonight... and watch what happens."

### Caption Styling

| Setting | Value | Why |
|---------|-------|-----|
| **Font** | Clean, bold sans-serif (Montserrat Bold, or CapCut's default bold) | Readability on mobile |
| **Font Size** | Large — fill about 60% of screen width | Must be readable on small phones |
| **Position** | Center-bottom of screen | Standard for Reels/TikTok |
| **Text Color** | White | Maximum contrast |
| **Outline/Shadow** | Black outline or drop shadow | Readable over any background |
| **Highlight** | Enable word-by-word highlight if available | Adds engagement |

> **Tip:** B-roll scenes (3, 4, 6, 7, 9, 10) don't need captions since there's no voice playing. Scene 12 (end card) also has no voice.

---

## Step 8.7 — CapCut Effects (Optional Polish)

These are subtle enhancements. Skip if the video already looks great.

### Recommended Effects

| Effect | Where | How |
|--------|-------|-----|
| **Subtle zoom/scale** | On B-roll clips that feel static | Add a keyframe at start (100% scale), end (105% scale) — creates a gentle "Ken Burns" effect |
| **Warm color filter** | All clips | Apply same warm tone filter globally for consistency |
| **Light vignette** | Anchor clips only | Adds cinematic focus on Lola's face |

### Effects to AVOID

- ❌ Heavy color filters that change the animated art style
- ❌ Flashy text animations or stickers
- ❌ Overused TikTok effects that date the content
- ❌ Anything that makes it look less professional

---

## Step 8.8 — Final Review (Watch the Whole Video)

Watch the assembled video **3 times** before exporting:

### Watch 1: Flow & Pacing
- [ ] Does the hook grab attention in the first **2 seconds**?
- [ ] Does every scene earn its time? (Nothing feels too long or too short)
- [ ] Does the CTA feel warm and natural, not rushed?
- [ ] Total duration is **30-50 seconds**?

### Watch 2: Audio
- [ ] Lola's voice is **always clearly audible** on anchor clips
- [ ] Background music sits **behind** the voice, never competing
- [ ] SFX are subtle and well-timed
- [ ] No audio gaps, pops, or clicks between clips
- [ ] Music fades in at the start, fades out at the end

### Watch 3: Visuals & Captions
- [ ] All 12 scenes are in the correct order
- [ ] Captions are **accurate** and match the script exactly
- [ ] Captions are synced to the voice (no delay or early appearance)
- [ ] Transitions are smooth and consistent
- [ ] No visible AI artifacts (warping faces, extra fingers, glitching)
- [ ] Aspect ratio is 9:16 (no black bars)

---

## Step 8.9 — Export

### CapCut Export Settings

1. Click **Export** (usually top-right)
2. Set these settings:

   | Setting | Value |
   |---------|-------|
   | **Resolution** | 1080×1920 |
   | **Frame Rate** | 30 fps |
   | **Format** | MP4 (H.264) |
   | **Quality** | Highest available |

3. Save as: `3_habits_respectful_kids_reel_v1.mp4`
4. Save location: project root or `assets/final/`

### Create the Final Folder

```
assets/final/
└── 3_habits_respectful_kids_reel_v1.mp4
```

---

## Step 8.10 — Mobile Preview

**Source:** Lesson 67, Step 7 — "Did you preview on mobile before publishing?"

This is critical — most viewers watch on phones. Transfer the exported video to your phone and check:

- [ ] Video looks sharp (not blurry or pixelated)
- [ ] Captions are **readable on a small screen**
- [ ] Audio is clear through phone speakers
- [ ] Colors look right (not washed out)
- [ ] The hook works when scrolling — **would YOU stop?**
- [ ] The overall feeling is warm, authentic, and shareable

---

## Post-Production: Engagement Strategy (Lesson 87)

After the video is ready to post, use these proven engagement hacks:

### 1. Filter Comments (Pre-emptive)
- TikTok → Settings → Comments → Filter Keywords
- Add: "AI", "fake", "not real", "animated", "cartoon"
- TikTok still counts filtered comments as engagement — they're just hidden

### 2. Seed Early Engagement
- Within **5-10 minutes** of posting, use a second device/account
- Drop an **opinion-based comment** that creates a divide: e.g., "Rule 2 is actually the most important one"
- Reply from your main account to start a conversation

### 3. 60-Minute Engagement Window
- Set a timer for **1 hour** after posting
- Reply to **every single comment** during this window
- Turn 1 comment into 3-4 by asking follow-ups
- TikTok sees spiking engagement and pushes the video harder

### 4. Optional: Intentional Micro-Mistake
- Include one small, subtle mistake that triggers people to "correct" you in comments
- Example: mislabel a rule number, or use "your" instead of "you're" once
- Creates a debate zone that skyrockets engagement

---

## Quality Gate — Phase 8 (FINAL)

Before publishing:

- [ ] Exported MP4 at **1080×1920, H.264, 30fps**
- [ ] Duration: **30-50 seconds**
- [ ] Veo voice is synced to lip movements throughout
- [ ] Captions present and accurate
- [ ] Background music at appropriate volume (not competing)
- [ ] SFX well-placed and subtle
- [ ] Transitions smooth and consistent
- [ ] Mobile preview passed
- [ ] Hook grabs attention in first 2 seconds
- [ ] CTA is clear at the end
- [ ] No AI artifacts visible
- [ ] Ready for upload to Facebook Reels, Instagram Reels, TikTok, YouTube Shorts

---

## Summary

| Step | Task | Time Estimate |
|------|------|---------------|
| 8.1 | Create CapCut project | 2 min |
| 8.2 | Import assets | 3 min |
| 8.3 | Arrange clips + trim + add audio | 15 min |
| 8.4 | Audio ducking | 10 min |
| 8.5 | Transitions | 5 min |
| 8.6 | Captions | 10 min |
| 8.7 | Effects (optional) | 5 min |
| 8.8 | Final review (3 watches) | 5 min |
| 8.9 | Export | 2 min |
| 8.10 | Mobile preview | 3 min |

**Estimated total: ~60 minutes**

**🎉 CONGRATULATIONS — when this is done, your first BuLoop reel is ready to publish!**

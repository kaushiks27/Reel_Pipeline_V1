---
description: End-to-end Reel Pipeline — from topic idea to polished 9:16 video
---

# Reel Pipeline Workflow

> **One command**: User says "today's topic is X" → Agent produces a finished 30-40s vertical video with transitions, captions, BGM, and lip-sync anchor.

---

## How It Works (User Perspective)

1. **You say**: "Today's topic is: *3 Things to Say When Your Child Fails a Test*"
2. **I reply** with my understanding of the video structure:
   - Hook line
   - 3 rules (each with an anchor scene + B-roll)
   - CTA line
3. **You approve** (or tweak) → I generate everything
4. **You review** the final video → approve or request changes

---

## What the Pipeline Does (8 Steps)

### Step 1: Topic & Concept
- **Tool**: ChatGPT 5.4
- **Output**: 3-item listicle structure (Hook → Rule 1 → Rule 2 → Rule 3 → CTA)
- **Gate**: User approves concept before proceeding

### Step 2: Script & Dialogue
- **Tool**: ChatGPT 5.4
- **Output**: Verbatim dialogue for the Lola anchor character
- **Voice**: Warm Filipina grandmother, Filipino-English accent
- **Gate**: User approves script

### Step 3: Image & Video Prompts
- **Tool**: ChatGPT 5.4
- **Output**: 8 image prompts (5 anchor reuse locked images + 3 B-roll new) + 8 video prompts
- **Anchor prompts**: Locked character + background descriptions
- **B-roll prompts**: 11-13 year old students, specific scenarios
- **Gate**: User approves prompts

### Step 4: Image Generation
- **Anchor images**: Reuse from `examples/anchor_character_lock/` (LOCKED, never regenerated)
  - scene_01 → A1 Hook
  - scene_02 → A2 Rule 1
  - scene_05 → A3 Rule 2
  - scene_08 → A4 Rule 3
  - scene_11 → A5 CTA
- **B-roll images**: Generate with `gpt-image-1.5` (1024x1792, 9:16)
- **Script**: `execution/generate_video01_images.py` (adapt for video number)
- **Gate**: User approves images

### Step 5: Video Generation
- **Anchor videos (Veo 3.1)**:
  - Script: `execution/generate_video01_anchor_videos.py`
  - REST API: `predictLongRunning` → poll → download
  - Lip-sync ON, 9:16, `allow_adult`
  - Each video: ~8 seconds raw
- **B-roll videos (Kling 3.0)**:
  - Script: `execution/generate_video01_broll_videos.py`
  - JWT auth, image-to-video, sound OFF
  - Each video: ~5 seconds raw
  - NO camera_control param (describe in prompt text)
- **Gate**: User approves all 8 videos

### Step 6: Assembly
- **Script**: `execution/assemble_video01.py`
- **Clip order**: A1 → A2 → B1 → A3 → B2 → A4 → B3 → A5
- **Anchor**: 1.2x speed (`setpts=PTS/1.2` + `atempo=1.2`)
- **B-roll**: Trim to last 40% (skip first 60%)
- **Audio**: Uniform 44100Hz stereo AAC, silent audio on B-roll, hard-cut with `-t`
- **Gate**: User approves assembled video

### Step 7: Polish
- **Script**: `execution/polish_video01.py`
- **4 sequential stages**:
  1. **Cross-dissolve** (0.3s xfade between all clips)
  2. **Poppins SemiBold captions** (PIL-rendered, white setup + yellow #FFD700 keywords, at 60% from top)
  3. **Fade-to-black** (1.0s ending)
  4. **BGM overlay** (`bgm_track.mp3` looped at 15% volume)
- **Gate**: User approves polished video

### Step 8: Push to Git
- Repo: `kaushiks27/Reel_Pipeline_V1`
- `.gitignore` excludes: `.env`, `env.md`, `.tmp/`, credentials
- Commit and push after each approved video

---

## Approval Gates (Non-Negotiable)

| Gate | What is reviewed | Must approve before |
|------|-----------------|-------------------|
| 1 | Topic + script | Generating images |
| 2 | Image prompts | Image generation |
| 3 | Generated images | Video generation |
| 4 | Generated videos | Assembly |
| 5 | Assembled video | Polish |
| 6 | Polished final video | Git push |

---

## Quick Start

```
User: "Today's topic is: 5 Ways to Handle Tantrums"

Agent: "Here's my understanding:
  - Hook: 'Next time your child throws a tantrum... try these 5—'
  Wait, this violates Rule Set 1 (always exactly 3 items).
  Adjusting to: '3 Ways to Handle Tantrums'
  
  Hook: 'Next time your child has a meltdown...'
  Rule 1: 'Get down to their level...'
  Rule 2: 'Name the feeling for them...'
  Rule 3: 'Offer two choices...'
  CTA: 'Share this...'
  
  Approve and I'll generate everything?"
```

---

## Files & Environment

```
.env                        # API keys (NEVER committed)
directives/video_pipeline_master.md  # Full SOP + 14 learnings
execution/                  # All Python scripts
assets/fonts/               # Poppins SemiBold
assets/video_XX/            # Per-video assets
examples/anchor_character_lock/  # Locked anchor images
examples/audio_lock/        # BGM track
```

**Required API keys** (in `.env`):
- `GOOGLE_AI_STUDIO_API_KEY` — Veo 3.1
- `KLING_ACCESS_KEY` + `KLING_SECRET_KEY` — Kling 3.0
- `OPENAI_API_KEY` — GPT Image, ChatGPT scripting

// turbo-all

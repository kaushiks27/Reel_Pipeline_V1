# Video Pipeline — Master Directive

> This directive defines the 8-phase AI Video Production Pipeline for BuLoop short-form vertical content.

## ⚠️ MANDATORY: Pre-Execution Checklist (EVERY Phase)

Before executing ANY phase:
1. **Read `directives/compliance_map.md`** → look up which lessons apply
2. **Read the relevant lesson files in `Video_Expert/`** → this is the source of truth
3. **Run Reverse Prompting** → ask 5 clarifying questions (`directives/reverse_prompting.md`)
4. **Define Prompt Contract** → GOAL/CONSTRAINTS/FORMAT/FAILURE (`directives/prompt_contracts.md`)
5. **Zero deviations from coursework** → if it's not in a lesson, ask the user
6. **Manual tasks must include exact prompts** → every manual task file in `planning/manual_tasks/` must contain copy-paste-ready prompts with full detail from coursework lessons, not summaries or placeholders. Include which Lesson 72 realism categories are used and why.
7. **Manual tasks must include exact tool settings** → reference `directives/tool_settings.md` for the locked settings per tool (aspect ratio, resolution, image count, etc.). Never leave tool configuration ambiguous.
8. **Manual tasks must be beginner-friendly** → assume the user is new to every tool. Write click-by-click instructions: where to click, what to look for on screen, what each slider does, and troubleshooting tips if the output isn't right.
9. **Mandatory manual task gate before every phase transition** → before entering ANY new phase, create a manual task file in `planning/manual_tasks/Phase_N_Manual_Tasks.md`. If the phase has no manual tasks, create the file with a "No manual tasks" note and explain why. The user must always know what they need to do before the next phase starts.
10. **Reverse prompting is mandatory EVERY phase — not just Phase 2** → Rule 3 says "ask 5 clarifying questions." This applies to EVERY phase, even phases that seem like pure execution. Root cause of prior miss: phases with detailed planning docs were treated as "execution-only" and reverse prompting was skipped. Fix: always present at least 3-5 clarifying questions with default assumptions before executing any phase. If defaults are obvious, state them explicitly and ask the user to override.

## Target Output
- **Format:** 9:16 vertical, 1080×1920, 30–50 seconds
- **Platforms:** Facebook Reels (primary), Instagram Reels, TikTok, YouTube Shorts
- **Audience:** Filipino parents aged 25–45, especially mothers
- **Tone:** Warm, aspirational, action-oriented
- **Structure:** HOOK (0–3s) → BODY (3 rules/habits/tips) → CTA ("follow for more")
- **Language:** English

## ⚠️ Visual Style (FROM CLIENT BRIEF — overrides Lesson 72 photorealism)
- **Style:** Animated, soft Pixar-adjacent illustrations — NOT photorealistic
- **Characters:** Expressive Filipino characters (parents, children, grandparents)
- **Settings:** Recognizable Filipino locations: modest homes, school classrooms, barangay courts, family dining tables
- **Lighting:** Bright, warm-lit, approachable — not dark, not cinematic
- **Cultural markers:** Filipino clothing, food, home interiors, family dynamics (respect for elders, bayanihan)
- **Captions:** On-screen throughout with highlighted keywords
- **Format:** Listicle with anchor character (Lola talking to camera) intercut with illustrated B-roll
- **Feel:** Something a Filipino parent would stop scrolling, save, and share on Facebook

> **NOTE:** Lesson 72 photorealism triggers (visible pores, DSLR, etc.) do NOT apply. Image prompts must target warm, animated illustration style instead. The Nanobanana PRO prompts shift accordingly.

## 8-Step Workflow (locked tools)

| Phase | Step | Tool |
|-------|------|------|
| 1 | Concept & Planning | ChatGPT |
| 2 | Script & Voice Planning | ChatGPT |
| 3 | Image Creation | Nanobanana PRO (Higgsfield) |
| 4 | Image Editing | Canva |
| 5 | Upscaling | Gigapixel 8 / Bigjpg / Nanobanana PRO |
| 6 | Video Generation | Veo 3.1 (anchor) + Kling 3.0 (B-roll) |
| 7 | Sound Effects & Voiceover | ElevenLabs + Pixabay |
| 8 | Editing | CapCut |

## Anchor Character: Lola
- 55–60 year old Filipino grandmother
- Warm, nurturing, natural beauty, modest Filipino clothing
- Reference image: `assets/lola_reference.png`

## Voice Blueprint (Veo 3.1)
```
"speaks with a subtle Filipino accent, warm and nurturing tone, medium pace with natural pauses between ideas. voice carries gentle authority and maternal warmth. sentences taper off softly rather than ending sharply."
```

```

## Veo 3.1 Voice + Lip-Sync (Updated March 19, 2026)

> **IMPORTANT UPDATE:** Veo 3.1 CAN successfully generate voice + lip-sync when prompted correctly.
> The safety filter issue from Learnings Report §3 did NOT block prompts during Pipeline 2.
> Use the `[Lola speaks]: "dialogue"` + voice blueprint format directly in Veo prompts.

| Status | Approach |
|--------|----------|
| ✅ Primary (working) | Veo 3.1 with `[Character speaks]` dialogue + voice blueprint → native voice + lip-sync |
| ⚠️ Fallback (if blocked) | Veo (silent motion) → ElevenLabs voiceover → separate audio track |

**Key implication for editing:** Since Veo generates voice + lip-sync natively, do NOT add a separate voiceover. Only layer BGM + SFX on separate audio tracks. Never unlink anchor clip audio.

## Fallback Chains (Learnings Report §5)
- Anchor: Veo 3.1 (voice+lip-sync) → Kling lip-sync → Higgsfield DoP
- B-Roll: Kling 3.0 → Higgsfield DoP

## ElevenLabs Settings (Learnings Report §13)
- Model: `eleven_multilingual_v2`
- Stability: 65–70%
- Clarity + Similarity: 75%
- Style: 30%
- Speed: Slightly slower than default
- Voice ID: `W15P89PIs2rD5Xo7XQ7V` (locked)
- **Primary use:** BGM generation + SFX (not voiceover — Veo handles voice)

## Safety Rules (non-negotiable)
1. All characters fully clothed in age-appropriate attire
2. Children shown ONLY in positive, happy activities
3. Settings bright, well-lit, and safe
4. No conflict, distress, tears, isolation
5. All adults in nurturing, supportive roles
6. No physical contact beyond natural family affection
7. Safety clause appended to every image prompt

## Scene-by-Scene Delivery Protocol
1. Generate Scene N
2. Present with: prompt used, output, self-assessment
3. Wait for: APPROVED / REDO + feedback / SKIP
4. Never batch-generate. Never skip approval.

## Prompt Framework (6-layer)
All prompts follow: PURPOSE → ROLE → STRUCTURE → STYLE → DETAILS → EXAMPLE

## API Keys Required (in `.env`)
```
GOOGLE_AI_STUDIO_API_KEY=
KLING_ACCESS_KEY=
KLING_SECRET_KEY=
HIGGSFIELD_API_KEY=
HIGGSFIELD_API_SECRET=
ELEVENLABS_API_KEY=
ELEVENLABS_VOICE_ID=
OPENAI_API_KEY=
```

## Pipeline 2 Production Learnings (March 19, 2026)

### Naming Conventions
- Anchor clips: `scene_XX_anchor_video.mp4`
- B-roll clips: `scene_XX_broll_video.mp4`
- Audio: `assets/audio/bgm_track.mp3`, `sfx_*.mp3`
- Final export: `assets/final/[topic_slug]_reel_v1.mp4`

### Audio Architecture (Lip-Sync-Safe)
```
Track 1 (Video):  Scene clips in order → Veo audio stays bonded
Track 2 (Music):  BGM at 10-15% (duck to 8-10% under voice, raise to 20-25% under B-roll)
Track 3 (SFX):    Rule chimes at habit intros + transition whooshes
```

### Key Production Rules
1. **Never unlink video+audio on anchor clips** — Veo lip-sync is baked in
2. **Audio ducking** is essential — lower BGM under voice, raise under B-roll
3. **Kling defaults to 16:9** — always change to 9:16 before generating
4. **Veo max is 720p** — upscaling happens at CapCut export (1080p)
5. **Trim from the end** — Veo/Kling clips are longer than needed

### Automation Pipeline (for future builds)
- See: `planning/AI_Video_Pipeline_Automation_Overview.md`
- 5-phase pipeline with user review gates at every critical stage
- ~80% automated, ~20% human review time


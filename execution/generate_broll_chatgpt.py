#!/usr/bin/env python3
"""
B-Roll Scene Generation — OpenAI DALL-E 3 (Native 9:16)

Generates 3 B-roll images per scene (3 scenes = 9 total) using OpenAI's
DALL-E 3 API with native 1024x1792 portrait output, then resizes to 1080x1920.

Usage:
    python3 execution/generate_broll_chatgpt.py
"""
from __future__ import annotations

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

# ─── Config ───────────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("assets/broll_scenes/chatgpt_9x16")

# ─── Load .env ────────────────────────────────────────────────────────────────
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    print("ERROR: OPENAI_API_KEY not in .env")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# ─── Locked style ─────────────────────────────────────────────────────────────
STYLE_SUFFIX = (
    "Same concept art style as anchor scenes — smooth digital illustration, "
    "clean lines, warm palette, soft lighting with gentle gradients. "
    "Vertical portrait composition with space above and below for text overlays. "
    "No photorealistic, no harsh shadows, no cold tones, no text, "
    "no watermark."
)

# ─── 3 B-Roll Scenes × 3 variants each ──────────────────────────────────────
SCENES = [
    {
        "scene_id": "b1_confidence",
        "scene_title": "Rule 1: 'I believe in you' → CONFIDENCE",
        "variants": [
            {
                "id": "b1_v1",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s kneeling on a wooden floor to be at eye-level "
                    "with her young daughter (approximately 6 years old). The mother "
                    "gently holds both of the child's small hands in hers. The child "
                    "looks up at the mother with wide trusting eyes and a hopeful "
                    "smile. The mother gazes directly at the child with an expression "
                    "of deep belief and encouragement. "
                    "The setting is a bright, warm Filipino home interior — soft "
                    "natural daylight streaming through a window with sheer curtains "
                    "on the left, creating warm glow across both figures. A potted "
                    "plant sits on the windowsill. Wooden flooring, warm-toned walls. "
                    "Medium shot, slightly low angle (from the child's perspective). "
                    "Warm color palette: golden sunlight, soft coral, warm wood tones. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b1_v2",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s crouching down to her young son's level (about 6 "
                    "years old) in a warm home hallway. She places one hand gently "
                    "on his shoulder while looking into his eyes with unwavering "
                    "confidence. The boy stands a little taller, beaming with pride. "
                    "Morning light streams through a nearby window, casting warm "
                    "golden light across both figures. Wooden floors, family photos "
                    "on the wall behind them. "
                    "Medium shot, eye-level camera. Warm golden color palette. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b1_v3",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s sitting cross-legged on the floor facing her "
                    "young daughter (about 5 years old). They are holding hands "
                    "together, the mother looking at the child with warmth and pride. "
                    "The child smiles shyly but brightly. "
                    "The setting is a cozy Filipino living room with soft carpet, "
                    "warm lamplight, potted plants nearby. Afternoon golden light. "
                    "Medium shot, eye-level. Warm amber and coral palette. "
                    f"{STYLE_SUFFIX}"
                ),
            },
        ],
    },
    {
        "scene_id": "b2_connection",
        "scene_title": "Rule 2: 'Tell me about your day' → CONNECTION",
        "variants": [
            {
                "id": "b2_v1",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s and her young son (approximately 8 years old) "
                    "sitting together on a cozy brown sofa in a warm living room. "
                    "The mother is leaning forward with genuine interest, her chin "
                    "resting lightly on her hand, listening attentively. The boy is "
                    "mid-gesture, hands animated, clearly telling an exciting story "
                    "about his day. Both are smiling. "
                    "The setting is a cozy Filipino home living room in the evening — "
                    "warm amber lamplight from a side table lamp. A warm woven throw "
                    "blanket draped on the sofa, a small potted plant on a side table. "
                    "Medium shot, eye-level camera. Warm amber color palette. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b2_v2",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s sitting at a small wooden dining table with her "
                    "young daughter (about 7 years old). The daughter leans across "
                    "the table excitedly telling a story, gesturing with her hands. "
                    "The mother rests her chin on both hands, eyes wide and engaged, "
                    "fully present in the conversation. A cup of tea sits between them. "
                    "The setting is a modest Filipino kitchen with warm overhead light, "
                    "wooden cabinets, a small window showing evening sky. "
                    "Medium shot, eye-level camera. Warm golden and brown tones. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b2_v3",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s and her young son (about 8 years old) sitting "
                    "on veranda steps of a modest Filipino home at sunset. The boy "
                    "is talking animatedly while the mother listens with a warm smile, "
                    "one arm around his shoulder. Golden sunset light bathes both "
                    "figures. Plants and a simple wooden railing in the background. "
                    "Medium shot, eye-level. Warm sunset palette: golden, amber, coral. "
                    f"{STYLE_SUFFIX}"
                ),
            },
        ],
    },
    {
        "scene_id": "b3_selfworth",
        "scene_title": "Rule 3: 'I'm proud of you' → SELF-WORTH",
        "variants": [
            {
                "id": "b3_v1",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s kneeling and embracing her young daughter "
                    "(approximately 7 years old) at the front doorway of their home. "
                    "The child wears a light blue school uniform with a small backpack, "
                    "looking up at her mother with a bright, confident smile. The "
                    "mother wraps her arms around the child in a warm, proud hug, "
                    "her eyes closed with a gentle smile of contentment. "
                    "Soft morning daylight streaming through the open front door, "
                    "creating a warm backlit glow. A small shoe rack visible to the "
                    "side, potted plants by the doorframe. "
                    "Medium shot, eye-level camera. Warm morning palette: soft golden "
                    "light, warm skin tones, light blue uniform accent. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b3_v2",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s hugging her young son (about 8 years old) who "
                    "is holding up a hand-drawn picture proudly. The mother kneels "
                    "beside him with her arm around his back, looking at the drawing "
                    "with a beaming smile of genuine pride. The boy grins ear to ear. "
                    "The setting is a warm Filipino home living room with afternoon "
                    "golden light streaming through a window. Wooden shelves with "
                    "children's artwork pinned on the wall behind them. "
                    "Medium shot, eye-level. Warm golden and amber palette. "
                    f"{STYLE_SUFFIX}"
                ),
            },
            {
                "id": "b3_v3",
                "prompt": (
                    "A warm concept art digital illustration of a Filipina mother "
                    "in her mid-30s walking her young daughter (about 6 years old) "
                    "to school, holding her hand. The mother looks down at the child "
                    "with an expression of deep pride. The child walks confidently "
                    "wearing a school uniform and small backpack, looking up at her mom. "
                    "The setting is a quiet Filipino neighborhood street in the morning "
                    "with warm golden sunlight, simple houses, a few tropical plants. "
                    "Medium shot, slightly low angle. Warm morning palette. "
                    f"{STYLE_SUFFIX}"
                ),
            },
        ],
    },
]


def generate_image(prompt_text, output_path):
    """Generate image via OpenAI API with native 9:16."""
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model": "dall-e-3",
        "prompt": prompt_text,
        "n": 1,
        "size": "1024x1792",
        "quality": "hd",
        "style": "vivid",
    }

    try:
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=120)
        if resp.status_code == 200:
            data = resp.json()
            img_url = data["data"][0]["url"]

            img_resp = requests.get(img_url, timeout=60)
            if img_resp.status_code == 200:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(img_resp.content)

                # Resize to 1080x1920
                if HAS_PIL:
                    img = Image.open(output_path)
                    resized = img.resize((1080, 1920), Image.LANCZOS)
                    resized.save(output_path)
                    print(f"   Saved + resized: {output_path} (1080x1920)")
                else:
                    print(f"   Saved: {output_path} (1024x1792, PIL not available for resize)")
                return True
            else:
                print(f"   Download failed: {img_resp.status_code}")
        else:
            print(f"   API error: {resp.status_code} — {resp.text[:300]}")
    except Exception as e:
        print(f"   Error: {e}")
    return False


def main():
    print("=" * 70)
    print("B-ROLL SCENE GENERATION — OpenAI DALL-E 3 (Native 9:16)")
    print("   Size: 1024x1792 → resized to 1080x1920")
    print("   Quality: HD | Style: Vivid")
    print(f"   Scenes: {len(SCENES)} × 3 variants = 9 images")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    total = sum(len(s["variants"]) for s in SCENES)
    count = 0

    for scene in SCENES:
        scene_dir = OUTPUT_DIR / scene["scene_id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"SCENE: {scene['scene_title']}")

        for variant in scene["variants"]:
            count += 1
            print(f"\n  [{count}/{total}] {variant['id']}")
            print(f"   Prompt: {len(variant['prompt'])} chars")

            output_path = scene_dir / f"{variant['id']}.png"
            if generate_image(variant["prompt"], output_path):
                successes += 1
            else:
                print(f"   FAILED")

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/{total} B-roll images generated")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

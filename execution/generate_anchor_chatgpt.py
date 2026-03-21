#!/usr/bin/env python3
"""
Anchor Scene Generation — OpenAI DALL-E (Native 9:16)

Generates 3 anchor scene images using OpenAI's image generation API
with native 1024x1792 (9:16 portrait) output.

Usage:
    python3 execution/generate_anchor_chatgpt.py
"""
from __future__ import annotations

import os
import sys
import json
import requests
from pathlib import Path
from datetime import datetime

# ─── Config ───────────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("assets/anchor_scenes/chatgpt_9x16")

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

# ─── Locked descriptions ─────────────────────────────────────────────────────
CHAR_DESC = (
    "A warm concept art digital illustration of a Filipina woman in her mid-30s "
    "with shoulder-length straight black hair with a slight center part, warm "
    "medium-brown skin, kind almond-shaped dark brown eyes, small gold stud "
    "earrings, a gentle half-smile with soft rounded cheeks, and a natural "
    "Filipino facial structure. She wears a coral-pink floral blouse with "
    "blue and green leaf accents, button-front, 3/4 sleeves. She sits in a "
    "green cushioned armchair with tufted back."
)

BG_DESC = (
    "The background is a cozy Filipino living room with warm wood-paneled "
    "walls, a dark wooden bookshelf filled with books and small framed family "
    "photos, a ceramic table lamp with warm golden glow on a wooden side "
    "table to her right, a potted golden pothos plant with trailing vines, "
    "a monstera plant to her left, and warm woven tribal-print throw "
    "pillows on the armchair. The overall color palette is dominated by "
    "warm amber, golden brown, olive green, and soft coral tones. Warm "
    "golden lamplight creates soft directional lighting from the right side."
)

STYLE_SUFFIX = (
    "Concept art style, smooth digital illustration, clean lines, warm "
    "color palette, soft lighting with gentle gradients. Vertical portrait "
    "composition with space above head and below waist for text overlays. "
    "No photorealistic, no harsh shadows, no cold tones, no text, "
    "no watermark, no extra characters."
)

# ─── 3 Anchor Prompts ────────────────────────────────────────────────────────
PROMPTS = [
    {
        "id": "a1_hook",
        "title": "A1 — Hook: Warm Inviting Smile",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She is looking directly at the viewer with "
            "a warm, welcoming smile — eyes slightly crinkled as if greeting an old "
            "friend. Both hands resting naturally on the armrests of the chair. Her "
            "posture is relaxed and open, conveying trust and warmth. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a2_speaking",
        "title": "A2 — Speaking: Gentle Explaining Gesture",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera, slightly tighter framing on face and "
            "upper body. She is mid-speech with her mouth slightly open, her right hand "
            "raised at chest level making a gentle open-palm explaining gesture. Her "
            "expression is warm and engaged — like a mother sharing wisdom she deeply "
            "believes in. Her eyes are focused and kind. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a3_cta",
        "title": "A3 — CTA: Warm Closing Smile, Hands Together",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She has both hands clasped together at "
            "chest level in a caring, prayer-like gesture. Her expression is a full "
            "warm smile — grateful, compassionate. Her eyes are looking directly at "
            "the camera with gentle confidence, conveying deep maternal warmth. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
]


def generate_image(prompt_text, output_path):
    """Generate image via OpenAI API with native 9:16."""
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model": "dall-e-3",
        "prompt": prompt_text,
        "n": 1,
        "size": "1024x1792",  # Native 9:16 portrait
        "quality": "hd",
        "style": "vivid",
    }

    try:
        print(f"   Calling OpenAI API (DALL-E 3, 1024x1792 HD)...")
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=120)
        if resp.status_code == 200:
            data = resp.json()
            img_url = data["data"][0]["url"]
            revised_prompt = data["data"][0].get("revised_prompt", "")

            # Download image
            img_resp = requests.get(img_url, timeout=60)
            if img_resp.status_code == 200:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(img_resp.content)
                print(f"   Saved: {output_path} ({len(img_resp.content) // 1024}KB)")

                # Save revised prompt for reference
                meta = {
                    "original_prompt_length": len(prompt_text),
                    "revised_prompt": revised_prompt,
                    "size": "1024x1792",
                    "quality": "hd",
                    "model": "dall-e-3",
                }
                (output_path.parent / f"{output_path.stem}_meta.json").write_text(
                    json.dumps(meta, indent=2)
                )
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
    print("ANCHOR SCENE GENERATION — OpenAI DALL-E 3 (Native 9:16)")
    print("   Size: 1024x1792 (portrait 9:16)")
    print("   Quality: HD | Style: Vivid")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0

    for i, p in enumerate(PROMPTS, 1):
        print(f"\n{'_' * 70}")
        print(f"[{i}/3] {p['title']}")
        print(f"   Prompt: {len(p['prompt'])} chars")

        output_path = OUTPUT_DIR / f"{p['id']}.png"
        if generate_image(p["prompt"], output_path):
            successes += 1
            print(f"   Done [{successes} total]")
        else:
            print(f"   FAILED")

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/3 anchor scenes generated")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

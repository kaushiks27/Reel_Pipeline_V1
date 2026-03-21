#!/usr/bin/env python3
"""
Video 01 — Image Generation v4 (OpenAI gpt-image-1.5)

Primary generation via gpt-image-1.5 with FULL locked character descriptions.
Higgsfield abandoned due to: (1) aggressive NSFW filter, (2) poor character consistency.

Usage:
    python3 execution/generate_video01_images_v4.py
"""
from __future__ import annotations

import os
import sys
import json
import base64
import requests
from pathlib import Path
from datetime import datetime

# ─── Config ───────────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("assets/video_01/images")

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

# ─── Locked character description (verbatim from directive) ──────────────────
CHAR_DESC = (
    "A warm 3D-animated Pixar-style digital illustration of a Filipina grandmother "
    "(Lola) in her late 50s to early 60s, with grey-streaked black hair pulled back "
    "in a neat low bun, warm medium-brown skin with gentle smile lines and soft "
    "wrinkles around the eyes, kind dark brown eyes, small pearl stud earrings, a "
    "gentle warm smile with soft rounded cheeks, and a natural Filipino facial "
    "structure. She wears a cream/beige embroidered blouse with delicate vine and "
    "floral embroidery down the center front, small buttons, short sleeves. She "
    "sits in a wooden chair with a warm backrest."
)

BG_DESC = (
    "The background is a cozy Filipino home interior with warm cream/beige walls, "
    "framed family photos on the walls, a potted green plant (pothos) to one side, "
    "a warm golden glow from natural light through a window, a tablecloth-covered "
    "side table with more framed photos and a vase of flowers, warm terracotta and "
    "wood tones throughout. The overall color palette is warm cream, amber, golden "
    "brown, and soft green accents."
)

STYLE_SUFFIX = (
    "Warm 3D-animated Pixar-style, smooth digital illustration, clean lines, warm "
    "color palette, soft lighting with gentle gradients. 9:16 vertical composition "
    "with space at top and bottom for text overlays. No photorealistic, no harsh "
    "shadows, no cold tones, no text, no watermark, no extra characters."
)

# ─── Scene Prompts (full character descriptions for consistency) ──────────────
PROMPTS = [
    {
        "id": "a1_hook",
        "title": "A1 — Hook: Warm Concerned-But-Loving Smile",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She is looking directly at the viewer with "
            "a warm, knowing smile — her eyes carry gentle empathy, as if she understands "
            "what you're going through. Both hands resting naturally on the armrests of the "
            "chair. Her posture is relaxed and open, conveying comfort and wisdom. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a2_index_finger",
        "title": 'A2 — Speaking: Index Finger Raised, "Number One"',
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera, slightly tighter framing on face and upper "
            "body. She is mid-speech with her mouth slightly open, her right hand raised "
            "with index finger pointing up — a teaching gesture. Her expression is warm "
            "and engaged, her eyes focused on the camera with gentle authority, like a "
            "grandmother sharing something she deeply believes in. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a3_three_fingers",
        "title": 'A3 — Speaking: Three Fingers Raised, "Number Three"',
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera. She is mid-speech, her right hand raised "
            "showing three fingers. Her expression is deeply warm — soft eyes, a knowing "
            "half-smile, slight head tilt to the side. This is the most emotional moment. "
            "Her eyes communicate tenderness. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a4_cta_hands_clasped",
        "title": "A4 — CTA: Warm Closing Smile, Hands Clasped",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She has both hands clasped together at chest "
            "level in a caring, prayer-like gesture. Her expression is a full warm smile — "
            "grateful, compassionate. Her eyes are looking directly at the camera with "
            "gentle confidence, conveying deep grandmother warmth and sincerity. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "b1_safety",
        "title": 'B1 — Rule 1: Study Desk Scene → SAFETY',
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s sitting beside her 12-year-old son at a wooden study desk. The "
            "mother has her arm around the boy's shoulder in a comforting gesture. The boy "
            "looks down at a test paper on the desk with a thoughtful expression. "
            "The mother's face shows warm reassurance and support. "
            "The setting is a warm Filipino home study corner — a wooden desk with an open "
            "textbook and pencils, a desk lamp with warm golden glow, a bookshelf with "
            "school books in the background, warm cream walls. The boy wears a white "
            "school polo shirt. "
            "Medium shot, eye-level camera. "
            f"{STYLE_SUFFIX}"
        ),
    },
    {
        "id": "b2_understanding",
        "title": 'B2 — Rule 2: Notebook Scene → UNDERSTANDING',
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s and her 11-year-old daughter sitting together on the floor of a "
            "warm living room. They sit cross-legged facing each other. The girl holds an "
            "open notebook and points at a page while explaining something. The mother "
            "leans forward with genuine interest, nodding with an encouraging smile. "
            "The setting is a warm Filipino home living room — warm afternoon sunlight "
            "through a window with sheer curtains, a woven rattan mat, warm wood flooring, "
            "potted plants on the windowsill. The girl wears a light blue school uniform. "
            "Medium shot, slightly high angle camera. "
            f"{STYLE_SUFFIX}"
        ),
    },
    {
        "id": "b3_belief",
        "title": 'B3 — Rule 3: High-Five Scene → BELIEF',
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s and her 13-year-old son giving each other a high-five across a "
            "study table. Both are smiling confidently. Open textbooks and notebooks are "
            "spread on the table. The boy's expression shows renewed determination. "
            "The setting is a warm Filipino home dining area in the evening — a wooden "
            "dining table, warm amber lamplight, warm cream walls with a framed photo, "
            "a potted plant in the corner. The boy wears a casual t-shirt. "
            "Medium shot, eye-level camera — the high-five hands at center of frame. "
            f"{STYLE_SUFFIX}"
        ),
    },
]


def generate_image(prompt_text, output_path):
    """Generate image via OpenAI gpt-image-1.5."""
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model": "gpt-image-1.5",
        "prompt": prompt_text,
        "n": 1,
        "size": "1024x1536",  # Portrait mode for gpt-image-1.5
        "quality": "high",
    }

    try:
        print(f"   Calling OpenAI gpt-image-1.5 (1024x1536, high)...")
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=180)
        if resp.status_code == 200:
            data = resp.json()
            img_data = data["data"][0]

            # gpt-image-1.5 may return b64_json or url
            if "b64_json" in img_data:
                img_bytes = base64.b64decode(img_data["b64_json"])
                output_path.parent.mkdir(parents=True, exist_ok=True)
                output_path.write_bytes(img_bytes)
                print(f"   ✓ Saved: {output_path} ({len(img_bytes) // 1024}KB)")
            elif "url" in img_data:
                img_resp = requests.get(img_data["url"], timeout=60)
                if img_resp.status_code == 200:
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_bytes(img_resp.content)
                    print(f"   ✓ Saved: {output_path} ({len(img_resp.content) // 1024}KB)")
                else:
                    print(f"   Download failed: {img_resp.status_code}")
                    return False
            else:
                print(f"   No image data in response")
                return False

            # Save metadata
            revised = img_data.get("revised_prompt", "")
            meta = {
                "model": "gpt-image-1.5",
                "size": "1024x1536",
                "quality": "high",
                "revised_prompt": revised,
            }
            (output_path.parent / f"{output_path.stem}_meta.json").write_text(
                json.dumps(meta, indent=2)
            )
            return True
        else:
            print(f"   API error: {resp.status_code} — {resp.text[:300]}")
    except Exception as e:
        print(f"   Error: {e}")
    return False


def main():
    total = len(PROMPTS)
    print("=" * 70)
    print("VIDEO 01 — IMAGE GENERATION v4 (gpt-image-1.5)")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
    print(f"   Model: gpt-image-1.5")
    print(f"   Size: 1024x1536 (portrait 2:3)")
    print(f"   Quality: high")
    print(f"   Scenes: {total} (4 anchor + 3 B-roll)")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, p in enumerate(PROMPTS, 1):
        scene_dir = OUTPUT_DIR / p["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/{total}] {p['title']}")
        print(f"   Prompt: {len(p['prompt'])} chars")

        output_path = scene_dir / "gpt_image.png"
        if generate_image(p["prompt"], output_path):
            successes += 1
            results.append({"id": p["id"], "title": p["title"], "file": str(output_path), "status": "OK"})
            print(f"   Done [{successes}/{total}]")
        else:
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "FAILED"})
            print(f"   FAILED")

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/{total} images generated via gpt-image-1.5")
    for r in results:
        icon = "✓" if r["status"] == "OK" else "✗"
        print(f"   {icon} {r['id']}: {r['status']}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Video 01 — Image Generation (Nanobanana PRO / Higgsfield API)

Generates all 7 scene images for Video 01:
  - 4 anchor scenes (Lola grandmother)
  - 3 B-roll scenes (parent + 11-13yo student)

Usage:
    python3 execution/generate_video01_images.py
"""
from __future__ import annotations

import os
import sys
import json
import time
import base64
import requests
from pathlib import Path
from datetime import datetime

# ─── Config ───────────────────────────────────────────────────────────────────
BASE_URL = "https://platform.higgsfield.ai"
MODEL_ID = "higgsfield-ai/soul/standard"
POLL_INTERVAL = 8
MAX_POLL_TIME = 300
OUTPUT_DIR = Path("assets/video_01/images")

# Reference images for character consistency (anchor character lock)
REF_IMAGES = [
    Path("examples/anchor_character_lock/scene_01_anchor_upscaled.png"),
    Path("examples/anchor_character_lock/scene_05_anchor_upscaled.png"),
]

# ─── Load .env ────────────────────────────────────────────────────────────────
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.getenv("HIGGSFIELD_API_KEY")
API_SECRET = os.getenv("HIGGSFIELD_API_SECRET")
if not API_KEY or not API_SECRET:
    print("ERROR: HIGGSFIELD_API_KEY or HIGGSFIELD_API_SECRET not in .env")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Key {API_KEY}:{API_SECRET}",
    "Content-Type": "application/json",
}

# ─── Load reference images ────────────────────────────────────────────────────
REF_B64_LIST = []
for ref in REF_IMAGES:
    if ref.exists():
        raw = ref.read_bytes()
        REF_B64_LIST.append(f"data:image/png;base64,{base64.b64encode(raw).decode()}")
        print(f"Reference loaded: {ref} ({len(raw) // 1024}KB)")
    else:
        print(f"WARNING: Reference not found: {ref}")

# ─── Locked descriptions (per video_pipeline_master.md) ──────────────────────
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
    "color palette, soft lighting with gentle gradients. 6:19 vertical composition "
    "with space at top and bottom for text overlays. No photorealistic, no harsh "
    "shadows, no cold tones, no text, no watermark, no extra characters."
)

# ─── Scene Prompts ────────────────────────────────────────────────────────────
PROMPTS = [
    # ── Anchor scenes (use reference image) ──
    {
        "id": "a1_hook",
        "title": "A1 — Hook: Warm Concerned-But-Loving Smile",
        "type": "anchor",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She is looking directly at the viewer with "
            "a warm, knowing smile — her eyes carry gentle empathy, as if she understands "
            "what you're going through. Both hands resting naturally on the armrests of the "
            "chair. Her posture is relaxed and open, conveying comfort and wisdom. Her "
            'expression says "I know this is hard... let me help." '
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a2_index_finger",
        "title": 'A2 — Speaking: Index Finger Raised, "Number One"',
        "type": "anchor",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera, slightly tighter framing on face and upper "
            "body. She is mid-speech with her mouth slightly open, her right hand raised "
            'with index finger pointing up — the classic "listen to this" gesture. Her '
            "expression is warm and engaged, her eyes focused on the camera with gentle "
            "authority, like a grandmother sharing something she deeply believes in. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a3_three_fingers",
        "title": 'A3 — Speaking: Three Fingers Raised, "Number Three"',
        "type": "anchor",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera. She is mid-speech, her right hand raised "
            "showing three fingers. Her expression is deeply warm — soft eyes, a knowing "
            "half-smile, slight head tilt to the side. This is the most emotional moment. "
            'Her eyes communicate tenderness, as if saying "this one matters most." '
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a4_cta_hands_clasped",
        "title": "A4 — CTA: Warm Closing Smile, Hands Clasped",
        "type": "anchor",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She has both hands clasped together at chest "
            "level in a caring, prayer-like gesture. Her expression is a full warm smile — "
            'grateful, compassionate, as if saying "I hope this helps you." Her eyes are '
            "looking directly at the camera with gentle confidence, conveying deep "
            "grandmother warmth and sincerity. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    # ── B-roll scenes (no reference image needed) ──
    {
        "id": "b1_safety",
        "title": 'B1 — Rule 1: "It\'s okay... let\'s look at it together." → SAFETY',
        "type": "broll",
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s sitting beside her 12-year-old son at a wooden study desk. The "
            "mother has her arm around the boy's shoulder in a comforting gesture. The boy "
            "looks down at a test paper on the desk with a sad, disappointed expression. "
            "The mother leans in close, her face showing warm reassurance — not anger, not "
            "disappointment, just love and support. "
            "The setting is a warm Filipino home study corner — a wooden desk with an open "
            "textbook and scattered pencils, a small desk lamp with warm golden glow as the "
            "main light source, a bookshelf with school books in the background, warm "
            "cream-colored walls. The boy wears a white school polo shirt. "
            "Medium shot, eye-level camera - both figures equally framed. Warm color "
            "palette: golden desk lamp glow, warm wood tones, cream walls. "
            f"{STYLE_SUFFIX}"
        ),
    },
    {
        "id": "b2_understanding",
        "title": 'B2 — Rule 2: "What part was hardest for you?" → UNDERSTANDING',
        "type": "broll",
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s and her 11-year-old daughter sitting together on the floor of a "
            "warm living room. They sit cross-legged facing each other. The girl holds an "
            "open notebook and points at a page while explaining something, her brow "
            "slightly furrowed in concentration. The mother leans forward with genuine "
            "interest, chin resting lightly on her hand, nodding with an encouraging smile. "
            "The setting is a warm Filipino home living room — warm afternoon sunlight "
            "streaming through a window with sheer curtains, a woven rattan mat under "
            "them, warm wood flooring, potted plants on the windowsill, a cozy sofa in the "
            "background. The girl wears a light blue school uniform. "
            "Medium shot, slightly high angle camera — looking down at both figures on the "
            "floor with warmth. Warm color palette: golden afternoon light, warm wood tones, "
            "light blue accent from uniform. "
            f"{STYLE_SUFFIX}"
        ),
    },
    {
        "id": "b3_belief",
        "title": 'B3 — Rule 3: "I know you\'ll do better next time." → BELIEF',
        "type": "broll",
        "prompt": (
            "A warm 3D-animated Pixar-style digital illustration of a Filipina mother in "
            "her mid-30s and her 13-year-old son giving each other a high-five across a "
            "study table. Both are smiling confidently. Open textbooks and notebooks are "
            "spread on the table between them. The boy's expression is one of renewed "
            "determination and hope. The mother beams with genuine pride and belief. "
            "The setting is a warm Filipino home dining/study area in the evening — a "
            "wooden dining table serving as a study space, warm amber lamplight from an "
            "overhead lamp, a glass of water and a small plate of snacks on the table, "
            "warm cream walls with a framed certificate or family photo visible, a potted "
            "plant in the corner. The boy wears a casual t-shirt. "
            "Medium shot, eye-level camera — the high-five hands at center of frame, both "
            "faces visible and smiling. Warm color palette: amber evening light, warm wood "
            "tones, warm skin tones. "
            f"{STYLE_SUFFIX}"
        ),
    },
]


def submit_generation(prompt_text, use_ref=False):
    """Submit generation to Higgsfield API."""
    url = f"{BASE_URL}/{MODEL_ID}"
    payload = {
        "prompt": prompt_text,
        "aspect_ratio": "9:16",
        "resolution": "1080p",
    }

    # Include reference image for anchor character consistency
    if use_ref and REF_B64_LIST:
        payload["reference_image"] = REF_B64_LIST[0]

    try:
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=60)
        if resp.status_code in (200, 201, 202):
            data = resp.json()
            return data.get("request_id"), data
        elif resp.status_code == 422 and use_ref:
            # Retry without reference if rejected
            print("   Ref image rejected, retrying without...")
            payload_clean = {
                "prompt": prompt_text,
                "aspect_ratio": "6:19",
                "resolution": "1080p",
            }
            resp2 = requests.post(url, headers=HEADERS, json=payload_clean, timeout=30)
            if resp2.status_code in (200, 201, 202):
                data = resp2.json()
                return data.get("request_id"), data
            else:
                print(f"   Submit failed: {resp2.status_code} — {resp2.text[:300]}")
        else:
            print(f"   Submit failed: {resp.status_code} — {resp.text[:300]}")
        return None, None
    except Exception as e:
        print(f"   Request error: {e}")
        return None, None


def poll_until_done(request_id):
    """Poll until completed or timeout."""
    url = f"{BASE_URL}/requests/{request_id}/status"
    start = time.time()
    while time.time() - start < MAX_POLL_TIME:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                status = data.get("status", "").lower()
                if status == "completed":
                    return data
                elif status in ("failed", "nsfw", "error"):
                    print(f"   Generation {status}: {json.dumps(data, indent=2)[:300]}")
                    return None
                else:
                    elapsed = int(time.time() - start)
                    print(f"   Status: {status} ({elapsed}s)")
            else:
                print(f"   Poll {resp.status_code}: {resp.text[:100]}")
        except Exception as e:
            print(f"   Poll error: {e}")
        time.sleep(POLL_INTERVAL)
    print("   Timeout")
    return None


def download_image(url, dest):
    """Download image from URL."""
    try:
        resp = requests.get(url, timeout=60)
        if resp.status_code == 200:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(resp.content)
            return True
    except Exception as e:
        print(f"   Download error: {e}")
    return False


def main():
    total = len(PROMPTS)
    print("=" * 70)
    print("VIDEO 01 — IMAGE GENERATION (Nanobanana PRO)")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
    print(f"   Model: {MODEL_ID}")
    print(f"   Aspect Ratio: 9:16 (native — will upscale later if needed)")
    print(f"   References: {len(REF_B64_LIST)} loaded")
    print(f"   Scenes: {total} (4 anchor + 3 B-roll)")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, p in enumerate(PROMPTS, 1):
        scene_dir = OUTPUT_DIR / p["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        use_ref = p["type"] == "anchor"
        ref_label = " [+REF]" if use_ref else ""

        print(f"\n{'_' * 70}")
        print(f"[{i}/{total}] {p['title']}{ref_label}")
        print(f"   Type: {p['type']}")
        print(f"   Prompt: {len(p['prompt'])} chars")
        print(f"   Submitting...")

        request_id, submit_data = submit_generation(p["prompt"], use_ref=use_ref)
        if not request_id:
            results.append({"id": p["id"], "title": p["title"], "type": p["type"], "file": None, "status": "FAILED"})
            continue

        print(f"   Request: {request_id}")
        (scene_dir / "submit_response.json").write_text(json.dumps(submit_data, indent=2))

        print(f"   Polling...")
        result = poll_until_done(request_id)
        if not result:
            results.append({"id": p["id"], "title": p["title"], "type": p["type"], "file": None, "status": "FAILED"})
            continue

        (scene_dir / "result.json").write_text(json.dumps(result, indent=2))

        images = result.get("images", [])
        files_saved = []
        for j, img in enumerate(images, 1):
            img_url = img.get("url", "")
            if img_url:
                ext = "jpg" if "jpg" in img_url.lower() else "png"
                dest = scene_dir / f"variant_{j}.{ext}"
                if download_image(img_url, dest):
                    files_saved.append(str(dest))
                    print(f"   Saved: {dest}")

        if files_saved:
            successes += 1
            results.append({"id": p["id"], "title": p["title"], "type": p["type"], "file": files_saved[0], "status": "OK"})
            print(f"   Done [{successes} total]")
        else:
            results.append({"id": p["id"], "title": p["title"], "type": p["type"], "file": None, "status": "NO_IMAGES"})

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/{total} images generated")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    for r in results:
        status_icon = "✓" if r["status"] == "OK" else "✗"
        print(f"   {status_icon} {r['id']}: {r['status']}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

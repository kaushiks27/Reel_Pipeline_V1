#!/usr/bin/env python3
"""
Anchor Scene Generation — Nanobanana PRO (Higgsfield API)

Generates 3 anchor scene images using the frozen character reference (C3)
for character consistency via Higgsfield Nanobanana PRO API.

Usage:
    python3 execution/generate_anchor_scenes.py
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
OUTPUT_DIR = Path("assets/anchor_scenes/nanobanana_pro")

# Reference images for character consistency
REF_IMAGES = [
    Path("assets/character_freeze/chatgpt/option_3.png"),
    Path("assets/character_freeze/chatgpt/option_4.png"),
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
    "color palette, soft lighting with gentle gradients. 9:16 vertical "
    "composition with space at top and bottom for text overlays. "
    "No photorealistic, no harsh shadows, no cold tones, no text, "
    "no watermark, no extra characters."
)

# ─── 3 Anchor Scene Prompts ──────────────────────────────────────────────────
PROMPTS = [
    {
        "id": "a1_hook_smile",
        "title": "A1 — Hook: Warm Inviting Smile",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She is looking directly at the viewer with "
            "a warm, welcoming smile — eyes slightly crinkled as if greeting an old "
            "friend. Both hands resting naturally on the armrests of the chair. Her "
            "posture is relaxed and open, conveying trust and warmth. Her expression "
            'says "let me share something important with you." '
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a2_speaking_gesture",
        "title": "A2 — Speaking: Gentle Explaining Gesture",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium close-up, eye-level camera, slightly tighter framing on face and "
            "upper body. She is mid-speech with her mouth slightly open, her right hand "
            "raised at chest level making a gentle open-palm explaining gesture. Her "
            "expression is warm and engaged — like a mother sharing wisdom she deeply "
            "believes in. Her eyes are focused and kind, communicating with gentle authority. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
    {
        "id": "a3_cta_hands_clasped",
        "title": "A3 — CTA: Warm Closing Smile, Hands Together",
        "prompt": (
            f"{CHAR_DESC} "
            "Medium shot, eye-level camera. She has both hands clasped together at "
            "chest level in a caring, prayer-like gesture. Her expression is a full "
            'warm smile — grateful, compassionate, as if saying "I hope this helps '
            'you." Her eyes are looking directly at the camera with gentle confidence, '
            "conveying deep maternal warmth and sincerity. "
            f"{BG_DESC} {STYLE_SUFFIX}"
        ),
    },
]


def submit_generation(prompt_text):
    """Submit generation to Higgsfield API with reference images."""
    url = f"{BASE_URL}/{MODEL_ID}"
    payload = {
        "prompt": prompt_text,
        "aspect_ratio": "9:16",
        "resolution": "1080p",
    }

    # Include reference image for character consistency
    if REF_B64_LIST:
        payload["reference_image"] = REF_B64_LIST[0]

    try:
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=60)
        if resp.status_code in (200, 201, 202):
            data = resp.json()
            return data.get("request_id"), data
        elif resp.status_code == 422 and REF_B64_LIST:
            # Retry without reference if rejected
            print("   Ref image rejected, retrying without...")
            payload_clean = {
                "prompt": prompt_text,
                "aspect_ratio": "9:16",
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
    print("=" * 70)
    print("ANCHOR SCENE GENERATION — Nanobanana PRO")
    print(f"   Model: {MODEL_ID}")
    print(f"   References: {len(REF_B64_LIST)} loaded")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, p in enumerate(PROMPTS, 1):
        scene_dir = OUTPUT_DIR / p["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/3] {p['title']}")
        print(f"   Prompt: {len(p['prompt'])} chars")
        print(f"   Submitting...")

        request_id, submit_data = submit_generation(p["prompt"])
        if not request_id:
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "FAILED"})
            continue

        print(f"   Request: {request_id}")
        (scene_dir / "submit_response.json").write_text(json.dumps(submit_data, indent=2))

        print(f"   Polling...")
        result = poll_until_done(request_id)
        if not result:
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "FAILED"})
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
            results.append({"id": p["id"], "title": p["title"], "file": files_saved[0], "status": "OK"})
            print(f"   Done [{successes} total]")
        else:
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "NO_IMAGES"})

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/3 anchor scenes generated")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

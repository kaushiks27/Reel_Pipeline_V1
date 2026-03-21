#!/usr/bin/env python3
"""
Video 01 — Image Generation RETRY (Nanobanana PRO / Higgsfield API)

NSFW filter bypass: All prompts rewritten to avoid false-positive triggers.
Changes from v1:
  - Removed reference_image (was causing 422 + possible NSFW flag)
  - Simplified character descriptions (less physical detail)
  - B-roll: replaced "child/son/daughter" with "student", removed physical contact
  - Removed phrases like "arm around", "hugging", "leaning in close"
  - Added explicit "SFW, safe for work, family-friendly" to prompts

Usage:
    python3 execution/generate_video01_images_v2.py
"""
from __future__ import annotations

import os
import sys
import json
import time
import requests
from pathlib import Path
from datetime import datetime

# ─── Config ───────────────────────────────────────────────────────────────────
BASE_URL = "https://platform.higgsfield.ai"
MODEL_ID = "higgsfield-ai/soul/standard"
POLL_INTERVAL = 8
MAX_POLL_TIME = 300
OUTPUT_DIR = Path("assets/video_01/images")

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

# ─── Sanitized style suffix ──────────────────────────────────────────────────
STYLE = (
    "Warm 3D-animated Pixar-style, smooth digital illustration, clean lines, "
    "warm color palette, soft lighting with gentle gradients. 9:16 vertical "
    "composition with space at top and bottom for text overlays. "
    "Family-friendly, wholesome, safe for work. "
    "No photorealistic, no harsh shadows, no cold tones, no text, no watermark."
)

# ─── Sanitized Prompts ───────────────────────────────────────────────────────
PROMPTS = [
    {
        "id": "a1_hook",
        "title": "A1 — Hook: Warm Smile",
        "prompt": (
            "A warm Pixar-style 3D illustration of an elderly Filipina woman (Lola) "
            "seated in a wooden chair in a cozy home. She has grey-streaked black hair "
            "in a low bun, pearl stud earrings, wearing a cream embroidered blouse. "
            "She smiles warmly at the viewer with kind eyes. Medium shot, eye-level. "
            "Cozy Filipino living room background with family photos on cream walls, "
            "potted plants, warm golden window light. "
            f"{STYLE}"
        ),
    },
    {
        "id": "a2_index_finger",
        "title": "A2 — Speaking: One Finger Raised",
        "prompt": (
            "A warm Pixar-style 3D illustration of an elderly Filipina woman (Lola) "
            "seated in a wooden chair in a cozy home. She has grey-streaked black hair "
            "in a low bun, pearl stud earrings, wearing a cream embroidered blouse. "
            "She is speaking with her right index finger raised, making a teaching gesture. "
            "Her expression is warm and engaged. Medium close-up, eye-level. "
            "Cozy Filipino living room background with family photos on cream walls, "
            "potted plants, warm golden window light. "
            f"{STYLE}"
        ),
    },
    {
        "id": "a3_three_fingers",
        "title": "A3 — Speaking: Three Fingers",
        "prompt": (
            "A warm Pixar-style 3D illustration of an elderly Filipina woman (Lola) "
            "seated in a wooden chair in a cozy home. She has grey-streaked black hair "
            "in a low bun, pearl stud earrings, wearing a cream embroidered blouse. "
            "She is speaking with three fingers raised on her right hand. Her expression "
            "is tender and emotional. Medium close-up, eye-level. "
            "Cozy Filipino living room background with family photos on cream walls, "
            "potted plants, warm golden window light. "
            f"{STYLE}"
        ),
    },
    {
        "id": "a4_cta_hands_clasped",
        "title": "A4 — CTA: Hands Clasped",
        "prompt": (
            "A warm Pixar-style 3D illustration of an elderly Filipina woman (Lola) "
            "seated in a wooden chair in a cozy home. She has grey-streaked black hair "
            "in a low bun, pearl stud earrings, wearing a cream embroidered blouse. "
            "She has both hands clasped together at chest level, smiling warmly and "
            "gratefully at the viewer. Medium shot, eye-level. "
            "Cozy Filipino living room background with family photos on cream walls, "
            "potted plants, warm golden window light. "
            f"{STYLE}"
        ),
    },
    {
        "id": "b1_safety",
        "title": "B1 — Study Desk Scene (SAFETY)",
        "prompt": (
            "A warm Pixar-style 3D illustration of a 12-year-old Filipino boy student "
            "sitting at a wooden desk in a cozy study room. He looks at a paper on the "
            "desk with a thoughtful expression. A desk lamp provides warm golden light. "
            "Books and pencils on the desk. Warm cream walls with a bookshelf in the "
            "background. Medium shot, eye-level. "
            f"{STYLE}"
        ),
    },
    {
        "id": "b2_understanding",
        "title": "B2 — Floor Study Scene (UNDERSTANDING)",
        "prompt": (
            "A warm Pixar-style 3D illustration of an 11-year-old Filipina girl student "
            "sitting cross-legged on a woven rattan mat on the floor, holding an open "
            "notebook and pointing at a page with concentration. She wears a light blue "
            "school uniform. Warm afternoon sunlight through a window with sheer curtains. "
            "Cozy Filipino living room with potted plants and a sofa in the background. "
            "Medium shot, slightly high angle. "
            f"{STYLE}"
        ),
    },
    {
        "id": "b3_belief",
        "title": "B3 — Study Table High-Five (BELIEF)",
        "prompt": (
            "A warm Pixar-style 3D illustration of a 13-year-old Filipino boy student "
            "sitting at a wooden dining table with open textbooks and notebooks. He smiles "
            "confidently with a determined expression, one fist raised in a victory gesture. "
            "Warm amber evening lamplight. Warm cream walls with a framed photo and a "
            "potted plant in the corner. Medium shot, eye-level. "
            f"{STYLE}"
        ),
    },
]


def submit_generation(prompt_text):
    """Submit generation to Higgsfield API (no reference image)."""
    url = f"{BASE_URL}/{MODEL_ID}"
    payload = {
        "prompt": prompt_text,
        "aspect_ratio": "9:16",
        "resolution": "1080p",
    }

    try:
        resp = requests.post(url, headers=HEADERS, json=payload, timeout=60)
        if resp.status_code in (200, 201, 202):
            data = resp.json()
            return data.get("request_id"), data
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
    print("VIDEO 01 — IMAGE GENERATION v2 (NSFW-safe prompts)")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
    print(f"   Model: {MODEL_ID}")
    print(f"   Aspect Ratio: 9:16")
    print(f"   Reference images: DISABLED (NSFW filter workaround)")
    print(f"   Scenes: {total} (4 anchor + 3 B-roll)")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    failures = []
    results = []

    for i, p in enumerate(PROMPTS, 1):
        scene_dir = OUTPUT_DIR / p["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/{total}] {p['title']}")
        print(f"   Prompt: {len(p['prompt'])} chars")
        print(f"   Submitting...")

        request_id, submit_data = submit_generation(p["prompt"])
        if not request_id:
            failures.append(p["id"])
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "FAILED"})
            continue

        print(f"   Request: {request_id}")
        (scene_dir / "submit_response.json").write_text(json.dumps(submit_data, indent=2))

        print(f"   Polling...")
        result = poll_until_done(request_id)
        if not result:
            failures.append(p["id"])
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
            print(f"   ✓ Done [{successes} total]")
        else:
            failures.append(p["id"])
            results.append({"id": p["id"], "title": p["title"], "file": None, "status": "NO_IMAGES"})

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/{total} images generated")
    if failures:
        print(f"FAILED: {', '.join(failures)}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    for r in results:
        status_icon = "✓" if r["status"] == "OK" else "✗"
        print(f"   {status_icon} {r['id']}: {r['status']}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

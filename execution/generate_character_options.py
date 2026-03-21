#!/usr/bin/env python3
"""
Character Design Freeze — Filipina Mother Avatar (Nanobanana PRO)

Generates 5 concept-animated character variations of a Filipina mother (30-40yo)
via Higgsfield Nanobanana PRO API for character freeze selection.

Grounded in:
- 16_Nano_banana.md: character consistency, talk like crew
- 21_Making_Your_Avatar_More_Realistic.md: prompt modifier categories
- 54_AI_Video_Creation_Workflow.md: Step 3 image creation
- directives/client_video_production.md: concept-animated style (NOT photorealistic)

Usage:
    python3 execution/generate_character_options.py
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
OUTPUT_DIR = Path("assets/character_freeze/nanobanana_pro")

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

# ─── Character Base Description ───────────────────────────────────────────────
# Concept-animated style (per client_video_production.md — NOT photorealistic)
# Each prompt varies the expression/angle while keeping the character locked

CHAR_BASE = (
    "A warm, inviting concept art illustration of a Filipina woman in her mid-30s. "
    "She has shoulder-length straight black hair with soft layers, warm brown skin, "
    "kind dark brown eyes, a gentle knowing smile, and a natural Filipino facial structure "
    "with soft cheekbones. She wears a casual floral blouse in soft coral tones. "
)

SETTING_BASE = (
    "She is sitting comfortably in a cushioned armchair in a cozy Filipino living room. "
    "Warm golden lamplight from a side table lamp, potted plants in the background, "
    "a small wooden side table. Warm color palette dominated by golden amber, soft brown, "
    "and muted green from plants. "
)

STYLE_BASE = (
    "Concept art style, smooth digital illustration, clean lines, warm color palette, "
    "soft lighting, gentle gradients. 9:16 vertical composition. "
    "No photorealistic, no harsh lighting, no cold tones, no text, no watermark."
)

# ─── 5 Variations ─────────────────────────────────────────────────────────────
PROMPTS = [
    {
        "id": "option_1_warm_smile",
        "title": "Warm Welcoming Smile — Medium Shot",
        "prompt": (
            f"{CHAR_BASE}"
            f"{SETTING_BASE}"
            "Medium shot, eye-level camera. She smiles warmly with her eyes slightly crinkled, "
            "both hands resting on the armrest, looking directly at the viewer with a gentle, "
            "inviting expression. Soft golden light illuminating her face from the side. "
            f"{STYLE_BASE}"
        ),
    },
    {
        "id": "option_2_speaking",
        "title": "Speaking Gently — Medium Close-Up",
        "prompt": (
            f"{CHAR_BASE}"
            f"{SETTING_BASE}"
            "Medium close-up, eye-level camera. She is mid-speech with her mouth slightly open, "
            "one hand making a gentle explaining gesture. Expression is warm and engaged, as if "
            "sharing motherly advice. Soft golden lamplight highlighting her features. "
            f"{STYLE_BASE}"
        ),
    },
    {
        "id": "option_3_thoughtful",
        "title": "Thoughtful Moment — Medium Shot",
        "prompt": (
            f"{CHAR_BASE}"
            f"{SETTING_BASE}"
            "Medium shot, slight low angle. She has a thoughtful, knowing expression with a "
            "slight half-smile, one hand touching her chin gently. Looking slightly off-camera "
            "as if remembering something meaningful. Warm side lighting creating gentle shadows. "
            f"{STYLE_BASE}"
        ),
    },
    {
        "id": "option_4_hands_together",
        "title": "Hands Together, Caring Expression — Medium Shot",
        "prompt": (
            f"{CHAR_BASE}"
            f"{SETTING_BASE}"
            "Medium shot, eye-level camera. She has her hands clasped together at chest level, "
            "a caring and compassionate expression on her face. Looking directly at camera with "
            "gentle confidence, like a mother about to share an important truth. Warm balanced "
            "lighting from both the lamp and ambient fill. "
            f"{STYLE_BASE}"
        ),
    },
    {
        "id": "option_5_closeup_eyes",
        "title": "Close-Up with Kind Eyes — Medium Close-Up",
        "prompt": (
            f"{CHAR_BASE}"
            f"{SETTING_BASE}"
            "Medium close-up, eye-level camera, tighter framing on her face and shoulders. "
            "She has a soft, knowing smile with kind eyes that convey deep warmth and wisdom "
            "beyond her years. Golden lamplight creating a soft rim light on her hair. "
            "Expression is maternal and reassuring. "
            f"{STYLE_BASE}"
        ),
    },
]


def submit_generation(prompt_text):
    """Submit generation to Higgsfield API."""
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
    print("=" * 70)
    print("CHARACTER DESIGN FREEZE — Filipina Mother (Nanobanana PRO)")
    print(f"   Model: Nanobanana PRO via Higgsfield ({MODEL_ID})")
    print("   Style: Concept-Animated (warm, clean illustration)")
    print("   Aspect: 9:16 vertical | Resolution: 1080p")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, p in enumerate(PROMPTS, 1):
        scene_dir = OUTPUT_DIR / p["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/5] {p['title']}")
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

    # Write results
    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/5 character options generated")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

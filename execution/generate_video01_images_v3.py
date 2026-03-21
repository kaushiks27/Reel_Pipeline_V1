#!/usr/bin/env python3
"""
Video 01 — Image Generation v3 (Nanobanana PRO → gpt-image-1.5 fallback)

NSFW avoidance per expert guide (examples/avoid_nsfw.md):
  - Editorial/neutral language only
  - No body-focused descriptions
  - Short, clean prompts
  - Professional tone

If Higgsfield returns NSFW → auto-fallback to OpenAI gpt-image-1.5

Usage:
    python3 execution/generate_video01_images_v3.py
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
HF_BASE_URL = "https://platform.higgsfield.ai"
HF_MODEL_ID = "higgsfield-ai/soul/standard"
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

HF_API_KEY = os.getenv("HIGGSFIELD_API_KEY")
HF_API_SECRET = os.getenv("HIGGSFIELD_API_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not HF_API_KEY or not HF_API_SECRET:
    print("WARNING: HIGGSFIELD_API_KEY or HIGGSFIELD_API_SECRET not in .env — Higgsfield disabled")
if not OPENAI_API_KEY:
    print("WARNING: OPENAI_API_KEY not in .env — ChatGPT fallback disabled")

HF_HEADERS = {
    "Authorization": f"Key {HF_API_KEY}:{HF_API_SECRET}",
    "Content-Type": "application/json",
} if HF_API_KEY and HF_API_SECRET else {}

OAI_HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json",
} if OPENAI_API_KEY else {}

# ─── Editorial-style prompts (per expert NSFW avoidance guide) ────────────────
# Key changes: short prompts, editorial tone, no physical descriptions,
# no body-focused language, professional neutral wording
PROMPTS = [
    {
        "id": "a1_hook",
        "title": "A1 — Hook: Warm Smile",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "An elderly Filipina grandmother seated in a wooden chair, "
            "warm smile, grey-streaked hair in a low bun, pearl earrings, "
            "cream embroidered blouse. Cozy home interior, family photos on walls, "
            "potted plants, warm golden window light. "
            "Medium shot, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "a2_index_finger",
        "title": "A2 — Speaking: Teaching Gesture",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "An elderly Filipina grandmother seated in a wooden chair, "
            "speaking with index finger raised in a teaching gesture, "
            "grey-streaked hair in a low bun, pearl earrings, "
            "cream embroidered blouse. Cozy home interior, family photos, "
            "potted plants, warm golden light. "
            "Medium close-up, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "a3_three_fingers",
        "title": "A3 — Speaking: Three Fingers",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "An elderly Filipina grandmother seated in a wooden chair, "
            "holding up three fingers, warm expression, "
            "grey-streaked hair in a low bun, pearl earrings, "
            "cream embroidered blouse. Cozy home interior, family photos, "
            "warm golden light. "
            "Medium close-up, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "a4_cta_hands_clasped",
        "title": "A4 — CTA: Hands Clasped",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "An elderly Filipina grandmother seated in a wooden chair, "
            "hands clasped together at chest, grateful smile, "
            "grey-streaked hair in a low bun, pearl earrings, "
            "cream embroidered blouse. Cozy home interior, family photos, "
            "warm golden light. "
            "Medium shot, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "b1_safety",
        "title": "B1 — Study Scene (SAFETY)",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "A Filipino student, age 12, sitting at a wooden study desk, "
            "looking at schoolwork with a thoughtful expression. "
            "Desk lamp, textbooks, pencils. Warm study room, cream walls, bookshelf. "
            "Medium shot, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "b2_understanding",
        "title": "B2 — Notebook Scene (UNDERSTANDING)",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "A Filipina student, age 11, sitting cross-legged on a woven mat, "
            "holding an open notebook, pointing at a page. Light blue school uniform. "
            "Warm living room, afternoon sunlight, potted plants, cozy sofa. "
            "Medium shot, slightly high angle, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
    {
        "id": "b3_belief",
        "title": "B3 — Victory Gesture (BELIEF)",
        "prompt": (
            "Editorial illustration, Pixar-style 3D render. "
            "A Filipino student, age 13, sitting at a dining table with textbooks, "
            "smiling confidently with a fist raised in a victory gesture. "
            "Warm evening lamplight, cream walls, framed photos, potted plant. "
            "Medium shot, eye-level, 9:16 vertical portrait. "
            "Clean digital illustration, warm palette, soft lighting."
        ),
    },
]


# ─── Higgsfield Functions ────────────────────────────────────────────────────

def hf_submit(prompt_text):
    """Submit to Higgsfield Nanobanana PRO."""
    url = f"{HF_BASE_URL}/{HF_MODEL_ID}"
    payload = {
        "prompt": prompt_text,
        "aspect_ratio": "9:16",
        "resolution": "1080p",
    }
    try:
        resp = requests.post(url, headers=HF_HEADERS, json=payload, timeout=60)
        if resp.status_code in (200, 201, 202):
            data = resp.json()
            return data.get("request_id"), data
        else:
            print(f"   [HF] Submit failed: {resp.status_code} — {resp.text[:200]}")
        return None, None
    except Exception as e:
        print(f"   [HF] Request error: {e}")
        return None, None


def hf_poll(request_id):
    """Poll Higgsfield until done."""
    url = f"{HF_BASE_URL}/requests/{request_id}/status"
    start = time.time()
    while time.time() - start < MAX_POLL_TIME:
        try:
            resp = requests.get(url, headers=HF_HEADERS, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                status = data.get("status", "").lower()
                if status == "completed":
                    return data
                elif status in ("failed", "nsfw", "error"):
                    print(f"   [HF] Generation {status}")
                    return None
                else:
                    elapsed = int(time.time() - start)
                    print(f"   [HF] Status: {status} ({elapsed}s)")
            else:
                print(f"   [HF] Poll {resp.status_code}")
        except Exception as e:
            print(f"   [HF] Poll error: {e}")
        time.sleep(POLL_INTERVAL)
    print("   [HF] Timeout")
    return None


def hf_generate(prompt_text, scene_dir):
    """Try Higgsfield. Returns list of saved file paths or empty list."""
    print("   [HF] Submitting to Nanobanana PRO...")
    request_id, submit_data = hf_submit(prompt_text)
    if not request_id:
        return []

    print(f"   [HF] Request: {request_id}")
    (scene_dir / "hf_submit.json").write_text(json.dumps(submit_data, indent=2))

    print("   [HF] Polling...")
    result = hf_poll(request_id)
    if not result:
        return []

    (scene_dir / "hf_result.json").write_text(json.dumps(result, indent=2))
    images = result.get("images", [])
    files = []
    for j, img in enumerate(images, 1):
        img_url = img.get("url", "")
        if img_url:
            ext = "jpg" if "jpg" in img_url.lower() else "png"
            dest = scene_dir / f"hf_variant_{j}.{ext}"
            if download_image(img_url, dest):
                files.append(str(dest))
                print(f"   [HF] ✓ Saved: {dest}")
    return files


# ─── OpenAI ChatGPT Fallback ─────────────────────────────────────────────────

def oai_generate(prompt_text, scene_dir):
    """Fallback: generate via OpenAI chatgpt-image-latest."""
    if not OAI_HEADERS:
        print("   [OAI] No API key — skipping fallback")
        return []

    print("   [OAI] Falling back to chatgpt-image-latest...")
    url = "https://api.openai.com/v1/images/generations"
    payload = {
        "model": "chatgpt-image-latest",
        "prompt": prompt_text,
        "n": 1,
        "size": "1024x1536",  # Closest portrait size for chatgpt-image-latest
        "quality": "high",
    }

    try:
        resp = requests.post(url, headers=OAI_HEADERS, json=payload, timeout=120)
        if resp.status_code == 200:
            data = resp.json()
            img_data = data["data"][0]

            if "b64_json" in img_data:
                img_bytes = base64.b64decode(img_data["b64_json"])
                dest = scene_dir / "oai_image.png"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(img_bytes)
                print(f"   [OAI] ✓ Saved: {dest} ({len(img_bytes) // 1024}KB)")
                return [str(dest)]
            elif "url" in img_data:
                img_url = img_data["url"]
                dest = scene_dir / "oai_image.png"
                if download_image(img_url, dest):
                    print(f"   [OAI] ✓ Saved: {dest}")
                    return [str(dest)]

            # Save metadata
            revised = img_data.get("revised_prompt", "")
            if revised:
                (scene_dir / "oai_meta.json").write_text(json.dumps({
                    "revised_prompt": revised,
                    "model": "chatgpt-image-latest",
                    "size": "1024x1792",
                }, indent=2))

        else:
            error_text = resp.text[:300]
            print(f"   [OAI] API error: {resp.status_code} — {error_text}")

    except Exception as e:
        print(f"   [OAI] Error: {e}")
    return []


# ─── Utils ────────────────────────────────────────────────────────────────────

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


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    total = len(PROMPTS)
    print("=" * 70)
    print("VIDEO 01 — IMAGE GENERATION v3")
    print("   Strategy: Nanobanana PRO (editorial prompts) → gpt-image-1.5 fallback")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
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

        # Try Higgsfield first
        files = hf_generate(p["prompt"], scene_dir)

        # If Higgsfield failed → fallback to ChatGPT
        if not files:
            print("   [HF] ✗ Failed — trying ChatGPT fallback...")
            files = oai_generate(p["prompt"], scene_dir)

        if files:
            successes += 1
            source = "HF" if "hf_" in files[0] else "OAI"
            results.append({"id": p["id"], "title": p["title"], "file": files[0], "source": source, "status": "OK"})
            print(f"   ✓ Done via {source} [{successes}/{total}]")
        else:
            results.append({"id": p["id"], "title": p["title"], "file": None, "source": None, "status": "FAILED"})
            print(f"   ✗ FAILED on both HF and OAI")

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"COMPLETE: {successes}/{total} images generated")
    for r in results:
        icon = "✓" if r["status"] == "OK" else "✗"
        src = f" [{r['source']}]" if r["source"] else ""
        print(f"   {icon} {r['id']}: {r['status']}{src}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

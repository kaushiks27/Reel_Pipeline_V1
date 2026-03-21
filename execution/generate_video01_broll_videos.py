#!/usr/bin/env python3
"""
Video 01 — B-Roll Video Generation (Kling 3.0 via API)

Generates 3 B-roll motion videos (NO dialogue, NO sound) from B-roll images.
Uses Kling 3.0 Pro mode via api-singapore.klingai.com.

Usage:
    python3 execution/generate_video01_broll_videos.py
"""
from __future__ import annotations

import os
import sys
import time
import base64
import json
import requests
from pathlib import Path
from datetime import datetime

try:
    import jwt
except ImportError:
    print("ERROR: PyJWT not installed. Run: pip3 install PyJWT")
    sys.exit(1)

# ─── Load .env ────────────────────────────────────────────────────────────────
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

ACCESS_KEY = os.getenv("KLING_ACCESS_KEY")
SECRET_KEY = os.getenv("KLING_SECRET_KEY")
if not ACCESS_KEY or not SECRET_KEY:
    print("ERROR: KLING_ACCESS_KEY and/or KLING_SECRET_KEY not in .env")
    sys.exit(1)

# ─── Kling API Config ────────────────────────────────────────────────────────
BASE_URL = "https://api-singapore.klingai.com"
MODEL = "kling-v3"
MODE = "pro"
DURATION = "5"
SOUND = "off"  # NO dialogue for B-roll

OUTPUT_DIR = Path("assets/video_01/videos")


def get_jwt_token():
    """Generate JWT token from access/secret key."""
    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {
        "iss": ACCESS_KEY,
        "exp": int(time.time()) + 1800,
        "nbf": int(time.time()) - 5,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256", headers=headers)


def create_video_task(image_path, prompt, camera_control=None):
    """Submit an image-to-video task to Kling API."""
    token = get_jwt_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    # Read and encode image (raw base64, NO data: prefix)
    image_bytes = Path(image_path).read_bytes()
    image_b64 = base64.b64encode(image_bytes).decode()

    payload = {
        "model_name": MODEL,
        "image": image_b64,
        "prompt": prompt,
        "negative_prompt": "blurry, distorted, text, watermark, ugly, deformed hands",
        "duration": DURATION,
        "mode": MODE,
        "sound": SOUND,
    }

    if camera_control:
        payload["camera_control"] = camera_control

    resp = requests.post(
        f"{BASE_URL}/v1/videos/image2video",
        headers=headers,
        json=payload,
        timeout=60,
    )

    if resp.status_code == 200:
        data = resp.json()
        if data.get("code") == 0:
            task_id = data["data"]["task_id"]
            print(f"   Task created: {task_id}")
            return task_id
        else:
            print(f"   API error: {data.get('message', 'unknown')}")
    else:
        print(f"   HTTP error: {resp.status_code} — {resp.text[:300]}")
    return None


def poll_task(task_id, max_wait=600):
    """Poll a task until it completes or times out."""
    start = time.time()
    while time.time() - start < max_wait:
        token = get_jwt_token()
        headers = {"Authorization": f"Bearer {token}"}
        resp = requests.get(
            f"{BASE_URL}/v1/videos/image2video/{task_id}",
            headers=headers,
            timeout=30,
        )

        if resp.status_code == 200:
            data = resp.json()
            if data.get("code") == 0:
                status = data["data"]["task_status"]
                elapsed = int(time.time() - start)
                print(f"   Status: {status} ({elapsed}s elapsed)")

                if status == "succeed":
                    videos = data["data"]["task_result"]["videos"]
                    if videos:
                        return videos[0]["url"]
                elif status == "failed":
                    msg = data["data"].get("task_status_msg", "unknown")
                    print(f"   FAILED: {msg}")
                    return None
            else:
                print(f"   Poll error: {data.get('message', 'unknown')}")

        time.sleep(15)

    print(f"   TIMEOUT after {max_wait}s")
    return None


def download_video(url, output_path):
    """Download video from URL."""
    resp = requests.get(url, timeout=120)
    if resp.status_code == 200:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(resp.content)
        size_kb = len(resp.content) // 1024
        print(f"   ✓ Saved: {output_path} ({size_kb}KB)")
        return True
    else:
        print(f"   Download failed: {resp.status_code}")
        return False


# ─── B-Roll Scenes ───────────────────────────────────────────────────────────
BROLL_SCENES = [
    {
        "id": "b1_safety",
        "title": 'B1 — RULE 1 B-ROLL: "Safety" [00:08 → 00:12]',
        "image": "assets/video_01/images/b1_safety/broll_image.png",
        "prompt": (
            "Medium shot, eye-level, gentle slow dolly in. "
            "A warm Pixar-style illustration of a Filipina mother sitting beside her "
            "son at a wooden study desk. Warm desk lamp glow illuminates the scene. "
            "The mother gently puts her arm around the boy's shoulder in a comforting "
            "gesture. The boy, looking down at papers, slowly looks up at his mother. "
            "A slow, reassuring smile appears on the mother's face. The desk lamp "
            "flickers softly with warm golden light. Smooth movement, no shake."
        ),
    },
    {
        "id": "b2_understanding",
        "title": 'B2 — RULE 2 B-ROLL: "Understanding" [00:16 → 00:20]',
        "image": "assets/video_01/images/b2_understanding/broll_image.png",
        "prompt": (
            "Medium shot, slightly high angle, slow pan right from daughter to mother. "
            "A warm Pixar-style illustration of a Filipina mother and her daughter "
            "sitting on a woven rattan mat on the floor. Warm afternoon sunlight "
            "through a window. The daughter points at a page in her notebook and "
            "looks up at her mother. The mother leans forward with genuine interest, "
            "nodding slowly, her smile widening. Curtains sway gently. Smooth camera."
        ),
    },
    {
        "id": "b3_belief",
        "title": 'B3 — RULE 3 B-ROLL: "Belief" [00:24 → 00:28]',
        "image": "assets/video_01/images/b3_belief/broll_image.png",
        "prompt": (
            "Medium shot, eye-level, static hold then slow crane up. "
            "A warm Pixar-style illustration of a Filipina mother and her teenage "
            "son at a dining table with open textbooks. Warm amber evening lamplight. "
            "The mother and son lean toward each other and give a confident high-five. "
            "Both break into wide, genuine smiles. The lamp's warm light intensifies "
            "slightly. Smooth, lifting feeling."
        ),
    },
]


def main():
    total = len(BROLL_SCENES)
    print("=" * 70)
    print("VIDEO 01 — B-ROLL VIDEO GENERATION (Kling 3.0)")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
    print(f"   Model: {MODEL} | Mode: {MODE}")
    print(f"   Duration: {DURATION}s | Sound: {SOUND}")
    print(f"   B-roll scenes: {total}")
    print(f"   NOTE: NO dialogue in B-roll — motion animation only")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, scene in enumerate(BROLL_SCENES, 1):
        scene_dir = OUTPUT_DIR / scene["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/{total}] {scene['title']}")
        print(f"   Image: {scene['image']}")
        print(f"   Prompt: {len(scene['prompt'])} chars")

        output_path = scene_dir / "broll_video.mp4"

        # Create task
        task_id = create_video_task(
            scene["image"], scene["prompt"], scene.get("camera")
        )
        if not task_id:
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": None, "status": "FAILED"})
            continue

        # Poll for completion
        video_url = poll_task(task_id)
        if not video_url:
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": None, "status": "FAILED"})
            continue

        # Download
        if download_video(video_url, output_path):
            successes += 1
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": str(output_path), "status": "OK"})

            # Save metadata
            meta = {
                "model": MODEL,
                "mode": MODE,
                "duration": DURATION,
                "sound": SOUND,
                "task_id": task_id,
                "video_url": video_url,
            }
            (scene_dir / "broll_video_meta.json").write_text(
                json.dumps(meta, indent=2)
            )
        else:
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": None, "status": "FAILED"})

    # Save results
    results_path = OUTPUT_DIR / "broll_results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"B-ROLL VIDEOS: {successes}/{total} generated via Kling 3.0")
    for r in results:
        icon = "✓" if r["status"] == "OK" else "✗"
        print(f"   {icon} {r['id']}: {r['status']}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

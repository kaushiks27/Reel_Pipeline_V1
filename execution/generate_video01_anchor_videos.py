#!/usr/bin/env python3
"""
Video 01 — Anchor Video Generation (Veo 3.1 via REST API)

Generates 5 anchor videos with lip-sync using locked anchor images.
Uses REST API directly (Python 3.8 compatible — no google-genai SDK needed).

Usage:
    python3 execution/generate_video01_anchor_videos.py
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

# ─── Load .env ────────────────────────────────────────────────────────────────
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, val = line.partition("=")
            os.environ.setdefault(key.strip(), val.strip())

API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
if not API_KEY:
    print("ERROR: GOOGLE_AI_STUDIO_API_KEY not in .env")
    sys.exit(1)

# ─── Veo 3.1 REST API Config ─────────────────────────────────────────────────
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"
MODEL = "models/veo-3.1-generate-preview"
GENERATE_URL = f"{BASE_URL}/{MODEL}:predictLongRunning?key={API_KEY}"

# ─── Locked voice blueprint ──────────────────────────────────────────────────
VOICE_BLUEPRINT = (
    'Filipino-English accent (speaks English with a natural Filipino accent), '
    'warm maternal tone, medium pace, gentle authority. '
    'brief pauses before key phrases as if thinking. sentences taper off '
    'slightly with reassurance.'
)

OUTPUT_DIR = Path("assets/video_01/videos")

# ─── Anchor scenes ───────────────────────────────────────────────────────────
ANCHOR_SCENES = [
    {
        "id": "a1_hook",
        "title": "A1 — HOOK [00:00 → 00:04]",
        "image": "assets/video_01/images/a1_hook/anchor.png",
        "prompt": (
            "Slow dolly in, medium shot to medium close-up, eye-level camera. "
            "The grandmother in the image begins to speak directly to the camera. Her "
            "lips part gently, her head tilts forward in a slight welcoming nod. Her "
            "eyes crinkle with warmth as she starts talking. Her hands remain resting "
            "naturally on the armrests. "
            "The warm golden window light creates soft highlights on her face. Very "
            "subtle parallax as the camera slowly pushes in over 4 seconds. "
            "Camera: Smooth slow dolly in. No handheld shake. Gentle, cinematic. "
            "Mood: Inviting, empathetic, curiosity-building. "
            'The woman says: "When your child fails a test... say these three things." '
            f"Voice: {VOICE_BLUEPRINT}"
        ),
    },
    {
        "id": "a2_rule1_speaking",
        "title": "A2 — RULE 1 LEAD [00:04 → 00:08]",
        "image": "assets/video_01/images/a2_rule1_speaking/anchor.png",
        "prompt": (
            "Medium close-up, eye-level, very subtle push-in. "
            "The grandmother is mid-speech. Her lips move naturally, her right "
            "hand lifts in a fluid open-palm explaining gesture at chest level. "
            "Slight eyebrow raise to emphasize importance. Her eyes stay focused on "
            "the camera with gentle authority. "
            "Warm golden light casts a soft glow on her face. Background steady and warm. "
            "Camera: Very subtle slow push-in, near-static. Smooth, cinematic. "
            "Mood: Engaged, nurturing. "
            "The woman says: \"Number one... 'It's okay... let's look at it together.'\" "
            f"Voice: {VOICE_BLUEPRINT}"
        ),
    },
    {
        "id": "a3_rule2_speaking",
        "title": "A3 — RULE 2 LEAD [00:12 → 00:16]",
        "image": "assets/video_01/images/a3_rule2_speaking/anchor.png",
        "prompt": (
            "Medium close-up, eye-level, slow dolly in. "
            "The grandmother raises her index finger in a teaching gesture. Her mouth "
            "opens to speak with natural lip movement. She leans slightly toward the "
            "camera with warm, engaged expression. "
            "Warm golden light creates soft highlights. Background cozy home setting. "
            "Camera: Slow dolly in over 4 seconds. Smooth, no shake. "
            "Mood: Patient, attentive. "
            "The woman says: \"Number two... 'What part was hardest for you?'\" "
            f"Voice: {VOICE_BLUEPRINT}"
        ),
    },
    {
        "id": "a4_rule3_speaking",
        "title": "A4 — RULE 3 LEAD [00:20 → 00:24]",
        "image": "assets/video_01/images/a4_rule3_speaking/anchor.png",
        "prompt": (
            "Medium close-up, eye-level, subtle push-in. "
            "The grandmother holds up three fingers. Her expression shifts to deeply "
            "warm — soft eyes, knowing half-smile, slight head tilt. Natural lip "
            "movement. Expression softens when she says the quoted phrase. Gentle "
            "eyebrow lift conveying tenderness. "
            "Camera: Very slow push-in. Smooth, intimate. Shallow depth of field. "
            "Mood: Tender, most emotional moment. "
            "The woman says: \"Number three... 'I know you'll do better next time.'\" "
            f"Voice: {VOICE_BLUEPRINT}"
        ),
    },
    {
        "id": "a5_cta",
        "title": "A5 — CTA [00:28 → 00:32]",
        "image": "assets/video_01/images/a5_cta/anchor.png",
        "prompt": (
            "Medium shot, eye-level, static then slow push-in. "
            "The grandmother leans forward slightly with a warm, grateful smile. "
            "Deeply compassionate expression — eyes crinkle, soft nod. Lips move "
            "naturally as she speaks. Hands come together gently at chest level. "
            "Warm golden light creates a soft rim light on her hair. "
            "Camera: Static first second, then very slow push-in. Warm, inviting. "
            "Mood: Warm closing, call to action. "
            'The woman says: "Share this... to help another parent." '
            f"Voice: {VOICE_BLUEPRINT}"
        ),
    },
]


def generate_anchor_video(scene, output_path):
    """Generate a single anchor video via Veo 3.1 REST API."""
    image_path = Path(scene["image"])
    if not image_path.exists():
        print(f"   ERROR: Image not found: {image_path}")
        return False

    try:
        # Read and encode image
        image_bytes = image_path.read_bytes()
        image_b64 = base64.standard_b64encode(image_bytes).decode()

        # Build request
        payload = {
            "instances": [
                {
                    "prompt": scene["prompt"],
                    "image": {
                        "bytesBase64Encoded": image_b64,
                        "mimeType": "image/png",
                    },
                }
            ],
            "parameters": {
                "aspectRatio": "9:16",
                "personGeneration": "allow_adult",
                "sampleCount": 1,
            },
        }

        print(f"   Calling Veo 3.1 REST API (9:16, allow_all)...")
        resp = requests.post(GENERATE_URL, json=payload, timeout=60)

        if resp.status_code != 200:
            print(f"   HTTP error: {resp.status_code} — {resp.text[:500]}")
            return False

        data = resp.json()

        # Handle long-running operation
        if "name" in data:
            operation_name = data["name"]
            print(f"   Operation: {operation_name}")
            return poll_operation(operation_name, output_path)
        elif "error" in data:
            print(f"   API error: {data['error']}")
            return False
        else:
            # Immediate response (unlikely for video)
            return save_video_from_response(data, output_path)

    except Exception as e:
        print(f"   ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def poll_operation(operation_name, output_path, max_wait=600):
    """Poll a long-running operation until done."""
    poll_url = f"{BASE_URL}/{operation_name}?key={API_KEY}"
    start = time.time()

    while time.time() - start < max_wait:
        time.sleep(15)
        elapsed = int(time.time() - start)

        try:
            resp = requests.get(poll_url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                done = data.get("done", False)
                print(f"   Polling... ({elapsed}s) done={done}")

                if done:
                    if "error" in data:
                        print(f"   Operation failed: {data['error']}")
                        return False
                    if "response" in data:
                        return save_video_from_response(data["response"], output_path)
                    print(f"   No response in completed operation")
                    return False
            else:
                print(f"   Poll HTTP error: {resp.status_code}")
        except Exception as e:
            print(f"   Poll error: {e}")

    print(f"   TIMEOUT after {max_wait}s")
    return False


def save_video_from_response(response_data, output_path):
    """Extract and save video from API response."""
    try:
        video_uri = None

        # Veo 3.1 predictLongRunning format:
        # response.generateVideoResponse.generatedSamples[0].video.uri
        gen_resp = response_data.get("generateVideoResponse", {})
        samples = gen_resp.get("generatedSamples", [])
        if samples:
            video_uri = samples[0].get("video", {}).get("uri")

        # Fallback: check other formats
        if not video_uri:
            videos = response_data.get("generatedVideos", response_data.get("videos", []))
            if videos:
                v = videos[0]
                video_uri = v.get("video", {}).get("uri") if isinstance(v.get("video"), dict) else None
                if not video_uri and "uri" in v:
                    video_uri = v["uri"]
                if not video_uri and "bytesBase64Encoded" in v.get("video", {}):
                    video_bytes = base64.b64decode(v["video"]["bytesBase64Encoded"])
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_bytes(video_bytes)
                    print(f"   ✓ Saved (base64): {output_path} ({len(video_bytes)//1024}KB)")
                    return True

        if not video_uri:
            print(f"   Cannot extract video URI from response")
            print(f"   Response keys: {list(response_data.keys())}")
            return False

        # Download from URI (must append API key)
        download_url = f"{video_uri}&key={API_KEY}" if "?" in video_uri else f"{video_uri}?key={API_KEY}"
        print(f"   Downloading video from URI...")
        download_resp = requests.get(download_url, timeout=120)
        if download_resp.status_code == 200:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(download_resp.content)
            size_kb = len(download_resp.content) // 1024
            print(f"   ✓ Saved: {output_path} ({size_kb}KB)")
            return True
        else:
            print(f"   Download failed: {download_resp.status_code} — {download_resp.text[:200]}")
            return False

    except Exception as e:
        print(f"   Save error: {e}")
        return False


def main():
    total = len(ANCHOR_SCENES)
    print("=" * 70)
    print("VIDEO 01 — ANCHOR VIDEO GENERATION (Veo 3.1 REST API)")
    print(f"   Topic: 3 Things to Say When Your Child Fails a Test")
    print(f"   Model: veo-3.1-generate-preview")
    print(f"   Aspect ratio: 9:16 (portrait)")
    print(f"   Lip-sync: ON (voice blueprint in every prompt)")
    print(f"   Anchor scenes: {total}")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    successes = 0
    results = []

    for i, scene in enumerate(ANCHOR_SCENES, 1):
        scene_dir = OUTPUT_DIR / scene["id"]
        scene_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n{'_' * 70}")
        print(f"[{i}/{total}] {scene['title']}")
        print(f"   Image: {scene['image']}")
        print(f"   Prompt: {len(scene['prompt'])} chars")

        output_path = scene_dir / "anchor_video.mp4"
        if generate_anchor_video(scene, output_path):
            successes += 1
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": str(output_path), "status": "OK"})
        else:
            results.append({"id": scene["id"], "title": scene["title"],
                            "file": None, "status": "FAILED"})

    # Save results
    results_path = OUTPUT_DIR / "anchor_results.json"
    results_path.write_text(json.dumps(results, indent=2))

    print(f"\n{'=' * 70}")
    print(f"ANCHOR VIDEOS: {successes}/{total} generated via Veo 3.1")
    for r in results:
        icon = "✓" if r["status"] == "OK" else "✗"
        print(f"   {icon} {r['id']}: {r['status']}")
    print(f"Output: {OUTPUT_DIR.resolve()}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()

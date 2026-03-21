#!/usr/bin/env python3
"""
BuLoop AI Video Pipeline — Automated Final Assembly
====================================================
Stitches 12 video clips into one reel with:
  - Anchor clips at FULL native length (voice + lip-sync preserved)
  - B-roll clips SHORTENED aggressively (~2s each)
  - B-roll native audio reduced to 50%
  - Anchor native audio at 100%
  - Background music layered across everything
  - Crossfade transitions between clips
  - Final export: 1080×1920, H.264+AAC, 30fps

Usage:
    python3 execution/assemble_reel.py
    python3 execution/assemble_reel.py --bgm assets/audio/bgm_track.mp3
    python3 execution/assemble_reel.py --no-transitions
"""

import subprocess
import json
import os
import sys
import shutil
import argparse
from pathlib import Path

# ─── CONFIGURATION ─────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
CLIPS_DIR = BASE_DIR / "assets" / "video_clips"
AUDIO_DIR = BASE_DIR / "assets" / "audio"
FINAL_DIR = BASE_DIR / "assets" / "final"
TMP_DIR = BASE_DIR / ".tmp" / "assembly"

# Scene definitions: (filename, type, trim_duration)
# ANCHOR clips: use None → keep full native duration (voice + lip-sync)
# B-ROLL clips: trim SHORT (~2s) to keep the reel tight
SCENES = [
    ("scene_01_anchor_video.mp4", "anchor", None),   # HOOK — full length
    ("scene_02_anchor_video.mp4", "anchor", None),   # Rule 1 — full length
    ("scene_03_broll_video.mp4",  "broll",  2.0),    # Mano Po — shortened
    ("scene_04_broll_video.mp4",  "broll",  2.0),    # Greeting — shortened
    ("scene_05_anchor_video.mp4", "anchor", None),   # Rule 2 — full length
    ("scene_06_broll_video.mp4",  "broll",  2.0),    # Family dinner — shortened
    ("scene_07_broll_video.mp4",  "broll",  2.0),    # Clearing table — shortened
    ("scene_08_anchor_video.mp4", "anchor", None),   # Rule 3 — full length
    ("scene_09_broll_video.mp4",  "broll",  2.0),    # Watering plants — shortened
    ("scene_10_broll_video.mp4",  "broll",  2.0),    # Family chores — shortened
    ("scene_11_anchor_video.mp4", "anchor", None),   # CTA — full length
    ("scene_12_broll_video.mp4",  "broll",  1.5),    # End card — shortest
]

TRANSITION_DURATION = 0.3   # seconds for crossfade
OUTPUT_FPS = 30
OUTPUT_FILE = "3_habits_respectful_kids_reel_v1.mp4"

# Volume levels
BROLL_AUDIO_VOLUME = 0.50    # B-roll native audio at 50%
ANCHOR_AUDIO_VOLUME = 1.0    # Anchor native audio at 100%
BGM_VOLUME = 0.15            # Background music at 15%
BGM_FADE_IN = 2.0            # seconds
BGM_FADE_OUT = 3.0           # seconds


def run_ffmpeg(cmd, label=""):
    """Run FFmpeg command with error handling."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ⚠️ FFmpeg error{f' ({label})' if label else ''}: {result.stderr[-300:]}")
        return False
    return True


def check_ffmpeg():
    """Verify FFmpeg is installed."""
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True, check=True)
        print(f"  ✅ {result.stdout.split(chr(10))[0]}")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("  ❌ FFmpeg not found. Install with: brew install ffmpeg")
        return False


def get_duration(filepath):
    """Get video duration in seconds."""
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", str(filepath)],
        capture_output=True, text=True, check=True
    )
    return float(json.loads(result.stdout)["format"]["duration"])


def step_1_prepare_clips():
    """Trim clips and adjust audio levels per type."""
    print("\n📐 Step 1/4: Preparing clips (trim B-rolls, adjust audio)...")
    prepared = []

    for i, (filename, scene_type, trim_dur) in enumerate(SCENES):
        src = CLIPS_DIR / filename
        dst = TMP_DIR / f"prep_{i:02d}.mp4"

        if not src.exists():
            print(f"  ❌ Missing: {src}")
            sys.exit(1)

        actual_dur = get_duration(src)

        # Determine trim: anchor=full, broll=short
        if trim_dur is None:
            use_dur = actual_dur  # anchor: full length
        else:
            use_dur = min(trim_dur, actual_dur)  # broll: trimmed short

        # Determine audio volume
        vol = ANCHOR_AUDIO_VOLUME if scene_type == "anchor" else BROLL_AUDIO_VOLUME

        cmd = [
            "ffmpeg", "-y", "-i", str(src),
            "-t", f"{use_dur:.3f}",
            "-vf", f"fps={OUTPUT_FPS},scale=1080:1920:force_original_aspect_ratio=decrease,"
                   f"pad=1080:1920:(ow-iw)/2:(oh-ih)/2,format=yuv420p",
            "-af", f"volume={vol}",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
            "-movflags", "+faststart",
            str(dst)
        ]

        if not run_ffmpeg(cmd, f"prep clip {i}"):
            sys.exit(1)

        tag = "FULL" if trim_dur is None else f"→{use_dur:.1f}s"
        vol_tag = "100%" if scene_type == "anchor" else "50%"
        print(f"  ✅ {filename}: {actual_dur:.1f}s {tag} | audio {vol_tag} ({scene_type})")
        prepared.append((dst, use_dur))

    return prepared


def step_2_stitch_with_transitions(prepared, use_transitions):
    """Concatenate clips with optional crossfade transitions."""
    output = TMP_DIR / "stitched.mp4"
    n = len(prepared)

    if not use_transitions or n < 2:
        print(f"\n🎬 Step 2/4: Stitching {n} clips (hard cuts)...")
        return concat_simple([p for p, _ in prepared], output)

    print(f"\n🎬 Step 2/4: Stitching {n} clips with {TRANSITION_DURATION}s crossfade transitions...")

    # Build FFmpeg inputs
    inputs = []
    for p, _ in prepared:
        inputs.extend(["-i", str(p)])

    # Build xfade filter chain
    durations = [dur for _, dur in prepared]
    video_parts = []
    audio_parts = []

    # First pair
    offset = durations[0] - TRANSITION_DURATION
    video_parts.append(f"[0:v][1:v]xfade=transition=fade:duration={TRANSITION_DURATION}:offset={offset:.3f}[xv1]")
    audio_parts.append(f"[0:a][1:a]acrossfade=d={TRANSITION_DURATION}[xa1]")

    # Chain remaining clips
    for i in range(2, n):
        offset += durations[i - 1] - TRANSITION_DURATION
        v_in = f"xv{i - 1}"
        a_in = f"xa{i - 1}"
        v_out = f"xv{i}"
        a_out = f"xa{i}"
        video_parts.append(f"[{v_in}][{i}:v]xfade=transition=fade:duration={TRANSITION_DURATION}:offset={offset:.3f}[{v_out}]")
        audio_parts.append(f"[{a_in}][{i}:a]acrossfade=d={TRANSITION_DURATION}[{a_out}]")

    final_v = f"xv{n - 1}"
    final_a = f"xa{n - 1}"
    filter_complex = ";".join(video_parts + audio_parts)

    cmd = [
        "ffmpeg", "-y", *inputs,
        "-filter_complex", filter_complex,
        "-map", f"[{final_v}]", "-map", f"[{final_a}]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output)
    ]

    if run_ffmpeg(cmd, "xfade transitions"):
        print(f"  ✅ Stitched with {n - 1} crossfade transitions")
        return output
    else:
        print(f"  ⚠️ Transitions failed — falling back to hard cuts...")
        return concat_simple([p for p, _ in prepared], output)


def concat_simple(paths, output):
    """Reliable fallback: concat demuxer (hard cuts)."""
    concat_file = TMP_DIR / "concat_list.txt"
    with open(concat_file, "w") as f:
        for p in paths:
            f.write(f"file '{p}'\n")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c:v", "libx264", "-preset", "fast", "-crf", "18",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output)
    ]
    if not run_ffmpeg(cmd, "concat"):
        sys.exit(1)
    print(f"  ✅ Stitched with hard cuts")
    return output


def step_3_add_bgm(video_path, bgm_path):
    """Layer background music across the entire video."""
    print("\n🎵 Step 3/4: Layering background music...")
    output = TMP_DIR / "with_bgm.mp4"

    if not bgm_path or not bgm_path.exists():
        print("  ⚠️ No BGM file found — exporting without music")
        shutil.copy(video_path, output)
        return output

    video_dur = get_duration(video_path)
    fade_out_start = max(0, video_dur - BGM_FADE_OUT)

    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-i", str(bgm_path),
        "-filter_complex",
        f"[1:a]aloop=loop=-1:size=2e+09,atrim=0:{video_dur:.2f},"
        f"volume={BGM_VOLUME},"
        f"afade=t=in:d={BGM_FADE_IN},afade=t=out:st={fade_out_start:.2f}:d={BGM_FADE_OUT}[bgm];"
        f"[0:a][bgm]amix=inputs=2:duration=first:dropout_transition=3[out]",
        "-map", "0:v", "-map", "[out]",
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(output)
    ]

    if run_ffmpeg(cmd, "BGM layer"):
        print(f"  ✅ BGM at {int(BGM_VOLUME * 100)}% with {BGM_FADE_IN}s fade-in, {BGM_FADE_OUT}s fade-out")
        return output
    else:
        print(f"  ⚠️ BGM layering failed — exporting without music")
        shutil.copy(video_path, output)
        return output


def step_4_finalize(video_path):
    """Final export to output directory."""
    print("\n📦 Step 4/4: Final export...")
    FINAL_DIR.mkdir(parents=True, exist_ok=True)
    output = FINAL_DIR / OUTPUT_FILE

    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-c:v", "libx264", "-preset", "slow", "-crf", "17",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
        "-movflags", "+faststart",
        str(output)
    ]

    if not run_ffmpeg(cmd, "final export"):
        sys.exit(1)

    dur = get_duration(output)
    size_mb = output.stat().st_size / (1024 * 1024)

    print(f"\n{'═' * 55}")
    print(f"  🎉 REEL EXPORTED SUCCESSFULLY")
    print(f"{'═' * 55}")
    print(f"  📁 {output}")
    print(f"  ⏱️  {dur:.1f}s  |  📐 1080×1920  |  🎞️ {OUTPUT_FPS}fps")
    print(f"  💾 {size_mb:.1f} MB  |  📺 H.264 + AAC")
    print(f"{'═' * 55}")
    return output


def main():
    parser = argparse.ArgumentParser(description="Assemble BuLoop reel from video clips")
    parser.add_argument("--bgm", type=str, default=str(AUDIO_DIR / "bgm_track.mp3"),
                        help="Path to background music file")
    parser.add_argument("--no-transitions", action="store_true",
                        help="Use hard cuts instead of crossfade transitions")
    parser.add_argument("--output", type=str, default=None,
                        help="Custom output filename")
    args = parser.parse_args()

    global OUTPUT_FILE
    if args.output:
        OUTPUT_FILE = args.output

    use_transitions = not args.no_transitions

    print("=" * 55)
    print("  BuLoop AI Video Pipeline — Final Assembly")
    print("=" * 55)

    # Pre-flight
    print("\n🔍 Pre-flight checks...")
    if not check_ffmpeg():
        sys.exit(1)

    missing = [s[0] for s in SCENES if not (CLIPS_DIR / s[0]).exists()]
    if missing:
        print(f"  ❌ Missing clips: {missing}")
        sys.exit(1)
    print(f"  ✅ All {len(SCENES)} clips found")

    bgm_path = Path(args.bgm)
    if bgm_path.exists():
        print(f"  ✅ BGM: {bgm_path.name}")
    else:
        print(f"  ⚠️ No BGM at {args.bgm}")
        bgm_path = None

    anchor_count = sum(1 for s in SCENES if s[1] == "anchor")
    broll_count = sum(1 for s in SCENES if s[1] == "broll")
    print(f"  🎬 {anchor_count} anchor (full length, 100% audio) + {broll_count} B-roll (trimmed, 50% audio)")
    print(f"  ✨ Transitions: {'crossfade' if use_transitions else 'hard cuts'}")

    TMP_DIR.mkdir(parents=True, exist_ok=True)

    try:
        prepared = step_1_prepare_clips()
        stitched = step_2_stitch_with_transitions(prepared, use_transitions)
        with_bgm = step_3_add_bgm(stitched, bgm_path)
        final = step_4_finalize(with_bgm)

        print(f"\n✅ Done! Transfer to mobile for preview before publishing.")
    finally:
        print(f"\n🧹 Cleaning up...")
        if TMP_DIR.exists():
            shutil.rmtree(TMP_DIR)
            print(f"  ✅ Temp files removed")


if __name__ == "__main__":
    main()

# Experience — Phase 5 Upscaling

## Learnings (March 19, 2026)

1. **Phase 5 is fully automatable** — using macOS `sips` command. No external tools needed. The pipeline: `sips -s format png` (convert) → `sips --resampleWidth 1080` (scale) → `sips -c 1920 1080` (crop to exact dimensions). Total time: ~10 seconds for all 12 images.
2. **Nanobanana PRO output (768×1376) is NOT exactly 9:16** — it's 768:1376 = 0.5581 vs 9:16 = 0.5625. The images are slightly taller than true 9:16. The crop step trims ~15px from top/bottom, which is invisible.
3. **No need for Gigapixel 8 or external upscaling tools** — for animated content, `sips` resampling produces clean results. The Pixar-adjacent style doesn't have fine texture detail that would benefit from AI upscaling (unlike photorealistic content).
4. **Output format standardization** — converting all images to PNG during upscaling eliminates the mixed PNG/JPEG issue from Phase 3. All upscaled images are now consistently PNG.

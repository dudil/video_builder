# src/video_builder/speedup.py

from pathlib import Path

import ffmpeg

from video_builder import settings


def speedup_clip(input_path: Path, output_path: Path, speed_factor: float):
    """Apply speedup to a video clip."""
    setpts_value = 1 / speed_factor
    (
        ffmpeg.input(str(input_path))
        .filter_("setpts", f"{setpts_value}*PTS")
        .output(
            str(output_path),
            vcodec="libx264",
            pix_fmt=settings.PIX_FMT,
            r=settings.FPS,
            g=settings.GOP_LENGTH,
            crf=settings.CRF,
        )
        .overwrite_output()
        .run()
    )


def speedup_all(
    input_dir: Path = settings.TRIM_DIR, output_dir: Path = settings.FINAL_DIR
):
    """Apply speedup to selected clips."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, clip_name in enumerate(settings.TRIM_TIMES.keys(), start=1):
        input_path = input_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        output_path = output_dir / settings.CLIP_FILENAME_FORMAT.format(idx)

        if clip_name in settings.SPEEDUP_CLIPS:
            speed_factor = settings.SPEEDUP_CLIPS[clip_name]
            print(f"⚡ Speeding up {clip_name} by {speed_factor}x...")
            speedup_clip(input_path, output_path, speed_factor)
        else:
            print(f"➡️ Keeping {clip_name} at normal speed...")
            output_path.write_bytes(input_path.read_bytes())  # Copy as-is


if __name__ == "__main__":
    speedup_all()

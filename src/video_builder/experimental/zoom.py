from pathlib import Path

import ffmpeg

from video_builder import settings


def zoom_clip(input_path: Path, output_path: Path, zoom_factor: float):
    """Apply a slow zoom-in effect to a clip."""
    width = settings.FINAL_WIDTH
    height = settings.FINAL_HEIGHT

    (
        ffmpeg.input(str(input_path))
        .filter(
            "zoompan",
            z="zoom+0.0005",  # Slow zoom increment
            d="1",  # Duplicate each frame only once (no delay)
            x="iw/2-(iw/zoom/2)",
            y="ih/2-(ih/zoom/2)",
            s=f"{width}x{height}",
        )
        .output(
            str(output_path),
            vcodec="libx264",
            pix_fmt=settings.PIX_FMT,
            r=settings.FPS,
            g=60,
            crf=settings.CRF,
        )
        .overwrite_output()
        .run()
    )


def rescale_clip(input_path: Path, output_path: Path):
    """Rescale the clip without zoom if no zoom factor is defined."""
    (
        ffmpeg.input(str(input_path))
        .filter("scale", settings.FINAL_WIDTH, settings.FINAL_HEIGHT)
        .output(
            str(output_path),
            vcodec="libx264",
            pix_fmt=settings.PIX_FMT,
            r=settings.FPS,
            g=60,
            crf=settings.CRF,
        )
        .overwrite_output()
        .run()
    )


def zoom_all():
    """Apply zoom or just rescale for all clips."""
    zoom_dir = Path(settings.ZOOM_DIR)
    zoom_dir.mkdir(parents=True, exist_ok=True)

    trim_dir = Path(settings.TRIM_DIR)

    for idx, clip_name in enumerate(settings.TRIM_TIMES.keys(), start=1):
        input_path = trim_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        output_path = zoom_dir / settings.CLIP_FILENAME_FORMAT.format(idx)

        zoom_factor = settings.ZOOM_SETTINGS.get(clip_name, None)

        if zoom_factor:
            print(f"🔍 Applying zoom to {clip_name} (factor {zoom_factor})...")
            zoom_clip(input_path, output_path, zoom_factor)
        else:
            print(f"📏 Rescaling {clip_name} without zoom...")
            rescale_clip(input_path, output_path)


if __name__ == "__main__":
    zoom_all()

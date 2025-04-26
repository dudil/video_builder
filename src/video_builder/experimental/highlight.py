from pathlib import Path

import ffmpeg

from video_builder import settings


def apply_pointer(input_path: Path, output_path: Path, pointer_config: dict):
    """Draw a static pulse (pointer) at given (x, y) coordinates."""
    x = pointer_config["x"]
    y = pointer_config["y"]
    radius = pointer_config["radius"]

    (
        ffmpeg.input(str(input_path))
        .filter_(
            "drawbox",
            x=x - radius,
            y=y - radius,
            w=2 * radius,
            h=2 * radius,
            color="red@0.5",
            t=3,
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


def copy_clip(input_path: Path, output_path: Path):
    """Copy a clip without adding pointer if not needed."""
    (
        ffmpeg.input(str(input_path))
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


def apply_all(
    input_dir: Path = Path(settings.ZOOM_DIR),
    output_dir: Path = Path(settings.FINAL_DIR),
) -> None:
    """Apply pointer effect where needed or just copy the clip."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, clip_name in enumerate(settings.TRIM_TIMES.keys(), start=1):
        input_path = input_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        output_path = output_dir / settings.CLIP_FILENAME_FORMAT.format(idx)

        pointer = settings.POINTER_EFFECTS.get(clip_name, None)

        if pointer:
            print(f"📍 Adding pointer highlight to {clip_name}...")
            apply_pointer(input_path, output_path, pointer)
        else:
            print(f"➔ No pointer needed for {clip_name}, copying...")
            copy_clip(input_path, output_path)


if __name__ == "__main__":
    apply_all()

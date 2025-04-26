from pathlib import Path

import ffmpeg

from video_builder import settings


def trim_all(
    input_video: str = settings.INPUT_VIDEO, output_dir: Path = settings.TRIM_DIR
) -> None:
    """Trim the input video into multiple clips based on TRIM_TIMES."""
    # Ensure the output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, (clip_name, (start, end)) in enumerate(
        settings.TRIM_TIMES.items(), start=1
    ):
        output_path = output_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        (
            ffmpeg.input(input_video, ss=start, to=end)
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

        print(f"✅ Trimmed {clip_name} into {output_path}")


if __name__ == "__main__":
    trim_all()

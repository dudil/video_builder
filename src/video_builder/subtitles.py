# src/video_builder/subtitles.py

from pathlib import Path

import ffmpeg

from video_builder import settings


def burn_subtitles(input_path: Path, subtitle_path: Path, output_path: Path):
    """Burn subtitles onto a video clip (no timing adjustment here)."""
    input_stream = ffmpeg.input(str(input_path))

    input_stream = (
        input_stream.filter_("fps", fps=settings.FPS, round="up")
        .filter_("format", settings.PIX_FMT)
        .filter_(
            "subtitles",
            str(subtitle_path),
            force_style=settings.SUBTITLE_FORCE_STYLE,
        )
    )

    (
        input_stream.output(
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


def burn_all(
    input_dir: Path = settings.FINAL_DIR,
    subtitle_dir: Path = settings.SUBTITLE_FOLDER,
    output_dir: Path = settings.SUBTITLED_DIR,
):
    """Burn subtitles onto all clips dynamically from specified folders."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, clip_name in enumerate(settings.TRIM_TIMES.keys(), start=1):
        input_path = input_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        subtitle_path = subtitle_dir / f"clip{idx:02d}.srt"
        output_path = output_dir / settings.CLIP_FILENAME_FORMAT.format(idx)

        if subtitle_path.exists():
            print(f"📝 Burning subtitles into {clip_name}...")
            burn_subtitles(input_path, subtitle_path, output_path)
        else:
            print(f"⚠️ No subtitles found for {clip_name}, copying without burning...")
            output_path.write_bytes(input_path.read_bytes())  # Just copy clip


if __name__ == "__main__":
    burn_all()

from pathlib import Path

import ffmpeg

from video_builder import settings


def concatenate_final(
    input_dir: Path = settings.SUBTITLED_DIR, output_path: Path = settings.FINAL_VIDEO
) -> None:
    input_files = [
        input_dir / settings.CLIP_FILENAME_FORMAT.format(idx)
        for idx in range(1, len(settings.TRIM_TIMES) + 1)
    ]

    inputs = [ffmpeg.input(str(file)) for file in input_files]

    joined = ffmpeg.concat(*inputs, v=1, a=0).node
    v = joined[0]

    (
        ffmpeg.output(
            v,
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

    print(f"🎬 Final video created: {output_path}")


if __name__ == "__main__":
    concatenate_final()

from video_builder import assemble, settings, speedup, subtitles, trim


def main_cli():
    print("\n🚀 Starting GDPR Copilot Video Builder...\n")

    trim.trim_all(input_video=settings.INPUT_VIDEO, output_dir=settings.TRIM_DIR)
    print("\n✅ Trimming done.\n")

    speedup.speedup_all(input_dir=settings.TRIM_DIR, output_dir=settings.FINAL_DIR)
    print("\n✅ Speedup applied.\n")

    subtitles.burn_all(
        input_dir=settings.FINAL_DIR,
        subtitle_dir=settings.SUBTITLE_FOLDER,
        output_dir=settings.SUBTITLED_DIR,
    )
    print("\n✅ Subtitles burned.\n")

    assemble.concatenate_final(
        input_dir=settings.SUBTITLED_DIR, output_path=settings.FINAL_VIDEO
    )
    print(f"\n🎬 Your final video is ready at: {settings.FINAL_VIDEO}\n")


if __name__ == "__main__":
    main_cli()

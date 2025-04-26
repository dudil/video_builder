from pathlib import Path

# === Project-Wide Configuration ===

# Input
WORK_DIR = Path("./videos")
INPUT_VIDEO = WORK_DIR / "1-workspace-example.mp4"

# Output Folders
TRIM_DIR = WORK_DIR / "trimmed_clips"
ZOOM_DIR = WORK_DIR / "zoomed_clips"
FINAL_DIR = WORK_DIR / "final_clips"
SUBTITLED_DIR = WORK_DIR / "subtitled_clips"

# Final Output
FINAL_VIDEO = WORK_DIR / "final_gdpr_walkthrough.mp4"

# Subtitle Settings
SUBTITLE_FOLDER = WORK_DIR / "subtitles"
SUBTITLE_FORCE_STYLE = (
    "FontName=Noto Sans,"
    "FontSize=16,"
    "Alignment=2,"
    "MarginV=70,"
    "BorderStyle=4,"
    "Outline=1,"
    "OutlineColour=&H40000000",
    "BackColour=&H80000000",
)

# Resolution and Encoding
FINAL_WIDTH = 1280
FINAL_HEIGHT = 720
FPS = 30
GOP_LENGTH = 15  # Keyframe every 0.5s (for smooth fast-forward, clean playback)
PIX_FMT = "yuv420p"
CRF = 23

# Clip Timings (start, end) for Trimming
TRIM_TIMES = {
    "clip01": ("00:00:04", "00:00:15"),
    "clip02": ("00:00:20", "00:00:30"),
    "clip03": ("00:00:43", "00:01:00"),
    "clip04": ("00:01:05", "00:01:21"),
    "clip05": ("00:01:41", "00:01:52"),
    "clip06": ("00:02:20", "00:02:37"),
    "clip07": ("00:03:27", "00:04:00"),
    "clip08": ("00:04:16", "00:04:36"),
    "clip09": ("00:05:05", "00:05:10"),
    "clip10": ("00:05:25", "00:05:40"),
}

# Zoom Settings (clip -> zoom factor)
ZOOM_SETTINGS = {
    "clip02": 1.2,  # Brainstorm console
    "clip07": 1.5,  # Code diffs
    "clip10": 1.2,  # Build/test screen
}

# Pointer/Highlight Settings
POINTER_EFFECTS = {
    "clip02": {"x": 600, "y": 300, "radius": 30},
    "clip07": {"x": 450, "y": 250, "radius": 40},
}

# File Naming Format
CLIP_FILENAME_FORMAT = "clip{:02d}.mp4"

# Clips that need speeding up
# Format: clip_name -> speed_factor
SPEEDUP_CLIPS = {
    "clip02": 1.2,
    "clip03": 1.2,
    "clip06": 1.2,
    "clip07": 1.5,
    "clip10": 1.2,
}

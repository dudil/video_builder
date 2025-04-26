# GDPR Copilot Workspace Video Builder 🎬

![Python Version](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![pdmPy](https://img.shields.io/badge/package%20manager-pdm-blue)
![MypyPy](https://img.shields.io/badge/mypy-checked-blue)
![BlackPy](https://img.shields.io/badge/code%20style-black-black)

An automated, professional-quality video processing pipeline built in Python.  
Designed to create clean, engaging, high-quality walkthrough videos, especially for showcasing GitHub Copilot Workspace interactions.

---

## ✨ Features

- 📂 **Modular pipeline**: Trim ➔ Speedup ➔ Subtitles ➔ Assemble
- 🛠 **ffmpeg-python** powered fast video editing
- 🏃 **Speedup slow clips** selectively for better engagement
- 💬 **Subtitles** with clean semi-transparent background box
- 🎥 **Final polished video** export at 30fps with smooth keyframes
- 📁 **Centralized settings**: easy FPS, GOP, subtitle styling control
- 🚀 **Simple CLI command**: just type `vbuild` to run the full pipeline

---

## 🚀 Quick Start

### Requirements

- Python 3.12+
- PDM package manager (`pip install pdm`)
- FFmpeg installed (`brew install ffmpeg` on Mac)

### Install dependencies

```bash
pdm install
```

### Run the pipeline

```bash
pdm run vbuild
```

✅ Output will appear in `/videos/` folder.

---

## 🧠 Project Structure

```bash
/video_builder/
├── src/
│   └── video_builder/
│       ├── assemble.py
│       ├── speedup.py
│       ├── subtitles.py
│       ├── settings.py
│       ├── trim.py
│       ├── __main__.py
│       └── experimental/     # Old prototype modules (zoom, highlight)
├── videos/                   # Input/output media
├── README.md
├── ROADMAP.md
├── pdm.lock
└── pyproject.toml
```

---

## ⚡ Roadmap Highlights

- 🔥 CLI upgrade (using Typer)
- ✍️ Config in YAML/TOML
- 🎵 Background music support
- 🎬 Smooth clip transitions
- ✨ Word-by-word subtitle animations
- 🧠 Smart zoom / focus detection
- 🌎 Multi-language subtitle support

See full details in [`ROADMAP.md`](./ROADMAP.md)!

---

## 🏆 Status

| Version | Status       | Notes                              |
| :------ | :----------- | :--------------------------------- |
| v1.0    | ✅ Completed | Core modular pipeline ready        |
| v1.5    | 🔜 Planned   | Quality-of-life developer upgrades |
| v2.0    | 🔮 Future    | Full studio-grade features         |

---

## 👨‍💻 Author

Built with ❤️ by [dudil](https://github.com/dudil) and ChatGPT 🤝

---

## 📜 License

MIT License.  
Feel free to use, modify, contribute, and make it even better!

# 🎧 ESA1 Audio Recorder

A CLI-based audio recorder for capturing live MP3 streams from the internet.

![CI Status](https://github.com/junesdream/esa1-audio-recorder/actions/workflows/main.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ✨ Features

| Feature | Description |
|---|---|
| 📡 **Stream Recording** | Record live MP3 streams via URL |
| ⏱️ **Configurable Duration** | Set custom recording length in seconds |
| 💾 **Custom Filename** | Define your own output file name |
| 🔧 **Adjustable Block Size** | Control chunk size for stream capture |
| 📂 **List Recordings** | View all saved recordings at a glance |

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 📦 argparse
- 🌐 requests

---

## 📦 Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

---

## 🚀 Usage

```bash
python cli_audiorecorder.py <url> [--filename <name>] [--duration <seconds>] [--blocksize <size>] [--list]
```

### Parameters

| Parameter | Description | Default |
|---|---|---|
| `url` | Stream URL | required |
| `--filename` | Output file name | `myRadio.mp3` |
| `--duration` | Recording duration (seconds) | `30` |
| `--blocksize` | Chunk size in bytes | `64` |
| `--list` | Show all saved MP3 files | `False` |

---

## 💡 Examples

### Record a stream for 10 seconds
```bash
python cli_audiorecorder.py https://icecast.vrtcdn.be/mnm-high.mp3 --duration 10
```

### Record with a custom filename
```bash
python cli_audiorecorder.py https://stream.laut.fm/eins --filename test.mp3 --duration 5
```

### List all saved recordings
```bash
python cli_audiorecorder.py dummy --list
```

---

## 📝 Notes

- Works with public MP3 streams (Icecast, etc.)
- Output files are stored in the project directory

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes (`git commit -m 'feat: add your idea'`)
4. Push to the branch (`git push origin feature/your-idea`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

## 👤 Author

JuNe aka RainbowDev — System Architect • Full-Stack Development • Electronic Music

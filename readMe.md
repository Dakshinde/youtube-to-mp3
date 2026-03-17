
# VaultSync: Automated Audio Ingestion & Analysis Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Ubuntu Supported](https://img.shields.io/badge/Platform-Ubuntu-orange.svg)](https://ubuntu.com/)

**VaultSync** is a modular, high-efficiency pipeline designed for personal media archival and metadata enrichment. It replaces ad-heavy, insecure web converters with a clean, local-first engineering solution.

---

## ⚖️ Legal Disclaimer & Terms

This project is strictly for **educational and personal use**. 

* **Personal Use:** This tool is designed to facilitate "Fair Dealing" under **Section 52(1)(a) of the Indian Copyright Act, 1957**, which permits the use of copyrighted works for private or personal use.
* **No Redistribution:** Users are strictly prohibited from using this tool to redistribute, sell, or commercially exploit copyrighted content.
* **TOS Compliance:** Users are responsible for complying with the Terms of Service of any third-party content providers.
* **No Warranty:** This software is provided "as is" without warranty of any kind. The author assumes no liability for misuse.

---

## 🚀 Key Features

* **High-Efficiency Ingestion:** Uses `yt-dlp` to extract high-quality 192kbps audio directly from source streams.
* **Smart Archiving:** Implements a `download_archive` system to prevent duplicate downloads, saving bandwidth and electricity.
* **AI-Driven Categorization:** Integrated `librosa` module for BPM analysis to auto-sort music into "Workout" vs. "Study" profiles.
* **Metadata Enrichment:** Automated embedding of thumbnails and ID3 tags for a clean library experience.
* **Ubuntu Optimized:** Specifically tuned for Linux environments with FFmpeg integration.

---

## 🛠️ Architecture

```mermaid
graph LR
    A[Source URL] --> B[yt-dlp Engine]
    B --> C{FFmpeg Processor}
    C --> D[Raw MP3 Store]
    D --> E[AI Analysis Module]
    E --> F[Categorized Library]
    F --> G[React/Streamlit UI]
````

---

## 📦 Installation (Ubuntu)

### 1. System Dependencies

```bash
sudo apt update && sudo apt install ffmpeg nodejs -y
```

### 2. Project Setup

```bash
git clone https://github.com/yourusername/VaultSync.git
cd VaultSync
python3 -m venv venv
source venv/bin/activate
pip install yt-dlp streamlit rich librosa numpy
```

### 3. Running the Pipeline

```bash
python3 sync.py
```

---

## 🗺️ Roadmap

* [x] High-quality MP3 Extraction engine
* [x] Metadata & Thumbnail embedding
* [ ] React + FastAPI dashboard for library browsing
* [ ] Librosa integration for automated BPM categorization
* [ ] Dockerization for self-hosted home servers

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information. This license allows for free use and modification while protecting the author from liability.

**Developed by Daksh Shinde**
*IT Engineering Undergraduate*


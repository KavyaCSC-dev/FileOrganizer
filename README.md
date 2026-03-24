# 🗂️ FileOrganizer

![Python](https://img.shields.io/badge/Python-100%25-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![LLM](https://img.shields.io/badge/LLM-Groq-orange)

> A fast and lightweight Python CLI tool that automatically organizes your messy folders by sorting files into categorized subfolders based on their extension — with **AI-powered handling for unknown file types**.

---

## 📋 Table of Contents

- [Features](#-features)
- [What's New](#-whats-new)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Supported File Types](#-supported-file-types)
- [AI Support](#-ai-support-for-unknown-extensions)
- [Logging](#-logging)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Author](#-author)

---

## ✨ Features

- 📁 **Auto Categorization** — Sorts files into folders by type (images, code, documents, etc.)
- 🔁 **Duplicate File Handling** — Renames duplicates safely without overwriting anything
- 📂 **Auto Folder Creation** — Creates category folders automatically if they don't exist
- 🤖 **AI-Powered Unknown Extensions** — Uses Groq LLM to decide the best folder for unrecognized file types and remembers them for next time
- 📝 **Logging** — Every file move is recorded in `log.txt` for full transparency
- ⚡ **Fast & Lightweight** — Pure Python, minimal dependencies

---

## 🆕 What's New

### v1.1 — AI Support for Unknown Extensions *(Latest)*
- Unknown file extensions are now handled by **Groq LLM** — it decides the best folder name
- New extension-to-folder mappings are **saved back to `data.json`** automatically so the AI is only called once per extension
- Improved logging captures AI-assisted decisions separately

### v1.0 — Initial Release
- Core file organization by extension
- Auto folder creation
- Duplicate file safety with rename logic
- Basic logging

---

## 🚀 Installation

### Prerequisites
- Python 3.8+
- A [Groq API key](https://console.groq.com) (free)

### Clone the Repository

```bash
git clone https://github.com/UnKnown-4656/FileOrganizer.git
cd FileOrganizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Your API Key

On Windows (PowerShell):
```powershell
$env:GROQ_API_KEY="your_key_here"
```

On Mac/Linux:
```bash
export GROQ_API_KEY="your_key_here"
```

---

## 🛠️ Usage

```bash
python main.py <folder_path>
```

**Example:**
```bash
python main.py C:\Users\user\Desktop\MessyFolder
```

The tool will scan the folder, sort all files, and log every action.

---

## ⚙️ How It Works

```
📁 Messy Folder
├── photo.jpg        →   📁 images/
├── report.pdf       →   📁 documents/
├── script.py        →   📁 code/
├── song.mp3         →   📁 music/
└── unknown.xyz      →   🤖 Groq decides → 📁 misc/
```

1. Scans all files in the target folder (top level)
2. Looks up each file extension in `data.json`
3. If extension is unknown → asks Groq LLM for the best folder name → saves it to `data.json`
4. Creates destination folder if it doesn't exist
5. Moves the file safely, renaming if a duplicate exists
6. Logs every action to `log.txt`

---

## 📂 Supported File Types

Built-in mappings are stored in `data.json`. Default categories include:

| Category   | Extensions                                                  |
|------------|-------------------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`   |
| Videos     | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`             |
| Music      | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`                    |
| Documents  | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`          |
| Archives   | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`                       |
| Code       | `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.cs`      |
| Unknown    | Anything else → **handled by Groq AI** 🤖                  |

---

## 🤖 AI Support for Unknown Extensions

When FileOrganizer encounters a file with an unrecognized extension, it sends the extension to **Groq's LLM** which returns an appropriate folder name.

That mapping is then **saved permanently to `data.json`** — so the next time the same extension appears, no API call is needed.

```
Unknown extension: .blend
Groq response: { "extension": ".blend", "folder_name": "design_files" }
Saved to data.json ✓
```

> Requires a valid `GROQ_API_KEY` environment variable.

---

## 📝 Logging

All operations are recorded in `log.txt`:

```
photo.jpg Moved to C:\Desktop\MessyFolder\images
report(1).pdf Already Exists: moved as report(1).pdf
unknown file extension: .xyz added to dict
```

---

## 📁 Project Structure

```
FileOrganizer/
├── main.py           # Core logic — scanning, organizing, moving files
├── utilities.py      # Helper functions — AI lookup, duplicate renaming
├── data.json         # Extension-to-folder mappings (auto-updated)
├── log.txt           # Auto-generated operation log
├── requirements.txt  # Dependencies
└── README.md         # You are here
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push and open a Pull Request

---

## 👨‍💻 Author

**UnKnown** — [@UnKnown-4656](https://github.com/UnKnown-4656)

> Built with ❤️ — because no one should manually sort their Downloads folder.

---

*⭐ If this helped you, drop a star on GitHub!*
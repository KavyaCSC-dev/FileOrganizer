# 🗂️ FileOrganizer

![Python](https://img.shields.io/badge/Python-100%25-blue?logo=python&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-Groq%20AI-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
<<<<<<< HEAD
![LLM](https://img.shields.io/badge/LLM-Groq-orange)

> A fast and lightweight Python CLI tool that automatically organizes your messy folders by sorting files into categorized subfolders based on their extension — with **AI-powered handling for unknown file types**.
=======
![License](https://img.shields.io/badge/License-MIT-green)

> A fast and efficient Python CLI tool that automatically organizes files in any folder into categorized subfolders based on file extension — powered by **Groq AI** for unknown file types.
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

---

## 📋 Table of Contents

- [Features](#-features)
<<<<<<< HEAD
- [What's New](#-whats-new)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Supported File Types](#-supported-file-types)
- [AI Support](#-ai-support-for-unknown-extensions)
=======
- [How It Works](#-how-it-works)
- [Supported Categories](#-supported-categories)
- [LLM Support](#-llm-support-for-unknown-extensions)
- [Installation](#-installation)
- [Usage](#-usage)
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e
- [Logging](#-logging)
- [Project Structure](#-project-structure)
- [Known Issues & Notes](#-known-issues--notes)
- [Author](#-author)

---

## ✨ Features

<<<<<<< HEAD
- 📁 **Auto Categorization** — Sorts files into folders by type (images, code, documents, etc.)
- 🔁 **Duplicate File Handling** — Renames duplicates safely without overwriting anything
- 📂 **Auto Folder Creation** — Creates category folders automatically if they don't exist
- 🤖 **AI-Powered Unknown Extensions** — Uses Groq LLM to decide the best folder for unrecognized file types and remembers them for next time
- 📝 **Logging** — Every file move is recorded in `log.txt` for full transparency
- ⚡ **Fast & Lightweight** — Pure Python, minimal dependencies
=======
- 📁 **Auto Categorization** — Sorts files into folders by extension using a large built-in extension map
- 🤖 **Groq AI Fallback** — Unknown file extensions are sent to Groq AI which returns the best folder name
- 🔁 **Duplicate File Safety** — Files with the same name get renamed as `file(1).ext`, `file(2).ext` etc. instead of being overwritten
- 📂 **Auto Folder Creation** — Creates destination folders automatically if they don't exist
- 📝 **Logging** — Every file move, duplicate, and unknown extension is logged to `log.txt`
- ⚡ **Fast Lookup** — Uses a dictionary (`ext_map`) for O(1) extension lookup instead of slow loops
- 🖥️ **CLI Based** — Run directly from terminal with a folder path as argument
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

---

## ⚙️ How It Works

<<<<<<< HEAD
### v1.1 — AI Support for Unknown Extensions *(Latest)*
- Unknown file extensions are now handled by **Groq LLM** — it decides the best folder name
- New extension-to-folder mappings are **saved back to `data.json`** automatically so the AI is only called once per extension
- Improved logging captures AI-assisted decisions separately

### v1.0 — Initial Release
- Core file organization by extension
- Auto folder creation
- Duplicate file safety with rename logic
- Basic logging
=======
```
📁 Messy Folder (input via CLI)
│
├── photo.jpg       →  📁 images/
├── report.pdf      →  📁 documents/
├── song.mp3        →  📁 audio/
├── movie.mp4       →  📁 video/
├── script.py       →  📁 code/
├── data.json       →  📁 data/
├── model.gguf      →  📁 ml_models/
├── report.pdf      →  📁 documents/report(1).pdf  ← duplicate handled
└── weird.xyz       →  🤖 Groq AI decides → 📁 <ai_suggested_folder>/
```

**Internal flow:**
1. Reads folder path from CLI argument (`sys.argv[1]`)
2. Lists all files using `os.listdir()`
3. Skips subfolders — only processes files
4. Extracts extension using `os.path.splitext()`
5. Looks up extension in `ext_map` dictionary
6. If not found → calls `unknown_file(ext)` which queries Groq AI
7. Groq AI returns a JSON with `{"extension": "...", "folder_name": "..."}`
8. Adds new extension to `ext_map` for future use in same run
9. Creates destination folder if it doesn't exist
10. Checks for duplicates → renames if needed
11. Moves file using `shutil.move()`
12. Logs every action to `log.txt`

---

## 📂 Supported Categories

| Category | Example Extensions |
|---|---|
| `documents` | `.pdf` `.docx` `.txt` `.md` `.epub` `.pages` |
| `spreadsheets` | `.xlsx` `.xls` `.csv` `.ods` `.numbers` |
| `presentations` | `.pptx` `.ppt` `.odp` `.key` |
| `images` | `.jpg` `.png` `.gif` `.svg` `.psd` `.raw` `.heic` |
| `audio` | `.mp3` `.wav` `.flac` `.aac` `.ogg` `.m4a` |
| `video` | `.mp4` `.mkv` `.avi` `.mov` `.webm` `.3gp` |
| `archives` | `.zip` `.rar` `.7z` `.tar` `.gz` `.iso` `.apk` |
| `code` | `.py` `.js` `.ts` `.html` `.css` `.java` `.cpp` `.go` `.rs` |
| `scripts` | `.sh` `.bat` `.ps1` `.cmd` `.bash` |
| `data` | `.json` `.xml` `.yaml` `.toml` `.env` `.parquet` |
| `database` | `.sql` `.db` `.sqlite` `.sqlite3` |
| `fonts` | `.ttf` `.otf` `.woff` `.woff2` |
| `3d` | `.obj` `.fbx` `.stl` `.blend` `.glb` `.dwg` |
| `executables` | `.exe` `.msi` `.dll` `.bin` `.pyc` |
| `subtitles` | `.srt` `.vtt` `.ass` `.sub` |
| `gis` | `.shp` `.geojson` `.gpx` `.kml` |
| `certificates` | `.pem` `.crt` `.p12` `.pfx` `.gpg` |
| `ml_models` | `.pt` `.onnx` `.gguf` `.safetensors` `.keras` |
| `shortcuts` | `.lnk` `.url` `.webloc` |
| `logs` | `.log` `.trace` `.evtx` |
| `unknown` | anything else → **Groq AI decides** 🤖 |

---

## 🤖 LLM Support for Unknown Extensions

When a file extension is **not found** in the built-in `ext_map`, the tool calls **Groq AI**:

```python
def unknown_file(ext):
    groq = Groq(api_key=api)
    response = groq.chat.completions.create(
        model="openai/gpt-oss-20b",
        ...
        response_format={"type": "json_schema", ...}
    )
    return {result["extension"]: result["folder_name"]}
```

- Groq returns a structured JSON response: `{"extension": ".xyz", "folder_name": "misc"}`
- The new extension is **added to `ext_map`** so it's reused within the same run
- The decision is logged in `log.txt`

> ⚠️ Requires a valid `GROQ_API_KEY` in your `.env` file
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

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
pip install groq
```

<<<<<<< HEAD
### Set Your API Key

On Windows (PowerShell):
```powershell
$env:GROQ_API_KEY="your_key_here"
```

On Mac/Linux:
```bash
export GROQ_API_KEY="your_key_here"
```
=======
### Setup API Key

Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Get your free API key at [console.groq.com](https://console.groq.com)
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

---

## 🖥️ Usage

```bash
<<<<<<< HEAD
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
=======
python main.py "C:\Users\user\Desktop\MessyFolder"
```

**On Linux/Mac:**
```bash
python main.py /home/user/Downloads
```

**What happens:**
- All files in the given folder get sorted into subfolders
- A `log.txt` file is created/updated with every action
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

---

## 📝 Logging

<<<<<<< HEAD
All operations are recorded in `log.txt`:

```
photo.jpg Moved to C:\Desktop\MessyFolder\images
report(1).pdf Already Exists: moved as report(1).pdf
unknown file extension: .xyz added to dict
=======
All operations are appended to `log.txt` in your project directory:

```
photo.jpg Moved to C:\Desktop\MessyFolder\images
report.pdf Moved to C:\Desktop\MessyFolder\documents
Already Exists: report.pdf moved as report(1).pdf
unknown file extension: weird.xyz added to dict
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e
```

---

## 📁 Project Structure

```
FileOrganizer/
<<<<<<< HEAD
├── main.py           # Core logic — scanning, organizing, moving files
├── utilities.py      # Helper functions — AI lookup, duplicate renaming
├── data.json         # Extension-to-folder mappings (auto-updated)
├── log.txt           # Auto-generated operation log
├── requirements.txt  # Dependencies
=======
├── main.py           # Core logic — scanning, categorizing, moving files
├── pyproject.toml    # Project config and dependencies
├── uv.lock           # Locked dependency versions
├── log.txt           # Auto-generated operation log (git ignored)
├── .env              # Your Groq API key (git ignored ⚠️ never commit this)
├── .gitignore        # Ignores .env and log.txt
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e
└── README.md         # You are here
```

---

## ⚠️ Known Issues & Notes

<<<<<<< HEAD
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push and open a Pull Request
=======
- `log.txt` is created in the **project directory**, not the organized folder
- The `.env` file **must never be committed** to GitHub — always keep it in `.gitignore`
- Groq AI is called **once per unknown extension** per run — if the same unknown extension appears multiple times, it reuses the cached result
- Currently only supports **flat folders** — files inside subfolders are not organized recursively
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

---

## 👨‍💻 Author

**UnKnown** — [@UnKnown-4656](https://github.com/UnKnown-4656)

<<<<<<< HEAD
> Built with ❤️ — because no one should manually sort their Downloads folder.

---

*⭐ If this helped you, drop a star on GitHub!*
=======
> Built from scratch with Python — learning by doing 🚀

---

## 🔍 Keywords

`file-organizer` `python` `automation` `file-management` `groq-ai` `llm` `cli-tool` `python-tool` `file-sorting` `productivity`

---

*⭐ If this tool helped you, consider giving it a star!*
>>>>>>> 555f4e2a3143871d691221d0acb328d71ed5e53e

# 📁 FileOrganizer

A smart Python-based file organizer that automatically sorts files into folders based on their extensions. Includes AI-powered handling for unknown file types and an undo system to revert changes.

---

## 🚀 Features

* 📂 Organizes files by extension (e.g., `.jpg → Images/`)
* 🤖 AI-powered detection for unknown file types (via Groq API)
* 📝 Logs all file movements (`log.txt`)
* 🔄 Undo last operation using log history
* ⚠️ Handles duplicate file names safely
* 📦 JSON-based extension mapping (`data.json`)

---

## 🛠️ Tech Stack

* Python
* OS & Shutil (file handling)
* JSON (data storage)
* Groq API (AI classification)

---

## 📦 Project Structure

```
FileOrganizer/
│
├── main.py            # Main execution script
├── utilities.py       # Helper functions
├── data.json          # Extension → Folder mapping
├── log.txt            # Operation logs
├── requirements.txt   # Dependencies
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/FileOrganizer.git
cd FileOrganizer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your API key (for AI feature):

```bash
set GROQ_API_KEY=your_api_key   # Windows
export GROQ_API_KEY=your_api_key  # Linux/Mac
```

---

## ▶️ Usage

### Organize Files

```bash
python main.py "C:\Your\Folder\Path"
```

### Undo Last Operation

```bash
python main.py "C:\Your\Folder\Path" --undo
```

---

## 🧠 How It Works

1. Reads all files in the given directory
2. Checks extension from `data.json`
3. If unknown:

   * Calls AI model to suggest folder name
   * Updates `data.json` automatically
4. Moves file to corresponding folder
5. Logs every move for undo functionality

---

## 🔁 Undo System

* Uses `log.txt` to track operations
* `--undo` restores files to original location
* Automatically removes empty folders

---

## ⚠️ Notes

* Ensure `data.json` exists and is valid JSON
* AI feature requires internet + API key
* Works best on non-system directories

---

## 💡 Future Improvements

* GUI version (Tkinter / Web UI)
* Batch undo support
* File preview before organizing
* Configurable rules
* Performance optimization for large folders

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📜 License

MIT License (recommended)

---

## 🔥 Author

Unknown-4656

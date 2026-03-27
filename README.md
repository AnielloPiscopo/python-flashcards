# 🃏 Flashcards

A terminal-based flashcard application built in Python as part of the [JetBrains Academy / Hyperskill](https://hyperskill.org) Python track.

---

## 📖 Overview

Flashcards is a command-line tool that helps you memorize terms and definitions through interactive study sessions. Cards are stored in memory during a session and can be saved to and loaded from files (JSON or CSV) for future use.

---

## ✨ Features

### Core (from Hyperskill project)
- **Add** flashcards with unique terms and definitions
- **Remove** cards by term
- **Import / Export** cards from/to file (with error count preserved)
- **Ask** mode: study a set of random cards and get instant feedback
- **Log**: save the full session history to a file
- **Hardest card**: see which card(s) you make the most mistakes on
- **Reset stats**: clear all mistake counters
- **Command-line arguments**: auto-import and auto-export on startup/exit via `--import_from` and `--export_to`

### Extra features
- **CSV support** in addition to JSON for import/export
- **Reverse mode**: study by seeing the definition and guessing the term
- **Session statistics**: summary of correct and wrong answers at the end of each `ask` session
- **Study all cards**: option to go through all cards without specifying a number
- **Exit confirmation**: warns if there are unsaved cards before quitting
- **Docstrings** on all public methods and classes
- **Unit tests** for core logic

---

## 🚀 Getting Started

### Requirements
- Python 3.10+

### Installation

```bash
git clone https://github.com/your-username/flashcards.git
cd flashcards
```

No external dependencies required — only Python standard library modules are used.

### Run

```bash
python flashcards.py
```

### Run with arguments

```bash
# Load cards on startup
python flashcards.py --import_from=mydecks.json

# Save cards automatically on exit
python flashcards.py --export_to=mydecks.json

# Both at once
python flashcards.py --import_from=mydecks.json --export_to=mydecks.json
```

---

## 🎮 Usage

Once running, the program will prompt you for an action:

```
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
```

| Action | Description |
|---|---|
| `add` | Add a new flashcard |
| `remove` | Remove a card by term |
| `import` | Load cards from a file (JSON or CSV) |
| `export` | Save all cards to a file (JSON or CSV) |
| `ask` | Start a study session |
| `log` | Save the session log to a file |
| `hardest card` | Show the card(s) with the most mistakes |
| `reset stats` | Reset all mistake counters |
| `exit` | Exit the program |

---

## 📁 File Format

### JSON
```json
[
  {"term": "France", "definition": "Paris", "mistakes": 3},
  {"term": "Japan", "definition": "Tokyo", "mistakes": 0}
]
```

### CSV
```
term,definition,mistakes
France,Paris,3
Japan,Tokyo,0
```

---

## 🧪 Tests

```bash
python -m pytest
```

---

## 📚 Project Background

This project was built as part of the [Flashcards (Python)](https://hyperskill.org/projects/159) track on JetBrains Academy / Hyperskill, completing all 7 stages plus additional custom features.

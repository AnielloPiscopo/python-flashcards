from pathlib import Path

__all__ = ["INPUT_DIR", "OUTPUT_DIR", "FLASHCARDS_OUTPUT_DIR", "LOG_OUTPUT_DIR"]

_PROJECT_ROOT = Path(__file__).parents[2]

INPUT_DIR = _PROJECT_ROOT / "resources" / "data" / "input"
OUTPUT_DIR = _PROJECT_ROOT / "resources" / "data" / "output"

FLASHCARDS_OUTPUT_DIR = OUTPUT_DIR / "flashcards"
LOG_OUTPUT_DIR = OUTPUT_DIR / "log"

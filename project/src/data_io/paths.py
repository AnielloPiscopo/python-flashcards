from pathlib import Path

__all__ = ["INPUT_DIR", "OUTPUT_DIR"]

_PROJECT_ROOT = Path(__file__).parents[2]

INPUT_DIR = _PROJECT_ROOT / "resources" / "data" / "input"
OUTPUT_DIR = _PROJECT_ROOT / "resources" / "data" / "output"

from pathlib import Path

__all__ = ['check_presence']

def check_presence(path: str) -> bool:
    return Path(path).exists()
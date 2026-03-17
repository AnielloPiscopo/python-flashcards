from dataclasses import dataclass

__all__ = ['Flashcard']

@dataclass(frozen=True)
class Flashcard:
    term:str
    definition:str
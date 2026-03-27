import sys
import os

# Add src/ to path so all test imports resolve identically to the application
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from models.flashcard import Flashcard, FlashcardSet


@pytest.fixture
def card():
    return Flashcard("cat", "a small animal", mistakes=0)


@pytest.fixture
def card_with_mistakes():
    return Flashcard("dog", "a big animal", mistakes=3)


@pytest.fixture
def flashcard_set():
    fs = FlashcardSet()
    fs.add(Flashcard("cat", "a small animal"))
    fs.add(Flashcard("dog", "a big animal"))
    return fs
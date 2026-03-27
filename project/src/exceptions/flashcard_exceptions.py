__all__ = ['FlashcardDuplicateError', 'FlashcardNotFoundError', 'FlashcardWithNoMistakesError']

class FlashcardDuplicateError(Exception):
    """Raised when adding a flashcard whose term or definition already exists."""

    is_term: bool
    value: str

    def __init__(self, is_term: bool, value: str):
        self.is_term = is_term
        self.value = value
        message = self._build_message(is_term, value)
        super().__init__(message)

    @staticmethod
    def _build_message(is_term: bool, value: str) -> str:
        return f"The {"card" if is_term else "definition"} \"{value}\" already exists. Try again:"

class FlashcardNotFoundError(Exception):
    """Raised when trying to remove a flashcard that does not exist."""

    value: str

    def __init__(self, value: str):
        self.value = value
        message = self._build_message(value)
        super().__init__(message)

    @staticmethod
    def _build_message(value: str) -> str:
        return f"Can't remove \"{value}\": there is no such card."

class FlashcardWithNoMistakesError(Exception):
    """Raised when requesting the hardest card but no mistakes have been recorded."""

    def __init__(self):
        message = self._build_message()
        super().__init__(message)

    @staticmethod
    def _build_message() -> str:
        return "There are no cards with errors."
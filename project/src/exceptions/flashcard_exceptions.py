__all__ = ['FlashcardDuplicateError']

class FlashcardDuplicateError(Exception):
    is_term: bool
    value: str

    def __init__(self, is_term: bool, value: str):
        self.is_term = is_term
        self.value = value
        message = self._build_message(is_term, value)
        super().__init__(message)

    @staticmethod
    def _build_message(is_term: bool, value: str) -> str:
        return f"The {"term" if is_term else "definition"} \"{value}\" already exists. Try again:"
__all__ = ['Flashcard']

class Flashcard:
    term:str
    definition:str

    def __init__(self,term:str,definition:str):
        self.term:str = term
        self.definition:str = definition
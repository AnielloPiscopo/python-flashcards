from ui.console import show_answer_feedback_in_console, console

__all__ = ["show_answer_feedback", "console"]

def show_answer_feedback(is_correct: bool, correct_definition: str) -> None:
    return show_answer_feedback_in_console(is_correct, correct_definition)
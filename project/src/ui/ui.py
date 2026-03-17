from ui.console_ui import show_answer_feedback_in_console

__all__ = ["show_answer_feedback"]

def show_answer_feedback(is_correct: bool, correct_definition: str) -> None:
    return show_answer_feedback_in_console(is_correct, correct_definition)
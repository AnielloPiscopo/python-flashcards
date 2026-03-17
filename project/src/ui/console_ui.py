__all__=['show_answer_feedback_in_console']

def show_answer_feedback_in_console(is_correct: bool, correct_definition: str) -> None:
    print("Correct!" if is_correct else f"Wrong. The right answer is \"{correct_definition}\".")

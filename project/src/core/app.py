from core.engine import play

__all__ = ['start']

def start()->None:
    try:
        play()
    except ValueError as e:
        print(e)
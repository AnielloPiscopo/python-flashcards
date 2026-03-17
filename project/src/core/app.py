from core.engine import play
from exceptions import OutOfRangeError

__all__ = ['start']

def start()->None:
    try:
        play()
    except (ValueError,OutOfRangeError) as e:
        print(e)
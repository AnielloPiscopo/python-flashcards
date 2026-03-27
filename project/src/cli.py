import argparse
import sys
from argparse import ArgumentParser, Namespace
from enum import Enum

from models import FilePathParams

__all__ = ['parse_flashcards_params']

class CliArgument(Enum):
    """Supported CLI arguments for the flashcard application."""

    IMPORT = "--import_from"
    EXPORT = "--export_to"

    @classmethod
    def values_tuple(cls) -> tuple[str, ...]:
        """Return all argument names as a tuple of strings."""
        return tuple(item.value for item in cls)

def _get_args(parser: ArgumentParser) -> Namespace:
    """Parse CLI arguments, printing an error and exiting on invalid input."""
    try:
        args: Namespace = parser.parse_args()
    except SystemExit:
        print("Incorrect parameters")
        sys.exit()
    else:
        return args


def parse_flashcards_params() -> FilePathParams:
    """Build the argument parser and return the parsed import/export file paths."""
    parser: ArgumentParser = argparse.ArgumentParser()

    parser.add_argument(
        CliArgument.IMPORT.value,
        type=str,
    )

    parser.add_argument(
        CliArgument.EXPORT.value,
        type=str,
    )

    args: Namespace = _get_args(parser)

    return FilePathParams(import_file_name=args.import_from, export_file_name=args.export_to)
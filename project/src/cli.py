import argparse
import sys
from argparse import ArgumentParser, Namespace
from enum import Enum

from models import FilePathParams

__all__ = ['parse_flashcards_params']

class CliArgument(Enum):
    IMPORT = "--import_from"
    EXPORT = "--export_to"

    @classmethod
    def values_tuple(cls) -> tuple[str, ...]:
        return tuple(item.value for item in cls)

def _get_args(parser: ArgumentParser) -> Namespace:
    try:
        args: Namespace = parser.parse_args()
    except SystemExit:
        print("Incorrect parameters")
        sys.exit()
    else:
        return args


def parse_flashcards_params() -> FilePathParams:
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
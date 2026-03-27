from dataclasses import dataclass

__all__ = ['FilePathParams']

@dataclass(frozen=True)
class FilePathParams:
    """Immutable container for the optional import and export file paths from CLI args."""

    import_file_name: str | None
    export_file_name: str | None
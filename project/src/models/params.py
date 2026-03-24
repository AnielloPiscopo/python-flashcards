from dataclasses import dataclass

__all__ = ['FilePathParams']

@dataclass(frozen=True)
class FilePathParams:
    import_file_name: str | None
    export_file_name: str | None
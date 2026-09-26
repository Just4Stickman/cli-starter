from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass
class FileInfo:
    path: Path
    size: int
    sha256: str


def hash_file(path: Path, chunk_size: int = 65536) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def inspect_file(path: Path) -> FileInfo:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    return FileInfo(path=path, size=path.stat().st_size, sha256=hash_file(path))


def inspect_directory(directory: Path) -> list[FileInfo]:
    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")
    return [inspect_file(p) for p in sorted(directory.rglob("*")) if p.is_file()]

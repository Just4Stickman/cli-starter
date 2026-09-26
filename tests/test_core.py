from pathlib import Path

import pytest

from forge_cli.core import hash_file, inspect_directory, inspect_file


def test_hash_file_known_content(tmp_path: Path) -> None:
    f = tmp_path / "hello.txt"
    f.write_text("hello")
    expected = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert hash_file(f) == expected


def test_inspect_file(tmp_path: Path) -> None:
    f = tmp_path / "a.txt"
    f.write_text("abc")
    info = inspect_file(f)
    assert info.size == 3
    assert len(info.sha256) == 64


def test_inspect_file_missing(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        inspect_file(tmp_path / "missing.txt")


def test_inspect_directory(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("bb")
    infos = inspect_directory(tmp_path)
    assert len(infos) == 2


def test_inspect_directory_not_a_dir(tmp_path: Path) -> None:
    f = tmp_path / "x.txt"
    f.write_text("x")
    with pytest.raises(NotADirectoryError):
        inspect_directory(f)

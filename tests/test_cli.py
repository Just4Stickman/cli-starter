from typer.testing import CliRunner

from forge_cli import __version__
from forge_cli.cli import app

runner = CliRunner()


def test_version() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_info() -> None:
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "forge" in result.stdout


def test_prepare(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("FORGE_OUTPUT_DIR", str(tmp_path / "out"))
    result = runner.invoke(app, ["prepare"])
    assert result.exit_code == 0

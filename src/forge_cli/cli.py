from __future__ import annotations

from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from forge_cli import __version__
from forge_cli.config import settings
from forge_cli.core import inspect_directory, inspect_file
from forge_cli.utils import ensure_dir, human_size, setup_logging

app = typer.Typer(
    name="forge",
    help="Production-grade Python CLI starter.",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()
log = setup_logging()


def _version_callback(value: bool) -> None:
    if value:
        console.print(f"[bold green]forge[/] version [cyan]{__version__}[/]")
        raise typer.Exit()


@app.callback()
def main(
    version: Annotated[
        bool,
        typer.Option("--version", "-V", callback=_version_callback, is_eager=True),
    ] = False,
) -> None:
    pass


@app.command()
def info() -> None:
    table = Table(title="Forge Info", show_header=True, header_style="bold magenta")
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="white")
    table.add_row("Version", __version__)
    table.add_row("App Name", settings.app_name)
    table.add_row("Debug", str(settings.debug))
    table.add_row("Log Level", settings.log_level)
    table.add_row("Output Dir", settings.output_dir)
    console.print(table)


@app.command()
def inspect(
    path: Annotated[Path, typer.Argument(help="File or directory to inspect")],
) -> None:
    if path.is_file():
        fi = inspect_file(path)
        console.print(f"[green]{fi.path}[/]")
        console.print(f"  Size   : {human_size(fi.size)}")
        console.print(f"  SHA256 : {fi.sha256}")
    elif path.is_dir():
        infos = inspect_directory(path)
        table = Table(title=f"Contents of {path}", show_header=True, header_style="bold magenta")
        table.add_column("File", style="cyan")
        table.add_column("Size", justify="right", style="green")
        table.add_column("SHA256 (short)", style="dim")
        total = 0
        for fi in infos:
            table.add_row(str(fi.path), human_size(fi.size), fi.sha256[:12])
            total += fi.size
        console.print(table)
        console.print(f"[bold]Total:[/] {len(infos)} files, {human_size(total)}")
    else:
        console.print(f"[red]Path does not exist:[/] {path}")
        raise typer.Exit(code=1)


@app.command()
def prepare() -> None:
    p = ensure_dir(settings.output_dir)
    console.print(f"[green]Ready:[/] {p}")


if __name__ == "__main__":
    app()

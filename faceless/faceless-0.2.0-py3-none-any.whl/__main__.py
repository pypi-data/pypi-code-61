"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Faceless."""


if __name__ == "__main__":
    main(prog_name="faceless")  # pragma: no cover

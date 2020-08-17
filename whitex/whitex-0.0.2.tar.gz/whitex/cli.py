"""Console script for whitex."""
import sys
import click

from whitex.whitex import clean_buffer


@click.command()
@click.argument(
    "input_fname",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.argument(
    "output_fname",
    type=click.Path(dir_okay=False),
)
def main(input_fname, output_fname):
    """Console script for whitex."""
    if not input_fname.endswith('.tex'):
        msg = (
            'Expected input file with tex extension, '
            f'but encountered {input_fname}'
        )
        raise click.Abort(msg)

    with open(input_fname, 'r') as input_buf:
        with open(output_fname, 'w') as output_buf:
            clean_buffer(input_buf, output_buf)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

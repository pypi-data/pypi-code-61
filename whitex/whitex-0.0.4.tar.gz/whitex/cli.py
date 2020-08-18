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
@click.option(
    '--keep-comments',
    help='Add if need to keep comments.',
    is_flag=True,
)
def main(input_fname, output_fname, keep_comments):
    """Console script for whitex."""
    if not input_fname.endswith('.tex'):
        msg = (
            'Expected input file with tex extension, '
            f'but encountered {input_fname}'
        )
        raise click.Abort(msg)

    with open(input_fname, 'r') as input_buf:
        with open(output_fname, 'w') as output_buf:
            clean_buffer(
                input_buf=input_buf,
                output_buf=output_buf,
                keep_comments=keep_comments,
            )


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

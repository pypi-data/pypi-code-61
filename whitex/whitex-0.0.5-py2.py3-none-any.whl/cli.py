"""Console script for whitex."""
import os
import shutil
import sys
import click

from whitex.whitex import clean_buffer


@click.command()
@click.argument(
    "input_fname",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.option(
    '--keep-comments',
    help='Add if need to keep comments.',
    is_flag=True,
)
@click.option(
    '--no-backup',
    help='Add if there is no need for backup',
    is_flag=True,
)
def main(input_fname, keep_comments, no_backup):
    """Console script for whitex."""
    if not input_fname.endswith('.tex'):
        msg = (
            'Expected input file with tex extension, '
            f'but encountered {input_fname}'
        )
        click.echo(msg)
        raise click.Abort(msg)

    with open(input_fname, 'r') as input_buf:
        clean_string = clean_buffer(
            input_buf=input_buf,
            keep_comments=keep_comments,
        )

    if not no_backup:
        _make_backup(input_fname)

    output_fname = input_fname

    with open(output_fname, 'w') as output_buf:
        output_buf.write(clean_string)


def _make_backup(fname):
    name, extension = os.path.splitext(fname)
    backup_fname = ''.join([
        '.',
        name,
        '_whitex_bkp',
        extension,
    ])
    shutil.copy(fname, backup_fname)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

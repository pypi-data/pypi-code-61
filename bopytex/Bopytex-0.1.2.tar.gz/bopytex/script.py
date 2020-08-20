#!/usr/bin/env python
# encoding: utf-8


import click
import logging
from pathlib import Path
from .bopytex import subject_metadatas, crazy_feed, pdfjoin, feed, clean, texcompile, setup, activate_printanswers

formatter = logging.Formatter("%(name)s :: %(levelname)s :: %(message)s")
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(steam_handler)

@click.command()
@click.argument(
    "template",
    type=click.Path(exists=True),
    nargs=1,
    # help="File with the template. The name should have the following form tpl_... .",
)
@click.option(
    "-w",
    "--working-dir",
    type=click.Path(exists=True),
    help="Where fed templates and compiled files will be placed",
)
@click.option(
    "-s",
    "--students-csv",
    type=str,
    default="",
    help="CSV containing list of students names",
)
@click.option(
    "-d", "--dirty", is_flag=True, default=False, help="Do not clean after compilation",
)
@click.option(
    "-n",
    "--no-compile",
    is_flag=True,
    default=False,
    help="Do not compile source code",
)
@click.option(
    "-N",
    "--number_subjects",
    type=int,
    default=1,
    help="The number of subjects to make",
)
@click.option(
    "-j",
    "--no-join",
    is_flag=True,
    default=False,
    help="Do not join pdfs to a single pdf and remove individuals",
)
@click.option(
    "-O",
    "--only-corr",
    is_flag=True,
    default=False,
    help="Create and compile only correction from existing subjects",
)
@click.option(
    "-c",
    "--corr",
    is_flag=True,
    default=False,
    help="Create and compile correction while making subjects",
)
@click.option(
    "-C",
    "--crazy",
    is_flag=True,
    default=False,
    help="Crazy mode. Tries and tries again until template feeding success!",
)
def new(**options):
    """ Bopytex

    Feed the template (tpl_...) and then compile it with latex.

    """
    setup()

    logger.debug(f"CI parser gets {options}")

    template = Path(options["template"]).name
    directory = Path(options["template"]).parent
    metadatas = subject_metadatas(options)
    logger.debug(f"Metadata {metadatas}")

    for meta in metadatas:
        logger.debug(f"Feeding template toward {meta['texfile']}")
        if options["crazy"]:
            crazy_feed(
                template=Path(meta["directory"]) / meta["template"],
                data=meta,
                output=meta["texfile"],
                force=1,
            )
        else:
            feed(
                template=Path(meta["directory"]) / meta["template"],
                data=meta,
                output=meta["texfile"],
                force=1,
            )
        assert(Path(meta["texfile"]).exists())
        logger.debug(f"{meta['texfile']} fed")

        if options["corr"]:
            logger.debug(f"Building correction for {meta['texfile']}")
            meta.update({
                "corr_texfile": activate_printanswers(meta["texfile"]),
            })

        if not options["no_compile"]:
            for prefix in ["", "corr_"]:
                key = prefix + "texfile"
                try:
                    meta[key]
                except KeyError:
                    pass
                else:
                    texcompile(meta[key])
                    meta.update({
                        prefix+'pdffile': meta[key].replace('tex', 'pdf')
                    })

    if not options["no_join"]:
        for prefix in ["", "corr_"]:
            key = prefix + "pdffile"
            try:
                pdfs = [m[key] for m in metadatas]
            except KeyError:
                pass
            else:
                pdfjoin(
                    pdfs,
                    template.replace("tpl", prefix+"all").replace(".tex", ".pdf"),
                    directory,
                    rm_pdfs=1,
                )

    if not options["dirty"]:
        clean(directory)

    # produce_and_compile(options)


if __name__ == "__main__":
    new()

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del

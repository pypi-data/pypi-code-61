#!/usr/bin/env python
# encoding: utf-8

"""
Producing then compiling templates
"""

import csv
import os
import logging

from pathlib import Path
import pytex
from mapytex import Expression, Integer, Decimal
import bopytex.filters as filters

formatter = logging.Formatter("%(name)s :: %(levelname)s :: %(message)s")
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.DEBUG)
steam_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(steam_handler)


def setup():
    Expression.set_render("tex")
    logger.debug(f"Render for Expression is {Expression.RENDER}")
    mapytex_tools = {
        "Expression": Expression,
        "Integer": Integer,
        "Decimal": Decimal,
        # "Polynom": mapytex.Polynom,
        # "Fraction": mapytex.Fraction,
        # "Equation": mapytex.Equation,
        # "random_str": mapytex.random_str,
        # "random_pythagore": mapytex.random_pythagore,
        # "Dataset": mapytex.Dataset,
        # "WeightedDataset": mapytex.WeightedDataset,
    }
    pytex.update_export_dict(mapytex_tools)

    pytex.add_filter("calculus", filters.do_calculus)


def get_working_dir(options):
    """ Get the working directory """
    if options["working_dir"]:
        working_dir = Path(options["working_dir"])
    else:
        try:
            template = Path(options["template"])
        except TypeError:
            raise ValueError(
                "Need to set the working directory \
                    or to give a template"
            )
        else:
            working_dir = template.parent
    logger.debug(f"The output directory will be {working_dir}")
    return working_dir


def activate_printanswers(
    texfile, noans=r"solution/print = false", ans=r"solution/print = true"
):
    """ Activate printanswers mod in texfile """
    output_fname = "corr_" + texfile
    with open(texfile, "r") as input_f:
        with open(output_fname, "w") as output_f:
            for line in input_f.readlines():
                output_f.write(line.replace(noans, ans))
    return output_fname


def deactivate_printanswers(corr_fname):
    """ Activate printanswers mod in texfile """
    Path(corr_fname).remove()


def pdfjoin(pdf_files, destname, working_dir=".", rm_pdfs=1):
    """TODO: Docstring for pdfjoin.

    :param pdf_files: list of pdf files to join
    :param destname: name for joined pdf
    :param working_dir: the working directory
    :param rm_pdfs: Remove pdf_files after joining them
    :returns: TODO

    """
    joined_pdfs = Path(working_dir) / Path(destname)
    pdf_files_str = " ".join(pdf_files)
    pdfjam = f"pdfjam {pdf_files_str} -o {joined_pdfs}"
    logger.debug(f"Run {pdfjam}")
    logger.info("Joining pdf files")
    os.system(pdfjam)
    if rm_pdfs:
        logger.info(f"Remove {pdf_files_str}")
        os.system(f"rm {pdf_files_str}")


def extract_student_csv(csv_filename):
    """ Extract student list from csv_filename """
    with open(csv_filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        return [r for r in reader]


def subject_metadatas(options):
    """ Return metadata on subject to produce

    if csv is given it will based on is
    otherwise it will be based on quantity

    :example:
    >>> subject_metadata(10)
    """
    if options["students_csv"]:
        metadatas = []
        for (i, s) in enumerate(extract_student_csv(options["students_csv"])):
            d = {"num": f"{i+1:02d}"}
            d.update(s)
            metadatas.append(d)
    elif options["number_subjects"] > 0:
        metadatas = [{"num": f"{i+1:02d}"} for i in range(options["number_subjects"])]
    else:
        raise ValueError("Need metacsv or quantity to build subject metadata")

    for meta in metadatas:
        meta.update(
            {
                "template": str(Path(options["template"]).name),
                "texfile": str(Path(options["template"]).name).replace(
                    "tpl", meta["num"]
                ),
                "directory": str(Path(options["template"]).parent),
            }
        )

    return metadatas


def feed(*args, **kwrds):
    """ Nice and smooth pytex feed """
    pytex.feed(*args, **kwrds)


def crazy_feed(*args, **kwrds):
    """ Crazy mod for pytex feed """
    while True:
        try:
            pytex.feed(*args, **kwrds)
        except:
            logger.debug(f"Crazy feed is working hard...! {args} {kwrds}")
        else:
            break


def clean(directory):
    pytex.clean(directory)


def texcompile(filename):
    logger.debug(f"Start compiling {filename}")
    pytex.pdflatex(Path(filename))
    logger.debug(f"End compiling")


def produce_and_compile(options):
    """ Produce and compile subjects
    """
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


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del

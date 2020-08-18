__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

import os
import configparser
import shutil
import click
import io
from pathlib import Path
import bandalyzer_app
import bandalyzer_app.defects
import bandalyzer_app.poissonequations
import bandalyzer_app.poissonrelaxationsolver
import bandalyzer_app.poissonNRsolver
import bandalyzer_app.schrodpoissonequations
import bandalyzer_app.schrodpoissonNRsolver
import bandalyzer_app.solver
import bandalyzer_app.diamondsoln
import bandalyzer_app.settingsobject

config_folder = Path(bandalyzer_app.__path__[0]) / ".config"
if not config_folder.exists():
    print(f"Could'nt find .config folder!")


def safe_callback(func):
    def inner(ctx, param, value):
        if not value or ctx.resilient_parsing:
            return
        return func(ctx, param, value)

    return inner


def init_folder(directory):
    if not type(directory) is Path:
        directory = Path(directory)

    if not directory.exists():
        directory.mkdir()

    shutil.copy(config_folder / "default_settings.ini", directory / "settings.ini")
    shutil.copy(config_folder / "example_defects.ini", directory / "defects.ini")

    config_parser = configparser.ConfigParser(comment_prefixes=None, allow_no_value=True)

    # This is some hacky shit that allows reading in of comments preceding any sections in the settings.ini file.
    temp_heading = "[DEFUALT]\n"
    with open(directory / "settings.ini") as f:
        data = f.read()
    config_parser.read_string(temp_heading + data)

    # Update the values for settings_file and local_dir preserving any inline comments.
    for option, value in zip(['settings_file', 'local_dir'], ["settings.ini", str(directory.absolute())]):
        try:
            inline_comments = " ; " + config_parser.get(bandalyzer_app.settingsobject.SettingsObject._settings_heading_, option).split(";")[1]
        except IndexError:
            inline_comments = ''
        config_parser.set(bandalyzer_app.settingsobject.SettingsObject._settings_heading_, option,
                          value + inline_comments)

    # This is some hacky shit to remove the first line that says [DEFAULT] above the comments.
    data = ''
    out_stream = io.StringIO()
    config_parser.write(out_stream)
    with open(directory / "settings.ini", mode='w') as f:
        f.write(out_stream.getvalue()[len(temp_heading):])

    # with open(directory / "settings.ini", mode='w') as f:
    #     config_parser.write(f)
    # with open(directory / "settings.ini", mode='r') as f:
    #     line = f.readline()
    #     line = f.readline()
    #     while line:
    #         data = data + line
    #         line = f.readline()
    # with open(directory / "settings.ini", mode='w') as f:
    #     f.write(data)


def solve(directory, solver_type, init_file, settings_file, plotQ,  plot_level, dry_run_flag, overwrite_flag):
    fom_file = None
    if settings_file is None:
        settings_file = Path(directory) / "settings.ini"
    if init_file is not None:
        fom_file = Path(directory) / init_file.replace('_solution_space_', '_FOM_')
        if not fom_file.is_file():
            click.echo(f"Could'nt find matching FOM file {str(fom_file)}")
            fom_file = None
    solver = bandalyzer_app.diamondsoln.DiamondSoln(settings_file=str(settings_file), local_dir=directory,
                                                    dry_run=dry_run_flag, initial_solution_file=init_file,
                                                    initial_fom_file=fom_file, solver_type=solver_type, overwrite=overwrite_flag)
    solver.initialise()
    if plotQ is None:
        solver.solve()
    else:
        solver.plot_solve(plotQ, plot_level)
    if not dry_run_flag:
        solver.save_and_data_and_settings()

@safe_callback
def plot_help(ctx, param, value):
    click.echo("Plot things")
    ctx.exit()

@safe_callback
def print_library(ctx, param, value):
    click.echo(config_folder / "defect_library.ini")
    with open(config_folder / "defect_library.ini", mode='r') as f:
        click.echo_via_pager(f.read())
    ctx.exit()


@safe_callback
def build_defaults(ctx, param, value):
    settings_objects = [bandalyzer_app.diamondsoln.DiamondSoln,
                        bandalyzer_app.diamondsoln.FiguresOfMerit,
                        bandalyzer_app.defects.Defects,
                        bandalyzer_app.schrodpoissonNRsolver.SchrodingerPoissonNRSolver,
                        bandalyzer_app.poissonNRsolver.PoissonNRSolver,
                        bandalyzer_app.poissonrelaxationsolver.PoissonRelaxationSolver,
                        bandalyzer_app.schrodpoissonequations.SchrodingerPoissonEquations,
                        bandalyzer_app.poissonequations.PoissonEquations,
                        bandalyzer_app.solver.Solver,
                        bandalyzer_app.settingsobject.SettingsObject
                        ]
    default_settings_dict = {}
    for obj in settings_objects:
        default_settings_dict[obj._settings_heading_] = obj.default_settings
    bandalyzer_app.settingsobject.__create_default_ini__(default_settings_dict)
    click.echo("Created new default settings.ini from programmed defaults at ", nl=False)
    click.echo(click.style(str(config_folder / "default_settings.ini"), fg="red"))
    with open(config_folder / "default_settings.ini", mode='r') as f:
        click.echo_via_pager(f.read())
    ctx.exit()

@safe_callback
def do_nothing(ctx, param, value):
    click.echo('did nothing')
    ctx.exit()

@safe_callback
def print_solvers(ctx, param, value):
    x, y = click.get_terminal_size()
    max_len = 1
    for solver_type in bandalyzer_app.diamondsoln.solver_types.keys():
        max_len = max(len(solver_type), max_len)
    desc_len = max(1, x - max_len - 4)
    for solver_type, description in bandalyzer_app.diamondsoln.solver_types.items():
        click.echo(click.style(solver_type, fg='green'), nl=False)
        click.echo(" " * (max_len - len(solver_type) + 1) + "-- ", nl=False)
        for i in range(0, len(description[0]), desc_len):
            if i == 0:
                click.echo(description[0][i:i + desc_len])
            else:
                click.echo(" " * (x - desc_len) + description[0][i:i + desc_len])
    ctx.exit()

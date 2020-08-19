import kfp
import click
from tabulate import tabulate

import ast

from kfp_command_line_tools.read_config.config_file import read_or_build_config_file


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


@click.group()
@click.pass_context
def experiment(ctx):
    config = read_or_build_config_file()
    if not config:
        return
    host = config['host']
    namespace = config['namespace']
    ctx.ensure_object(kfp.Client)

    ctx.obj = kfp.Client(host=host, namespace=namespace)


@experiment.command()
@click.pass_context
def show(ctx):
    if not ctx.obj:
        return
    all_experiments = ctx.obj.list_experiments().experiments
    important_features = []
    headers = ['name', 'id', 'created at']
    for exp in all_experiments:
        important_features.append([exp.name, exp.id, exp.created_at])

    click.echo(tabulate(important_features, headers=headers, tablefmt='github'))


@experiment.command()
@click.argument('name')
@click.pass_context
def create(ctx, name):
    if not ctx.obj:
        return
    ctx.obj.create_experiment(name=name, description='teste')

    click.echo(f'experiment created.')

import kfp
import click
import ast
from tabulate import tabulate

from kfp_command_line_tools.read_config.config_file import read_or_build_config_file
from kfp_command_line_tools.utils import verify


class PythonLiteralOption(click.Option):

    def type_cast_value(self, ctx, value):
        try:
            return ast.literal_eval(value)
        except:
            raise click.BadParameter(value)


@click.group()
@click.pass_context
def runs(ctx):
    config = read_or_build_config_file()
    if not config:
        return
    host = config['host']
    namespace = config['namespace']

    ctx.ensure_object(kfp.Client)

    ctx.obj = kfp.Client(host=host, namespace=namespace)


@runs.command()
@click.pass_context
def show(ctx):
    if not ctx.obj:
        return
    all_runs = ctx.obj.list_runs().runs
    important_features = []
    headers = ['name', 'status', 'id']
    for run in all_runs:
        important_features.append([run.name, run.status, run.id])

    click.echo(tabulate(important_features, headers=headers, tablefmt='github'))


@runs.command()
@click.argument('pipeline_id', default=None)
@click.argument('experiment_id', default=None)
@click.argument('job_name', default=None)
@click.argument('params', nargs=-1, default=None)
@click.option('--file_params', default=None)
@click.option('--version_id', default=None)
@click.option('--pipeline_package_path', default=None)
@click.pass_context
def pipeline(ctx, pipeline_id: str, experiment_id: str, job_name: str, params, file_params, version_id: str,
             pipeline_package_path: str):
    if not ctx.obj:
        return

    parameters = verify(params, file_params)

    ctx.obj.run_pipeline(pipeline_id=pipeline_id,
                         experiment_id=experiment_id,
                         job_name=job_name,
                         params=parameters,
                         version_id=version_id,
                         pipeline_package_path=pipeline_package_path
                         )
    click.echo(f'running {job_name}')

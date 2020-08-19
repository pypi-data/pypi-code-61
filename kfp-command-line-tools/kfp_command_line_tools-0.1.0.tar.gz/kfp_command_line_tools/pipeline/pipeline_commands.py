import kfp
import click
import pandas as pd
from tabulate import tabulate

from kfp_command_line_tools.read_config.config_file import read_or_build_config_file


@click.group()
@click.pass_context
def pipelines(ctx):
    config = read_or_build_config_file()
    if not config:
        return
    host = config['host']
    namespace = config['namespace']
    ctx.ensure_object(kfp.Client)

    ctx.obj = kfp.Client(host=host, namespace=namespace)


@pipelines.command()
@click.pass_context
def show(ctx):
    if not ctx.obj:
        return
    all_pipelines = ctx.obj.list_pipelines().pipelines
    important_features = [[pipeline.name, pipeline.id, pipeline.created_at] for pipeline in all_pipelines]
    headers = ['name', 'id', 'created at']

    click.echo(tabulate(important_features, headers=headers, tablefmt='github'))


@pipelines.command()
@click.argument('pipeline_id', default=None)
@click.pass_context
def parameters(ctx, pipeline_id: str):
    if not ctx.obj:
        return
    all_pipelines = ctx.obj.get_pipeline(pipeline_id=pipeline_id).parameters

    parameters_dict = {'name': [key.name for key in all_pipelines], 'value': [value.value for value in all_pipelines]}

    dataframe = pd.DataFrame(parameters_dict).fillna('No default value')

    click.echo(tabulate(dataframe, headers='keys', tablefmt='github', showindex=False))


@pipelines.command()
@click.argument('file_path')
@click.argument('pipeline_name')
@click.pass_context
def upload(ctx, file_path: str, pipeline_name: str):
    if not ctx.obj:
        return
    ctx.obj.upload_pipeline(pipeline_package_path=file_path, pipeline_name=pipeline_name)
    click.echo(f'your pipeline {pipeline_name} was uploaded.')


@pipelines.command()
@click.argument('pipeline_id')
@click.argument('version_file')
@click.argument('version_name')
@click.pass_context
def upload_version(ctx, pipeline_id: str, version_file: str, version_name: str):
    if not ctx.obj:
        return
    ctx.obj.pipeline_uploads.upload_pipeline_version(
        uploadfile=version_file,
        name=version_name,
        pipelineid=pipeline_id
    )
    click.echo(f'the pipeline {pipeline_id} now has a new version {version_name}')


@pipelines.command()
@click.argument('pipeline_id')
@click.pass_context
def delete(ctx, pipeline_id: str):
    if not ctx.obj:
        return
    ctx.obj.delete_pipeline(pipeline_id=pipeline_id)
    click.echo(f'pipeline {pipeline_id} was deleted.')

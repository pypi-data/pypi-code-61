import sys, os
import click
import configparser
from .loader import connect, update_resource, new_resource

## set up logging
import logging
logging.basicConfig(level=os.environ.get("LOGLEVEL","INFO"))
log = logging.getLogger(__name__)

configFile = os.path.join(os.path.abspath(os.path.join(os.path.expanduser('~/.config'),"ckanconfig.ini")))

@click.group()
def main():
    """ CKAN Remote Datastore Upload """
    pass


@main.command()
@click.option('-u', '--url', type=str, required=True, prompt="CKAN Site Url")
@click.option('-a', '--apikey', type=str, required=True, prompt="API Key")
def configure(url, apikey):
    """ Configure CKAN connection"""
    try:
        ckan = connect(str(url), str(apikey))
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'url': str(url),
                             'apikey': str(apikey)}
        with open(configFile, 'w') as conf:
            config.write(conf)
    except:
        log.error('connection not established, try again')
    

@main.command()
@click.option('-f', '--file', type=str, required=True, help="Input File")
@click.option('-r', '--resource', type=str, required=True, help='Resource ID')
def update(**kwargs):
    """ Update an existing resource """
    try:
        config = configparser.ConfigParser()
        config.read(configFile)
        ckan_url = config['DEFAULT']['url']
        api_key = config['DEFAULT']['apikey']
        try:
            ckan = connect(str(ckan_url), str(api_key))
        except KeyError:
            log.error("Improper Configuration. Run `ckanloader configure` from the command line.")
        click.echo(kwargs)
        update_resource(ckan, kwargs.get("file"), kwargs.get("resource"))
    except KeyError:
        log.error("Improper Configuration. Run `ckanloader configure` from the command line.")
    except FileNotFoundError:
        log.error("File not found, check file name and try again")


@main.command()
@click.option('-f', '--file', type=str, required=True, help="Input File")
@click.option('-p', '--package', type=str, required=True, help="Package ID (Dataset Name)")
@click.option('-n', '--name', type=str, required=False, help="Provide a name for the new resource")
def create(**kwargs):
    """ Create a new resource in an existing dataset """
    try:
        config = configparser.ConfigParser()
        config.read(configFile)
        ckan_url = config['DEFAULT']['url']
        api_key = config['DEFAULT']['apikey']
        try:
            ckan = connect(str(ckan_url), str(api_key))
        except KeyError:
            log.error("Improper Configuration. Run `ckanloader configure` from the command line.")
        click.echo(kwargs)
        new_resource(ckan, kwargs.get("file"), kwargs.get("package"), kwargs.get("name"))
    except FileNotFoundError:
        log.error("File not found, check file name and try again")


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("CKAN Remote Datastore Upload")
    main()
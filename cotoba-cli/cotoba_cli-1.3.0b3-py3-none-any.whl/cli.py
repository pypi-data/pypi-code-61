import getpass
import os
import pkg_resources
import sys
import locale as loc

import click

from cotoba_cli import platform
from cotoba_cli import cli_nlu
from cotoba_cli import cli_platform
from cotoba_cli import config
from cotoba_cli import session
from cotoba_cli.error import ApiResponseError
from logging import config as logging_config
from logging import getLogger

logger = getLogger(__name__)
VERSION = pkg_resources.get_distribution('cotoba-cli').version


@click.group()
@click.version_option(version=VERSION, prog_name='cotoba-cli')
def cli_root():
    pass


@cli_root.command(help='Login and renews session token.')
@click.option('--id', 'login_id', type=str, help='Id.', required=True)
@click.option('--password', prompt=True, hide_input=True, help='Password.')
def login(login_id, password):
    response = platform.login(login_id, password)
    session.initialize()
    session.save(
        login_id=login_id,
        id_token=response['AuthenticationResult']['IdToken'],
        access_token=response['AuthenticationResult']['AccessToken'],
        refresh_token=response['AuthenticationResult']['RefreshToken'])

    click.secho(login_id + ' has successfully logged in.', fg='bright_blue')


@cli_root.command(help='Change password.')
@click.option('--old-password', type=str, help='Old password.')
@click.option('--new-password', type=str, help='New password.')
def change_password(old_password, new_password):
    if not old_password:
        old_password = getpass.getpass('Old password: ')

    login_id = session.load()['default'].get('id')
    response = platform.login(login_id, old_password)
    session.initialize()
    session.save(
        login_id=login_id,
        id_token=response['AuthenticationResult']['IdToken'],
        access_token=response['AuthenticationResult']['AccessToken'],
        refresh_token=response['AuthenticationResult']['RefreshToken'])
    if not new_password:
        new_password = getpass.getpass('New password: ')
        new_password_confirm = getpass.getpass('Confirm new password: ')
        if new_password != new_password_confirm:
            click.echo('Password do not match.', err=True)
            sys.exit(1)

    access_token = response['AuthenticationResult']['AccessToken']
    platform.change_password(
        old_password=old_password,
        new_password=new_password,
        access_token=access_token
    )
    click.secho('Password updated successfully.', fg='bright_blue')


@cli_root.command(help='Config setting.')
# @click.option('--x-api-key', type=str, help='X-Api-Key.')
# @click.option('--dev-key', type=str, help='Developer-Key.')
# @click.option('--api-key', type=str, help='Api-Key.')
# @click.option('--user', type=str, help='User ID.')
@click.option('--locale', type=str, help='Locale.')
@click.option('--endpoint-url', 'url', type=str, help='Endpoint URL.')
@click.option('--authorization', type=str, help='Authorization ID.')
@click.option('--show-config', 'show_config', is_flag=True,
              help='Show Config.')
def configure(locale,
              url,
              authorization,
              show_config):

    config_dict = config.load()['default']

    if show_config:
        # コンソール上に現在の設定値一覧表示
        # click.echo('x-api-key:' + config_dict['x-api-key'])
        # click.echo('developer-key:' + config_dict['developer-key'])
        # click.echo('api-key:' + config_dict['api-key'])
        # click.echo('user-id:' + config_dict['user-id'])
        click.echo('locale:' + config_dict['locale'])
        click.echo('endpoint-url:' + config_dict['endpoint-url'])
        click.echo('authorization:' + config_dict['authorization'])
        return

    if any(
            [
                # x_api_key,
                # dev_key,
                # api_key,
                # user,
                locale,
                url,
                authorization
            ]
    ):
        # オプション設定時は指定されたものだけ上書きする
        # x_api_key = (x_api_key if x_api_key is not None
        #              else config_dict['x-api-key'])
        # dev_key = (dev_key if dev_key is not None
        #            else config_dict['developer-key'])
        # api_key = (api_key if api_key is not None
        #            else config_dict['api-key'])
        # user_id = (user if user is not None
        #            else config_dict['user-id'])
        locale = (locale if locale is not None
                  else config_dict['locale'])
        url = (url if url is not None
               else config_dict['endpoint-url'])
        authorization = (authorization if authorization is not None
                         else config_dict['authorization'])
    else:
        # オプションで未指定の場合のみコンソールで入力を行う
        click.secho('<leave blank in case unchanged>',
                    fg='bright_cyan')
        # x_api_key = show_current_and_input_value('x-api-key', config_dict)
        # dev_key = show_current_and_input_value('developer-key', config_dict)
        # api_key = show_current_and_input_value('api-key', config_dict)
        # user_id = show_current_and_input_value('user-id', config_dict)
        locale = show_current_and_input_value('locale', config_dict)
        url = show_current_and_input_value('endpoint-url', config_dict)
        authorization = show_current_and_input_value('authorization',
                                                     config_dict)

    available_locales_values = loc.windows_locale.values()
    available_locales = [
        v.replace('_', '-') for v in available_locales_values
    ]
    if locale not in available_locales:
        # 不正なロケール指定時はエラーの旨を表示し変更しない
        click.secho('Invalid locale.', fg='red')
        locale = config_dict['locale']
    # 設定した値をファイルに保存
    config.save(
        # x_api_key=x_api_key,
        # dev_key=dev_key,
        # api_key=api_key,
        # user_id=user_id,
        locale=locale,
        url=url,
        authorization=authorization
    )


# 現在の設定値の表示と値の入力
def show_current_and_input_value(key_name, config_dict):
    key_and_colon = key_name + ':'
    # 現在の設定値を緑色で表示
    click.echo(click.style(key_and_colon
                           + config_dict[key_name],
                           fg='green')
               )
    input_value = input(key_and_colon)
    # 未入力時は設定しない
    input_value = (input_value if len(str(input_value)) != 0
                   else config_dict[key_name])
    return input_value


cli_root.add_command(cli_platform.cli_platform, 'bot')
cli_root.add_command(cli_nlu.cli_nlu, 'nlu')


def main():
    # TODO: move this initialization to config or somewhere.
    # need refactoring.
    filepath = config.get_config_filepath()
    directory, _ = os.path.split(filepath)
    if not os.path.exists(directory):
        os.mkdir(directory)
    log_file = config.get_config_filepath('cotoba-cli.log')
    logging_config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'fileFormatter': {
                'format': '[%(levelname)s] '
                          '%(asctime)s '
                          '%(pathname)s(%(lineno)s):%(message)s'
            }
        },
        'handlers': {
            'fileHandler': {
                'level': 'INFO',
                'formatter': 'fileFormatter',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': log_file,
                'maxBytes': 1000000,
                'backupCount': 3,
                'encoding': 'utf-8',
            }
        },
        'loggers': {
            '': {
                'handlers': ['fileHandler'],
                'level': 'INFO',
            }
        }
    })

    try:
        '''
        See Click Exceptions (https://click.palletsprojects.com/en/7.x/api/#exceptions)
        for exception details.
        '''
        cli_root.main(sys.argv[1:], standalone_mode=False)
    except click.UsageError as e:
        # Usage error (error code: 2)
        click.echo(e.format_message(), err=True)
        logger.error(e.format_message())
        sys.exit(e.exit_code)
    except ApiResponseError as e:
        # Server response error (error code: 3)
        logger.error(e)
        click.secho(str(e), fg='red', err=True)
        click.echo(e.body)
        sys.exit(e.exit_code)
    except click.ClickException as e:
        # User abort or other error (error code: 1)
        click.echo(e.format_message(), err=True)
        logger.error(e.format_message())
        sys.exit(e.exit_code)
    except Exception as e:
        # Unhandled exception (error code: 255)
        click.echo(f'Unexpected Error has occurred. See {log_file} in detail.', err=True)
        logger.error(f'Unexpected Error: {str(e)}', exc_info=True)
        sys.exit(-1)


if __name__ == '__main__':
    main()

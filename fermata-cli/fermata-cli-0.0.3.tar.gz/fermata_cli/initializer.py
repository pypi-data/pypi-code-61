import os
import sys
import stat

from .util import logger

FILES = [
    {
        'name': 'app.py',
        'tpl': '''from fermata import Fermata

app = Fermata(
    '{package}',
    spec_glob='specs/*.yml',
    )
'''
    },
    {
        'name': 'http.sh',
        'tpl': 'gunicorn -w=2 -k"egg:meinheld#gunicorn_worker" app:app\n',
        'stat': { '-': stat.S_IEXEC }
    },
    {
        'name': 'specs/api.yml',
        'tpl': 'openapi: 3.0.3\n'
    },
    {
        'name': 'requirements.txt',
        'tpl': '''fermata
pyyaml
'''
    },
]


def init():
    base = os.getcwd()
    for item in FILES:
        name, tpl = item['name'], item['tpl']
        path = os.path.join(base, name)
        kwargs = {
            'package': os.path.split(base)[1] or 'apis',
        }
        if os.path.exists(path):
            logger.error(f'{name} already exists.')
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            f.write(tpl.format(**kwargs))

        if 'stat' in item:
            mode = os.stat(path).st_mode
            plus = item['stat'].get('+')
            dash = item['stat'].get('-')
            if plus:
                mode = mode | plus
            if dash:
                mode = mode & ~dash
            os.chmod(path, mode)

    logger.info(f'app created.')

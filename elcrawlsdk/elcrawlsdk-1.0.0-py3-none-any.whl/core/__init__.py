import os

home = os.curdir

if 'HOME' in os.environ:
    home = os.environ['HOME']
elif os.name == 'posix':
    home = os.path.expanduser('~/')
elif os.name == 'nt':
    if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
        home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
elif 'HOMEPATH' in os.environ:
    home = os.environ['HOMEPATH']

ELCRAWL_ROOT = os.path.join(home, '.elcrawl')
ELCRAWL_TMP = os.path.join(ELCRAWL_ROOT, 'tmp')

if not os.path.exists(ELCRAWL_ROOT):
    os.mkdir(ELCRAWL_ROOT)

if not os.path.exists(ELCRAWL_TMP):
    os.mkdir(ELCRAWL_TMP)

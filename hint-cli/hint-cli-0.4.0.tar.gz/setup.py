# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hint_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'colorama>=0.4.3,<0.5.0', 'gitpython>=3.1.7,<4.0.0']

entry_points = \
{'console_scripts': ['hint = hint_cli.hint:cli']}

setup_kwargs = {
    'name': 'hint-cli',
    'version': '0.4.0',
    'description': 'Hint exists to get help on commands from the command line, without switching context or applications.',
    'long_description': '# hint\n\nHint exists to get help on commands from the command line, without switching context or applications. \n\n## Project status\n\nThis is currently a POC project I\'m using to see what I find useful and how I want the project to develop. For all intents and purposes this tool is completely unsupported. I make no guarantees about backwards compatibility or commitment to responding to issues or PRs. It is a personal project which I\'m happy to share, as open source software licensed with the MIT license if you find it useful and/or want any changes I would suggest forking this repo.    \n\n## Installation\n\nRecommended installation method is with [pipx](https://pipxproject.github.io/pipx/).\n\n`pipx install hint-cli`\n\n## Usage\n\nThe first time you run `hint <topic>` it will prompt for configuration values for the following:\n\n* Git repository for the hint source - Address of the remote repository to clone containing your hint content. Use the sample repo from GitHub of `git@github.com:agarthetiger/hint-cli-samples.git` to get started. It is expected that you will create your own content and configure your own repo later. The only topic in the example repo is `bash`. Note that while both the ssh and https clone addresses will work to view content, much of the functionality to add and modify content will require the ssh style repo address. \n\nThen run `hint <topic>` where topic is the name of a markdown file in the repository root, without the .md file extension.\n\n* `hint bash` - Display the formatted contents of https://raw.githubusercontent.com/agarthetiger/hint/trunk/docs/examples/bash.md \n* `hint bash curl` - Display only the `curl` subsection from the bash.md file. Valid subsections are any level headings in the markdown document. To display only an H4 subsection, just use the H4 heading text as the 2nd argument. \n* `hint --help` - Get help\n\n## Upgrading\n\nThis project is still in an unstable state and minor version bumps may be breaking until 1.0.0 is released. When upgrading I recommend deleting the config file `~/.hintrc` before running the new version, so that the correct config options are set.\n\nFrom 1.0.0 onwards, releases will be versioned semantically according to [semver.org 2.0.0](https://semver.org/).\n\n## Creating content\n\n`hint` is written for you to create your own content, for whatever useful information you would like to access from the command line. It is expected that you will setup your own repository with your own hints.    \n\nThe repository is expected to contain markdown files with a .md file extension in the root of the repository. Each file name is considered a topic, and each heading a subsection. There is some basic formatting applied to the markdown before being displayed using Click\'s [echo and style support](https://click.palletsprojects.com/en/7.x/api/?highlight=secho#click.secho).\n\n* Section headings are displayed in bold and cyan.\n* Text surrounded by \\` characters is displayed in bold and blue.\n* All other text is displayed as typed in the markdown file.\n\n## Switching hint repositories\n\nVersion 0.4.0 changes from using requests to using GitPython to clone the remote repository for the hint content. If you are using >=0.4.0 and want to change the remote repository, update the value for `repo` in `~/.hintrc` and delete the folder `~/.hints.d/hints` before running hint again.   \n\n## Alternatives\n\nIf you want a tool which pulls community content rather than writing your own, look at [cheat.sh](https://github.com/chubin/cheat.sh). It provides "unified access to the best community driven cheat sheets repositories of the world".  \n\n## System Requirements\n\n* Python3\n* Pip3\n* Access to pypi.org or another pip repo with the `hint-cli` python package and dependencies\n* Network access to the hints git repository. This may be internet access to GitHub.com but could also be an internal Git server.\n\n## Concept\n\nI use GitHub Pages and MKDocs as well as other Notes applications to collect technical information which I personally find useful. I have a few cheat-sheets with reminders on commands I use regularly but infrequently. The `man` and `info` commands provide help on most commands, however they are very detailed and more useful commands often involve multiple cli tools. Examples bridge the gap between the low level documentation and complex infrequent commands which won\'t necessarily be in the command history for the current system. \n\nOften I\'m using a terminal within PyCharm or VS Code and it\'s undesirable to switch context to a different application, navigate to a site which may not be open, get the right page and click or scroll to the relevant section. It\'s not an insurmountable problem, but a workflow which I wanted to optimise. \n\nThis tool was inspired in multiple ways by Thomas Stringer\'s post on [My Personal Wiki … Now Through the Terminal](https://medium.com/@trstringer/my-personal-wiki-now-through-the-terminal-689794e07b42). The fact that I stumbled across this while searching for something else is validation for having a tool and workflow which enables me to remain in the IDE and not switch to a browser. It\'s similar to taking an alcoholic to a pub and constantly offering them a drink, then saying it\'s his fault if he ends up drinking. Sure, there is some level of personal responsibility with the alcoholic to resist but a better solution would be to avoid the pub. `hint` keeps me focused, puts the information I need at my fingertips away from distractions.\n\n## Backlog of ideas for improvement\n\nErr, it\'s vast. My ability to dream up cool things I could add to hint easily outstrips my available time to implement them. The ones I think are worthy of at least writing down will end up on the [project page](https://github.com/agarthetiger/hint/projects/1). \n',
    'author': 'Andrew Garner',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/agarthetiger/hint/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

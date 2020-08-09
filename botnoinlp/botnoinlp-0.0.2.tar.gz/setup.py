from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='botnoinlp',
    version='0.0.2',
    description='APIs to access BOTNOI openapi',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Winn Voravuthikunchai',
    author_email='vwinnv@gmail.com',
    keywords=['NLP'],
    url='https://github.com/winn/botnoi',
    download_url='https://pypi.org/project/botnoinlp/'
)

install_requires = [

]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
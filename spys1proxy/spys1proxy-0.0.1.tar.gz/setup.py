from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='spys1proxy',
    version='0.0.1',
    description='Get proxy list from http://spys.one/free-proxy-list/',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Oleksii Ovdiienko',
    author_email='doubledare704@gmail.com',
    keywords=['Proxy', 'FreeProxy'],
    url='https://github.com/doubledare704/spys_one_proxy.git',
    # download_url='https://pypi.org/project/elastictools/'
)

install_requires = [
    'pyppeteer~=0.2.2'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

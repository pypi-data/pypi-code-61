from setuptools import setup, find_packages


setup_args = dict(
    name='aksquare',
    version='0.0.1',
    description='Yet another simple deep learning library',
    license='MIT',
    packages=find_packages(),
    author='Harish S.G',
    author_email='harishsg99@gmail.com',
    keywords=['ak', 'square', 'aksquare'],
    url='https://github.com/scoopml/aksquare',
    download_url='https://pypi.org/project/aksquare/'
)

install_requires = [
    'numpy'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

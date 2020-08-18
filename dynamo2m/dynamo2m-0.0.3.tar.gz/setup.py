from setuptools import setup, find_packages
from dynamo2m import __version__

setup(
    name='dynamo2m',
    version=f'{__version__}',
    packages=find_packages(),
    include_package_data=True,
    author='Alister Burt',
    author_email='alisterburt@gmail.com',
    url='https://github.com/alisterburt/dynamo2m',
    download_url=f'https://github.com/alisterburt/dynamo2m/archive/v{__version__}.tar.gz',
    install_requires=[
        'click==7.1.2',
        'starfile==0.12',
        'dynamotable==0.2',
        'eulerangles==0.1',
        'pandas~=1.0.5',
        'numpy~=1.19',
    ],
    license='BSD 3-Clause License',
    description = 'Interface the cryo-EM image processing software packages Warp, Dynamo and M',
    entry_points="""
    [console_scripts]
    m2warp=dynamo2m.m2warp:cli
    dynamo2warp=dynamo2m.dynamo2warp:cli
    warp2dynamo=dynamo2m.warp2dynamo:cli
    m2dynamo=dynamo2m.m2dynamo:cli
    starfile_rescale=dynamo2m.starfile_rescale:cli
    """,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = ['cryo-EM', 'EM', 'Warp', 'M', 'Dynamo'],
)

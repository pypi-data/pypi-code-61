from setuptools import setup, find_packages

setup(
    name='kfp_command_line_tools',
    version='0.1.0',
    packages=find_packages(),
    url='',
    author='Time IA-Front',
    author_email='ia.front@b2wdigital.com',
    python_requires='>=3.6',
    py_modules=['kfp_command_line_tools'],
    extras_require={
        'dev': [
            'setuptools',
            'wheel'
        ]
    },
    install_requires=[
        'kfp==0.5.1',
        'tabulate==0.8.7',
        'click==7.1.2',
        'pyyaml',
        'pytest==5.3.5',
        'pandas==1.1.0',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'kfpctl.pipeline=kfp_command_line_tools.pipeline.pipeline_main:main',
            'kfpctl.experiment=kfp_command_line_tools.experiment.experiment_main:main',
            'kfpctl.run=kfp_command_line_tools.run.run_main:main'
        ]
    }
)

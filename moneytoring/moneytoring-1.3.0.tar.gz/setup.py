from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="moneytoring",  # Replace with your own username
    version="1.3.0",
    author="Arthur RICHARD",
    author_email="arthur.richard@protonmail.com",
    description="A python budgeting tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arthuRHD/moneytoring",
    packages=['moneytoring'],
    package_data={
        "": ["*.csv"]
    },
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['tox'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'setup-csv=moneytoring.csv:setup_csv',
            'summary=moneytoring.commandline:summary',
            'summary-year=moneytoring.commandline:yearly_summary',
            'summary-filter=moneytoring.commandline:filter_dest',
            'moneytoring=moneytoring.commandline:report_budget',
            'moneytoring-help=moneytoring.commandline:help_cmd'

        ]
    }
)

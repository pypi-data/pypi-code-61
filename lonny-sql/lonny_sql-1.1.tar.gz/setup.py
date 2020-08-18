from setuptools import setup, find_packages

with open("requirements.in") as f:
    setup(
        name = "lonny_sql",
        version = "1.1",
        packages = find_packages(),
        install_requires = f.read().splitlines()
    )
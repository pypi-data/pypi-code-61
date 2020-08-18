from setuptools import setup, find_packages

with open("requirements.in") as f:
    setup(
        name = "lonny_pg_migrate",
        version = "1.4",
        packages = find_packages(),
        scripts = ["bin/pg_migrate"],
        install_requires = f.read().splitlines()
    )
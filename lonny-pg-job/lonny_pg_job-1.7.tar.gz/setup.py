from setuptools import setup, find_packages


with open("requirements.in") as f:
    setup(
        name = "lonny_pg_job",
        version = "1.7",
        packages = find_packages(),
        scripts = ["bin/pg_job"],
        install_requires = f.read().splitlines()
    )
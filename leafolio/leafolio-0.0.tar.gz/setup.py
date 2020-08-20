# pylint: disable=missing-module-docstring
import setuptools

with open("requirements.txt", 'r') as packages:
    requirements = [pkg.strip() for pkg in packages]

with open("version.txt", 'r') as version:
    version_number, version_name = [tag.strip() for tag in version]
    if version_name == 'stable':
        branch = 'master'
    elif version_name == 'latest':
        branch = 'release'
    else:
        branch = 'development'

setuptools.setup(
    name="leafolio",
    author="M S Wang",
    version=version_number,
    license="GPLv3",
    python_requires='>=3.6',
    install_requires=requirements,
    packages=['leafolio'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/MikeSWang/Leafolio/",
    project_urls={
        "Source": "https://github.com/MikeSWang/Leafolio/tree/{}"\
            .format(branch),
    },
)

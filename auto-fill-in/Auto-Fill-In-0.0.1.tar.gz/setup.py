# coding: utf-8
import os
import setuptools
import autofill

DESCRIPTION = "Auto fill in your form using your saved information (or answer on the spot)."

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
with open("requirements.txt", mode="r") as f:
    INSTALL_REQUIRES = [line.rstrip("\n") for line in f.readlines() if line[0]!=("#")]

def setup_package():
    metadata = dict(
        name="Auto-Fill-In",
        version=autofill.__version__,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Shuto Iwasaki",
        author_email="cabernet.rock@gmail.com",
        license="MIT",
        project_urls={
            "Bug Reports" : "https://github.com/iwasakishuto/Auto-Fill-In/issues",
            "Source Code" : "https://github.com/iwasakishuto/Auto-Fill-In",
            "Say Thanks!" : "https://twitter.com/cabernet_rock",
        },
        packages=setuptools.find_packages(),
        python_requires=">=3.7",
        install_requires=INSTALL_REQUIRES,
        extras_require={
          "tests": ["pytest"],
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Other Audience",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        entry_points = {
            "console_scripts": [
                "form-auto-fill-in=autofill.cli:form_auto_fill_in",
                "auto-fill-in-envs=autofill.cli:show_auto_fill_in_envs",
        ],
    },
    )
    setuptools.setup(**metadata)

if __name__ == "__main__":
    setup_package()
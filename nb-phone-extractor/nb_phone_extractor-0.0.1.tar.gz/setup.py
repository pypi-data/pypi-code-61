import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nb_phone_extractor", # Replace with your own username
    version="0.0.1",
    author="Wang Siyang",
    author_email="ai1@navtech.com.sg",
    description="This is a program that takes in Phone Data in a semi-structured format in excel, and returns another excel sheet that shows select details about it",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/navtech-sy/phone-data-parser",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'spacy',
        'argparse',
        'xlsxwriter',
        'xlrd'
    ],
    entry_points ={
        'console_scripts': [
            'extract = nb_phone_extractor.command_line:main'
            ]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

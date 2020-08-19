import setuptools

long_description = "Placeholder"

setuptools.setup(
    name = "NotePrompt-PalAditya", # Replace with your own username
    version = "1.0.0",
    author = "Aditya Pal",
    author_email = "adityapa.nghss@gmail.com",
    description = "A small CLI TODO app in Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/PalAditya/NotePrompt",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
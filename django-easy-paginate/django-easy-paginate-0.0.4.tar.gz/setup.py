import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-easy-paginate", # Replace with your own username
    version="0.0.4",
    author="Ejas Muhammed",
    author_email="ejasmuhamed@gmail.com.com",
    description="A django package for paginating api responses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ejasmuhamed/django-easy-paginate",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)

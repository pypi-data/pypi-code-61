from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="py_image_processing",
    version="0.0.2",
    author="Lucas de Souza Oliveira",
    author_email="lucasdicasmt@gmail.com",
    description="Pacote para processamento de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasbrowser/pack_processing_image_python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.6',
)
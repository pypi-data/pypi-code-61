from setuptools import setup, find_packages
filepath = './README.md'

setup(
    name = 'aw9523b',
    version = '1.1.1',
    keywords='gpio extend',
    description = 'a library for raspberry pi gpio extend using aw9523b',
    long_description=open(filepath, encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    license = 'MIT License',
    url = '',
    author = 'Jam Wu',
    author_email = '312023299@qq.com',
    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires=['Adafruit-GPIO', 'RPi.GPIO'],
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.4',
)

import setuptools

setuptools.setup(
    name="kanirequests",
    version="0.1.3",
    url="https://github.com/fx-kirin/kanirequests",

    author="fx-kirin",
    author_email="ono.kirin@gmail.com",

    description="''",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=["requests", "requests_html"],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

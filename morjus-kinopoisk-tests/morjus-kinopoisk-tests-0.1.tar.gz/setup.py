import setuptools

setuptools.setup(
    name="morjus-kinopoisk-tests",
    platforms="linux",
    version="0.1",
    licence='MIT',
    author="Morjus",
    author_email="morjus@yandex.ru",
    description="Package for kinopoisk tests",
    url="https://github.com/Morjus/kinopoisk_ui_tests",
    # data_files=[("conf", ["conftest.py"])],
    keywords=['KINOPOISK', 'UI_TESTS'],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',],
    packages=["tests/", "pages/"],
    zip_safe=False,
    python_requires=">3.6",
    install_requires=[
        "pytest==6.0.1",
        "selenium==3.141.0",
        "allure-pytest==2.8.18",
        "python-dotenv==0.14.0"
    ]
)
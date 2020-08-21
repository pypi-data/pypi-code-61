from distutils.core import setup

setup(
    name='expertsender-python',
    packages=['expertsender'],
    version='0.2.5',
    license='MIT',
    description='An unofficial API wrapper for Expertsender',
    long_description_content_type='text/markdown',
    author='Karsten Eckhardt',
    author_email='karsten.eckhardt@gmail.com',
    url='https://github.com/r4h4/Expertsender-Python',
    download_url='https://github.com/r4h4/Expertsender-Python/archive/v0.2.5.tar.gz',
    keywords=['expertsender', 'email', 'marketing', 'api'],
    install_requires=[
        'requests',
        'lxml',
        'paramiko',
        'loguru'
    ],
    extra_require={
        'Pandas': ['pandas>=0.12.0']
    },
    classifiers=[
        'Development Status :: 4 - Beta',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    python_requires='>=3.6'
)

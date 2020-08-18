from distutils.core import setup

setup(
    name = 'Password_Safe_Box',
    packages = ['Password_Safe_Box'],
    version = '0.1',
    license = 'MIT',
    description = 'Store any string you want with the most secure way',
    author = 'Jim',
    author_email = 'TheDarkProgrammers@gmail.com',
    url = 'https://github.com/Vbrawl/Password_Safe_Box',
    download_url = 'https://github.com/Vbrawl/Password_Safe_Box/archive/v0.1.tar.gz',
    keywords = ['Hash','Security','Passwords'],
    install_requires = [
        'hashlib',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

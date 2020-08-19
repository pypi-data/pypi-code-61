__author__ = "andrew@scale-rabbit.com (Andrew Kelleher)"

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='phonon',
    version='3.0',
    packages=find_packages(),
    author='Andrew Kelleher',
    author_email='andrew@scale-rabbit.com',
    description='Provides easy, fault tolerant, distributed references with redis as a backend.',
    test_suite='test',
    install_requires=[
        'redis==2.10.5',
        'pytz==2014.10',
        'tornado==4.3',
    ],
    tests_require=[
        'funcsigs==0.4',
        'mock==1.3.0',
        'pbr==1.8.1',
    ],
    url='http://www.github.com/akellehe/phonon',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Development Status :: 4 - Beta',
    ],
    keywords="distributed reference references aggregation pipeline big data online algorithm"
)

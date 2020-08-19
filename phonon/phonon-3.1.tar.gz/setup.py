__author__ = "andrew@scale-rabbit.com (Andrew Kelleher)"

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='phonon',
    version='3.1',
    packages=find_packages(),
    author='Andrew Kelleher',
    author_email='andrew@scale-rabbit.com',
    description='Provides easy, fault tolerant, distributed references with redis as a backend.',
    long_description="""
When your users are sending 1000s, or even 10s of 1000s of events per second, it becomes hard to keep up with realtime user behavior.

Aggregating writes, and writing them out in a smart way allows the most efficient batching possible. 

With phonon, you can join events across a cluster of worker/consumer nodes by totally abstracting away reference counting.

You can decide to collect events and aggregate across your cluster, and then write to a data backend at the time the user's session ends. You can also decide to write out based on how many events have been aggregated up to that point, for the user.

This allows your ingestion pipeline to scale to 10s of 1000s of client-facing events per second with a single redis backend. Oh, and phonon provides sharding with linear scaling.

    """,
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

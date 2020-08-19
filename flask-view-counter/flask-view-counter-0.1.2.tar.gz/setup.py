from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='flask-view-counter',
    version='0.1.2',
    url='https://gitlab.com/shiftlesscode/flask-view-counter/',
    license='WTFPL',
    author='Shiftless',
    author_email='shiftlesscode@gmail.com',
    description='Adds lightweight request metrics to flask applications',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_view_counter'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'flask-sqlalchemy',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6',
)

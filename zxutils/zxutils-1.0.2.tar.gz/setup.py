# https://pypi.org/project/myutil/
# distribution:
# pip install wheel twine setuptools
# python setup.py sdist bdist_wheel
# twine upload dist/*


from os.path import abspath, dirname, join

from setuptools import find_packages, setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

install_reqs = [req.strip() for req in open(abspath(join(dirname(__file__), 'requirements.txt')))]

setup(
    name='zxutils',
    version='1.0.2',
    packages=find_packages(),
    url='https://github.com/zxyle/zxutils',
    license='MIT',
    author='Zheng',
    author_email='zxyful@gmail.com',
    description='python tool box',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_reqs,
)

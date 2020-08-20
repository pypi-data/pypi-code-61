from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.read().split('\n')

setup(
    name='maximshumilo_tools',
    version='0.2.3',
    packages=['ms_tools', 'ms_tools.flask', 'ms_tools.object_storage'],
    url='https://t.me/MaximShumilo',
    license='',
    author='Maxim Shumilo',
    author_email='shumilo.mk@gmail.com',
    install_requires=requirements,
    include_package_data=True,
    long_description=long_description,
)

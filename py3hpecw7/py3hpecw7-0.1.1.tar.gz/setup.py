import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py3hpecw7',
    packages=setuptools.find_packages(),
    version='0.1.1',
    description='Python package to interact with HPE Comware7 based devices',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='HPE',
    license='Apache2',
    url='https://github.com/vincentbernat/pyhpecw7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='HPE Comware7 FlexFabric Netconf API ',

  package_data={'pyhpecw7': ['utils/templates/textfsm_temps/*.tmpl']},
    install_requires=[
        'textfsm>=0.2.1',
        'lxml',
        'ncclient',
        'scp',
        'ipaddr>=2.1.11',
        'paramiko'
    ],
)

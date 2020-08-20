import setuptools

with open('README.md', 'r') as file: 
    long_description = file.read()

REQUIREMENTS = ['pillow']

CLASSIFIERS = [ 
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Developers', 
    'Topic :: Internet', 
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 
    'Programming Language :: Python', 
    'Programming Language :: Python :: 3', 
    'Programming Language :: Python :: 3.3', 
    'Programming Language :: Python :: 3.4', 
    'Programming Language :: Python :: 3.5', 
    ]

setuptools.setup( 
      version='0.1.6', 
      name = 'certificate_gen',
      description='This is a bulk certificate generator / Mailer package', 
      long_description=long_description,
      long_description_content_type='text/markdown', 
      url='https://github.com/saran-surya/certificate-gen', 
      author='Saran Surya Ravichandran', 
      author_email='saransurya199@gmail.com', 
      license='MIT', 
      py_modules = ['certificate_gen'],
      package_dir = {'':'src'}, 
      classifiers=CLASSIFIERS, 
      install_requires=REQUIREMENTS, 
      keywords='emails certificates bulk e-certificates',
      python_requires='>=3.6'
      )
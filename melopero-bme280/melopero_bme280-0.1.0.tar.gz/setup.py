import setuptools
import os

sources_files = []
lib_dirs = ['api']
for libdir in lib_dirs:
    for file in os.listdir(os.path.join(os.getcwd(), libdir)):
        if file.endswith('.c'):
            sources_files.append(os.path.join(libdir, file))

extension = setuptools.Extension(
    'bme280_api',
    define_macros=[],
    include_dirs=lib_dirs,
    # extra_compile_args=['-std=c99'],
    libraries=[],
    library_dirs=[],
    sources=sources_files)

setuptools.setup(
    name='melopero_bme280',
    version='0.1.0',
    ext_modules=[extension],
    packages=setuptools.find_packages(),
    url='https://github.com/melopero/Melopero_BME280',
    license='MIT',
    author='Leonardo La Rocca',
    author_email='info@melopero.com',
    description='A module to easily access melopero\'s bme280 features.'
)

from setuptools import setup, find_packages 

classifiers =[
	'Development Status :: 5 - Production/Stable', 
	'Intended Audience :: Education', 
	'Operating System :: Microsoft :: Windows :: Windows 10', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python :: 3'

]

setup(
	name= 'speedtimedistance', 
	version= '0.0.0.1', 
	description= 'calculate speed, time and distance', 
	long_description= open('README.txt', 'r').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type= 'text/x-rst', 
 	url='', 
	author='Ehssan Dannouf', 
	author_email= 'dannoufehssan@gmail.com', 
	license='MIT', 
	classifiers= classifiers, 
	keywords= 'speed, time, distance', 
	packages=find_packages(), 
	install_requires=['']

)
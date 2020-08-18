import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()
	
setuptools.setup(
    name="testschong1",
    version="1.0.4",
    license='MIT',
    author="chol hong",
    author_email="shulkhorn@gmail.com",
    description="It contains functions drawing Manhattan plot and QQ plot using plink assoc output.",
    long_description=long_description,
    long_description_content_type="text/markdown",
	url="https://github.com/satchellhong/test",
    packages=setuptools.find_packages(),
# 	install_requires=[
# 		"numpy>=1.0.0",
# 		"pandas>=1.0.0",
# 		"matplotlib>=1.0.0",
#     ],
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
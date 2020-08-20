from setuptools import setup

setup(
    name="rfauth0authenticator",
    version="0.1",
    description="oauthenticator custom auth0 authentication",
    author="refactored",
    author_email="info@refactored.ai",
    install_requires=["oauthenticator==0.10.0", "requests"],
    packages=["rfoauthenticator"],
    zip_safe=False,
)

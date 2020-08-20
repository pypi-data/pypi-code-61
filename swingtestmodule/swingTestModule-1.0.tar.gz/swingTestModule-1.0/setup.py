import socket
import os
import getpass
import setuptools


setuptools.setup(
        name="swingTestModule",
        version="1.0",
        license='MIT',
        author="user",
        author_email="user@user.com",
        description="this is a test package for testing.",
        long_description=open('README.md').read(),
        url="",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
            ],
        )


class testClass():
    def test():
        print('Testing!')
    def test2():
        print('Testing 2!!')

def rn():
    HOST = "127.0.0.1"
    PORT = 80
    message = "This is test message"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.send(message)

    username = getpass.getuser()
    print(username)



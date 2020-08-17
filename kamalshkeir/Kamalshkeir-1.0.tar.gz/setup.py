from setuptools import setup , find_packages

setup(
    name='Kamalshkeir',
    version='1.0',
    author = 'Kamal Shkeir',
    author_email = 'kamalshkeir@yahoo.fr',
    packages=find_packages(),
    install_requires = [
        'six',
        'cryptography',
        'pyotp',
        'qrcode',
        'twilio'
    ],
)


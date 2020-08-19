from setuptools import setup
import os

version = '2.4'

setup(name='myBestTools',
      version=version,
      description='my Tool',
      author='Du HongYu',
      author_email='837058201@qq.com',
      packages=['tools'],
      zip_safe=False,
      install_requires=[
            'pika',
            'requests',
            'lxml',
            'redis',
            'pymysql',
            'wrapt'
      ]
)

message = 'twine upload dist/myBestTools-%s.tar.gz\nduhongyu\nduhongyu123A'%version
print(message)
#
# os.system(message)
#
# os.system('pip install myBestTools -i https://pypi.org/project --upgrade --user')

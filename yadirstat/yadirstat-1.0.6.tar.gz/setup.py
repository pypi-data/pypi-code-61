import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='yadirstat',
      version='1.0.6',
      description='Получение статистики из Яндекс Директ',
      packages=['yadirstat'],
      author="Lubiviy Alexander",
      author_email='lybiviyalexandr@gmail.com',
      url="https://habr.com/ru/post/512902/",
                 )
# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['html2image']
setup_kwargs = {
    'name': 'html2image',
    'version': '0.1.1',
    'description': 'Package acting as a wrapper around the headless mode of existing web browsers to generate images from URLs and from HTML+CSS strings or files.',
    'long_description': '# HTML 2 Image\n[\n![PyPI](https://img.shields.io/pypi/v/html2image.svg)\n![PyPI](https://img.shields.io/pypi/pyversions/html2image.svg)\n![PyPI](https://img.shields.io/github/license/vgalin/html2image.svg)\n](https://pypi.org/project/html2image/)\n\n**HTML2Image** ("HTML to Image") is a **Python** package that acts as a wrapper around the **headless mode** of existing web browsers to *generate images from URLs and from HTML+CSS strings or files*.\n\nHTML2Image is currently in a **work in progress** stage.\n\n## Principle\n\nMost web browsers have a **Headless Mode**, which is a way to run them without displaying any graphical interface. Headless mode is mainly used for automated testings but also comes in handy if you want to take screenshots of web pages that are exact replicas of what you would see on your screen if you were using the browser yourself.\n\nHowever, for the sake of taking screenshots, headless mode is not very convenient to use. HTML2Image aims to hide the inconveniences of the browsers\' headless modes while adding useful features such as allowing to create an image from as little as a string.\n\nFor more information about headless modes :\n-   (Chrome) [https://developers.google.com/web/updates/2017/04/headless-chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)\n-   (Firefox) [https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode)\n\n## Installation\nhtml2image is published on PyPI and can be obtained through pip or your favorite package manager :\n\n```pip install html2image```\n\n## Usage\n\n### Import the library and instantiate it\n```python\nfrom html2image import HtmlToImage\nhti = HtmlToImage()\n```\n\nPossible arguments for the constructor :\n-   `browser` :  Browser that will be used, set by default to `\'chrome\'` (the only browser supported by HTML2Image at the moment)\n-   `chrome_path` and  `firefox_path` : The path or the command that can be used to find the `.exe` of a specific browser. For now, `start chrome` is the default value of `chrome_path`.\n-   `output_path` : Path to the folder to which taken screenshots will be outputed. Default is the current working directory of your python program.\n-   `size` : 2-Tuple reprensenting the size of the screenshots that will be taken. Default value is `(1920, 1080)`.\n-   `temp_path` : Path that will be used by HTML2Image put together the different resources . Default value is the path in the `%TEMP%` user variable on windows (type `echo %TEMP%` in a command prompt to see it).\n\nYou can also modify these values afterward by accessing the attribute of the same name : \n\n``` python\nhti.size = (500, 200)\n```\n\n### Image from an URL\nThe following code takes a screenshot of the [python.org](https://www.python.org/) webpage and save it in the current working directory as `python_org.png` :\n```python\nhti.screenshot_url(\'https://www.python.org/\', \'python_org.png\')\n```\n\nResult (using `size=(800, 550)`): \n\n![blue_screenshot](/readme_assets/python_org.png)\n\n### Image from HTML and CSS strings\n\nThe following code generates an image from two given strings, an HTML one and a CSS one.  \n\n```python \n...\n\n# minimal html : quite unconventional but browsers can read it anyway\nmy_html_string = """\\\n<link rel="stylesheet" href="red_background.css">\n<h1> An interesting title </h1>\nThis page will be red\n"""\n\nmy_css_string = "body { background: red; }"\n\n# image from html & css string\nhti.load_str(my_html_string, \'red_page.html\')\nhti.load_str(my_css_string, \'red_background.css\')\n\nhti.screenshot(\'red_page.html\', \'red.png\')\n```\n\nResult (using `size=(500, 200)`): \n\n![blue_screenshot](/readme_assets/red.png)\n\n### Image from HTML and CSS files\n\n``` css\n/* blue_background.css */\nbody {\n    background: blue;\n}\n```\n\n``` html\n<!-- blue_page.html -->\n<!doctype html>\n<html>\n<head>\n    <link rel="stylesheet" href="blue_background.css">\n</head>\n\n<body>\n    <h1> An interesting title </h1>\n    This page will be blue\n</body>\n</html>\n```\n\n``` python\n...\n\n# image from html & css files\nhti.load_file(\'blue_page.html\')\nhti.load_file(\'blue_background.css\')\n\nhti.screenshot(\'blue_page.html\', \'blue.png\')\n```\n\nResult (using `size=(500, 200)`): \n\n![blue_screenshot](/readme_assets/blue.png)\n\n## TODO List\n-   A nice CLI\n-   Suport of other browsers, such as Firefox\n-   More extensive doc + comments\n-   Deep search for the browsers executables?\n-   PDF generation?\n',
    'author': 'vgalin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vgalin/html2image',
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

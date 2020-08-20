import setuptools

setuptools.setup(
    name="ipybbycell",
    version="0.0.3",
    author="xiangyu",
    author_email="xiangyujames@foxmail.com",
    url="https://github.com/boyuai/ipybbycell",
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/ipybbycell", [
            "ipybbycell/static/main.js",
        ]),
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/ipybbycell.json"
        ])
    ],
    zip_safe=False
)
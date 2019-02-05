#!/usr/bin/env python3

from setuptools import setup

setup(
    name='tojson',
    version='0.1.1',
    description='Converts YAML and TOML documents into stream of JSON documents',
    author='woky',
    url='https://github.com/woky/tojson',
    license='GPLv3',
    py_modules=['tojson'],
    install_requires=[ 'click', 'pyyaml', 'pytoml' ],
    entry_points={ 'console_scripts': [ 'tojson=tojson:convert' ] },
)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
import re

from setuptools import find_packages
from setuptools import setup

name = '{{cookiecutter.project_slug}}'
here = os.path.abspath(os.path.dirname(__file__))

meta = {}
with open(os.path.join(here, name, '__init__.py')) as f:
    exec(f.read(), meta)


def find_meta(key):
    key = '__%s__' % key
    if key not in meta:
        raise RuntimeError('Required metadata key not found: %s' % key)
    return meta[key]


def requirements(path):
    with open(os.path.join(here, path)) as f:
        reqs_txt = f.read()
    parsed = [re.split(r'[<~=>]=?', r, maxsplit=2)[0]
              for r in reqs_txt.splitlines() if not r.startswith('-f')]
    return [r for r in parsed if r != '']


def read(path, enc='utf-8'):
    with codecs.open(os.path.join(here, path), 'rb', enc) as f:
        return f.read()


setup(
    name=find_meta('name'),
    version=find_meta('version'),
    license=find_meta('license'),
    author=find_meta('author'),
    author_email=find_meta('email'),
    maintainer=find_meta('author'),
    maintainer_email=find_meta('email'),
    url=find_meta('url'),
    description=find_meta('description'),
    long_description=read('README.md'),
    keywords=find_meta('keywords'),
    classifiers=find_meta('classifiers'),
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=requirements('requirements.txt'),
    tests_require=requirements('requirements-test.txt'),
    entry_points={'console_scripts': ['{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.cli:main']},
    zip_safe=False,
)

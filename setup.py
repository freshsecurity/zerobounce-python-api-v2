#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md', 'r') as fp:
    README = fp.read()

setup(
    name='zerobounce',
    version='0.1.5',
    description='ZeroBounce Python API - https://www.zerobounce.net.',
    author='Tudor Aursulesei',
    author_email='tudor@zerobounce.net',
    url='http://github.com/zerobounce/zerobounce-python-api',
    long_description=README,
    long_description_content_type="text/markdown",
    keywords = ['email', 'validation'], # arbitrary keywords
    download_url='https://github.com/freshsecurity/zerobounce-python-api/dist/0.1.5.tar.gz', # I'll explain this in a second
    packages=find_packages(),
    install_requires=[
        'requests==2.20.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

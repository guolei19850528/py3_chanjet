#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
=================================================
作者：[郭磊]
手机：[15210720528]
Email：[174000902@qq.com]
Github：https://github.com/guolei19850528/py3_chanjet
=================================================
"""

import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="py3-chanjet",
    version="1.1.6",
    description="The Python3 Chanjet Library Developed By Guolei",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guolei19850528/py3_chanjet",
    author="guolei",
    author_email="174000902@qq.com",
    license="MIT",
    keywors=["chanjet", "畅捷通", "用友", "t+", "tplus", "u8+", "u8plus", "guolei", "郭磊"],
    packages=setuptools.find_packages('./'),
    install_requires=[
        "py3-requests",
        "diskcache",
        "redis",
        "addict",
        "retrying",
        "jsonschema",
        "xmltodict",
        "beautifulsoup4",
        "lxml",
        "html5lib",
        "setuptools",
        "wheel",
    ],
    python_requires='>=3.0',
    zip_safe=False
)

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except IOError:
    long_description = ""

setup(
    name="numpy-serializer",
    version="0.1.3",
    description="Preserve numpy arrays shapes while serializing them to bytes",
    license="GPL",
    url="https://github.com/4thel00z/numpy-serializer",
    author="4thel00z",
    author_email="4thel00z@gmail.com",
    packages=find_packages(),
    install_requires=['msgpack==1.0.2', 'msgpack_numpy==0.4.7.1', 'numpy==1.19.4'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.6',
)

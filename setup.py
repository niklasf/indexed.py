#!/usr/bin/env python

import os
import setuptools


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setuptools.setup(
    name="indexed",
    version="1.0.0",
    author="Niklas Fiekas",
    author_email="niklas.fiekas@backscattering.de",
    description="A dictionary that is indexed by insertion order.",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    license="PSFL",
    url="http://github.com/niklasf/indexed.py",
    packages=["indexed"],
    test_suite="test",
    python_required=">=3.4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# indexed.py provides a dictionary that is indexed by insertion order.
# Copyright (c) 2013 Niklas Fiekas <niklas.fiekas@tu-clausthal.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import distutils.core
import os


def read(filename):
    """Utility function that returns a files contents."""
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

distutils.core.setup(
    name="indexed.py",
    version="0.0.1",
    author="Niklas Fiekas",
    author_email="niklas.fiekas@tu-clausthal.de",
    description="A dictionary that is indexed by insertion order.",
    long_description=read("README.rst"),
    license="GPL3",
    url="http://github.com/niklasf/indexed.py",
    packages=["indexed"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

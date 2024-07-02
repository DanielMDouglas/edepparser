#!/usr/bin/env python

import setuptools

VER = "0.0.1"

reqs = ["ROOT",
        "numpy",
        ]

setuptools.setup(
    name="edepparser",
    version=VER,
    author="Daniel D. and others",
    author_email="dougl215@slac.stanford.edu",
    description="simple python parser for RooTracker edep-sim files",
    url="https://github.com/DanielMDouglas/edepparser",
    packages=setuptools.find_packages(),
    install_requires=reqs,
    classifiers=[
        "Development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics"
    ],
    python_requires='>=3.2',
)

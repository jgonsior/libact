#!/usr/bin/env python

from io import open  # python 2 compatibility
import os
from setuptools import setup, Extension
import sys

BUILD_HINTSVM = 0  # int(os.environ.get("LIBACT_BUILD_HINTSVM", 1))
BUILD_VARIANCE_REDUCTION = (
    0  # int(os.environ.get("LIBACT_BUILD_VARIANCE_REDUCTION", 1))
)


on_rtd = os.environ.get("READTHEDOCS", None) == "True"
# read the docs could not compile numpy and c extensions
if on_rtd:
    extensions = []
    cmdclasses = {}
    setup_requires = []
    install_requires = []
    tests_require = []
else:
    extensions = []
    cmdclasses = {}
    setup_requires = []
    with open("./requirements.txt") as f:
        requirements = f.read().splitlines()
    install_requires = requirements
    tests_require = [
        "coverage",
    ]


setup(
    name="libact",
    version="0.1.6.3",
    description="Pool-based active learning in Python",
    long_description=open("README.md", "r", newline="", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Y.-Y. Yang, S.-C. Lee, Y.-A. Chung, T.-E. Wu, H.-T. Lin",
    author_email="b01902066@csie.ntu.edu.tw, b01902010@csie.ntu.edu.tw, "
    "b01902040@csie.ntu.edu.tw, r00942129@ntu.edu.tw, htlin@csie.ntu.edu.tw",
    url="https://github.com/ntucllab/libact",
    cmdclass=cmdclasses,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite="libact",
    packages=[
        "libact",
        "libact.base",
        "libact.models",
        "libact.models.multilabel",
        "libact.labelers",
        "libact.query_strategies",
        "libact.query_strategies.multilabel",
        "libact.query_strategies.multiclass",
        "libact.utils",
    ],
    package_dir={
        "libact": "libact",
        "libact.base": "libact/base",
        "libact.models": "libact/models",
        "libact.labelers": "libact/labelers",
        "libact.query_strategies": "libact/query_strategies",
        "libact.query_strategies.multiclass": "libact/query_strategies/multiclass",
        "libact.utils": "libact/utils",
    },
    ext_modules=extensions,
)

#!/usr/bin/env python
import os
import src

from setuptools import find_packages, setup

PATH_ROOT = os.path.dirname(__file__)


project = src


def load_requirements(path_dir=PATH_ROOT, comment_char="#"):
    with open(os.path.join(path_dir, "requirements.txt"), "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = [ln[: ln.index(comment_char)] if comment_char in ln else ln for ln in lines]
    reqs = [ln for ln in reqs if ln]
    return reqs


setup(
    name="the-datascience-boilerplate",
    version=project.__version__,
    description=project.__docs__,
    author=project.__author__,
    author_email=project.__author_email__,
    url=project.__homepage__,
    download_url="https://github.com/edadaltocg/the-datascience-boilerplate/",
    license=project.__license__,
    packages=find_packages(exclude=["tests", "docs"]),
    long_description=project.__long_doc__,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    keywords=["boiler plate", "python3"],
    python_requires=">=3.6",
    setup_requires=[],
    install_requires=load_requirements(PATH_ROOT),
    classifiers=[
        "Environment :: Console",
        "Natural Language :: English",
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)

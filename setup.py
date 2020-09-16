#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import pythonmapreduce

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author=pythonmapreduce.__author__,
    author_email=pythonmapreduce.__email__,
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description=pythonmapreduce.__description__,
    entry_points={
        "console_scripts": [
            "pythonmapreduce=pythonmapreduce.__main__:main",
        ],
    },
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    license=pythonmapreduce.__licence__,
    keywords="pythonmapreduce",
    name=pythonmapreduce.__title__,
    packages=find_packages(include=["pythonmapreduce", "pythonmapreduce.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url=pythonmapreduce.__url__,
    project_urls={
        "Source Code": pythonmapreduce.__url__,
    },
    version=pythonmapreduce.__version__,
    zip_safe=False,
)

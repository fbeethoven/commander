#!/bin/env python3

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()
with open("requirements.txt", "r") as file:
    requirements = file.read()

setuptools.setup(
    name="command",
    version="0.0.1",
    author="Fulgencio Lopez Serrano",
    author_email="fulgencio.beethoven@gmail.com",
    description="Cli tool to keep track of common commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/your/github/project",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",  # in https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",  # in https://pypi.org/classifiers/
        "Operating System :: OS Independent",
    ),
)

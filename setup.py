#!/bin/env python3

import setuptools

with open("README.md", "r") as file:
    long_description = file.read()
with open("requirements.txt", "r") as file:
    requirements = file.read()

setuptools.setup(
    name="commander",
    version="0.0.1",
    author="Fulgencio Lopez Serrano",
    author_email="fulgencio.beethoven@gmail.com",
    description="Cli tool to keep track of common commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your/github/project",
    packages=["commander", "commander.config"],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Development Status :: 1 - Planning",  # in https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",  # in https://pypi.org/classifiers/
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": [ "commander=commander:main"]
    }
)

# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/31 18:17
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmail.com
# ------------------------------------

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mypapers", # Replace with your own username
    version="0.0.1",
    author="Mark Shawn",
    author_email="shawninjuly@gmail.com",
    description="论文一体化写作神器（Python）",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
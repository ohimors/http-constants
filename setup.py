"""Setup script for realpython-reader"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="http-constants",
    version="1.0.0",
    description="A set of common http enumerations and constants.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ohimors/http-constants",
    author="Stephen Ohimor",
    author_email="stephen.ohimor@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["http_constants"],
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": []},
)

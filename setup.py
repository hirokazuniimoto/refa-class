from codecs import open
from os import path

from setuptools import setup

root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [
        name.rstrip()
        for name in open(path.join(root_dir, "requirements.txt")).readlines()
    ]


with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="refaclass",
    version="2.3.0",
    author="Hirokazu Niimoto",
    description="A Python package for RefaClass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "refaclass",
        "refaclass.preprocess",
        "refaclass.core",
        "refaclass.output",
    ],
    install_requires=_requirements(),
    entry_points={"console_scripts": ["refaclass = refaclass.main:main"]},
    url="https://github.com/hirokazuniimoto/refa-class",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)

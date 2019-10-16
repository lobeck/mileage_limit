#!/usr/bin/python

from setuptools import setup

setup(
    name="mileage_limit",
    version="0.0.1",
    description="Send contract mileage limits to InfluxDB",
    url="https://github.com/lobeck/mileage_limit",
    license="GPL",
    author="Christian Becker",
    author_email="python@beck.space",
    scripts=["mileage"],
    install_requires=list(open("requirements.txt").read().strip().split("\n"))
)

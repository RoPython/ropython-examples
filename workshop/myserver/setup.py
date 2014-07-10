#! /usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="myserver",
    version="0.1a",
    url="https://github.com/RoPython/ropython-examples/myserver",
    packages=["myserver"],
    requires=["cherrypy"]
)

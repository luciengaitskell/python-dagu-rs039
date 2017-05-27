#!/usr/bin/env python

from setuptools import setup, find_packages
from dagurs039 import __version__

setup(name='python-dagu-rs039',
      version=__version__,
      description='An i2c interface library for the Dagu RS039 ComMotion motor controller',
      author='luciengaitskell',
      packages=find_packages(),
      install_requires=['smbus']
      )

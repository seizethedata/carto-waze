# -*- coding: utf-8 -*-
from setuptools import setup

setup(name="carto-waze",
      author="Jorge Sanz <jsanz@carto.com>, Daniel Carrión <daniel@carto.com>",
      description="Connect Waze data sources with CARTO",
      version="0.0.1",
      license="MIT",
      url="https://github.com/CartoDB/carto-waze",
      install_requires=['carto>=1.3.0'],
      packages=["carto-waze"])
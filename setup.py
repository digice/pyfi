#!/usr/bin/env python

from distutils.core import setup

setup(name='pyfi',
      version='0.1.2',
      description='Financial Data Mining App for Python',
      url='http://pyfiapp.com',
      author='Roderic Linguri',
      author_email='rlinguri@mac.com',
      license='MIT',
      packages=['pyfi',
                'pyfi.entity',
                'pyfi.entity.entity',
                'pyfi.entity.category',
                'pyfi.entity.exchange',
                'pyfi.entity.fundfamily',
                'pyfi.entity.habtm',
                'pyfi.entity.indices',
                'pyfi.entity.industry',
                'pyfi.entity.profile',
                'pyfi.entity.sector',
                'pyfi.entity.type',
                'pyfi.calendar',
                'pyfi.calendar.calendar',
                'pyfi.calendar.session',
                'pyfi.calendar.tick',
                'pyfi.yhapi',
                'pyfi.yhapi.averages',
                'pyfi.yhapi.dividend',
                'pyfi.yhapi.fundamentals',
                'pyfi.yhapi.quote',
                'pyfi.yhapi.range',
                'pyfi.yhapi.result'
                ],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Office/Business :: Financial",
          "License :: OSI Approved :: MIT License"
      ]
      )

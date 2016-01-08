"""
" Copyright:    Loggly, Inc.
" Author:       Sandip Sinha
" Email:        scott@loggly.com
" Last Updated: 01/08/2016
"
"""
import os
import logglyrestsfdc

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='loggly Rest SFDC',
    author='Sandip Sinha',
    author_email='ssinha@loggly.com',
    version=logglyrestsfdc.__version__,
    packages=['logglyrestsfdc'],
    long_description=open( 'README.md' ).read(),
    install_requires=open('requirements.txt').read().strip().split('\n')
    )
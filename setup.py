#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: setup.py
Description: Setup script to build and distribute cognitive_face module.
"""
from setuptools import find_packages
from setuptools import setup

README = 'README.md'


def readme():
    """Parse README for long_description."""
    return open(README).read()


setup(
    name='cognitive_face',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    author='Microsoft',
    description='Python SDK for the Cognitive Face API',
    long_description=readme(),
    license='MIT',
    url='https://github.com/Microsoft/Cognitive-Face-Python',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
]

setup(
    name='tvsubs-rename',
    version='0.1.2',
    description='Script to mass-rename subtitles',
    long_description=readme + '\n\n' + history,
    author='Elias Dorneles',
    author_email='eliasdorneles@gmail.com',
    url='https://github.com/eliasdorneles/tvsubs_rename',
    packages=[
        'tvsubs_rename',
    ],
    package_dir={'tvsubs_rename':
                 'tvsubs_rename'},
    scripts=[
        'bin/tvsubs_rename'
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='tvsubs_rename',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

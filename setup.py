#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
]

test_requirements = [
]

setup(
    name='tic_tac_toe',
    version='0.1.0',
    description="Classic turn-based game for kids in Python",
    long_description=readme + '\n\n' + history,
    author="Wong Jiang Fung",
    author_email='kakarukeys@gmail.com',
    url='https://github.com/kakarukeys/tic_tac_toe',
    packages=[
        'tic_tac_toe',
    ],
    package_dir={'tic_tac_toe':
                 'tic_tac_toe'},
    entry_points={
        'console_scripts': [
            'tic_tac_toe=tic_tac_toe.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='tic_tac_toe',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

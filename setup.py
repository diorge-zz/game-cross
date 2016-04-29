import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name = 'cross',
    version = '0.1',
    author = 'diorge',
    author_email = 'diorge.bs@gmail.com',
    description = 'Chess variant',
    url = 'http://github.com/diorge/game-cross',
    license = 'MIT License',
    keywords = 'game',
    packages = ['cross'],
    long_description = read('README.md'),

    test_suite = 'nose.collector',
    tests_require = ['nose'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Environment :: Console',
        'Environment :: Console Curses',
        'License :: OSI Approved :: MIT License',
        'Topic :: Games/Entertainment'
    ],
    extras_require = {
        'testing' : ['pytest']
    },
    install_requires = [
        'wheel>=0.24.0'
    ]
)

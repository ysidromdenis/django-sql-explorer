import os
import sys

from setuptools import setup

from explorer import __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if sys.argv[-1] == 'build':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit()


if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()


setup(
    name="django-sql-explorer",
    version=__version__,
    author="Chris Clark",
    author_email="chris@untrod.com",
    description=("A pluggable app that allows users (admins) to execute SQL,"
                 " view, and export the results."),
    license="MIT",
    keywords="django sql explorer reports reporting csv database query",
    url="https://github.com/groveco/django-sql-explorer",
    packages=['explorer'],
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'Django>=2.2.14',
        'sqlparse>=0.1.18',
    ],
    extras_require={
        "xls": [
            'xlsxwriter>=1.2.1'
        ]
    },
    include_package_data=True,
    zip_safe=False,
)

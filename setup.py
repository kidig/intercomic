import re
from os import path
from setuptools import setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with open(filename) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


DESCRIPTION = "Tiny REST API Client for intercom.io"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='intercomic',
    version=find_version("intercomic", "__init__.py"),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords="intercom, api",
    author='Dmitrii Gerasimenko',
    author_email='kiddima@gmail.com',
    url='http://github.com/kidig/intercomic',
    license='MIT',
    packages=['intercomic'],
    install_requires=[
        "requests"
    ],
    include_package_data=True,
    zip_safe=False,
)
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "hello world",
    version = "0.0.1",
    author = "Sszark",
    author_email = "---",
    description = ("Tutorial Package"),
    license = "BSD",
    keywords = "tutorial",
    url = "http://packages.python.org/hello_world",
    packages=['hello_world', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
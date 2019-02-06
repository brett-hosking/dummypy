from distutils.core import setup
from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='dummypy',
      version='0.1.0',
      description='A dummy python package template',
      url='http://github.com/brett-hosking/dummypy',
      author='brett hosking',
      author_email='wilski@noc.ac.uk',
      packages=find_packages())

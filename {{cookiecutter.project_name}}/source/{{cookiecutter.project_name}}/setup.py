# coding: utf-8

from setuptools import setup, find_packages

    
setup(
    name='{{cookiecutter.project_name}}',
    version='1.0',
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.author_name}}',
    license='ASL',
    zip_safe=False,
    packages=['{{cookiecutter.project_slug}}'],
    include_package_data=False
)

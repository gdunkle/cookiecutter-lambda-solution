# coding: utf-8

from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    
setup(
    name='{{cookiecutter.project_name}}',
    version='1.0',
    description='{{cookiecutter.project_short_description}}',
    author='{{cookiecutter.author_name}}',
    license='ASL',
    zip_safe=False,
    packages=['{{cookiecutter.project_slug}}'],
    package_dir={'{{cookiecutter.project_slug}}': '.'},
    include_package_data=False,
    install_requires=[
        '{{cookiecutter.project_slug}}==1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
)

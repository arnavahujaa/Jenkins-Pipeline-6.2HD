from setuptools import setup, find_packages

setup(
    name='online_calculator',
    version='1.0',
    description='A simple online calculator API using Flask',
    packages=find_packages(),
    install_requires=[
        'flask',
        'pytest',
        'pylint',
        'flake8'
    ],
)

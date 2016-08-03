from distutils.core import setup
from setuptools import find_packages

setup(
    name='pi2go',
    version='0.0.1',
    url='https://github.com/konradko/pi2go',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=[
        'smbus-cffi==0.5.1',
        'RPi.GPIO==0.6.2',
    ],
)

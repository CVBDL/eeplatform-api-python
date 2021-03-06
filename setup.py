"""Setup module for EagleEye Platform Python API."""

from setuptools import setup, find_packages


setup(
    name='eagleeye-platform-api',
    version='0.1',
    description='EagleEye Platform API Client',
    url='https://github.com/CVBDL/eeplatform-api-python',
    author='Patrick Zhong',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests>=2.13.0']
)

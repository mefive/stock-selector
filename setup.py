from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='tradingtrainer',
    author='mefive',
    packages=find_packages(),
    install_requires=['dateutil', 'pandas', 'tushare']
)
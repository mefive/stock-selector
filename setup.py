from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='stock-selector',
    author='mefive',
    packages=find_packages(),
    install_requires=['bs4', 'python-dateutil', 'pandas', 'tushare', 'SQLAlchemy']
)
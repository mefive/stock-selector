from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='stockselector',
    author='mefive',
    packages=find_packages(),
    install_requires=[
        'tushare',
        'bs4',
        'python-dateutil',
        'pandas',
        'SQLAlchemy',
        'mysqlclient',
        'uwsgi',
        'flask',
    ]
)

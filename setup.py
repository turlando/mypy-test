from setuptools import setup, find_packages

setup(
    name='mypy-test',
    version='0.0.1',

    package_dir={'': 'src'},
    packages=find_packages('src'),

    package_data={
        'mypy_test': ['py.typed'],
    }
)

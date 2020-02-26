from setuptools import setup

setup(
    name='cvxportfolio',
    version='0.0.9',
    author='Enzo Busseti and Steven Diamond',
    author_email='enzo.busseti@gmail.com, stevend2@stanford.edu',
    packages=['cvxportfolio',
              'cvxportfolio.tests',
              'cvxportfolio.utils'],
    package_dir={'cvxportfolio': 'cvxportfolio'},
    package_data={'cvxportfolio': [
        'tests/returns.csv', 'tests/sigmas.csv', 'tests/volumes.csv']},
    url='http://github.com/cvxgrp/cvxportfolio/',
    license='Apache',
    zip_safe=False,
    description='ConVeX Portfolio Optimization and Simulation toolset.',
    install_requires=["pandas",
                      "numpy",
                      "matplotlib",
                      "cvxpy>=1.0.6",
                      "pandas_datareader"],
    use_2to3=True,
)

# setup.py

from setuptools import setup, find_packages

setup(
    name='READPred',
    version='1.0',
    description='Package for READ patient prediction using machine learning models',
    author='Rohit',
    author_email='rohit17145@iiitd.ac.in',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'READPred': ['models/*.pkl'],
    },
    install_requires=[
        'pandas',
        'joblib',
        'scikit-learn',
    ],
    license='MIT',
)


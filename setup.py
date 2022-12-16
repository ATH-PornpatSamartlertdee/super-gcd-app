# setup.py placed at root directory
import setuptools
setuptools.setup(
    # name='examplepackage'
    # version='1.0.1',
    # author='Giorgos Myrianthous',
    # description='This is an example project',
    # long_description='This is a longer description for the project',
    # url='https://medium.com/@gmyrianthous',
    # keywords='sample, example, setuptools',
    extras_require={
        'dev': ['pytest', 'pylink', 'black', 'isort', 'pyinstaller'],
    }
)
from setuptools import setup

setup(
    name='refaclass',
    version='1.0.0',
    author='Hirokazu Niimoto',
    description='A Python package for RefaClass',
    packages=['refaclass'],
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'refaclass = refaclass.main:main'
        ]
    }
)

from sys import version_info

from setuptools import find_packages, setup

if version_info[:2] < (3, 5):
    raise RuntimeError(
        'Unsupported python version %s.' % '.'.join(version_info)
    )

APP_NAME = 'copyrator'
setup(
    name=APP_NAME,
    version='0.0.1',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    author='Isuru',
    author_email='isurusiri@protonmail.com',
    include_package_data=True,
    install_requires=[
        'kubernetes==11.0.0',
    ],
    entry_points={
        'console_scripts': [
            '{0} = {0}.cli:main'.format(APP_NAME)
        ]
    }
)
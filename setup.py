import os

from setuptools import setup, find_packages

# README read-in
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
# END README read-in


def get_resources():
    directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'skytemple_icons')
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.py'):
                paths.append(os.path.join(os.path.relpath(os.path.join('..', path, filename), directory)))
    return paths


setup(
    name='skytemple-icons',
    version='0.1.0',
    packages=find_packages(),
    package_data={'skytemple_icons': get_resources()},
    description='Icons for SkyTemple',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/SkyTemple/skytemple-icons/',
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
)

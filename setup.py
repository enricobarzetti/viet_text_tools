import os
from setuptools import setup, find_packages
import viet_text_tools as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='viet_text_tools',
    version=app.__version__,
    description='Functions for working with Vietnamese text',
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='vietnamese',
    author='Enrico Barzetti',
    author_email='enricobarzetti@gmail.com',
    url='https://github.com/enricobarzetti/viet_text_tools',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
)

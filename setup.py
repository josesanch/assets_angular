# encoding: utf-8
from distutils.core import setup

from setuptools import find_packages

import assets_angular

setup(
    name='assets_angular',
    version=assets_angular.VERSION,
    author='José Sánchez Moreno',
    author_email='jose@o2w.es',
    packages=find_packages(),
    license='MIT',
    description=u'Django_assets angular template filter.',
    long_description=open('README.rst').read(),
    url='https://github.com/josesanch/assets_angular',
    platforms="All platforms",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],

)

import subprocess

from setuptools import setup
from setuptools import find_packages


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name='codestream_parser',
    version='v1.75',
    description='All-JPEG Codestream/File Format Parser Tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/thorfdbg/codestream-parser',
    author='Thomas Richter',
    author_email='thomas.richter@iis.fraunhofer.de',
    license='MIT',
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=['wheels'],
    packages=find_packages(exclude=['tests']),
    python_requires='>=3',  # recognized by pip >= 9.0.0
    entry_points={
        'console_scripts': [
            'caifile=codestream_parser.caifile:main',
            'icc=codestream_parser.icc:main',
            'jp2codestream=codestream_parser.jp2codestream:main',
            'jp2file=codestream_parser.jp2file:main',
            'jpgcodestream=codestream_parser.jpgcodestream:main',
            'jxrfile=codestream_parser.jxrfile:main',
            'jxscodestream=codestream_parser.jxscodestream:main',
        ]
    },
    test_suite='tests'
)

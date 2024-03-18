from setuptools import setup, find_packages

setup(
    name='urltotext',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        "requests",
        "bs4",
        "langdetect",
        "selenium",
    ],
    # Additional metadata about your package.
    author='Chinmay Shrivastava',
    author_email='cshrivastava99@gmail.com',
    description='A light weight library that takes in a url and extracts any readable text in it.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChinmayShrivastava/url2text',
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
    ],
    entry_points={},
)
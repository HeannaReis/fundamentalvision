from setuptools import setup, find_packages

setup(
    name='fundamentalvision',
    version='0.1.1',
    author='Joel Ferreira Heanna dos Reis',
    author_email='heannareis@gmail.com',
    description='A package for fundamental analysis of stocks on Brazil B3 Exchange.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/HeannaReis/fundamentalvision',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4',
        'streamlit',
        'plotly',
        'fundamentus',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
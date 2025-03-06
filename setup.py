from setuptools import setup, find_packages

setup(
    name='fundamentalvision',
    version='0.1.0',
    author='Joel FerreiraHeanna dos Reis',
    author_email='heannareis@gmail.com',
    description='A package for fundamental analysis of stocks on Brazil B3 Exchange.',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
        'beautifulsoup4',
        'streamlit',
        'plotly',
        'fundamentus'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
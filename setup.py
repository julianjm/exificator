from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='exificator',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'exificator = src.exificator:main'
        ]
    },
    install_requires=[
        'exif>=1.6.0'
    ],
    author='Julian J. M.',
    author_email='julianjm@gmail.com',
    description='A command line application for modifying EXIF metadata in JPEG images.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='exif jpeg image metadata xss payload',
    url='https://github.com/julianjm/exificator'
)
from setuptools import setup, find_packages

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
    license='MIT',
    keywords='exif jpeg image metadata xss payload',
    url='https://github.com/julianjm/exificator'
)
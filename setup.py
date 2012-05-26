from distutils.core import setup
from ccthumbs import VERSION

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='django-ccfiletypes',
    version=VERSION,
    license = 'BSD 3 Clause',
    description='Django templatefilters for displaying info about files.',
    long_description=long_description,
    author='c&c',
    author_email='studio@designcc.co.uk',
    url='https://github.com/designcc/django-ccfiletypes',
    packages=[
        'ccfiletypes',
        ],)


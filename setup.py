import os
from distutils.core import setup
from ccfiletypes import VERSION

root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)


setup(
    name='django-ccfiletypes',
    version=VERSION,
    license = 'BSD 3 Clause',
    description='Django templatefilters for displaying info about files.',
    long_description=open('README.rst').read(),
    author='c&c',
    author_email='studio@designcc.co.uk',
    url='https://github.com/designcc/django-ccfiletypes',
    package_data={
        'ccfiletypes': [
            'static/ccfiletypes/LICENSE',
            'static/ccfiletypes/small/*.png',
            'static/ccfiletypes/medium/*.png',
            'static/ccfiletypes/large/*.png',
            'static/ccfiletypes/xlarge/*.png',
        ],
    },
    packages=[
        'ccfiletypes',
        'ccfiletypes.templatetags',
        ],) 

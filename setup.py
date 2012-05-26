from distutils.core import setup
from ccthumbs import VERSION

setup(
    name="django-ccthumbs",
    version=VERSION,
    license = 'BSD 3 Clause',
    description='A thumbnail generating model field for Django',
    author='c&c',
    author_email='studio@designcc.co.uk',
    url='https://github.com/designcc/django-ccthumbs',
    packages=[
        'ccthumbs',
        ],
    install_requires = [
        'PIL',
        ])


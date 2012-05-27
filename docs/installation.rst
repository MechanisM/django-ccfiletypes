Installation
=====================================

Install via pip::

    pip install django-ccfiletypes

Once installed you will need to add it to your settings.INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'ccfiletypes',
    )

Finally you will need to run the collectstatic command to get 
the icon files into your static root::

    python manage.py collectstatic

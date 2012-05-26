About
=====================================
ccfiltypes is a small collection of template filters for django that
make the displaying of information from FileFields a little easier..

It's useful for displaying an icon for a certain filetype or getting
just the filename without the full path.



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


Usage
=====================================

Include the tags in your template::

    {% load ccfiletype_tags %}


Now you have access to two filters

icon
============

icon will return an icon for the filetype based on it's extention::

    {{object.filefield.path|icon:"size"}}

It can be called with an argument for size which can be small, medium,
large or xlarge.  If no argument is supplied then small will be the default.

The returned string from the icon filter is formed by using the value from 
settings.STATIC_URL. 


name
============

name will return only the filename from a path::

    {{objects.filefield.path|name}}


Full Example
=====================================

A common usage for these filters would be for something like this::

    <img src="{{object.filefield.path|icon}}"
         alt="{{object.filefield.path|name}}">


Attribution
=====================================

The icons in this package come from the `Free File Icons`_ project by `Teambox`_ and a copy of
the license can be found the ccfiletypes/static/ccfiletypes directory.


.. _Free File Icons: https://github.com/teambox/Free-file-icons
.. _Teambox: http://www.teambox.com/

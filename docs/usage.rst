
Usage
=====================================

See the `documentation`_


Include the tags in your template::

    {% load ccfiletype_tags %}


Now you have access to two filters

icon
-----------------
icon will return an icon for the filetype based on it's extention::

    {{object.filefield.path|icon:"size"}}

It can be called with an argument for size which can be small, medium,
large or xlarge.  If no argument is supplied then small will be the default.

.. note:: The returned string from the icon filter is formed by using the value from 
         settings.STATIC_URL. 


name
-----------------

name will return only the filename from a path::

    {{objects.filefield.path|name}}


full example
-----------------

A common usage for these filters would be for something like this::

    <img src="{{object.filefield.path|icon}}"
         alt="{{object.filefield.path|name}}">

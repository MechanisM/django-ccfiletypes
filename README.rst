About
-------------------

ccfiltypes is a small collection of template filters for django that
make the displaying of information from FileFields a little easier..

It's useful for displaying an icon for a certain filetype or getting
just the filename without the full path.



Installation
-------------------

Install via pip::

    pip install django-ccfiletypes

Once installed you will need to run the collectstatic command to get 
the icon files into your static root::

    python manage.py collectstatic


Usage
-------------------

Include the tags in your page::

    {% load ccfiletype_tags %}


Now you have access to two filters

icon
--------------

Icon will return an icon for the filetype based on it's extention::

    {{object.filefield.path|icon:"size"}}

It can be called with an argument for size where size can be small, medium,
large or xlarge.  If no argument is supplied then small will be the default.




Full example
--------------

A common usage for these filters would be for something like this::

    <img src="{{object.filefield.path|icon}}" alt="I



Attribution
----------------------

The icons in this package come from the .. _Free File Icons: https://github.com/teambox/Free-file-icons

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


Usage
-------------------

Include the tags in your page::

    {% load ccfiletype_tags %}


Now you have access to two filters

`icon`



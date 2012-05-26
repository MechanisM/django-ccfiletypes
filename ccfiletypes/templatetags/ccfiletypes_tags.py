import os
from django import template
from django.conf import settings

register = template.Library()


@register.filter
def name(path):
    """Given a path return the filename - a thin wrapper around
    os.path.basename"""
    return os.path.basename(path)

@register.filter
def icon(attachment, size="small"):
    """based on the file extention this will return a suitable icon"""

    path, ext = attachment.src.path.rsplit('.', 1)
    document_name = path.rsplit('/', 1)
    document_name.reverse()

    if ext == 'docx':
        ext = 'doc'

    extentions = ('aac','ai','aiff','avi','bmp','c','cpp','css',
    'dat','dmg','doc','dotx','dwg','dxf','eps','exe','flv','gif',
    'h','hpp','html','ics','iso','java','jpg','key','mid','mp3',
    'mp4','mpg','odf','ods','odt','otp','ots','ott','pdf','php',
    'ppt','psd','py','qt','rar','rb','rtf','sql','tga','tgz',
    'tiff','txt','wav','xls','xlsx','xml','yml','zip')

    if ext in extentions:
        image = '%s/%s.png' % (size, ext)
    else:
        image = '%s/_blank.png' % size

    return '%sccfiletypes/%s' % (
            settings.STATIC_URL,
            image)

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Camila'
SITENAME = 'Bits with anxiety disorder'
SITETITLE = 'Camila'
#SITEURL = 'http://camila.codes'
SITESUBTITLE = 'Bits with anxiety disorder. Coding <a href="https://github.com/nextcloud/desktop">C++ and Qt</a> @ <a href="https://nextcloud.com">Nextcloud</a>. she/her. <br><small>GPG Key ID D406 C75C EE1A 36D6<small>'
PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# flex stuff
THEME = 'Flex'
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%d %B %Y',
}
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)
SOCIAL = (
    ('goodreads', 'https://www.goodreads.com/thewomensroom'),
    ('github', 'https://github.com/camilasan'),
    ('twitter', 'https://camila.codes'),
    ('rss', '/blog/feeds/all.atom.xml'),
)

LINKS = (('Archives', '/archives.html'),
         ('Categories', '/categories.html'),
         ('Tags', '/tags.html'),)

DISPLAY_PAGES_ON_MENU = True
COPYRIGHT_NAME = 'Camila'
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}
COPYRIGHT_YEAR = datetime.now().year
#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = 'ra-55adbb025d4f7e55'
ARTICLE_EXCLUDES = ['archives']
STATIC_PATHS = ['assets']
PATH_METADATA = 'assets'
CUSTOM_CSS = 'assets/css/custom.css'

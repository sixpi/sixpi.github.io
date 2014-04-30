#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bing Xia'
SITENAME = u"Bing's Blog"
SITEURL = ''

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

STATIC_PATHS = ('extra/CNAME', 'CNAME',)
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GITHUB_USER = 'sixpi'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

THEME = 'pelican-octopress-theme/'

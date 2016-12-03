#!/usr/bin/python
# -*- coding: utf-8 -*-

import web

from controllers.about import About as about
from controllers.index import Index as index
from controllers.data import Data as data
from controllers.insert import Insert as insert
from controllers.add import Add as add

urls = (
    '/', 'index',
    '/about(.*)', 'about',
    '/data(.*)', 'data',
    '/insert', 'insert',
    '/add', 'add'
)

if __name__ == "__main__":
    app = web.application(urls, globals(), autoreload=False)
    web.config.debug = False
    app.run()
    
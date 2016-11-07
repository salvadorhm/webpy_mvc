#!/usr/bin/python
# -*- coding: utf-8 -*-

import web

from controllers.about import About as about
from controllers.index import Index as index
from controllers.data import Data as data

urls = (
    '/','index',
    '/about(.*)','about',
    '/data(.*)','data'
)

if __name__ == "__main__":
    app = web.application(urls, globals(), autoreload=False)
    web.config.debug = False
    app.run()
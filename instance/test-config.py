#!/usr/bin/python
# -*- coding: utf-8 -*-

# ------- IMPORT DEPENDENCIES ------- 
import os
# ------- IMPORT LOCAL DEPENDENCIES  -------

# absolute path for the parent directory of the directory your file is in
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

SECRET_KEY = 'p9Bv<6Zid2%$i01'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/db.sqlite')

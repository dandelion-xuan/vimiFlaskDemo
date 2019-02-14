#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class db_config():
    USER = os.getenv('MYSQL_ROOT_USER', default = 'root')
    PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', default = '123456')
    DATABASE = os.getenv('MYSQL_DATABASE', default = 'homepage')
    HOST = os.getenv('DB_HOST', default = '127.0.0.1')

config = db_config()
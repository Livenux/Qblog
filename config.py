#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Config(object):
    """ Base config class."""
    pass


class ProdConfig(Config):
    """Prodction config class."""
    pass


class DevConfig(Config):
    """ Develoment config class."""
    # Enable Debug
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://qblog:chan9eme!@172.16.0.131:3306/qblog'

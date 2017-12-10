#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy(app)
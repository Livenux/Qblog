#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


from flask import Flask
from config import DevConfig


app = Flask(__name__)

# Import the views module
views = __import__('views')


# Get the config from object of DecConfig
''' 使用 onfig.from_object() 而不使用 app.config['DEBUG']
因为这样可以加载 class DevConfig 的配置变量集合，
而不需要一项一项的添加和修改。
'''
app.config.from_object(DevConfig)

if __name__ == '__main__':
    # Entry the application
    app.run()

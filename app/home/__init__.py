# -*- coding:utf-8 -*-
__author__ = 'hedejun'
__date__ = '2018/1/23 22:02'

from flask import Blueprint

home = Blueprint("home", __name__)
import app.home.views

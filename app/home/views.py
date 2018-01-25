# -*- coding:utf-8 -*-
__author__ = 'hedejun'
__date__ = '2018/1/23 22:03'

from . import home
from flask import render_template, redirect, url_for


@home.route('/login/')
def login():
    return render_template("home/login.html")


@home.route('/logout/')
def logout():
    return redirect(url_for("home.login"))


@home.route('/register/')
def register():
    return render_template('home/register.html')


@home.route('/user/')
def user():
    return render_template('home/user.html')


@home.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')

@home.route('/comments/')
def comments():
    return render_template('home/comments.html')

@home.route('/loginlog/')
def loginlog():
    return render_template('home/loginlog.html')

@home.route('/moviecol/')
def moviecol():
    return render_template('home/moviecol.html')


# 列表
@home.route("/")
def index():
    return render_template("home/index.html")


# 动画
@home.route('/animation/')
def animation():
    return render_template("home/animation.html")


# 搜索
@home.route('/search/')
def search():
    return render_template('home/search.html')

# 详情
@home.route('/play/')
def play():
    return render_template('home/play.html')

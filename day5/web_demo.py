#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():

    a = request.args.get("a")  # 获取URL参数a的值，如果没有则为None
    b = request.args.get("b")

    return str(int(a) + int(b))


    f = open("index.html", "r", encoding="utf-8")
    data = f.read()
    f.close()
    return data

@app.route('/store')
def store():
    return "<marquee>商城页面</marquee>"

@app.route('/reg')
def reg():
    return "用户名：<input>"
if __name__ == '__main__':
    app.run(debug=True)
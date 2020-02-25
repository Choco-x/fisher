from flask import Flask, current_app

app = Flask(__name__)
ctx = app.app_context()
# 返回的是app核心对象而不是context上下文，那为啥还要绕这么一下呢
ctx.push()
a = current_app
d = current_app.config['DEBUG']

with app.app_context():
    a = current_app


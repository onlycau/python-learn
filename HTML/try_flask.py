#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__)

#Flask通过Python的装饰器在内部自动地把URL和函数给关联起来
@app.route('/',methods=['GET','POST'])
def homePage():
    return "<h1>Home主页:</h1><br><a href='signin'>登录</a>"

#通过装饰器定义登录界面
@app.route('/signin',methods=["GET"])
def signin_from():
    html = '''
        <form action='/signin' method='post' >
            <p>用户名:<input name='uname' width='120' /></p>
            <p>密　码:<input name='psw' width='120' /></p>
            <p><button type='submit'   >登录</button></p>
        </form>
    '''
    return html;

#通过装饰器定义接收的表单数据
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['uname']=='admin' and request.form['psw']=="123":
        return "<h1>wellcome to Flask</h1>"
    return "<h1>Bad user name or password!</h1>"


if __name__ == "__main__":
    app.run()
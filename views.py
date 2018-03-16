# Core logic
# coding:utf8

from flask import Flask, render_template, redirect, url_for
from forms import LoginForm,RegisterForm,ArticleForm
app = Flask(__name__)
app.config["SECRET_KEY"]="123445"

# Login
@app.route('/login/', methods=['GET', 'POST'])  # get 页面请求，post提交表单
def login():
    form=LoginForm()
    return render_template("login.html", title="Login",form=form)  # 把title变量传入


# Register
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    return render_template("register.html", title="Register",form=form)


# logout(302 redirect to login)
@app.route('/logout/', methods=['GET'])  # 不需要表单的提交操作
def logout():
    return redirect('/login/')


# post articles
@app.route('/art/add/', methods=['GET', 'POST'])
def art_add():
    form=ArticleForm()
    return render_template("art_add.html", title="Post Articles",form=form)


# edit articles
@app.route('/art/edit/<int:id>/', methods=['GET', 'POST'])  # Involving route matching涉及路由匹配
def art_edit(id):
    return render_template("art_edit.html")


# delete articles
@app.route('/art/del/<int:id>/', methods=['GET'])  # Involving route matching涉及路由匹配
def art_del(id):
    return redirect('/art/list/')


# articles list
@app.route('/art/list/', methods=['GET'])  # Involving route matching涉及路由匹配
def art_list():
    return render_template("art_list.html",title="Article List")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)  # debug->see error on webpage

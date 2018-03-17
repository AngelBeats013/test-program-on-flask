# coding:utf8
# Core logic
# coding:utf8
# session 保存会话
from flask import Flask, render_template, redirect, url_for, flash, session, Response, request
from forms import LoginForm, RegisterForm, ArticleForm
from models import User, db, Article
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import uuid
# 上传文件 安全名称
from datetime import datetime
import os

# request获取当前地址
from functools import wraps  # 登陆装饰器

app = Flask(__name__)
app.config["SECRET_KEY"] = "123445"
app.config["UP"] = os.path.join(os.path.dirname(__file__),"static/uploads")


# 登陆装饰器,防止通过url跳过登陆
def user_login_req(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)  # 必填参数，选填参数

    return login_req


# Login
@app.route('/login/', methods=['GET', 'POST'])  # get 页面请求，post提交表单
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["name"]
        # flash("login success","ok")
        return redirect("/art/list/")
    return render_template("login.html", title="Login", form=form)  # 把title变量传入


# Register
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # 表单数据提交过来进行验证
    if form.validate_on_submit():
        # 获取数据
        data = form.data
        # 保存数据
        user = User(
            name=data["name"],
            pwd=generate_password_hash(data["password"]),
            addtime=datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S")
        )
        db.session.add(user)
        db.session.commit()
        # 定会话闪现
        flash("Register success, please login", "ok")
        return redirect('/login/')
    # 验证错误
    else:
        flash("Input proper info", "error")
    return render_template("register.html", title="Register", form=form)


# varicode
@app.route('/code/', methods=['GET'])
def varicode():
    from varicode import VariCode
    c = VariCode()
    info = c.create_code()
    image = os.path.join(os.path.dirname(__file__), "static/code") + "/" + info["img_name"]
    with open(image, 'rb') as f:
        image = f.read()
    session["varicode"] = info["code"]
    return Response(image, mimetype="jpeg")


# logout(302 redirect to login)
@app.route('/logout/', methods=['GET'])  # 不需要表单的提交操作
@user_login_req
def logout():
    session.pop("user", None)
    return redirect('/login/')


# 修改文件名称
def change_file_name(filename):
    info = os.path.splitext(filename)
    # 文件名 时间格式字符串+唯一字符串+后缀
    name = datetime.utcnow().strftime('%Y%m%d%H%M%S') + str(uuid.uuid4().hex) + info[-1]
    return name


# post articles
@app.route('/art/add/', methods=['GET', 'POST'])
@user_login_req
def art_add():
    form = ArticleForm()
    if form.validate_on_submit():
        data = form.data
        # 上传cover
        file = secure_filename(form.cover.data.filename)
        cover = change_file_name(file)
        if not os.path.exists(app.config["UP"]):
            os.makedirs(app.config["UP"])
        # 保存文件
        form.cover.data.save(app.config["UP"]+"/"+cover)
        # 获取用户id
        user=User.query.filter_by(name=session["user"]).first()
        user_id=user.id
        # 保存数据
        article=Article(
            title=data["title"],
            category=data["category"],
            author=user_id,
            cover=cover,
            content=data["content"],
            addtime=datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S")
        )
        db.session.add(article)
        db.session.commit()
        flash("post success","ok")
    return render_template("art_add.html", title="Post Articles", form=form)


# edit articles
@app.route('/art/edit/<int:id>/', methods=['GET', 'POST'])  # Involving route matching涉及路由匹配
@user_login_req
def art_edit(id):
    return render_template("art_edit.html")


# delete articles
@app.route('/art/del/<int:id>/', methods=['GET'])  # Involving route matching涉及路由匹配
@user_login_req
def art_del(id):
    return redirect('/art/list/')


# articles list
@app.route('/art/list/', methods=['GET'])  # Involving route matching涉及路由匹配
@user_login_req
def art_list():
    return render_template("art_list.html", title="Article List")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)  # debug->see error on webpage

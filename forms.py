from flask import session  # 验证码校验
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError
# 数据必须存在，密码和确认密码要相同,自定义验证信息
from models import User,Article

# 不能有重复的用户名
'''
login forms
1.name
2.password
3.login btn
'''


class LoginForm(FlaskForm):
    name = StringField(
        label="username",
        validators=[
            DataRequired("name cannot be null")
        ],
        description="username",
        render_kw={
            "class": "form-control",
            "placeholder": "input username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("password cannot be null")
        ],
        description="password",
        render_kw={
            "class": "form-control",  # 从html中对应表单中找到
            "placeholder": "input password"
        }
    )
    submit = SubmitField(
        "login",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_password(self, field):
        password = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if not user:
            raise ValidationError("no user")
        if not user.check_password(password):
            raise ValidationError("wrong password")



'''
register forms
1.name
2.password
3.varify password
4.varification code
5.register btn
'''


class RegisterForm(FlaskForm):
    name = StringField(
        label="username",
        validators=[
            DataRequired("name cannot be null")
        ],
        description="username",
        render_kw={
            "class": "form-control",
            "placeholder": "input username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[
            DataRequired("password cannot be null")
        ],
        description="password",
        render_kw={
            "class": "form-control",  # 从html中对应表单中找到
            "placeholder": "input password"
        }
    )
    repassword = PasswordField(
        label="repassword",
        validators=[
            DataRequired("repassword cannot be null"),
            EqualTo('password', message="两次输入密码不一致")
        ],
        description="repassword",
        render_kw={
            "class": "form-control",  # 从html中对应表单中找到
            "placeholder": "input repassword"
        }
    )
    varicode = StringField(
        label="varification code",
        validators=[
            DataRequired("varicode cannot be null")
        ],
        description="varification code",
        render_kw={
            "class": "form-control",
            "placeholder": "input varicode"
        }
    )
    submit = SubmitField(
        "register",
        render_kw={
            "class": "btn btn-success"
        }
    )

    # 自定义字段验证 validate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError("no duplicate account")

    def validate_varicode(self, field):
        varicode = field.data
        if session.get("varicode") is None:
            raise ValidationError("no varicode")
        if session.get("varicode") is not None and session["varicode"].lower() != varicode.lower():
            raise ValidationError("wrong varicode")


'''
post article forms
1.title
2.category
3.cover
4.content
5.post btn
'''


class ArticleForm(FlaskForm):
    title = StringField(
        label="title",
        validators=[
            DataRequired("need title")
        ],
        description="title",
        render_kw={
            "class": "form-control",
            "placeholder": "input title"
        }
    )
    category = SelectField(
        label="category",
        validators=[
            DataRequired("need category")
        ],
        description="category",
        choices=[(1, 'Tech'), (2, 'Funny'), (3, 'Life')],
        default=1,
        coerce=int,  # 类型
        render_kw={
            "class": "form-control"
        }
    )
    cover = FileField(
        label="cover",
        validators=[
            DataRequired("need cover")
        ],
        description="cover",
        render_kw={
            "class": "form-control-file"  # 从html中对应表单中找到
        }
    )
    content = TextAreaField(
        label="content",
        validators=[
            DataRequired("need content")
        ],
        description="content",
        render_kw={
            "style": "height:300px",  # 从html中对应表单中找到
            "id": "content"
        }
    )
    post = SubmitField(
        "post",
        render_kw={
            "class": "btn btn-primary"
        }
    )
    def validate_title(self,field):
        title=field.data
        article=Article.query.filter_by(title=self.title.data).first()
        if article:
            raise ValidationError("no duplicate title")

'''
edit article forms
1.title
2.category
3.cover
4.content
5.post btn
'''


class EditArticleForm(FlaskForm):
    id=IntegerField(
        label="id",
        validators=[
            DataRequired("need id")
        ]
    )
    title = StringField(
        label="title",
        validators=[
            DataRequired("need title")
        ],
        description="title",
        render_kw={
            "class": "form-control",
            "placeholder": "input title"
        }
    )
    category = SelectField(
        label="category",
        validators=[
            DataRequired("need category")
        ],
        description="category",
        choices=[(1, 'Tech'), (2, 'Funny'), (3, 'Life')],
        default=1,
        coerce=int,  # 类型
        render_kw={
            "class": "form-control"
        }
    )
    cover = FileField(
        label="cover",
        validators=[
            DataRequired("need cover")
        ],
        description="cover",
        render_kw={
            "class": "form-control-file"  # 从html中对应表单中找到
        }
    )
    content = TextAreaField(
        label="content",
        validators=[
            DataRequired("need content")
        ],
        description="content",
        render_kw={
            "style": "height:300px",  # 从html中对应表单中找到
            "id": "content"
        }
    )
    post = SubmitField(
        "Submit",
        render_kw={
            "class": "btn btn-primary"
        }
    )
    def validate_title(self,field):
        title=field.data
        article=Article.query.filter_by(title=self.title.data).first()
        if article:
            raise ValidationError("no duplicate title")

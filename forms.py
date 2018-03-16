from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField, TextAreaField

'''
login forms
1.name
2.password
3.login btn
'''


class LoginForm(FlaskForm):
    name = StringField(
        label="username",
        validators=[],
        description="username",
        render_kw={
            "class": "form-control",
            "placeholder": "input username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[],
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
        validators=[],
        description="username",
        render_kw={
            "class": "form-control",
            "placeholder": "input username"
        }
    )
    password = PasswordField(
        label="password",
        validators=[],
        description="password",
        render_kw={
            "class": "form-control",  # 从html中对应表单中找到
            "placeholder": "input password"
        }
    )
    repassword = PasswordField(
        label="repassword",
        validators=[],
        description="repassword",
        render_kw={
            "class": "form-control",  # 从html中对应表单中找到
            "placeholder": "input repassword"
        }
    )
    varicode = StringField(
        label="varification code",
        validators=[],
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
        validators=[],
        description="title",
        render_kw={
            "class": "form-control",
            "placeholder": "input title"
        }
    )
    category = SelectField(
        label="category",
        validators=[],
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
        validators=[],
        description="cover",
        render_kw={
            "class": "form-control-file"  # 从html中对应表单中找到
        }
    )
    content = TextAreaField(
        label="content",
        validators=[],
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

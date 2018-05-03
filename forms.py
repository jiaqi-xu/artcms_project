# -*- encoding:utf-8 -*-
from flask import session
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, SelectField, FileField,
    TextAreaField, IntegerField
)
from wtforms.validators import DataRequired, EqualTo, ValidationError
from models import User

"""
登录表单：
1. 账号
2. 密码
3. 登录按钮
"""


class LoginForm(FlaskForm):
    name = StringField(
        label="account",
        validators=[
            DataRequired("Account is Required!")
        ],
        description="account",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter your account"
        }
    )
    pwd = PasswordField(
        label="password",
        validators=[
            DataRequired("Password is Required!")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter your password"
        }
    )
    submit = SubmitField(
        "login",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    def validate_pwd(self, field):
        pwd = field.data
        user = User.query.filter_by(name=self.name.data).first()
        if not user.check_pwd(pwd):
            raise ValidationError("Password is incorrect!")


"""
注册表单:
1. 账号
2. 密码
3. 确认密码
4. 验证码
5. 注册按钮
"""


class RegisterForm(FlaskForm):
    name = StringField(
        label="account",
        validators=[
            DataRequired("Account is required")
        ],
        description="account",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter your account"
        }
    )
    pwd = PasswordField(
        label="password",
        validators=[
            DataRequired("Password is required")
        ],
        description="password",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter your password"
        }
    )

    repwd = PasswordField(
        label="re_password",
        validators=[
            DataRequired("Re_password is required"),
            EqualTo("pwd", message="The password for the two time is inconsistent")
        ],
        description="re_password",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter your password again"
        }
    )
    code = StringField(
        label="security_code",
        validators=[
            DataRequired("Security Code is required")
        ],
        description="security_code",
        render_kw={
            "class": "form-control",
            "placeholder": "please enter security code"
        }
    )
    submit = SubmitField(
        "post",
        render_kw={
            "class": "btn btn-primary"
        }
    )

    # 自定义字段验证规则： validate_字段名
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user > 0:
            raise ValidationError('Account is already existed!')

    # 自定义验证码验证功能
    def validate_code(self, field):
        code = field.data
        if session.get('code') == "":
            raise ValidationError("No Security Code!")
        if session.get('code') and session['code'].lower() != code.lower():
            raise ValidationError("Security Code is incorrect!")

"""
发布文章表单
1. 标题
2. 分类
3. 封面
4. 内容
"""


class ArtForm(FlaskForm):
    title = StringField(
        label="title",
        description="title",
        validators=[
            DataRequired("Title is Required!")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "please enter title"
        }
    )
    cate = SelectField(
        label="category",
        description="category",
        validators=[
            DataRequired("Category is Required!")
        ],
        choices=[(1, "Science & Technology"), (2, "Funny"), (3, "Military")],
        default=2,
        coerce=int,
        render_kw={
            "class": "form-control",

        }
    )
    logo = FileField(
        label="cover",
        validators=[
            DataRequired("Cover is Required!")
        ],
        description="cover",
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label="content",
        validators=[
            DataRequired("Content is Required!")
        ],
        description="content",
        render_kw={
            "style": "height: 300px",
            "id": "content"
        }
    )
    submit = SubmitField(
        "post article",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class ArtEditForm(FlaskForm):
    id = IntegerField(
        label="id",
        validators=[
            DataRequired("Id is Required!")
        ]
    )
    title = StringField(
        label="title",
        description="title",
        validators=[
            DataRequired("Title is Required!")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "please enter title"
        }
    )
    cate = SelectField(
        label="category",
        description="category",
        validators=[
            DataRequired("Category is Required!")
        ],
        choices=[(1, "Science & Technology"), (2, "Funny"), (3, "Military")],
        default=2,
        coerce=int,
        render_kw={
            "class": "form-control",

        }
    )
    logo = FileField(
        label="cover",
        validators=[
            DataRequired("Cover is Required!")
        ],
        description="cover",
        render_kw={
            "class": "form-control-file"
        }
    )
    content = TextAreaField(
        label="content",
        validators=[
            DataRequired("Content is Required!")
        ],
        description="content",
        render_kw={
            "style": "height: 300px",
            "id": "content"
        }
    )
    submit = SubmitField(
        "edit article",
        render_kw={
            "class": "btn btn-primary"
        }
    )
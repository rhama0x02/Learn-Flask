from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, InputRequired, Email


class LoginForm(FlaskForm):
    username = StringField(label="Username")
    password = PasswordField(label="Password")
    remember_me = BooleanField(label="Remember Me")
    submit =  SubmitField("Submit")

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField(label="Username",validators=[InputRequired(),Length(min=6,max=24)])
    password = PasswordField(label="Password",validators=[DataRequired(),Length(min=6,max=32),EqualTo("password_confirm")])
    password_confirm = PasswordField(label="Password Confirm",validators=[DataRequired(),Length(min=6,max=32)])
    submit =  SubmitField("Submit")
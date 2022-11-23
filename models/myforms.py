from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, SubmitField, PasswordField, SelectField, FileField, DateTimeField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    mannumber = IntegerField('mannumber', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class RequestForm(FlaskForm):
    request_title = StringField('request_title', validators=[DataRequired()])
    request_info = TextAreaField('request_info', validators=[DataRequired()])
    submit = SubmitField('submit')

class RegisterForm(FlaskForm):
    mannumber = IntegerField('mannumber', validators=[DataRequired()])
    firstname = StringField('firstname', validators=[DataRequired()])
    secondname = StringField('secondname', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired()])
    role= StringField('role', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class SolutionForm(FlaskForm):
    request = IntegerField('request_id')
    solution = StringField('solution', validators=[DataRequired()])
    submit = SubmitField('submit')


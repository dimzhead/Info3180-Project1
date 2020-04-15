from app import db
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired,Email


class RegistrationForm(FlaskForm):
    first_name = StringField('Firstname', validators=[DataRequired()])
    last_name = StringField('Lastname', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male','Male'),('Female','Female')], validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography')
    profPic = FileField("Profile Picture",validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
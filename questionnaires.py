from flask_wtf import FlaskForm
from wtforms import Radiofield, SubmitField
from wtforms import validators, ValidationError


class Demographics(FlaskForm):
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female'),('O','Other')])

from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import NumberRange, InputRequired


class WelcomeForm(FlaskForm):
    consent = RadioField(
                        '',
                        choices=[('A', 'I hereby agree to participate in the study'), ('DNA', 'I do not agree (leave the study)')],
                        validators=[InputRequired()]
                        )
    submit = SubmitField(
                        'Next'
                        )


class DemographicsForm(FlaskForm):
    gender = RadioField(
                        'Gender',
                        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                        validators=[InputRequired()]
                        )
    age = IntegerField(
                        'Age',
                        validators=[InputRequired(), NumberRange(min=18, max=65, message='You must be between 18 and 65 years old to participate in the study')]
                        )
    nationality = StringField(
                        'Nationality',
                        validators=[InputRequired()]
                        )
    submit = SubmitField(
                        'Next'
                        )

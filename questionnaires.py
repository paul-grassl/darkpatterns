from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import DataRequired, NumberRange, InputRequired


class DemographicsForm(FlaskForm):
    Gender = RadioField(
                        'Gender',
                        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                        validators=[InputRequired()]
                        )
    Age = IntegerField(
                        'Age',
                        validators=[InputRequired(), NumberRange(min=18, max=65, message='You must be between 18 and 65 years old to participate in the study')]
                        )
    Nationality = StringField(
                        'Nationality',
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )


class ControlAndDeliberationForm(FlaskForm):
    PerceivedControlQ1 = DecimalRangeField(
                        '1. How much control did you feel the consent form gave you over the amount of your personal information collected by the company?',
                        default=50,
                        validators=[DataRequired()]
                        )
    PerceivedControlQ2 = DecimalRangeField(
                        '2. How much control did you feel the consent form gave you over who can get access your personal information?',
                        default=50,
                        validators=[DataRequired()]
                        )
    PerceivedControlQ3 = DecimalRangeField(
                        '3. How much control did you feel the consent form gave you over your personal information that has been released?',
                        default=50,
                        validators=[DataRequired()]
                        )
    PerceivedControlQ4 = DecimalRangeField(
                        '4. How much control did you feel the consent form gave you over how your personal information is being used by the company?',
                        default=50,
                        validators=[DataRequired()]
                        )
    PerceivedControlQ5 = DecimalRangeField(
                        '5. Overall, how much did the consent form made you feel in control over your personal information provided to the company?',
                        default=50,
                        validators=[DataRequired()]
                        )
    ManipulationCheck = RadioField(
                        '1. Which option did you choose?',
                        choices=[('A', 'Agree'), ('DNA', 'Do Not Agree')],
                        validators=[DataRequired()]
                        )
    Deliberation = DecimalRangeField(
                        '2. How much did you think about your decision before clicking on one option?',
                        default=50,
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )


class PrivacyConcernsForm(FlaskForm):
    PrivacyConcernsQ1 = RadioField(
                        '1. Compared to others I’m more sensitive about the way online companies handle my personal information',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    PrivacyConcernsQ2 = RadioField(
                        '2. To me, it is the most important thing to keep my privacy intact from online companies',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    PrivacyConcernsQ3 = RadioField(
                        '3. I’m concerned about threats to my personal privacy today',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )

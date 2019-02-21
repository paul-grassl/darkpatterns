from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import DecimalRangeField
import decimal
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


class ControlAndDeliberationForm(FlaskForm):
    perceivedControlQ1 = DecimalRangeField(
                        '1. How much control did you feel the consent form gave you over the amount of your personal information collected by the company?',
                        default=0,
                        )
    perceivedControlQ2 = DecimalRangeField(
                        '2. How much control did you feel the consent form gave you over who can get access to your personal information?',
                        default=0,
                        )
    perceivedControlQ3 = DecimalRangeField(
                        '3. How much control did you feel the consent form gave you over your personal information that has been released?',
                        default=0,
                        )
    perceivedControlQ4 = DecimalRangeField(
                        '4. How much control did you feel the consent form gave you over how your personal information is being used by the company?',
                        default=0,
                        )
    perceivedControlQ5 = DecimalRangeField(
                        '5. Overall, how much did the consent form made you feel in control over your personal information provided to the company?',
                        default=0,
                        )
    manipulationCheck = RadioField(
                        '1. Which option did you choose?',
                        choices=[('A', 'Agree'), ('DNA', 'Do Not Agree')],
                        validators=[InputRequired()]
                        )
    deliberation = DecimalRangeField(
                        '2. How much did you think about your decision before clicking on one option?',
                        default=0,
                        places=0
                        )
    submit = SubmitField(
                        'Next'
                        )


class PrivacyConcernsForm(FlaskForm):
    privacyConcernsQ1 = RadioField(
                        '1. Compared to others I’m more sensitive about the way online companies handle my personal information',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    privacyConcernsQ2 = RadioField(
                        '2. To me, it is the most important thing to keep my privacy intact from online companies',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    privacyConcernsQ3 = RadioField(
                        '3. I’m concerned about threats to my personal privacy today',
                        choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Somewhat Agree'), ('4', 'Neither Agree nor Disagree'), ('5', 'Somewhat Disagree'), ('6', 'Disagree'), ('7', 'Strongly Disagree')],
                        validators=[InputRequired()]
                        )
    correctDisplayed = RadioField(
                       'Were all websites and questionnaires of the study displayed correctly?',
                       choices=[('Y', 'Yes, all of them'), ('N', 'No, not all of them')],
                       validators=[InputRequired()]
                       )
    whichDevice = RadioField(
                       'On which device did you do the study?',
                       choices=[('PC', 'PC'), ('Phone', 'Phone'), ('Tablet', 'Tablet')],
                       validators=[InputRequired()]
                       )
    submit = SubmitField(
                        'Next'
                        )


class WebsiteDesignForm(FlaskForm):
    webDesignQ1 = DecimalRangeField(
                        '1. How appealing did you find the layout of this news website on first sight?',
                        default = 0
                        )
    webDesignQ2 = DecimalRangeField(
                        '2. How appealing did you find the colours of this news website on first sight?',
                        default = 0
                        )
    webDesignQ3 = DecimalRangeField(
                        '3. Overall, how appealing did you find the design of this website on first sight?',
                        default = 0
                        )
    submit = SubmitField(
                        'Next'
                        )

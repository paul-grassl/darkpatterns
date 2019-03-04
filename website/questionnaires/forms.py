from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import InputRequired


class ControlAndDeliberationForm(FlaskForm):
    perceivedControlQ1 = IntegerRangeField(
                        '1. How much control did you feel the consent form gave you over the amount of your personal information collected by the company?',
                        default=0,
                        )
    perceivedControlQ2 = IntegerRangeField(
                        '2. How much control did you feel the consent form gave you over who can get access to your personal information?',
                        default=0,
                        )
    perceivedControlQ3 = IntegerRangeField(
                        '3. How much control did you feel the consent form gave you over your personal information that has been released?',
                        default=0,
                        )
    perceivedControlQ4 = IntegerRangeField(
                        '4. How much control did you feel the consent form gave you over how your personal information is being used by the company?',
                        default=0,
                        )
    perceivedControlQ5 = IntegerRangeField(
                        '5. Overall, how much did the consent form made you feel in control over your personal information provided to the company?',
                        default=0,
                        )
    manipulationCheck = RadioField(
                        '1. Which option did you choose?',
                        choices=[('A', 'Agree'), ('DNA', 'Do Not Agree')],
                        validators=[InputRequired()]
                        )
    deliberation = IntegerRangeField(
                        '2. How much did you think about your decision before clicking on one option?',
                        default=0,
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
                       choices=[('PC', 'PC'), ('Tablet', 'Tablet'), ('Phone', 'Phone')],
                       validators=[InputRequired()]
                       )
    submit = SubmitField(
                        'Next'
                        )


class WebsiteDesignForm(FlaskForm):
    webDesignQ1 = IntegerRangeField(
                        '1. How appealing did you find the layout of this news website on first sight?',
                        default = 0
                        )
    webDesignQ2 = IntegerRangeField(
                        '2. How appealing did you find the colours of this news website on first sight?',
                        default = 0
                        )
    webDesignQ3 = IntegerRangeField(
                        '3. Overall, how appealing did you find the design of this website on first sight?',
                        default = 0
                        )
    submit = SubmitField(
                        'Next'
                        )

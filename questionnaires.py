from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired


class DemographicsForm(FlaskForm):
    Gender = RadioField(
                        'Gender',
                        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
                        validators=[DataRequired()]
                        )
    Age = IntegerField(
                        'Age',
                        validators=[DataRequired()]
                        )
    Nationality = StringField(
                        'Nationality',
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )


class PerceivedControlForm(FlaskForm):
    PerceivedControlQ1 = RadioField(
                        'How much control did you feel the consent form gave you over the amount of your personal information collected by the company?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Complete')],
                        validators=[DataRequired()]
                        )
    PerceivedControlQ2 = RadioField(
                        'How much control did you feel the consent form gave you over who can get access your personal information?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Complete')],
                        validators=[DataRequired()]
                        )
    PerceivedControlQ3 = RadioField(
                        'How much control did you feel the consent form gave you over your personal information that has been released?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Complete')],
                        validators=[DataRequired()]
                        )
    PerceivedControlQ4 = RadioField(
                        'How much control did you feel the consent form gave you over how your personal information is being used by the company?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Complete')],
                        validators=[DataRequired()]
                        )
    PerceivedControlQ5 = RadioField(
                        'Overall, how much did the consent form made you feel in control over your personal information provided to the company?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Complete')],
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )


class DeliberationForm(FlaskForm):
    ManipulationCheck = RadioField(
                        'Which option did you choose?',
                        choices=[('A', 'Agree'), ('DNA', 'Do Not Agree')],
                        validators=[DataRequired()]
                        )
    Deliberation = RadioField(
                        'How much did you think about your decision before clicking on one option?',
                        choices=[('1', 'None at all'), ('2', ''), ('3', ''), ('4', ''), ('5', 'A great deal')],
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )


class PrivacyConcernsForm(FlaskForm):
    PrivacyConcernsQ1 = RadioField(
                        'Compared to others I’m more sensitive about the way online companies handle my personal information',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    PrivacyConcernsQ2 = RadioField(
                        'To me, it is the most important thing to keep my privacy intact from online companies',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    PrivacyConcernsQ3 = RadioField(
                        'I’m concerned about threats to my personal privacy today',
                        choices=[('1', 'Strongly Disagree'), ('2', ''), ('3', ''), ('4', ''), ('5', ''), ('6', ''), ('7', 'Strongly Agree')],
                        validators=[DataRequired()]
                        )
    Submit = SubmitField(
                        'Next'
                        )

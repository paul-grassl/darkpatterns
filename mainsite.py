from flask import Flask, render_template, url_for, redirect
from questionnaires import DemographicsForm, PerceivedControlForm, DeliberationForm, PrivacyConcernsForm
app = Flask(__name__)


# At some point you will want to make this an environment variable
app.config['SECRET_KEY'] = 'd0e4240e6fb74743016fed54800852f8'


# Atm I'm just rendering templates directly. We will probably need to change
# this to redirecting to a link (one of our bought domains) later on
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/welcome")
def welcome():
    return render_template('welcome.html', title='Welcome')


@app.route("/newswebsite1")
def newswebsite1():
    return render_template('newswebsite1_viral.html')


# Route to our demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = DemographicsForm()
    return render_template('demographics.html', title='Demographic Information', form=form)


# Route to our demographic information form
@app.route("/questionnaire1")
def perceived_control():
    form = PerceivedControlForm()
    return render_template('perceived_control.html', title='Perceived Control', form=form)


def deliberation():
    form = DeliberationForm()
    return render_template('deliberation.html', title='Deliberation', form=form)


@app.route("/questionnaire2")
def privacy_concerns():
    form = PrivacyConcernsForm()
    return render_template('privacy_concerns.html', title='Privacy Attitude', form=form)


# This will run the application in debug mode by default, we may want to change
# that before going online
if __name__ == '__main__':
    app.run(debug=True)

# Next steps:
# - how to adjust DecimalRangeField in terms of width (not full screen) and
# labeling on both sides (left,right)
# - Radiofield, how to validate prpoerly and make horizontal

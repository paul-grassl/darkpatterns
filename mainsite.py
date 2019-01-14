from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from questionnaires import demographicsForm, websiteDesignForm, controlAndDeliberationForm, privacyConcernsForm
import random
import stimuliList, security


app = Flask(__name__)
# at some point you will want to make this an environment variable
app.config['SECRET_KEY'] = 'd0e4240e6fb74743016fed54800852f8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sona:{}@82.215.18.140/db'.format(security.password)
db = SQLAlchemy(app)


# modals for database structure
class Participant(db.Modal):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(1), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

class Consent(db.Modal):
    trial = db.Column(db.Integer, nullable=False)
    default= db.Column(db.Integer, nullable=False)
    aesthetic = db.Column(db.Integer, nullable=False)
    obstruction = db.Column(db.Integer, nullable=False)
    decision = db.Column(db.Integer, nullable=False)

class
    privatt = db.Column(db.Integer, nullable=False)
    percontrol = db.Column(db.Integer, nullable=False)
    deliberation = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Participant('')"


# make a list of all websites and then shuffle randomly for each participant
websiteList = list(stimuliList.stimuli.keys())


@app.route("/welcome")
def welcome():
    return render_template('welcome.html', title='Welcome')


@app.route("/newswebsite1")
def newsWebsite1():
    return render_template('newswebsite1_viral.html')


# route to our demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = demographicsForm()
    if form.validate_on_submit():
        # randomize websiteList
        randomWebsiteList = random.sample(websiteList, len(websiteList))
        return redirect(randomWebsiteList[0])
    return render_template('demographics.html', title='Demographic Information', form=form)


@app.route("/newswebsitedesign", methods=['GET', 'POST'])
def websiteDesign():
    form = websiteDesignForm()


# route to perceived control and deliberation form
@app.route("/questionnaire1", methods=['GET', 'POST'])
def controlAndDeliberation():
    form = controlAndDeliberationForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('controlAndDeliberation.html', title='Control and deliberation', form=form)


# route to privacy concerns form
# the redirect link needs to be back to SONA in the end
@app.route("/questionnaire2", methods=['GET', 'POST'])
def privacyConcerns():
    form = privacyConcernsForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('privacyConcerns.html', title='Privacy Attitude', form=form)


# This will run the application in debug mode by default, we may want to change
# that before going online
if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, url_for, redirect, request
from website import app, db
from website.models import demographicData, controlAndDeliberationData, privacyConcernsData
from website.questionnaires import demographicsForm, websiteDesignForm, controlAndDeliberationForm, privacyConcernsForm, welcomeForm
import random
from website import stimuliList


# make a list of all websites and then shuffle randomly for each participant
websiteList = list(stimuliList.stimuli.keys())


# route to welcome page with permission statement and consent form
@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    form = welcomeForm()
    if form.validate_on_submit():
        if request.form['consent'] == 'A':
            return redirect(url_for('demographics'))
        else:
            return redirect('https://www.google.com')
    return render_template('welcome.html', title='Welcome', form=form)


# route to demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = demographicsForm()
    if form.validate_on_submit():
        # randomize websiteList
        randomWebsiteList = random.sample(websiteList, len(websiteList))
        # save data to db
        participant = demographicData(gender=form.gender.data, age=form.age.data, nationality=form.nationality.data)
        db.session.add(participant)
        db.session.commit()
        return redirect(randomWebsiteList[0])
    return render_template('demographics.html', title='Demographic Information', form=form)


# route to cover-story questionnaire
@app.route("/newswebsitedesign", methods=['GET', 'POST'])
def websiteDesign():
    form = websiteDesignForm()
    return render_template('websiteDesign.html', title='News website design', form=form)


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

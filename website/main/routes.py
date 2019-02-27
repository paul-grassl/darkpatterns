from flask import Blueprint, request, session, redirect, render_template, url_for
from website.main.forms import WelcomeForm, DemographicsForm
from website import stimuli
from website import db
from website.models import DemographicData
import random
import json


main = Blueprint('main', __name__)

# make a list of all websites and then shuffle randomly for each participant
websiteList = list(stimuli.stimuliDict.keys())


@main.before_request
def make_session_permanent():
    session.permanent = True


# route to welcome page with permission statement and consent form
@main.route("/welcome", methods=['GET', 'POST'])
def welcome():
    form = WelcomeForm()
    if form.validate_on_submit():
        if request.form['consent'] == 'A':
            return redirect(url_for('main.demographics'))
        else:
            return redirect(url_for('main.goodbye'))
    return render_template('welcome.html', title='Welcome', form=form)


# route if participant decides to leave the study
@main.route("/goodbye")
def goodbye():
    return render_template('goodbye.html', title='Goodbye')


# route to demographic information form
@main.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = DemographicsForm()
    if form.validate_on_submit():
        if 'anonymous_user_id' not in session:
            # randomize websiteList
            randomWebsiteList = random.sample(websiteList, len(websiteList))
            s_randomWebsiteList = json.dumps(randomWebsiteList)
            participant = DemographicData(gender=form.gender.data,
                                          age=form.age.data,
                                          nationality=form.nationality.data,
                                          websiteList=s_randomWebsiteList)
            # save to database
            db.session.add(participant)
            db.session.commit()
            print('demographics: participant id:', participant.id)
            session['anonymous_user_id'] = participant.id
            print('demographics: randomWebsiteList:', participant.websiteList)
            session['websiteList'] = participant.websiteList
            session['websiteList2'] = participant.websiteList
            return redirect(url_for('distributors.distributor'))
        else:
            return redirect(url_for('distributors.distributor'))
    return render_template('demographics.html', title='Demographic Information', form=form)


# route to thank you page
@main.route("/thankyou")
def thankYou():
    return render_template('thankYou.html', title='Thank you')

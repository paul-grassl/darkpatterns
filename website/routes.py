# import flask
from flask import render_template, url_for, redirect, request, session
from website import app, db
from website.models import DemographicData, ModalData, ControlAndDeliberationData, PrivacyConcernsData
from website.questionnaires import DemographicsForm, WebsiteDesignForm, ControlAndDeliberationForm, PrivacyConcernsForm, WelcomeForm
import random
from website import stimuliList


# make a list of all websites and then shuffle randomly for each participant
websiteList = list(stimuliList.stimuli.keys())


@app.before_request
def make_session_permanent():
    session.permanent = True


# route to welcome page with permission statement and consent form
@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    form = WelcomeForm()
    if form.validate_on_submit():
        if request.form['consent'] == 'A':
            return redirect(url_for('demographics'))
        else:
            return redirect('https://www.google.com')  # create some kind of goodbye page for all who leave
    return render_template('welcome.html', title='Welcome', form=form)


# route to demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = DemographicsForm()
    if form.validate_on_submit():
        # if session.new:
            # randomize websiteList
        randomWebsiteList = random.sample(websiteList, len(websiteList))
        participant = DemographicData(gender=form.gender.data,
                                      age=form.age.data,
                                      nationality=form.nationality.data,
                                      websiteList=str(randomWebsiteList))
        session.anonymous_user_id = participant.id
        # save to database
        db.session.add(participant)
        db.session.commit()
        # else:
        #     participant = DemographicData.query.get(session.anonymous_user_id)
        return redirect(url_for('megazine')) #randomWebsiteList[0]
    return render_template('demographics.html', title='Demographic Information', form=form)


# route to website 1: avision
@app.route("/avision", methods=['GET', 'POST'])
def avision():
    return render_template('/newswebsite_templates/avision/index.html', title='Avision')


# route to website 2: megazine
@app.route("/megazine", methods=['GET', 'POST'])
def megazine():
    if request.method == 'POST':
        consentDecision = ModalData(participant_bref=DemographicData.query.get(session.anonymous_user_id),
                                    consent=request.form['consentForm'])
        db.session.add(consentDecision)
        db.session.commit()
        return redirect(url_for('motivemag'))
    return render_template('/newswebsite_templates/megazine/index.html', title='Megazine')


# route to website 3: motivemag
@app.route("/motivemag", methods=['GET', 'POST'])
def motivemag():
    return render_template('/newswebsite_templates/motivemag/index.html', title='Motivemag')


# route to website 4: quitelight
@app.route("/quitelight", methods=['GET', 'POST'])
def quitelight():
    return render_template('/newswebsite_templates/quitelight/index.html', title='Quitelight')


# route to website 5: techmag
@app.route("/techmag", methods=['GET', 'POST'])
def techmag():
    return render_template('/newswebsite_templates/techmag/index.html', title='Techmag')


# route to website 6: technews
@app.route("/technews", methods=['GET', 'POST'])
def technews():
    return render_template('/newswebsite_templates/technews/index.html', title='Technews')


# route to website 7: viral
@app.route("/viral", methods=['GET', 'POST'])
def viral():
    return render_template('/newswebsite_templates/viral/index.html', title='Viral')


# route to website 8: webmag
@app.route("/webmag", methods=['GET', 'POST'])
def webmag():
    return render_template('/newswebsite_templates/webmag/index.html', title='Webmag')


# route to cover-story questionnaire
@app.route("/newswebsitedesign", methods=['GET', 'POST'])
def websiteDesign():
    form = WebsiteDesignForm()
    return render_template('websiteDesign.html', title='News website design', form=form)


# route to perceived control and deliberation form
@app.route("/questionnaire1", methods=['GET', 'POST'])
def controlAndDeliberation():
    form = ControlAndDeliberationForm()
    if form.validate_on_submit():
        questionnaire1Data = ControlAndDeliberationData(participant_bref=DemographicData.id,
                                                        perceivedControlQ1=form.perceivedControlQ1.data,
                                                        perceivedControlQ2=form.perceivedControlQ2.data,
                                                        perceivedControlQ3=form.perceivedControlQ3.data,
                                                        perceivedControlQ4=form.perceivedControlQ4.data,
                                                        perceivedControlQ5=form.perceivedControlQ5.data,
                                                        manipulationCheck=form.manipulationCheck.data,
                                                        deliberation=form.deliberation.data)
        db.session.add(questionnaire1Data)
        db.session.commit()
        return redirect(url_for())
    return render_template('controlAndDeliberation.html', title='Control and deliberation', form=form)


# route to privacy concerns form
# the redirect link needs to be back to SONA in the end
@app.route("/questionnaire2", methods=['GET', 'POST'])
def privacyConcerns():
    form = PrivacyConcernsForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('privacyConcerns.html', title='Privacy Attitude', form=form)

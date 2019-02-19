# import flask
from flask import render_template, url_for, redirect, request, session
from website import app, db
from website.models import DemographicData, ModalData, ControlAndDeliberationData, PrivacyConcernsData
from website.questionnaires import DemographicsForm, WebsiteDesignForm, ControlAndDeliberationForm, PrivacyConcernsForm, WelcomeForm
import random
import json
from website import stimuli


# make a list of all websites and then shuffle randomly for each participant
websiteList = list(stimuli.stimuliDict.keys())


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
            return redirect(url_for('goodbye'))
    return render_template('welcome.html', title='Welcome', form=form)


@app.route("/goodbye")
def goodbye():
    return render_template('goodbye.html', title='Goodbye')


# route to demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
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
            return redirect(url_for('distributor'))
        else:
            return redirect(url_for('distributor'))
    return render_template('demographics.html', title='Demographic Information', form=form)


# distributor route to news websites (randomization)
@app.route("/distributor")
def distributor():
    l_randomWebsiteList = json.loads(session['websiteList'])
    if len(l_randomWebsiteList) != 0:
        nextPage = l_randomWebsiteList[0]
        l_randomWebsiteList.pop(0)
        s_randomWebsiteList = json.dumps(l_randomWebsiteList)
        session['websiteList'] = s_randomWebsiteList
        print('s_randomWebsiteList:', s_randomWebsiteList)
        return redirect(url_for(nextPage))
    else:
        return redirect(url_for('distributor2'))  # redirect to next distributor which goes to different controlAndDeliberation questionnaires
    return render_template('redirecting.html', title='Redirecting')


# distributor 2 route to control and deliberation questionnaires (following the same order as news websites were presented)
@app.route("/distributor2")
def distributor2():
    l_randomWebsiteList = json.loads(session['websiteList2'])
    if len(l_randomWebsiteList) != 0:
        nextScreenshot = stimuli.stimuliDict.get(l_randomWebsiteList[0])
        session['nextScreenshot'] = nextScreenshot
        l_randomWebsiteList.pop(0)
        s_randomWebsiteList = json.dumps(l_randomWebsiteList)
        session['websiteList2'] = s_randomWebsiteList
        print('s_randomWebsiteList:', s_randomWebsiteList)
        return redirect(url_for('questionnaire1'))
    else:
        return redirect(url_for('questionnaire2'))
    return render_template('redirecting.html', title='Redirecting')


# route to website 1: avision
@app.route("/avision", methods=['GET', 'POST'])
def avision():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='avision',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/avision/index2.html', title='Avision')

        else:
            return render_template('/newswebsite_templates/avision/index2.html', title='Avision')
    return render_template('/newswebsite_templates/avision/index.html', title='Avision')


# route to website 2: megazine
@app.route("/megazine", methods=['GET', 'POST'])
def megazine():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='megazine',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/megazine/index2.html', title='Megazine')
        else:
            return render_template('/newswebsite_templates/megazine/index2.html', title='Megazine')
    return render_template('/newswebsite_templates/megazine/index.html', title='Megazine')


# route to website 3: motivemag
@app.route("/motivemag", methods=['GET', 'POST'])
def motivemag():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='motivemag',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/motivemag/index2.html', title='Motivemag')
        else:
            return render_template('/newswebsite_templates/motivemag/index2.html', title='Motivemag')
    return render_template('/newswebsite_templates/motivemag/index.html', title='Motivemag')


# route to website 4: quitelight
@app.route("/quitelight", methods=['GET', 'POST'])
def quitelight():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='quitelight',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/quitelight/index2.html', title='Quitelight')
        else:
            return render_template('/newswebsite_templates/quitelight/index2.html', title='Quitelight')
    return render_template('/newswebsite_templates/quitelight/index.html', title='Quitelight')


# route to website 5: techmag
@app.route("/techmag", methods=['GET', 'POST'])
def techmag():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='techmag',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/techmag/index2.html', title='Techmag')
        else:
            return render_template('/newswebsite_templates/techmag/index2.html', title='Techmag')
    return render_template('/newswebsite_templates/techmag/index.html', title='Techmag')


# route to website 6: technews
@app.route("/technews", methods=['GET', 'POST'])
def technews():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='technews',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/technews/index2.html', title='Technews')
        else:
            return render_template('/newswebsite_templates/technews/index2.html', title='Technews')
    return render_template('/newswebsite_templates/technews/index.html', title='Technews')


# route to website 7: viral
@app.route("/viral", methods=['GET', 'POST'])
def viral():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='viral',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/viral/index2.html', title='Viral')
        else:
            return render_template('/newswebsite_templates/viral/index2.html', title='Viral')
    return render_template('/newswebsite_templates/viral/index.html', title='Viral')


# route to website 8: webmag
@app.route("/webmag", methods=['GET', 'POST'])
def webmag():
    if request.method == 'POST':
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            consentDecision = ModalData(participant_bref=participant,
                                        currentWebsite='webmag',
                                        consent=request.form['consentForm'])
            db.session.add(consentDecision)
            db.session.commit()
            return render_template('/newswebsite_templates/webmag/index2.html', title='Webmag')
        else:
            return render_template('/newswebsite_templates/webmag/index2.html', title='Webmag')
    return render_template('/newswebsite_templates/webmag/index.html', title='Webmag')


# route to cover-story questionnaire
@app.route("/newswebsitedesign", methods=['GET', 'POST'])
def websiteDesign():
    form = WebsiteDesignForm()
    if form.validate_on_submit():
        return redirect(url_for('distributor'))
    return render_template('websiteDesign.html', title='News website design', form=form)


# route to perceived control and deliberation form
@app.route("/questionnaire1", methods=['GET', 'POST'])
def controlAndDeliberation():
    form = ControlAndDeliberationForm()
    if form.validate_on_submit():
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            nextScreenshot = session['nextScreenshot']
            questionnaire1Data = ControlAndDeliberationData(participant_bref=participant,
                                                            perceivedControlQ1=form.perceivedControlQ1.data,
                                                            perceivedControlQ2=form.perceivedControlQ2.data,
                                                            perceivedControlQ3=form.perceivedControlQ3.data,
                                                            perceivedControlQ4=form.perceivedControlQ4.data,
                                                            perceivedControlQ5=form.perceivedControlQ5.data,
                                                            manipulationCheck=form.manipulationCheck.data,
                                                            deliberation=form.deliberation.data)
            db.session.add(questionnaire1Data)
            db.session.commit()
            return redirect(url_for('distributor2'))
        else:
            return redirect(url_for('distributor2'))
    return render_template('controlAndDeliberation.html', title='Control and deliberation', form=form, screenshot=nextScreenshot)


# route to privacy concerns form
# the redirect link needs to be back to SONA in the end (maybe you have to fetch the id from the incoming url in the beginning , save it to a session object and retrieve it here to redirect correctly back to SONA)
@app.route("/questionnaire2", methods=['GET', 'POST'])
def privacyConcerns():
    form = PrivacyConcernsForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('privacyConcerns.html', title='Privacy Attitude', form=form)

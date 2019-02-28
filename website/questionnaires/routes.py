from flask import Blueprint, render_template, url_for, redirect, session
from website import db
from website.models import DemographicData, ControlAndDeliberationData, PrivacyConcernsData
from website.questionnaires.forms import WebsiteDesignForm, ControlAndDeliberationForm, PrivacyConcernsForm

questionnaires = Blueprint('questionnaires', __name__)


# route to cover-story questionnaire
@questionnaires.route("/newswebsitedesign", methods=['GET', 'POST'])
def website_design():
    form = WebsiteDesignForm()
    if form.validate_on_submit():
        return redirect(url_for('distributors.distributor'))
    return render_template('website_design.html', title='News website design', form=form)


# route to perceived control and deliberation form
@questionnaires.route("/questionnaire1", methods=['GET', 'POST'])
def control_and_deliberation():
    nextScreenshot = session['nextScreenshot']
    currentWebsite = session['currentWebsite']
    form = ControlAndDeliberationForm()
    if form.validate_on_submit():
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            questionnaire1Data = ControlAndDeliberationData(participant_bref=participant,
                                                            currentWebsite=currentWebsite,
                                                            perceivedControlQ1=form.perceivedControlQ1.data,
                                                            perceivedControlQ2=form.perceivedControlQ2.data,
                                                            perceivedControlQ3=form.perceivedControlQ3.data,
                                                            perceivedControlQ4=form.perceivedControlQ4.data,
                                                            perceivedControlQ5=form.perceivedControlQ5.data,
                                                            manipulationCheck=form.manipulationCheck.data,
                                                            deliberation=form.deliberation.data)
            db.session.add(questionnaire1Data)
            db.session.commit()
            return redirect(url_for('distributors.distributor2'))
        else:
            return redirect(url_for('distributors.distributor2'))
    return render_template('control_and_deliberation.html', title='Questionnaire', form=form, screenshot=nextScreenshot)


# route to privacy concerns form
# the redirect link needs to be back to SONA in the end (maybe you have to fetch the id from the incoming url in the beginning , save it to a session object and retrieve it here to redirect correctly back to SONA)
@questionnaires.route("/questionnaire2", methods=['GET', 'POST'])
def privacy_concerns():
    form = PrivacyConcernsForm()
    if form.validate_on_submit():
        if 'anonymous_user_id' in session:
            participant = DemographicData.query.get(session['anonymous_user_id'])
            questionnaire2Data = PrivacyConcernsData(participant_bref=participant,
                                                     privacyConcernsQ1=form.privacyConcernsQ1.data,
                                                     privacyConcernsQ2=form.privacyConcernsQ2.data,
                                                     privacyConcernsQ3=form.privacyConcernsQ3.data,
                                                     correctDisplayed=form.correctDisplayed.data,
                                                     whichDevice=form.whichDevice.data)
            db.session.add(questionnaire2Data)
            db.session.commit()
            return redirect(url_for('main.thank_you'))
        else:
            return redirect(url_for('main.thank_you'))
    return render_template('privacy_concerns.html', title='Questionnaire', form=form)

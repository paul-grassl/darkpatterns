from flask import Blueprint, request, session, render_template
from website import db
from website.models import DemographicData, ModalData

news_websites = Blueprint('news_websites', __name__)


# route to website 1: avision
@news_websites.route("/avision", methods=['GET', 'POST'])
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
@news_websites.route("/megazine", methods=['GET', 'POST'])
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
@news_websites.route("/motivemag", methods=['GET', 'POST'])
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
@news_websites.route("/quitelight", methods=['GET', 'POST'])
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
@news_websites.route("/techmag", methods=['GET', 'POST'])
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
@news_websites.route("/technews", methods=['GET', 'POST'])
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
@news_websites.route("/viral", methods=['GET', 'POST'])
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
@news_websites.route("/webmag", methods=['GET', 'POST'])
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

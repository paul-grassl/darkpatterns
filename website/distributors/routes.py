from flask import Blueprint, session, redirect, render_template, url_for
from website import stimuli
import json


distributors = Blueprint('distributors', __name__)


# distributor route to news websites (randomization)
@distributors.route("/distributor")
def distributor():
    l_randomWebsiteList = json.loads(session['websiteList'])
    if len(l_randomWebsiteList) != 0:
        nextPage = l_randomWebsiteList[0]
        l_randomWebsiteList.pop(0)
        s_randomWebsiteList = json.dumps(l_randomWebsiteList)
        session['websiteList'] = s_randomWebsiteList
        print('s_randomWebsiteList:', s_randomWebsiteList)
        return redirect(url_for('news_websites.' + nextPage))
    else:
        return redirect(url_for('main.half_way'))  # redirect to next distributor which goes to different controlAndDeliberation questionnaires
    return render_template('redirecting.html', title='Redirecting')


# distributor 2 route to control and deliberation questionnaires (following the same order as news websites were presented)
@distributors.route("/distributor2")
def distributor2():
    l_randomWebsiteList = json.loads(session['websiteList2'])
    if len(l_randomWebsiteList) != 0:
        nextScreenshot = stimuli.stimuliDict.get(l_randomWebsiteList[0])
        session['nextScreenshot'] = nextScreenshot
        currentWebsite = l_randomWebsiteList[0]
        session['currentWebsite'] = currentWebsite
        l_randomWebsiteList.pop(0)
        s_randomWebsiteList = json.dumps(l_randomWebsiteList)
        session['websiteList2'] = s_randomWebsiteList
        print('s_randomWebsiteList:', s_randomWebsiteList)
        print('nextScreenshot:', nextScreenshot)
        return redirect(url_for('questionnaires.control_and_deliberation'))
    else:
        return redirect(url_for('questionnaires.privacy_concerns'))
    return render_template('redirecting.html', title='Redirecting')

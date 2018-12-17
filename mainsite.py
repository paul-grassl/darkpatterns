from flask import Flask, render_template, url_for, redirect
from questionnaires import DemographicsForm, ControlAndDeliberationForm, PrivacyConcernsForm
app = Flask(__name__)


# At some point you will want to make this an environment variable
app.config['SECRET_KEY'] = 'd0e4240e6fb74743016fed54800852f8'


# atm I'm just rendering templates directly. We will probably need to change
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


# route to our demographic information form
@app.route("/demographics", methods=['GET', 'POST'])
def demographics():
    form = DemographicsForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('demographics.html', title='Demographic Information', form=form)


# route to perceived control and deliberation form
@app.route("/questionnaire1", methods=['GET', 'POST'])
def control_and_deliberation():
    form = ControlAndDeliberationForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('control_and_deliberation.html', title='Control and deliberation', form=form)


# route to privacy concerns form
# the redirect link needs to be back to SONA in the end
@app.route("/questionnaire2", methods=['GET', 'POST'])
def privacy_concerns():
    form = PrivacyConcernsForm()
    if form.validate_on_submit():
        return redirect(url_for())
    return render_template('privacy_concerns.html', title='Privacy Attitude', form=form)


# This will run the application in debug mode by default, we may want to change
# that before going online
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for, redirect
from questionnaires import demographicsForm, controlAndDeliberationForm, privacyConcernsForm
import randomization
app = Flask(__name__)


# At some point you will want to make this an environment variable
app.config['SECRET_KEY'] = 'd0e4240e6fb74743016fed54800852f8'


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
        return redirect(list(randomization.stimuli.keys())[0])
    return render_template('demographics.html', title='Demographic Information', form=form)


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

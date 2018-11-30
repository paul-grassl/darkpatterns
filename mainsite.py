from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


# Atm I'm just rendering templates directly. We will probably need to change
# this to redirecting to a link (one of our bought domains) later on
@app.route("/")
def index():
    return render_template('index.html')


# This will run the application in debug mode by default, we may want to change
# that before going online
if __name__ == '__main__':
    app.run(debug=True)

# Next steps:
# - Create a study index file which will show the consent statement for the
# study
# - Then change your folder system for the newswebsites so they are separate
# from your RU-hosted templates (study index.html)
# - Search for Survey html templates online for your (own) consent statement
# and the questionnaires

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.security import secretKey


app = Flask(__name__)
app.config['SECRET_KEY'] = secretKey
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from website import routes

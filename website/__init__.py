from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website.config import Config

db = SQLAlchemy()


# create application factory to make multiple configurations easy managable
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from website.main.routes import main
    from website.distributors.routes import distributors
    from website.news_websites.routes import news_websites
    from website.questionnaires.routes import questionnaires
    from website.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(distributors)
    app.register_blueprint(news_websites)
    app.register_blueprint(questionnaires)
    app.register_blueprint(errors)

    # with app.app_context():
    #     db.create_all()

    return app

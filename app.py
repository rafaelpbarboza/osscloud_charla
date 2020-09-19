from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config='settings'):
    app = Flask(__name__)
    app.config.from_object(config)

    from json_rest import json_bp
    from rest import rest_bp
    from web_scraping import web_scraping

    app.register_blueprint(json_bp)
    app.register_blueprint(rest_bp)
    app.register_blueprint(web_scraping)
    registers_app(app)
    return app


def registers_app(app):
    database = db.init_app(app)
    migrate.init_app(app, database)


migrate = Migrate(create_app, db)

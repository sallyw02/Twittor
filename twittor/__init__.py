# this must come after bc route.py needs to import db first
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from twittor.config import Config 

db = SQLAlchemy()  # need to set up db first
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:twittor.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # only call this after db set up (route uses db)
    from twittor.route import index, login

    # same as @app.route('/') in old app.py
    app.add_url_rule('/', 'index', index)
    # 1st param: change endpoint URL HERE!!
    # 2nd param: internal naming of endpoint
    # 3rd param: call the index function defined in route.py
    # You could use url_for('index') in templates or other parts of your code to dynamically generate the URL for this route.

    # default is http GET, so cannot get valid data
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app

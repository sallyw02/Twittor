from flask import Flask
from twittor.route import index, login


def create_app():
    app = Flask(__name__)
    # same as @app.route('/') in old app.py
    app.add_url_rule('/', 'index', index)
    # 1st param: change endpoint URL HERE!!
    # 2nd param: internal naming of endpoint
    # 3rd param: call the index function defined in route.py
    # You could use url_for('index') in templates or other parts of your code to dynamically generate the URL for this route.

    # default is http GET, so cannot get valid data
    app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
    return app

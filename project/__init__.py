# STEPS :
# 1) python3 -m venv auth ==> For creating the py environment 
# 2) source auth/bin/activate ==> For connecting to the environment
# 3) pip install flask flask-sqlalchemy flask-login ==> Simply installing the requierments
# 4) export FLASK_APP=project
# 5) export FLASK_DEBUG=1

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app() :
    app = Flask(__name__)

    app.config['SECRET_KEY'] = ""
    app.config['SQLALCHEMY_DATABASE_URI'] = ""

    db.init_app(app)

    # Blueprint for auth routes in the app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for non-auth parts of the app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
    
from flask import Blueprint
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login() :
    return "Login"

@auth.route('/signup')
def signup() :
    return "Signup"

@auth.route("/Logout")
def logout() :
    return "Logout"        
    
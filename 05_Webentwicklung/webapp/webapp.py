# erstmal import
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

webapp = Flask(__name__)
webapp.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://...'
db = SQLAlchemy(webapp)


# Route's
@webapp.route("/")
@webapp.route("/home")
def home():
    return render_template("home.html")
@webapp.route("/about")
def about():
    return render_template("about.html")
@webapp.route("/register")
def register():
    return render_template("register.html")
@webapp.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    webapp.run(debugg=True)

''' test
@webapp.route("/")
def test():
    return "<h1>Willkomen in die mega Inteligente Systeme von SCALTEL</h1>"
'''
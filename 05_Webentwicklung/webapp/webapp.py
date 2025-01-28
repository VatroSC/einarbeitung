from flask import Flask # erstmal import

webapp = Flask(__name__)

@webapp.route("/")
def test():
    return "<h1>Willkomen in die mega Inteligente Systeme von SCALTEL</h1>"
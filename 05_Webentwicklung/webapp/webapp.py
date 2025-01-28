from flask import Flask, render_template # erstmal import
from flask import request, jsonify
# <link rel="stylesheet" href="{{url_for('static', irgeneinname='styles.css') }}">
webapp = Flask(__name__)

''' test
@webapp.route("/")
def test():
    return "<h1>Willkomen in die mega Inteligente Systeme von SCALTEL</h1>"
'''
@webapp.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    webapp.run(debugg=True)

@webapp.route("/json")
def test():
    return jsonify({"mesagge": "Hello JSON"})
    
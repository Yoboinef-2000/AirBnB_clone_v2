#!/usr/bin/python3

"""This script starts a Flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloHBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def displayC(text):
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(debug=True)

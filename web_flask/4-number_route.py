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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def displayPython(text="is cool"):
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def displayNumber(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True)

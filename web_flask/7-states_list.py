#!/usr/bin/python3

"""This script starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def tearItAllUp(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def statesList():
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(debug=True)

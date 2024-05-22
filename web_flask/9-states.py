#!/usr/bin/python3
"""Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def tearItAllUp(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def states_cities(state_id):
    state = storage.get(State, state_id)
    if state:
        return render_template('9-states.html', states=[state])
    else:
        return render_template('9-states.html', states=[])


if __name__ == "__main__":
    app.run(debug=True)

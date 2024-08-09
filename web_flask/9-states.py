#!/usr/bin/python3
"""
beggining of all  a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """display the states and cities listed in alphabetical order"""
    state = None
    for state_s in storage.all("State").values():
        if state_s.id == id:
            state = state_s
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
#!/usr/bin/python3
"""Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""script that starts
a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """this will be list all states"""
    all_states = sorted(list(storage.all("State").values()),
                        key=lambda st: st.name)
    return (render_template('7-states_list.html', states=all_states))


@app.teardown_appcontext
def db_closer(e):
    """and this will be close database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

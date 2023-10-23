#!/usr/bin/python3
"""script that starts
a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters(state_id=None):
    """this will be list all states"""
    all_states = storage.all("State").values()
    all_amenities = storage.all("Amenity").values()
    return (render_template('10-hbnb_filters.html',
                            states=all_states,
                            amenities=all_amenities))


@app.teardown_appcontext
def db_closer(e):
    """this will be close database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

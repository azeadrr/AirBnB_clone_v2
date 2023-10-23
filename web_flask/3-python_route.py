#!/usr/bin/python3
"""script that starts
a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """display Hello HBNB!"""
    return ('Hello HBNB!')


@app.route('/hbnb')
def home_hbnb():
    """ display HBNB"""
    return ('HBNB')


@app.route('/c/<text>')
def c_text(text):
    """display C followed by the value of the text"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def py_text(text=None):
    """display followed by the value of the text"""
    if (text is None):
        return ("Python is cool")
    else:
        return("Python {}".format(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

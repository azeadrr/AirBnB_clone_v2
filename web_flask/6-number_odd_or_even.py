#!/usr/bin/python3
"""script that starts
a Flask web application"""
from flask import Flask, render_template

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
    """display followed by the value of the text"""
    return("C {}".format(text.replace("_", " ")))


@app.route('/python/')
@app.route('/python/<text>')
def py_text(text=None):
    """display Python followed by the value of the text variable """
    if (text is None):
        return ("Python is cool")
    else:
        return("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>')
def temp_n(n):
    """display n is a number only if n is an integer"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def temp_n_check(n):
    """display a HTML page only if n is an integer"""
    return (render_template('5-number.html', number=n))


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """display a HTML page only if n is an integer"""
    return (render_template('6-number_odd_or_even.html', number=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

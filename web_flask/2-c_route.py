#!/usr/bin/python3
""" starts Flask """

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c():
    """ return C """
    return 'C'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

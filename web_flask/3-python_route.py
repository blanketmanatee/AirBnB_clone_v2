#!/usr/bin/python3
""" starts Flask """

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return C """
    replace = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route('/python/', defaults={"text": "is cool"})
@app.route('/python/(<text>)', strict_slashes=False)
def python(text):
    """ return Python """
    replace = text.replace("_", " ")
    return 'Python {}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

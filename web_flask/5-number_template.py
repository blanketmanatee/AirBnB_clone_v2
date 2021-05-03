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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return 'n is a number' """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ return html page if n is an int """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
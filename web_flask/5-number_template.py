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
def c(text):
    """ return C """
    return 'C'

@app.route('/python/(<text>)', strict_slashes=False)
def python(text='is cool'):
    """ return Python """
    return 'Python'

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return 'n is a number' """
    return 'n is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ return html page if n is an int """
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

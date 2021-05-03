#!/usr/bin/python3
""" starts Flask """

from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return Hello HBNB! """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
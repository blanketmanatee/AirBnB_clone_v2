#!/usr/bin/python3
""" starts Flask """

from flash import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return Hello HBNB! """
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port='5000')

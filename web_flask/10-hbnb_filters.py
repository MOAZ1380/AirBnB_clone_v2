#!/usr/bin/python3
"""
beggining of all  a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()
    
@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ hbnb_filters """
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
# all the imports
import os
import sqlite3
import Adafruit_PCA9685
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from werkzeug.utils import find_modules, import_string
from flask_cors import CORS

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , robot.py

app.config.update(dict(
    SECRET_KEY='development key',
))

app.config.from_envvar('ROBOT_SETTINGS', silent=True)

cors = CORS(app)

def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('robot.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None

register_blueprints(app)

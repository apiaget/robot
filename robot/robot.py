# all the imports
import os
import sqlite3
import Adafruit_PCA9685
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , robot.py

app.config.update(dict(
    SECRET_KEY='development key',
))

app.config.from_envvar('ROBOT_SETTINGS', silent=True)

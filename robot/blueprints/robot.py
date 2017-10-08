import Adafruit_PCA9685
import time
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app, jsonify, Response, json
from flask_cors import CORS, cross_origin

bp = Blueprint('robot', __name__)

pwm = Adafruit_PCA9685.PCA9685()
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
pwm.set_pwm_freq(60)

@bp.route('/')
def index():
    dict = {"robot": "v1"}
    resp = Response(json.dumps(dict), mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@bp.route('/activate', methods = ['POST', 'OPTIONS'])
@cross_origin()
def activate():
     resp = Response(json.dumps(request.json), mimetype='appliaction/json')
     return resp

@bp.route('/stop', methods = ['POST'])
@cross_origin()
def stop():
     resp = Response(json.dumps(request.json), mimetype='application/json')
     return resp


#    while True:
        # Move servo on channel O between extremes.
#        pwm.set_pwm(0, 0, servo_min)
#        time.sleep(1)
#        pwm.set_pwm(0, 0, servo_max)
#        time.sleep(1)
#    return render_template('index.html')

import Adafruit_PCA9685
import time
import threading

from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app, jsonify, Response, json
from flask_cors import CORS, cross_origin

bp = Blueprint('robot', __name__)

pwm = Adafruit_PCA9685.PCA9685()

servo_1_status = False
servo_1_position = 150

servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
pwm.set_pwm_freq(60)

@bp.route('/')
def index():
    dict = {"robot": "v1"}
    resp = Response(json.dumps(dict), mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@bp.route('/activate', methods = ['POST'])
@cross_origin()
def activate():
     global servo_1_status
     servo_1_status = True
     global t1
     t1 = threading.Thread(target = move, args = ())
     t1.start()
     resp = Response(json.dumps(request.json), mimetype='appliaction/json')
     return resp

@bp.route('/stop', methods = ['POST'])
@cross_origin()
def stop():
     global servo_1_status
     servo_1_status = False
     resp = Response(json.dumps(request.json), mimetype='application/json')
     return resp

def move():
     print(servo_1_status)
     while servo_1_status:
          global servo_1_position
          print(servo_1_position)
          servo_1_position = servo_1_position + 5
          pwm.set_pwm(0, 0, servo_1_position)
          time.sleep(0.2)

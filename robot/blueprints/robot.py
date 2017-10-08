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

servos = [[],[]]
servos[0].append(False)
servos[0].append(150)
servos[0].append(1)
servos[1].append(False)
servos[1].append(150)
servos[1].append(1)

#servo_min = 150  # Min pulse length out of 4096
#servo_max = 600  # Max pulse length out of 4096
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
     global t1
     t1 = threading.Thread(target = move, args = ())
     t1.start()
     global servos
     servos[0][0] = True
     rotation = request.json['rotation']

     if(rotation == 1 or rotation == -1):
          servos[0][2] = rotation
     else:
          print("faux")

     resp = Response(json.dumps(request.json), mimetype='appliaction/json')
     return resp

@bp.route('/stop', methods = ['POST'])
@cross_origin()
def stop():
     global servos
     servos[0][0] = False
#     global servo_1_status
#     servo_1_status = False
     resp = Response(json.dumps(request.json), mimetype='application/json')
     return resp

def move():
     print(servos[0][0])
     while servos[0][0]:
          print(servos[0][1])
          servos[0][1] = servos[0][1] +  (6 * servos[0][2])
          pwm.set_pwm(0, 0, servos[0][1])
          time.sleep(0.1)

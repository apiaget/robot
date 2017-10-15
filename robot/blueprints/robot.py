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

SERVO_MAX = 4

current_servo = 0

servos = [[],[]]
servos[0].append(False) #le servo tourne ?
servos[0].append(410)   #emplacement de la rotation
servos[0].append(1)     #sens de rotation
servos[0].append(160)   #minimum
servos[0].append(660)   #maximum
servos[0].append(5)     #servo speed
servos[1].append(False)
servos[1].append(410)
servos[1].append(1)
servos[1].append(160)
servos[1].append(660)
servos[1].append(10)

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

#    global servos
     #servos[0][0] = True

     rotation = request.json['rotation']
     servoid = request.json['id']

     if(isinstance( servoid, int ) == False or servoid > SERVO_MAX or servoid <= 0):
          dict = {"robot": "v1", "error": "Pas un nombre ou nombre trop grand !"}
          resp = Response(json.dumps(dict), mimetype='application/json')
          return resp
     else:
          servoid = servoid - 1

     if(isinstance( rotation, int) == False or (rotation  != 1 and rotation != -1)):
          dict = {"robot": "v1", "error": "Sens de rotation non valide !"}
          resp = Response(json.dumps(dict), mimetype='application/json')
          return resp

#     servos[0][2] = rotation
     global servos
     servos[servoid][0] = True
     servos[servoid][2] = rotation

     global current_servo
     current_servo = servoid
     print(servoid)
     print(servos[servoid][1])

     resp = Response(json.dumps(request.json), mimetype='appliaction/json')
     return resp

@bp.route('/stop', methods = ['POST'])
@cross_origin()
def stop():
     global servos
     servos[current_servo][0] = False
#     global servo_1_status
#     servo_1_status = False
     resp = Response(json.dumps(request.json), mimetype='application/json')
     return resp

def move():
     global servos
     print("move")
#     print(current_servo)
#     print(servos[current_servo][1])
     while servos[current_servo][0]:
          print(servos[current_servo][1])
          newvalue = servos[current_servo][1] + (servos[current_servo][5] * servos[current_servo][2])
          if(newvalue >= servos[current_servo][3] and newvalue <= servos[current_servo][4]):
               servos[current_servo][1] = newvalue
               pwm.set_pwm(current_servo, 0, servos[current_servo][1])
               time.sleep(0.1)
          else:
               time.sleep(0.1)


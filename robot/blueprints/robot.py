import Adafruit_PCA9685
import time
from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app, jsonify, Response, json

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

#    return jsonify(
#        robot="v1"
#    )



#    while True:
        # Move servo on channel O between extremes.
#        pwm.set_pwm(0, 0, servo_min)
#        time.sleep(1)
#        pwm.set_pwm(0, 0, servo_max)
#        time.sleep(1)
#    return render_template('index.html')

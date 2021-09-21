__author__ = 'Changming'
from flask import Flask, request
from electric_service import ElectricService
import re

electric = Flask(__name__)
eService = ElectricService()

@electric.route('/')
def home():
    return "Hello world"

@electric.route('/api/<user_key>/limits')
def limits(user_key):
    requestData = {}
    requestData['user_id'] = eService.verify_user(user_key)
    if requestData['user_id']:
        return eService.get_data('limits',requestData), 200
    else:
        return {"error": "User key is not valid."}, 401

@electric.route('/api/<user_key>/data/<resolution>/<start>/<count>', methods=['POST'])
def data(user_key, resolution, start, count):
    allowed_resolution = ['days','months']
    requestData = {}
    requestData['user_id'] = eService.verify_user(user_key)
    if requestData['user_id']:
        if (resolution not in allowed_resolution):
            return {"error": "resolution is not valid, only days and months are valid."}, 415
        if (re.search('^20[0-9][0-9](-)(0[1-9]|1[0-2])(-)(0[1-9]|1[0-9]|2[0-9]|3[0-1])$', start) == None):
            return {"error": "start date is not valid, format should be xxxx-xx-xx."}, 414
        if (~isinstance(count, int)):
            return {"error": "count need to be an integer."}, 416
        requestData['period'] = resolution
        requestData['start'] = start
        requestData['count'] = count
        return eService.get_data('data',requestData), 200
    else:
        return {"error": "User key is not valid."}, 401
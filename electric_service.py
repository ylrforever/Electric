import sqlite3
import json
from limits_obj import limits_obj
from limits_obj import LimitsEncoder

class ElectricService:
    
    data = []
    connection = sqlite3.connect("test_data.db")
    def __init__(self):
        self.dataJson = json.dumps(self.data)

    def get_data(self, requestAction, requestData):
        responseData = {}
        cur = self.connection.cursor()
        if requestAction == 'data':
            responseData['data'] = []
            query = 'SELECT `timestamp`, consumption, temperature FROM ' + requestData['period'] + ' WHERE user_id = ' + requestData['user_id'] + ' AND `timestamp` >= "' +  requestData['start'] + '" LIMIT ' + requestData['count']
            print (query)
            i = 0
            for row in cur.execute(query):
                responseData['data'].append(row)
        elif requestAction == 'limits':
            responseData['limits'] = {}
            data = limits_obj()
            query = 'SELECT MIN(`timestamp`) AS min_time, MAX(`timestamp`) AS max_time, MIN(consumption) AS min_con, MAX(consumption) AS max_con, MIN(temperature) AS min_temp, MAX(temperature) AS max_temp FROM months WHERE user_id = ' + requestData['user_id']
            d = cur.execute(query).fetchone()
            data.months.timestamp.minimum = d[0]
            data.months.timestamp.maximum = d[1]
            data.months.consumption.minimum = d[2]
            data.months.consumption.maximum = d[3]
            data.months.temperature.minimum = d[4]
            data.months.temperature.maximum = d[5]
            query = 'SELECT MIN(`timestamp`) AS min_time, MAX(`timestamp`) AS max_time, MIN(consumption) AS min_con, MAX(consumption) AS max_con, MIN(temperature) AS min_temp, MAX(temperature) AS max_temp FROM days WHERE user_id = ' + requestData['user_id']
            d = cur.execute(query).fetchone()
            data.days.timestamp.minimum = d[0]
            data.days.timestamp.maximum = d[1]
            data.days.consumption.minimum = d[2]
            data.days.consumption.maximum = d[3]
            data.days.temperature.minimum = d[4]
            data.days.temperature.maximum = d[5]
            responseData['limits'] = json.dumps(data, indent=4, cls=LimitsEncoder)
        return json.dumps(responseData)

    def verify_user(self, requestData):
        cur = self.connection.cursor()
        query = "SELECT user_id FROM user WHERE user_key = '" + requestData + "'"
        d = cur.execute(query).fetchone()
        if (d == None):
            return False
        else:
            return d[0]
    

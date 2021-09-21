from json import JSONEncoder
class limits_obj(object):
  def __init__(self):
    self.months = limits_detail()
    self.days = limits_detail()

class limits_detail(object):
  def __init__(self):
    self.timestamp = limits_value()
    self.consumption = limits_value()
    self.temperature = limits_value()

class limits_value(object):
  def __init__(self):
    self.minimum = ''
    self.maximum = ''

class LimitsEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
from collections import namedtuple


class Command:

  Param = namedtuple('Parameter', ['value', 'description'])
  
  def __init__(self):
    self.title = ""
    self.description = ""
    self.AT_read = ""
    self.AT_write = ""
    self.read_response = ""
    self.params = []
    self.default = None
  
  def __repr__(self):
    s = "Command[{}]".format(self.title)
    return s

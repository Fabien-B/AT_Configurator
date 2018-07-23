import serial

class SerialMonitor():
  def __init__(self, serial_textEdit):
    self.ser = None
    self.ending = ""
    self.serial_textEdit = serial_textEdit
  def connect(self, port, baud):
    self.ser = serial.Serial(port, baud)
    self.serial_timer.start()
  
  def disconnect(self):
    self.serial_timer.stop()
    self.ser.close()
    self.ser = None
  
  def write(self, string):
    self.serial_textEdit.append(">>>" + string)  #TODO faire en bien
  
  def write_ending(self, string):
    self.write(string+self.ending)
  
  def change_ending(self, index):
    if index == 0:
      self.ending = ""
    elif index == 1:
      self.ending = "\r"
    elif index == 2:
      self.ending = "\n"
    elif index == 3:
      self.ending = "\r\n"

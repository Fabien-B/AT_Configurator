import serial

class SerialMonitor():
  def __init__(self, port, baud, serial_textEdit):
    #self.ser = serial.Serial(port, baud)
    self.ending = ""
    self.serial_textEdit = serial_textEdit
  
  def write(self, string):
    #ser.write(string.encode())
    print(string)
    self.serial_textEdit.append(">>>" + string)  #TODO faire en bien
  
  def write_ending(self, string):
    self.write(string+self.ending)
  
  def change_ending(index):
    if index == 0:
      ending = ""
    elif index == 1:
      ending = "\r"
    elif index == 2:
      ending = "\n"
    elif index == 3:
      ending = "\r\n"

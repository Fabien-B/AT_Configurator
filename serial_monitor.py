import serial
from PyQt5 import QtCore, QtGui

class SerialMonitor():
  def __init__(self, serial_textEdit):
    self.ser = None
    self.serial_mutex = QtCore.QMutex()
    self.ending = ""
    self.serial_textEdit = serial_textEdit
    self.serial_timer = QtCore.QTimer()
    self.serial_timer.setInterval(200)
    self.serial_timer.timeout.connect(self.read_serial)
    self.read_buffer = ""
  
  def connect(self, port, baud):
    self.ser = serial.Serial(port, baud)
    self.serial_timer.start()
  
  def disconnect(self):
    self.serial_timer.stop()
    if self.ser is not None:
      self.ser.close()
      self.ser = None
  
  def write(self, string):
    if self.ser is not None:
        self.serial_mutex.lock()
        self.serial_textEdit.insertPlainText("\n>>>" + string + "\n")
        self.serial_textEdit.moveCursor(QtGui.QTextCursor.End)
        self.ser.write(string.encode())
        self.serial_mutex.unlock()
  
  def write_ending(self, string):
    self.write(string+self.ending)
  
  def read_serial(self):
    if self.ser is not None:
      self.serial_mutex.lock()
      if self.ser.in_waiting:
        data = self.ser.read(self.ser.in_waiting)
        string = data.decode()
        
        
        
        self.serial_textEdit.insertPlainText(string)
        self.serial_textEdit.moveCursor(QtGui.QTextCursor.End)
      self.serial_mutex.unlock()
  
  def change_ending(self, index):
    if index == 0:
      self.ending = ""
    elif index == 1:
      self.ending = "\r"
    elif index == 2:
      self.ending = "\n"
    elif index == 3:
      self.ending = "\r\n"

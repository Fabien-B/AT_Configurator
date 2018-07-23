import serial
from PyQt5 import QtCore, QtGui
from collections import namedtuple
import re

class SerialMonitor():

  Regex = namedtuple('Parameter', ['regex', 'callback'])
  
  def __init__(self, serial_textEdit):
    self.ser = None
    self.serial_mutex = QtCore.QMutex()
    self.ending = ""
    self.serial_textEdit = serial_textEdit
    self.serial_timer = QtCore.QTimer()
    self.serial_timer.setInterval(200)
    self.serial_timer.timeout.connect(self.read_serial)
    self.read_buffer = ""
    self.regexes = []
  
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
        self.read_buffer += string
        self.serial_textEdit.insertPlainText(string)
        self.serial_textEdit.moveCursor(QtGui.QTextCursor.End)
        self.check_regexes()
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
  
  def register_regex(self, regex, callback):
    reg = SerialMonitor.Regex(regex=regex, callback=callback)
    self.regexes.append(reg)
  
  def check_regexes(self):
    while self.read_buffer:
      strings = self.read_buffer.split("\n", 1)
      if len(strings) == 1: #Wait the \n (complete line) before trying to match regexes
        return
      first = strings[0]
      self.read_buffer = strings[1]
      for reg in self.regexes:
        print(reg.regex, first)
        matches = re.match(reg.regex, first)  #TODO compile regexes
        if matches is not None:
          reg.callback(*matches.groups())
  


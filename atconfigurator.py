from PyQt5 import QtCore, QtWidgets, QtGui
import json
from collections import namedtuple
from command import Command
import serial
from command_widget import CommandWidget
from ui.configurator_ui import Ui_MainWindow
from serial_monitor import SerialMonitor

class ATConfigurator(Ui_MainWindow):
  
  def __init__(self, filename, parent=None):
    Ui_MainWindow.__init__(self)
    self.commands = []
    self.data = self.parse(filename)
    self.serial_monitor = None  
    self.filter = None
    self.serial_history = [""]    # contains the history of the hand typed commands
    self.index_history = 0
  
  def built(self):
    self.serial_monitor = SerialMonitor("", 42, self.serial_textEdit)
    self.device_label.setText(self.data["name"])
    self.add_AT_ui()
    self.at_button.clicked.connect(self.at_ping)
    self.atw_button.clicked.connect(self.at_write)
    self.serial_lineEdit.returnPressed.connect(self.write_line_to_serial)
    self.crlf_comboBox.currentIndexChanged.connect(self.serial_monitor.change_ending)
    self.filter = Filter(self.serial_lineEdit, self.command_history_up, self.command_history_down)
    self.serial_lineEdit.installEventFilter(self.filter)
  
  def add_AT_ui(self):
    for command in self.commands:
      command_widget = CommandWidget(command, self.serial_monitor)
      self.verticalLayout.insertWidget(self.verticalLayout.count()-1, command_widget)

  def at_ping(self):
    print("ping")
    self.serial_monitor.write("AT\r\n")
      
      
  def at_write(self):
    print("write")
    self.serial_monitor.write("AT&W\r\n")
  
  def write_line_to_serial(self):
    text = self.serial_lineEdit.text()
    self.serial_lineEdit.clear()
    if text:
      self.serial_history.append(text)
    self.index_history = 0
    self.serial_monitor.write_ending(text)
  
  def command_history_up(self):
    self.index_history = max(self.index_history - 1, -(len(self.serial_history)-1))
    self.serial_lineEdit.setText(self.serial_history[self.index_history])
    
  def command_history_down(self):
    self.index_history = min(self.index_history + 1, 0)
    self.serial_lineEdit.setText(self.serial_history[self.index_history])
    
  def parse(self, filename):
    with open(filename, 'r') as f:
      data = json.load(f)
      for com in data["commands"]:
        command = Command()
        command.title = com["title"]
        command.description = com["description"]
        command.AT_read = com["AT_read"]
        command.AT_write = com["AT_write"]
        command.default = com["default"]
        for choice in com["parameter"]:
          param = Command.Param(value=choice["value"], description=choice["description"])
          command.params.append(param)
        self.commands.append(command)
      return data

class Filter(QtCore.QObject):
  def __init__(self, widget, up_callback, down_callback):
      super(QtCore.QObject, self).__init__()
      self.widget_concerned = widget
      self.up_callback = up_callback
      self.down_callback = down_callback

  def eventFilter(self, source, event):
    if (event.type() == QtCore.QEvent.KeyPress and source is self.widget_concerned):
      if event.key() == QtCore.Qt.Key_Up:
        self.up_callback()
      elif event.key() == QtCore.Qt.Key_Down:
        self.down_callback()
      
    return False

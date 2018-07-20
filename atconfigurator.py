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
  
  def built(self):
    self.serial_monitor = SerialMonitor("", 42, self.serial_textEdit)
    self.device_label.setText(self.data["name"])
    self.add_AT_ui()
    self.at_button.clicked.connect(self.at_ping)
    self.atw_button.clicked.connect(self.at_write)
  
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

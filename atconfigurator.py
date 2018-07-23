from PyQt5 import QtCore, QtWidgets, QtGui
import json
from collections import namedtuple
from command import Command
import serial
from command_widget import CommandWidget
from ui.configurator_ui import Ui_MainWindow
from serial_monitor import SerialMonitor
import traceback

class ATConfigurator(Ui_MainWindow):
  
  def __init__(self, filename, parent=None):
    Ui_MainWindow.__init__(self)
    self.commands = []
    self.data = self.parse(filename)
    self.serial_monitor = None  
    self.filter = None
    self.serial_history = [""]    # contains the history of the hand typed commands
    self.index_history = 0
    self.serial_connected = False
  
  def built(self):
    self.serial_monitor = SerialMonitor(self.serial_textEdit)
    self.device_label.setText(self.data["name"])
    self.add_AT_ui()
    self.at_button.clicked.connect(self.at_ping)
    self.atw_button.clicked.connect(self.at_write)
    self.serial_lineEdit.returnPressed.connect(self.write_line_to_serial)
    self.crlf_comboBox.currentIndexChanged.connect(self.serial_monitor.change_ending)
    self.filter = Filter(self.serial_lineEdit, self.command_history_up, self.command_history_down)
    self.serial_lineEdit.installEventFilter(self.filter)
    self.connect_button.clicked.connect(self.connect_serial)
  
  def connect_serial(self):
    if self.serial_connected is False:
        port = self.port_lineEdit.text()
        bauds = int(self.bauds_lineEdit.text())
        try:
          self.serial_monitor.connect(port, bauds)
          self.serial_connected = True
          self.connect_button.setText("Disconnect")
        except serial.serialutil.SerialException as e:
          print(e)
    else:
      self.serial_monitor.disconnect()
      self.connect_button.setText("Connect")
  
  def add_AT_ui(self):
    for command in self.commands:
      command_widget = CommandWidget(command, self.serial_monitor)
      self.verticalLayout.insertWidget(self.verticalLayout.count()-1, command_widget)

  def at_ping(self):
    self.serial_monitor.write("AT\r\n")
      
      
  def at_write(self):
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
      try:
        data = json.load(f)
      except json.decoder.JSONDecodeError:
        print("[ERROR] JSON file not valid, see exception below.")
        traceback.print_exc()
        exit(-1)
      for com in data["commands"]:
        command = Command()
        command.title = com.get("title")
        command.description = com.get("description")
        command.AT_read = com.get("AT_read")
        command.AT_write = com.get("AT_write")
        command.default = com.get("default", "")
        command.read_response = com.get("read_response", "")
        for choice in com["parameter"]:
          param = Command.Param(value=choice["value"], description=choice["description"])
          command.params.append(param)
        self.commands.append(command)
      return data
    
  def closing(self):
    self.serial_monitor.disconnect()

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

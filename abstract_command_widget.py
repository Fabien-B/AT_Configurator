from PyQt5 import QtCore, QtWidgets, QtGui
from command import Command
from abc import abstractmethod

class AbstractCommandWidget(QtWidgets.QWidget):
  def __init__(self, command, serial_monitor):
    QtWidgets.QWidget.__init__(self)
    self.serial_monitor = serial_monitor
    self.command = command
    self.serial_monitor.register_regex(self.command.read_response, self.update_value)
    self.ui = None
    
  def connectUi(self):
    self.ui.refresh_button.clicked.connect(self.refresh_value)

  @abstractmethod
  def write_value(self):
    pass
  
  def refresh_value(self):
    if self.serial_monitor is not None:
      self.serial_monitor.write(self.command.AT_read)
  
  @abstractmethod
  def update_value(self, *args):
    pass
  
  def set_enabled_buttons(self, enabled):
    self.ui.write_button.setEnabled(enabled)
    self.ui.refresh_button.setEnabled(enabled)

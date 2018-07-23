from PyQt5 import QtCore, QtWidgets, QtGui
from ui.command_ui import Ui_CommandUI
from command import Command

class CommandWidget(QtWidgets.QWidget):
  def __init__(self, command, serial_monitor):
    QtWidgets.QWidget.__init__(self)
    self.serial_monitor = serial_monitor
    self.command = command
    self.ui = Ui_CommandUI()
    self.ui.setupUi(self)
    self.ui.title_label.setText(command.title)
    self.ui.title_label.setToolTip(command.description)
    for choice in command.params:
      text = "[{}] {}".format(choice.value, choice.description)
      self.ui.comboBox.addItem(text)
    self.ui.write_button.clicked.connect(self.write_value)
    self.ui.refresh_button.clicked.connect(self.refresh_value)
  
  def write_value(self):
    choosen_index = self.ui.comboBox.currentIndex()
    value = self.command.params[choosen_index].value
    description = self.command.params[choosen_index].description
    at_command = self.command.AT_write.format(value)
    if self.serial_monitor is not None:
      self.serial_monitor.write(at_command)
  
  def refresh_value(self):
    if self.serial_monitor is not None:
      self.serial_monitor.write(self.command.AT_read)
      

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
    serial_monitor.register_regex(self.command.read_response, self.update_value)
  
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
  
  def update_value(self, *args):
    try:
      value = args[0]
      description = ""
      for param in self.command.params:
        if param.value == value:
          description = param.description
      text = description if description else value
      self.ui.label_current_value.setText(description)
    except IndexError as e:
      print(len(args), e)
  
  def set_enabled_buttons(self, enabled):
    self.ui.write_button.setEnabled(enabled)
    self.ui.refresh_button.setEnabled(enabled)

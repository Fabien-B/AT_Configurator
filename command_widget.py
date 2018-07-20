from PyQt5 import QtCore, QtWidgets, QtGui
from ui.command_ui import Ui_CommandUI
from command import Command

class CommandWidget(QtWidgets.QWidget):
  def __init__(self, command, serial_monitor):
    QtWidgets.QWidget.__init__(self)
    self.serial_monitor = serial_monitor
    self.ui = Ui_CommandUI()
    self.ui.setupUi(self)
    self.ui.title_label.setText(command.title)
    self.ui.title_label.setToolTip(command.description)
    for choice in command.params:
      text = "[{}] {}".format(choice.value, choice.description)
      self.ui.comboBox.addItem(text)
    self.ui.write_button.clicked.connect(lambda x, command=command: self.write_value(command))
  
  def write_value(self, command):
    choosen_index = self.ui.comboBox.currentIndex()
    value = command.params[choosen_index].value
    description = command.params[choosen_index].description
    at_command = command.AT_write.format(value)
    print("{} set to {} : {}".format(command, description, at_command).strip())
    if self.serial_monitor is not None:
      self.serial_monitor.write(at_command)

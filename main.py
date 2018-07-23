#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import atconfigurator

def main():
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  configurator = atconfigurator.ATConfigurator('hm-trlr-s.json')
  app.aboutToQuit.connect(configurator.closing)
  configurator.setupUi(MainWindow)
  configurator.built()
  MainWindow.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()

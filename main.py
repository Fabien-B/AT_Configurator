#!/usr/bin/python3
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import atconfigurator
import argparse

def main(config_file):
  app = QtWidgets.QApplication(sys.argv)
  MainWindow = QtWidgets.QMainWindow()
  configurator = atconfigurator.ATConfigurator(config_file)
  app.aboutToQuit.connect(configurator.closing)
  configurator.setupUi(MainWindow)
  configurator.built()
  MainWindow.show()
  sys.exit(app.exec_())


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Interface for AT device configuration")
  parser.add_argument('config_file', help="JSON configuration file")
  args = parser.parse_args()
  main(args.config_file)

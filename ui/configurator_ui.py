# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/configurator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_lineEdit.sizePolicy().hasHeightForWidth())
        self.port_lineEdit.setSizePolicy(sizePolicy)
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.horizontalLayout.addWidget(self.port_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bauds_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bauds_lineEdit.sizePolicy().hasHeightForWidth())
        self.bauds_lineEdit.setSizePolicy(sizePolicy)
        self.bauds_lineEdit.setObjectName("bauds_lineEdit")
        self.horizontalLayout.addWidget(self.bauds_lineEdit)
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout.addWidget(self.connect_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.device_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.device_label.setFont(font)
        self.device_label.setObjectName("device_label")
        self.horizontalLayout_2.addWidget(self.device_label)
        self.at_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.at_button.sizePolicy().hasHeightForWidth())
        self.at_button.setSizePolicy(sizePolicy)
        self.at_button.setObjectName("at_button")
        self.horizontalLayout_2.addWidget(self.at_button)
        self.atw_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.atw_button.sizePolicy().hasHeightForWidth())
        self.atw_button.setSizePolicy(sizePolicy)
        self.atw_button.setObjectName("atw_button")
        self.horizontalLayout_2.addWidget(self.atw_button)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2.addWidget(self.frame)
        self.read_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_button.sizePolicy().hasHeightForWidth())
        self.read_button.setSizePolicy(sizePolicy)
        self.read_button.setObjectName("read_button")
        self.horizontalLayout_2.addWidget(self.read_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 779, 297))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.serial_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.serial_lineEdit.setObjectName("serial_lineEdit")
        self.horizontalLayout_3.addWidget(self.serial_lineEdit)
        self.crlf_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.crlf_comboBox.setObjectName("crlf_comboBox")
        self.crlf_comboBox.addItem("")
        self.crlf_comboBox.addItem("")
        self.crlf_comboBox.addItem("")
        self.crlf_comboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.crlf_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.serial_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serial_textEdit.sizePolicy().hasHeightForWidth())
        self.serial_textEdit.setSizePolicy(sizePolicy)
        self.serial_textEdit.setBaseSize(QtCore.QSize(0, 60))
        self.serial_textEdit.setReadOnly(True)
        self.serial_textEdit.setObjectName("serial_textEdit")
        self.verticalLayout_2.addWidget(self.serial_textEdit)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Et AT configurator"))
        self.label.setText(_translate("MainWindow", "Port: "))
        self.port_lineEdit.setText(_translate("MainWindow", "/dev/ttyUSB0"))
        self.port_lineEdit.setPlaceholderText(_translate("MainWindow", "/dev/ttyUSB0"))
        self.label_3.setText(_translate("MainWindow", "Speed (bauds): "))
        self.bauds_lineEdit.setText(_translate("MainWindow", "115200"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "device: "))
        self.device_label.setText(_translate("MainWindow", "<device name>"))
        self.at_button.setText(_translate("MainWindow", "AT"))
        self.atw_button.setText(_translate("MainWindow", "ATW"))
        self.read_button.setText(_translate("MainWindow", "Read all values"))
        self.crlf_comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.crlf_comboBox.setItemText(1, _translate("MainWindow", "CR"))
        self.crlf_comboBox.setItemText(2, _translate("MainWindow", "LF"))
        self.crlf_comboBox.setItemText(3, _translate("MainWindow", "CR LF"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/command_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommandUI(object):
    def setupUi(self, CommandUI):
        CommandUI.setObjectName("CommandUI")
        CommandUI.resize(828, 114)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommandUI.sizePolicy().hasHeightForWidth())
        CommandUI.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(CommandUI)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(CommandUI)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(CommandUI)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_current_value = QtWidgets.QLabel(CommandUI)
        self.label_current_value.setObjectName("label_current_value")
        self.horizontalLayout_2.addWidget(self.label_current_value)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(CommandUI)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(CommandUI)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.write_button = QtWidgets.QPushButton(CommandUI)
        self.write_button.setObjectName("write_button")
        self.horizontalLayout_2.addWidget(self.write_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CommandUI)
        QtCore.QMetaObject.connectSlotsByName(CommandUI)

    def retranslateUi(self, CommandUI):
        _translate = QtCore.QCoreApplication.translate
        CommandUI.setWindowTitle(_translate("CommandUI", "Form"))
        self.title_label.setText(_translate("CommandUI", "Title"))
        self.label.setText(_translate("CommandUI", "current value:"))
        self.label_current_value.setText(_translate("CommandUI", "UNK."))
        self.label_3.setText(_translate("CommandUI", "possible values:"))
        self.write_button.setText(_translate("CommandUI", "Write"))


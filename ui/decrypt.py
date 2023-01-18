# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'decrypt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icon.icon_rc

class Ui_DecryptWin(object):
    def setupUi(self, DecryptWin):
        if not DecryptWin.objectName():
            DecryptWin.setObjectName(u"DecryptWin")
        DecryptWin.resize(420, 420)
        DecryptWin.setMinimumSize(QSize(420, 420))
        DecryptWin.setMaximumSize(QSize(420, 420))
        icon = QIcon()
        icon.addFile(u":/win icon/qwerty.png", QSize(), QIcon.Normal, QIcon.Off)
        DecryptWin.setWindowIcon(icon)
        DecryptWin.setStyleSheet(u"QLineEdit{border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius: 10px;\n"
"background-color: ;\n"
"}\n"
"QTextEdit{border-style: outset;\n"
"	border-width: 2px;\n"
"	border-radius: 3px;\n"
"}\n"
"QWidget{background-color: #badff5;}\n"
"QPushButton:pressed{background-color: #f9f9f9; color: black}\n"
"QRadioButton::indicator:unchecked{image: url(:/radio button/radioOff.png);\n"
"width:16px;}\n"
"QRadioButton::indicator:checked{\n"
"	image: url(:/radio button/radioON.png);\n"
"width:16px;}")
        self.gridLayout = QGridLayout(DecryptWin)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textOut = QTextEdit(DecryptWin)
        self.textOut.setObjectName(u"textOut")
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setPointSize(10)
        self.textOut.setFont(font)
        self.textOut.setReadOnly(True)

        self.gridLayout.addWidget(self.textOut, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DecryptWin)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineInput = QLineEdit(DecryptWin)
        self.lineInput.setObjectName(u"lineInput")
        self.lineInput.setFont(font)

        self.verticalLayout.addWidget(self.lineInput)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(DecryptWin)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioENG = QRadioButton(self.groupBox)
        self.radioENG.setObjectName(u"radioENG")
        self.radioENG.setFont(font)

        self.verticalLayout_2.addWidget(self.radioENG)

        self.radioRUS = QRadioButton(self.groupBox)
        self.radioRUS.setObjectName(u"radioRUS")
        self.radioRUS.setFont(font)

        self.verticalLayout_2.addWidget(self.radioRUS)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.decryptButton = QPushButton(DecryptWin)
        self.decryptButton.setObjectName(u"decryptButton")
        self.decryptButton.setFont(font)

        self.horizontalLayout.addWidget(self.decryptButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(DecryptWin)

        QMetaObject.connectSlotsByName(DecryptWin)
    # setupUi

    def retranslateUi(self, DecryptWin):
        DecryptWin.setWindowTitle(QCoreApplication.translate("DecryptWin", u"Qwerty decrypt by ferret22", None))
        self.label.setText(QCoreApplication.translate("DecryptWin", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442:", None))
        self.groupBox.setTitle(QCoreApplication.translate("DecryptWin", u"\u042f\u0437\u044b\u043a \u0438\u0441\u0445\u043e\u0434\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.radioENG.setText(QCoreApplication.translate("DecryptWin", u"ENG", None))
        self.radioRUS.setText(QCoreApplication.translate("DecryptWin", u"RUS", None))
        self.decryptButton.setText(QCoreApplication.translate("DecryptWin", u"\u0414\u0435\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi


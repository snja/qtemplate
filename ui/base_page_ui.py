# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(916, 428)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_side = QFrame(Form)
        self.widget_side.setObjectName(u"widget_side")
        self.widget_side.setMinimumSize(QSize(250, 0))
        self.widget_side.setMaximumSize(QSize(0, 16777215))
        self.widget_side.setFrameShape(QFrame.StyledPanel)
        self.widget_side.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.widget_side)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSave = QPushButton(self.widget_side)
        self.btnSave.setObjectName(u"btnSave")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btnSave, 0, 1, 1, 1)

        self.label = QLabel(self.widget_side)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.btnClose = QPushButton(self.widget_side)
        self.btnClose.setObjectName(u"btnClose")
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btnClose, 0, 2, 1, 1)

        self.scrollArea = QScrollArea(self.widget_side)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 230, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents { background-color: transparent; }")
        self.layout_form = QVBoxLayout(self.scrollAreaWidgetContents)
        self.layout_form.setObjectName(u"layout_form")
        self.layout_form.setContentsMargins(2, 2, 2, 2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)


        self.horizontalLayout.addWidget(self.widget_side)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_top = QFrame(self.frame_2)
        self.frame_top.setObjectName(u"frame_top")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy2)
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.layout_top = QHBoxLayout(self.frame_top)
        self.layout_top.setObjectName(u"layout_top")
        self.layout_top.setContentsMargins(0, 0, 0, 0)
        self.label_title = QLabel(self.frame_top)
        self.label_title.setObjectName(u"label_title")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy3)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.layout_top.addWidget(self.label_title)

        self.btnAdd = QPushButton(self.frame_top)
        self.btnAdd.setObjectName(u"btnAdd")
        sizePolicy.setHeightForWidth(self.btnAdd.sizePolicy().hasHeightForWidth())
        self.btnAdd.setSizePolicy(sizePolicy)

        self.layout_top.addWidget(self.btnAdd)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layout_frame = QHBoxLayout(self.frame)
        self.layout_frame.setObjectName(u"layout_frame")
        self.layout_frame.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnSave.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Add", None))
        self.btnClose.setText("")
        self.label_title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi


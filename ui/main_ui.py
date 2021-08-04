# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(809, 493)
        icon = QIcon()
        icon.addFile(u":/icon/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.layout_central = QHBoxLayout(self.centralwidget)
        self.layout_central.setSpacing(0)
        self.layout_central.setObjectName(u"layout_central")
        self.layout_central.setContentsMargins(0, 0, 0, 0)
        self.parent_left = QFrame(self.centralwidget)
        self.parent_left.setObjectName(u"parent_left")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parent_left.sizePolicy().hasHeightForWidth())
        self.parent_left.setSizePolicy(sizePolicy)
        self.parent_left.setMinimumSize(QSize(0, 0))
        self.parent_left.setMaximumSize(QSize(0, 16777215))
        self.parent_left.setFrameShape(QFrame.NoFrame)
        self.parent_left.setFrameShadow(QFrame.Raised)
        self.parent_left.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.parent_left)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.layout_central.addWidget(self.parent_left)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.frame)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy2)
        self.frame_main.setMinimumSize(QSize(375, 0))
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.layout_main = QVBoxLayout(self.frame_main)
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName(u"layout_main")
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.pages = QWidget()
        self.pages.setObjectName(u"pages")
        sizePolicy1.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget.addWidget(self.pages)

        self.layout_main.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_main)

        self.scrollSetting = QScrollArea(self.frame)
        self.scrollSetting.setObjectName(u"scrollSetting")
        sizePolicy.setHeightForWidth(self.scrollSetting.sizePolicy().hasHeightForWidth())
        self.scrollSetting.setSizePolicy(sizePolicy)
        self.scrollSetting.setMinimumSize(QSize(0, 0))
        self.scrollSetting.setMaximumSize(QSize(0, 16777215))
        self.scrollSetting.setFrameShape(QFrame.NoFrame)
        self.scrollSetting.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollSetting.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollSetting.setWidgetResizable(True)
        self.widget_side = QWidget()
        self.widget_side.setObjectName(u"widget_side")
        self.widget_side.setGeometry(QRect(0, 0, 16, 493))
        self.layout_widget_side = QVBoxLayout(self.widget_side)
        self.layout_widget_side.setSpacing(0)
        self.layout_widget_side.setObjectName(u"layout_widget_side")
        self.layout_widget_side.setContentsMargins(0, 0, 0, 0)
        self.scrollSetting.setWidget(self.widget_side)

        self.horizontalLayout_3.addWidget(self.scrollSetting)


        self.layout_central.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App", None))
    # retranslateUi


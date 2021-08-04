from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class ToolTips(QLabel):

    def __init__(self, text: str, parent=None, target=None):
        QLabel.__init__(self, text, parent)
        self.centralwidget = parent
        self.target = target
        self.setObjectName("tips")
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.hide()

    def repos(self):
        if self.centralwidget:
            gp = self.target.mapToGlobal(QPoint(0, 0))
            pos = self.centralwidget.mapFromGlobal(gp)
            pos_x = pos.x() + self.target.width() + 5
            pos_y = pos.y() + (self.target.height() - self.height()) // 2
            self.move(pos_x, pos_y)
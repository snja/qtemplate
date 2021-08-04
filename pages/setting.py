from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from widget import *


class PageSetting(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        lbl = QLabel("testing", self)
        self.anim = Anim(parent.scrollSetting)
        self.anim.setMin()

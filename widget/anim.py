from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qtawesome import icon


class Anim():
    def __init__(self, obj: QWidget, min_=0, max_=230, duration=500):
        self.obj = obj
        self.min = min_
        self.max = max_
        self.duration = duration
        self.obj.setMaximumWidth(0)
        self.anim = QPropertyAnimation(self.obj, b"minimumWidth")
        self.anim.setDuration(self.duration)
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)

    def show(self):
        if self.obj.minimumWidth() == self.max:
            return
        self.anim.setStartValue(self.obj.minimumWidth())
        self.anim.setEndValue(self.max)
        self.anim.start()

    def hide(self):
        if self.obj.minimumWidth() == self.min:
            return
        self.anim.setStartValue(self.obj.minimumWidth())
        self.anim.setEndValue(self.min)
        self.anim.start()

    def toggle(self):
        if self.obj.minimumWidth() == self.min:
            self.show()
        if self.obj.minimumWidth() == self.max:
            self.hide()

    def setMax(self):
        self.obj.setMinimumWidth(self.max)

    def setMin(self):
        self.obj.setMinimumWidth(self.min)

    def isMax(self):
        return self.obj.minimumWidth() == self.max

    def isMin(self):
        return self.obj.minimumWidth() == self.min

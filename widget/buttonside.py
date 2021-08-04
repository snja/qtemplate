from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from .tooltips import *
from qtawesome import icon



class QButtonSide(QPushButton):
    text_color = QColor("white")
    icon_size_default = QSize(26, 26)
    tooltip = None

    def __init__(self, text, parent=None, centralwidget=None):
        QPushButton.__init__(self, text, parent)
        self.is_hover = False
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setCheckable(True)
        self.setIconSize(self.icon_size_default)
        self.setMinimumHeight(50)
        if centralwidget:
            self.tooltip = ToolTips(text, centralwidget, self)

    def setQta(self, icon_name, color="white"):
        self.setIcon(icon(icon_name, color=color))

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)

        w, h = self.width(),  self.height()

        paint.setRenderHint(QPainter.RenderHint.Antialiasing)

        paint.setPen(Qt.NoPen)

        rect = QRect(0, 0, w, h)
        rect_text = QRect(h, 0, w - h, h)

        if self.isChecked():
            brush = QBrush(QColor(255, 255, 255, 100))
            paint.setBrush(brush)
            paint.drawRect(rect)

            brush_border = QBrush(QColor(255, 255, 255))
            paint.setBrush(brush_border)
            paint.drawRect(QRect(0, 0, 4, h))

        elif self.is_hover:
            brush = QBrush(QColor(255, 255, 255, 50))
            paint.setBrush(brush)
            paint.drawRect(rect)

        paint.setPen(self.text_color)
        paint.drawText(rect_text, Qt.AlignVCenter, self.text())

        ic_s = self.iconSize()
        ic_w, ic_h = ic_s.width(), ic_s.height()
        icp = (h - ic_h) / 2

        # self.icon().paint(paint, icp, icp, ic_w, ic_h )
        paint.drawPixmap(icp, icp, ic_w, ic_h, self.icon().pixmap(ic_s))
        paint.end()


    def enterEvent(self, event):
        self.is_hover = True
        self.setIconSize(QSize(30,30))
        self.repaint()
        if self.tooltip and self.width() <= 50:
            self.tooltip.show()

    def leaveEvent(self, event):
        self.is_hover = False
        self.setIconSize(self.icon_size_default)
        self.repaint()
        if self.tooltip:
            self.tooltip.hide()

    def resizeEvent(self, event):
        if self.tooltip:
            self.tooltip.repos()
            if self.width() > 50:
                self.tooltip.hide()


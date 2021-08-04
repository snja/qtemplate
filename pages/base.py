from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.base_page_ui import *
from widget import *


class PageBase(QWidget, Ui_Form):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.anim = Anim(self.widget_side)
        self.anim.setMin()

        self.btnAdd.clicked.connect(self.anim.toggle)
        self.btnSave.clicked.connect(self.save)
        self.btnClose.clicked.connect(self.anim.hide)

    def setup(self, title: str, form=True):
        self.label_title.setText(title)
        self.widget_side.setVisible(form)
        self.btnAdd.setVisible(form)
    
    def save(self):
        self.anim.hide()

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qtawesome import icon
from widget import *

class QSideMenu(QObject):
    clicked_menu = Signal(int)
    clicked_menu_bottom = Signal(int)

    def __init__(self, parent, centralwidget):
        QObject.__init__(self)
        self.btns = []
        self.btns2 = []
        self.parent = parent
        self.centralwidget = centralwidget
        self.anim = Anim(parent, 50, 200, 300)
        self.anim.anim.setEasingCurve(QEasingCurve.OutCurve)
        self.anim.setMin()
        self.setup_layout()
        self.setup_menu_toggle()

    def setup_layout(self):
        parent = self.parent
        frame_top = QFrame(parent)
        self.layout_top = QVBoxLayout(frame_top)
        self.layout_top.setMargin(0)
        self.layout_top.setSpacing(0)

        frame_bottom = QFrame(parent)
        self.layout_bottom = QVBoxLayout(frame_bottom)
        self.layout_bottom.setMargin(0)
        self.layout_bottom.setSpacing(0)

        space = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.parent.layout().addWidget(frame_top)
        self.parent.layout().addItem(space)
        self.parent.layout().addWidget(frame_bottom)

    def setup_menu_toggle(self):
        btn = QButtonSide("Hide Menu", self.parent)
        btn.setCheckable(False)
        btn.text_color = QColor(255, 255, 255, 60)
        color_icon = QColor(255,255,255,120)
        
        def _click():
            if self.anim.isMax():
                btn.setQta("mdi.menu", color=color_icon)
            else:
                btn.setQta("mdi.chevron-left",  color=color_icon)
            self.anim.toggle()

        btn.setQta("mdi.menu",  color=color_icon)

        btn.clicked.connect(_click)
        self.layout_top.addWidget(btn)

    def setup_menu(self, array: list):
        for txt, ic in array:
            self.add_menu(txt, ic)

    def setup_menu_bottom(self, array: list):
        for txt, ic in array:
            self.add_menu_bottom(txt, ic)

    def add_menu(self, txt, ic):
        i = self.layout_top.count()-1
        btn = QButtonSide(txt, self.parent, self.centralwidget)
        btn.setQta(ic)
        btn.clicked.connect(lambda: self.onclick(i))
        self.layout_top.addWidget(btn)
        self.btns += [btn]

    def add_menu_bottom(self, txt, ic):
        i = self.layout_bottom.count()
        btn = QButtonSide(txt, self.parent, self.centralwidget)
        btn.setQta(ic)
        btn.clicked.connect(lambda: self.onclick_bottom(i))
        self.layout_bottom.addWidget(btn)
        self.btns2+=[btn]
    
    def onclick(self, i):
        self.clicked_menu.emit(i)

    def onchange(self, i):
        for a, btn in enumerate(self.btns):
            btn: QButtonSide
            btn.setChecked(a==i)
            btn.setEnabled(a!=i)

    def onclick_bottom(self, i):
        for a, btn in enumerate(self.btns2):
            btn: QButtonSide
            btn.setChecked(a==i)
        
        if self.btns2[i].isChecked():
            self.clicked_menu_bottom.emit(i)

from .base import *
from .dashboard import *
from .setting import *
from .profile import *

class AllPage(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.stack = parent.stackedWidget
        self.stack.widget(0).deleteLater()

        self.dashboard = PageDashboard(self)
        self.profile = PageProfile(self)

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.profile)

        
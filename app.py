import os
import sys
import ui.gen
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.main_ui import *
from widget import *
from app_config import *
from pages import *


class MainApp(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setupStylesheet()
        self.setWindowTitle(app_name)

        self.side = QSideMenu(self.parent_left, self.centralWidget())
        self.side.setup_menu(config_menu_side)
        self.side.setup_menu_bottom(config_menu_side_bottom)        

        self.page = AllPage(self)

        self.setting = PageSetting(self)
        self.layout_widget_side.addWidget(self.setting)

        self.side.clicked_menu.connect( lambda i: self.stackedWidget.setCurrentIndex(i))
        self.side.clicked_menu_bottom.connect(lambda i: self.setting.anim.toggle())
        self.stackedWidget.currentChanged.connect(self.side.onchange)
        
        setIcons(self.frame.findChildren(QPushButton))

    def setupStylesheet(self):
        style = open("ui/style.css").read()
        self.centralwidget.setStyleSheet(style)
        
    
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainApp()
    main.show()
    sys.exit(app.exec_())

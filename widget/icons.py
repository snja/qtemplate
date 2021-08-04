from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from qtawesome import icon

style_btn2 = "QPushButton { background-color: #888; } QPushButton:hover { background-color: #444; } "


icon_map = {
    "add": "fa.plus",
    "start": "fa5s.play",
    "save": "fa.check",
    "cancel": "fa.times",
    "stop": "fa.stop",
    "edit": "fa5s.edit",
    "btnClose": "fa.times",
    "btnSave": "fa.check",
    "auto posting": "mdi.file-export",
    "auto register": "fa5b.blogger-b",
    "export": "mdi.content-save",
    "reset failed": "mdi.reload-alert"
}


def setIcon(btn: QPushButton, icon_name=None):
    tx = btn.text().lower()
    tx2 = btn.objectName()
    if tx in icon_map.keys():
        icon_name = icon_map[tx]
        ic = icon(icon_name, color="white")
        btn.setIcon(ic)
    elif tx2 in icon_map.keys():
        icon_name = icon_map[tx2]
        ic = icon(icon_name, color="white")
        btn.setIcon(ic)

    if tx in ["cancel", "stop"]:
        btn.setStyleSheet(style_btn2)
    elif btn.styleSheet() == style_btn2:
        btn.setStyleSheet("")

    btn.setCursor(QCursor(Qt.PointingHandCursor))


def setIcons(btns: list):
    for btn in btns:
        setIcon(btn)

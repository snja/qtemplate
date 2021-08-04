import os
ui_root = "ui"
if os.path.isdir(ui_root):
    for f in os.listdir(ui_root):
        file = os.path.join(ui_root, f)
        if file.endswith(".ui"):
            target = file.replace(".ui", "_ui.py")
            os.system(f'pyside2-uic {file} > {target}')
        elif file.endswith(".qrc"):
            target = f.replace(".qrc", "_rc.py")
            os.system(f'pyside2-rcc {file} -o {target}')
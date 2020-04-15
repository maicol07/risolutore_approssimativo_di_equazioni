from PySide2.QtWidgets import QApplication
import sys
from src.Window import Window

app = QApplication(sys.argv)

window = Window(app, "main")
print(window.label_2.text())

app.exec_()


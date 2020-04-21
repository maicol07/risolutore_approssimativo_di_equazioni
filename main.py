from PySide2.QtWidgets import QApplication
import sys
from src.windows.Window import Window

app = QApplication(sys.argv)

window = Window("main")

app.exec_()

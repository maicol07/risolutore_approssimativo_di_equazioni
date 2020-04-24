import sys

from PySide2.QtWidgets import QApplication

from src.windows.MainWindow import MainWindow

app = QApplication(sys.argv)

window = MainWindow()

app.exec_()

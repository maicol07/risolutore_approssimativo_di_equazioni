import sys

from PySide2.QtCore import QSettings, QCoreApplication
from PySide2.QtWidgets import QApplication

from src.windows.MainWindow import MainWindow

# Set info
QCoreApplication.setApplicationName('Risolutore approssimativo di equazioni')
QCoreApplication.setApplicationVersion('1.0')
QCoreApplication.setOrganizationName('maicol07')
QCoreApplication.setOrganizationDomain('maicol07.it')

app = QApplication(sys.argv)

# Load style

settings = QSettings('settings.ini', QSettings.IniFormat)
theme = settings.value('appearance/style')
if theme:
    app.setStyle(theme)
font = settings.value('appearance/font')
if font:
    app.setFont(font)

window = MainWindow()

app.exec_()

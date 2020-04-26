import sys

try:
    from PySide2.QtCore import QSettings, QCoreApplication
    from PySide2.QtWidgets import QApplication
except ImportError:
    import subprocess
    import os

    subprocess.call('pip install -r requirements.txt', cwd=os.getcwd())
finally:
    try:
        from PySide2.QtCore import QSettings, QCoreApplication
        from PySide2.QtWidgets import QApplication
    except ImportError:
        import tkinter.messagebox as tkmb

        tkmb.showerror('Errore!', 'Non è possibile importare le librerie esterne necessarie per il funzionamento del '
                                  'programma.\nSi prega di installarle con il seguente comando:\npip install -r '
                                  'requirements.txt')
        exit()

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

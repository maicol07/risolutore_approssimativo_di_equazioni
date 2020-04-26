from PySide2 import QtWidgets
from PySide2.QtCore import QSettings
from PySide2.QtWidgets import QStyleFactory, QApplication

from src.windows.Window import get_window

Dialog = get_window('dialog')
settings = QSettings('settings.ini', QSettings.IniFormat)


class Settings(Dialog):
    def __init__(self):
        super().__init__('settings')
        self.app = QApplication.instance()

        idx = self.fontComboBox.findText(settings.value('appearance/font', 'MS Shell Dlg 2'))
        self.fontComboBox.setCurrentIndex(idx)

        self.styleComboBox.addItems(QStyleFactory.keys())
        idx = self.styleComboBox.findText(settings.value('appearance/style', self.app.style().objectName()))
        self.styleComboBox.setCurrentIndex(idx)

        self.loopsSpinBox.setValue(int(settings.value('loopsNumber', 8)))

        self.buttonBox.accepted.connect(self.saveSettings)
        self.buttonBox.button(self.buttonBox.Reset).clicked.connect(self.resetSettings)

    def saveSettings(self):
        # Font
        newfont = self.fontComboBox.currentText()
        print(newfont)
        settings.setValue('appearance/font', newfont)
        self.app.setFont(newfont)

        # Theme
        newtheme = self.styleComboBox.currentText()
        settings.setValue('appearance/style', newtheme)
        self.app.setStyle(newtheme)

        # Loops
        settings.setValue('loopsNumber', self.loopsSpinBox.value())
        settings.sync()

        self.close()

    def resetSettings(self):
        self.fontComboBox.setCurrentText('MS Shell Dlg 2')
        self.styleComboBox.setCurrentText(QStyleFactory.keys()[0])
        self.loopsSpinBox.setValue(8)

    def __stubs(self):
        """ This just enables code completion. It should never be called """
        self.Dialog = QtWidgets.QDialog()
        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.fontComboBox = QtWidgets.QFontComboBox()
        self.label = QtWidgets.QLabel()
        self.styleComboBox = QtWidgets.QComboBox()
        self.label_2 = QtWidgets.QLabel()
        self.loopsSpinBox = QtWidgets.QSpinBox()
        self.label_3 = QtWidgets.QLabel()
        raise AssertionError("This should never be called")

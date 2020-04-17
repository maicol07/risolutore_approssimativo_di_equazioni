from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from lib.UiLoader import loadUi
from PySide2.QtCore import QFile


class Window(QtWidgets.QMainWindow):
    def __init__(self, view: str):
        """
        Window constructor

        Parameters
        ----------
        view: str
            The name of the view to load
        """
        super(Window, self).__init__()
        ui_file = QFile("views/{}.ui".format(view))
        ui_file.open(QFile.ReadOnly)

        loadUi(ui_file, self, workingDirectory="views/")
        ui_file.close()

        self.show()

    def __stubs(self):
        """ This just enables code completion. It should never be called """
        self.MainWindow = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget()
        self.title = QtWidgets.QLabel()
        self.label_2 = QtWidgets.QLabel()
        self.logo = QtWidgets.QLabel()
        self.okButton = QtWidgets.QPushButton()
        self.equationLineEdit = QtWidgets.QLineEdit()
        self.tabWidget = QtWidgets.QTabWidget()
        self.bisezioneTab = QtWidgets.QWidget()
        self.bisezioneTable = QtWidgets.QTableWidget()
        self.NewtonTab = QtWidgets.QWidget()
        self.newtonTable = QtWidgets.QTableWidget()
        self.graphButton = QtWidgets.QPushButton()
        self.label = QtWidgets.QLabel()
        self.equationLabel = QtWidgets.QLabel()
        self.menubar = QtWidgets.QMenuBar()
        self.menuFile = QtWidgets.QMenu()
        self.menuStrumenti = QtWidgets.QMenu()
        self.menuAiuto = QtWidgets.QMenu()
        self.statusbar = QtWidgets.QStatusBar()
        raise AssertionError("This should never be called")

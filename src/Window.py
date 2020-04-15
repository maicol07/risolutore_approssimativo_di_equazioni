from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class Window(QtWidgets.QWidget):
    def __init__(self, app: QApplication, view: str):
        """
        Window constructor

        Parameters
        ----------
        app: QApplication
            The QApplication parent object
        view: str
            The name of the view to load
        """
        super().__init__()
        ui_file = QFile("views/{}.ui".format(view))
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader(self)
        self.window = loader.load(ui_file, self)
        ui_file.close()

        self.window.show()

    def __stubs(self):
        """
        This just enables code completion. It should never be called

        Returns
        -------

        """
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
        self.menubar = QtWidgets.QMenuBar()
        self.menuFile = QtWidgets.QMenu()
        self.menuStrumenti = QtWidgets.QMenu()
        self.menuAiuto = QtWidgets.QMenu()
        self.statusbar = QtWidgets.QStatusBar()
        raise AssertionError("This should never be called")

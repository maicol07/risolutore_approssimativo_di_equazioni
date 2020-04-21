import warnings

from PySide2 import QtWidgets
from PySide2.QtWidgets import QErrorMessage, QMessageBox
from PySide2.QtGui import QPixmap
from matplotlib import MatplotlibDeprecationWarning
from sympy import plot_implicit, latex
from sympy.parsing.latex import parse_latex

from src import Utils
from src.windows.Window import Window


# noinspection PyMethodMayBeStatic
class MainWindow(Window):
    equation = None

    def __init__(self):
        super().__init__('main')
        # OK Button
        self.okButton.clicked.connect(self.equation_builder)

        # Menu Bar
        self.actionEsci.triggered.connect(self.close)
        self.actionLaTex.triggered.connect(self.open_latex_window)

    def open_latex_window(self):
        w = Window('latex')
        w.pushButton.clicked.connect(w.close)

    def graph(self):
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        plot_implicit(self.equation, title="Grafico di " + str(self.equation))

    def equation_builder(self):
        try:
            equation = parse_latex(self.equationLineEdit.text())
            Utils.renderLatex(latex(equation), 15, file='equation.svg')
            image = QPixmap('equation.svg')
            self.equationLabel.setPixmap(image)
            # Enable buttons
            self.graphButton.setEnabled(True)
            self.tabWidget.setEnabled(True)
            # Set graph
            self.graphButton.clicked.connect(self.graph)
            # Calculate table values

        except SyntaxError as error:
            msg = QErrorMessage()
            msg.showMessage("Errore di sintassi!")
            return msg

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
        self.label_3 = QtWidgets.QLabel()
        self.StartIntervalDoubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.label_4 = QtWidgets.QLabel()
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox()
        self.menubar = QtWidgets.QMenuBar()
        self.menuFile = QtWidgets.QMenu()
        self.menuStrumenti = QtWidgets.QMenu()
        self.menuAiuto = QtWidgets.QMenu()
        self.statusbar = QtWidgets.QStatusBar()
        raise AssertionError("This should never be called")

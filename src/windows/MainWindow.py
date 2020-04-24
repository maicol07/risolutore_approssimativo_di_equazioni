import warnings

import numpy
from PySide2 import QtWidgets
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QErrorMessage, QTableWidgetItem, QMessageBox
from matplotlib import MatplotlibDeprecationWarning
from sympy import plot_implicit, latex, lambdify, diff, solve, sign, N, E
from sympy.abc import x, e
from sympy.parsing.latex import parse_latex

from src import Utils
from src.windows.Settings import Settings
from src.windows.Window import get_window

Window = get_window()


# noinspection PyMethodMayBeStatic
class MainWindow(Window):
    equation = None
    __raw_equation = None
    display_equation = None
    f = None

    def __init__(self):
        super().__init__('main')

        # OK Button
        self.okButton.clicked.connect(self.equation_builder)

        # Menu Bar
        self.actionEsci.triggered.connect(self.close)
        self.actionLaTex.triggered.connect(self.open_latex_window)
        self.actionInformazioni.triggered.connect(self.open_info)
        self.actionInformazioniQt.triggered.connect(lambda: QMessageBox.aboutQt(self, "Informazioni su Qt"))
        self.actionImpostazioni.triggered.connect(self.open_settings)

    def open_latex_window(self):
        html = open("resources/html/latex.html")
        QMessageBox.information(self, "Formato LaTex", html.read())
        html.close()

    def open_info(self):
        html = open("resources/html/about.html")
        QMessageBox.about(self, "Informazioni su Risolutore approssimativo di equazioni", html.read())
        html.close()

    def open_settings(self):
        Settings()

    def graph(self):
        warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)
        plot_implicit(self.display_equation.subs(e, E), title="Grafico di " + str(self.display_equation.subs(e, E)))

    def equation_builder(self):
        try:
            self.__raw_equation = self.equationLineEdit.text() \
                .replace("=0", "").replace("= 0", "").replace("0=", "").replace("0 =", ""). \
                replace("y=", "").replace("y =", "").replace("=y", "").replace("= y", "")

            # Render equation
            self.display_equation = parse_latex("y = " + self.__raw_equation)
            Utils.renderLatex(latex(self.display_equation), 15, file='equation.svg')
            image = QPixmap('equation.svg')
            self.equationLabel.setPixmap(image)

            # Fix exp (Add missing closing bracket)
            self.__raw_equation = self.__raw_equation.replace("e^", r"\exp(")
            pos = self.__raw_equation.find(r'\exp(')
            self.__raw_equation = self.__raw_equation[:pos] + \
                                  self.__raw_equation[pos:len(r'\exp(') + 2] + ")" + \
                                  self.__raw_equation[pos + len(r'\exp(') + 1:]

            self.equation = parse_latex(self.__raw_equation)
            self.f = lambdify(x, self.equation, 'numpy')

            # Enable buttons
            self.graphButton.setEnabled(True)
            self.tabWidget.setEnabled(True)

            # Set graph
            self.graphButton.clicked.connect(self.graph)

            # Calculate table values
            self.tabWidget.setEnabled(True)
            self.bisezioneTable.setEnabled(True)
            self.bisezione()
            self.newtonTangent()
        except SyntaxError as error:
            msg = QErrorMessage()
            msg.showMessage("Errore di sintassi!")
            return msg

    def bisezione(self):
        a = float(self.startIntervalDoubleSpinBox.text().replace(",", "."))
        b = float(self.endIntervalDoubleSpinBox.text().replace(",", "."))
        # Calculate table
        eps = b - a
        r = None
        nlimit = 8
        self.bisezioneTable.clear()
        for n in range(nlimit):
            c = (a + b) / 2
            f = {a: self.f(a), b: self.f(b), c: self.f(c)}
            # Add to table
            for p, e in enumerate([a, b, f[a], f[b], c, f[c], eps / (2 ** (n + 1))]):
                if type(e) == numpy.float64:
                    e = N(e, 10)
                self.bisezioneTable.setItem(n, p, QTableWidgetItem(str(e)))
            solved = False
            for v in [a, b, c]:
                if f[v] == 0:
                    r = "<span style='font-size:12pt;'>La soluzione è stata trovata dopo {} iterazioni: {}</span>".format(
                        n + 1, v)
                    solved = True
                    break
            if solved:
                break

            if sign(f[a] * f[c]) == -1:  # Opposite sign a and c
                b = c
            else:  # Opposite sign b and c
                a = c

        if not r:
            r = "<span style='font-size:12pt;'>La soluzione trovata dopo {} iterazioni è stata riscontrata nell'intervallo: [{}; {}]</span>".format(
                n + 1, a, b)
        self.bisezioneResultLabel.setText(r)

    def newtonTangent(self):
        a = float(self.startIntervalDoubleSpinBox.text().replace(",", "."))
        b = float(self.endIntervalDoubleSpinBox.text().replace(",", "."))
        f = {a: self.f(a), b: self.f(b)}
        d = self.equation.diff(x)
        f2d = lambdify(x, diff(d, x), 'numpy')
        self.newtonTable.clear()
        if not (f[a] < 0 and f[b] > 0):
            self.newtonResultLabel.setText(
                "<span style='font-size:12pt;'>La funzione non può essere risolta con questo metodo</span>")
            return
        nlimit = 8
        for n in range(nlimit):
            f = {a: self.f(a), b: self.f(b)}
            # Derivative is a number or an equation?
            try:
                ds = float(d)
            except TypeError:
                ds = solve(d, x)[0]
            pb = b
            b -= (f[b] / ds)
            if pb == b:
                n -= 1
                break
            self.newtonTable.setItem(n, 0, QTableWidgetItem(str(b)))
        self.newtonResultLabel.setText(
            "<span style='font-size: 12pt;'>La soluzione trovata dopo {} iterazioni è: {}</span>".format(n, b))


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
    self.bisezioneResultLabel = QtWidgets.QLabel()
    self.NewtonTab = QtWidgets.QWidget()
    self.newtonTable = QtWidgets.QTableWidget()
    self.newtonResultLabel = QtWidgets.QLabel()
    self.graphButton = QtWidgets.QPushButton()
    self.label = QtWidgets.QLabel()
    self.equationLabel = QtWidgets.QLabel()
    self.label_3 = QtWidgets.QLabel()
    self.startIntervalDoubleSpinBox = QtWidgets.QDoubleSpinBox()
    self.label_4 = QtWidgets.QLabel()
    self.endIntervalDoubleSpinBox = QtWidgets.QDoubleSpinBox()
    self.menubar = QtWidgets.QMenuBar()
    self.menuFile = QtWidgets.QMenu()
    self.menuStrumenti = QtWidgets.QMenu()
    self.menuAiuto = QtWidgets.QMenu()
    self.statusbar = QtWidgets.QStatusBar()
    self.actionEsci = QtWidgets.QAction()
    self.actionCronologia = QtWidgets.QAction()
    self.actionImpostazioni = QtWidgets.QAction()
    self.actionLaTex = QtWidgets.QAction()
    self.actionInformazioni = QtWidgets.QAction()
    self.actionInformazioniQt = QtWidgets.QAction()
    raise AssertionError("This should never be called")

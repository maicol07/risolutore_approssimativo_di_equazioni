from PySide2.QtWidgets import QMainWindow
from lib.UiLoader import loadUi
from PySide2.QtCore import QFile


class Window(QMainWindow):
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

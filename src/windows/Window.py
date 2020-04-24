from PySide2.QtCore import QFile
from PySide2.QtWidgets import QMainWindow, QDialog

import resources.resources
from lib.UiLoader import loadUi


def get_window(window_type='window'):
    if window_type == 'window':
        parent = QMainWindow
    else:
        parent = QDialog

    # noinspection PyMethodMayBeStatic
    class Window(parent):
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

            loadUi(ui_file, self, workingDirectory="views")
            ui_file.close()

            self.show()

        def __stub(self):
            """ This code is only for imports optimizations. Don't run it """
            a = resources.resources
            raise AssertionError("You shouldn't run this code!" + str(a))

    return Window

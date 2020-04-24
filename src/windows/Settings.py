from src.windows.Window import get_window

Dialog = get_window('dialog')


class Settings(Dialog):
    def __init__(self):
        super().__init__('settings')

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from template.janela_user import Ui_Form

class Janela_user(QWidget):
    def __init__(self, *args, **argvs):
        super(Janela_user, self).__init__(*args,**argvs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
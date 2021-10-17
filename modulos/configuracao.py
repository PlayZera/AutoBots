from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from template.janela_config import Ui_Configuracao

class Janela_config(QWidget):
    def __init__(self, *args, **argvs):
        super(Janela_config, self).__init__(*args,**argvs)
        self.ui = Ui_Configuracao()
        self.ui.setupUi(self)
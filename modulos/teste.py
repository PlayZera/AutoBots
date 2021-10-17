from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import *
from template.janela_teste import Ui_Form

class Janela_teste(QWidget):
    def __init__(self, *args, **argvs):
        super(Janela_teste, self).__init__(*args,**argvs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.mdfe_chck.stateChanged.connect(self.mdfe)
        mdfe = self.ui.mdfe_chck.isChecked()
        print(mdfe)

    def mdfe(self):
        mdfe = self.ui.mdfe_chck.isChecked()
        if mdfe == True:
            self.ui.recep_chck.hide()
        else:
            self.ui.recep_chck.show()

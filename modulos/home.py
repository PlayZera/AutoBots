from PyQt5.QtWidgets import *
from PyQt5 import *

from template.janela_home import Ui_home
from modulos.configuracao import Janela_config
from modulos.user import Janela_user
from modulos.teste import Janela_teste

class Janela_home(QMainWindow):
    def __init__(self, *args, **argvs):
        super(Janela_home, self).__init__(*args,**argvs)
        self.ui = Ui_home()
        self.ui.setupUi(self)
        self.ui.botao_config.clicked.connect(self.config_tela)
        self.ui.botao_user.clicked.connect(self.user_tela)
        self.ui.botao_teste.clicked.connect(self.teste_tela)
        self.ui.botao_doc.clicked.connect(self.doc_tela)

    def config_tela(self):
        self.window = Janela_config()
        self.window.show()

    def user_tela(self):
        self.window = Janela_user()
        self.window.show()

    def teste_tela(self):
        self.window = Janela_teste()
        self.window.show()

    def doc_tela(self):
        doc = QMessageBox()
        doc.setIcon(QMessageBox.Warning)
        doc.setWindowTitle("Alerta!")
        doc.setText("Estamos implementando essa função!")
        doc.exec()




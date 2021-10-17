from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import os,sys

#chamando modulo da tela
from modulos.home import Janela_home


app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = Janela_home()
    window.show()
sys.exit(app.exec_())
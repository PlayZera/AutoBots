# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela_teste.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 249)
        Form.setMinimumSize(QtCore.QSize(453, 249))
        Form.setMaximumSize(QtCore.QSize(453, 249))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setStyleSheet("background-color: rgb(133, 0, 153);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(134, -43, 171, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/teste/testes.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background-color: rgb(118, 118, 118);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cte_chck = QtWidgets.QCheckBox(self.frame)
        self.cte_chck.setGeometry(QtCore.QRect(70, 60, 41, 21))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.cte_chck.setFont(font)
        self.cte_chck.setObjectName("cte_chck")
        self.nfe_chck = QtWidgets.QCheckBox(self.frame)
        self.nfe_chck.setGeometry(QtCore.QRect(70, 40, 41, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.nfe_chck.setFont(font)
        self.nfe_chck.setObjectName("nfe_chck")
        self.mdfe_chck = QtWidgets.QCheckBox(self.frame)
        self.mdfe_chck.setGeometry(QtCore.QRect(10, 40, 51, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.mdfe_chck.setFont(font)
        self.mdfe_chck.setObjectName("mdfe_chck")
        self.nfse_chck = QtWidgets.QCheckBox(self.frame)
        self.nfse_chck.setGeometry(QtCore.QRect(10, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.nfse_chck.setFont(font)
        self.nfse_chck.setObjectName("nfse_chck")
        self.Doc = QtWidgets.QLabel(self.frame)
        self.Doc.setGeometry(QtCore.QRect(20, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(12)
        self.Doc.setFont(font)
        self.Doc.setObjectName("Doc")
        self.emissao_chck = QtWidgets.QCheckBox(self.frame)
        self.emissao_chck.setGeometry(QtCore.QRect(10, 120, 71, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.emissao_chck.setFont(font)
        self.emissao_chck.setObjectName("emissao_chck")
        self.recep_chck = QtWidgets.QCheckBox(self.frame)
        self.recep_chck.setGeometry(QtCore.QRect(10, 140, 81, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.recep_chck.setFont(font)
        self.recep_chck.setObjectName("recep_chck")
        self.event_chck = QtWidgets.QCheckBox(self.frame)
        self.event_chck.setGeometry(QtCore.QRect(80, 120, 71, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.event_chck.setFont(font)
        self.event_chck.setObjectName("event_chck")
        self.Prod = QtWidgets.QLabel(self.frame)
        self.Prod.setGeometry(QtCore.QRect(20, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(12)
        self.Prod.setFont(font)
        self.Prod.setObjectName("Prod")
        self.Prod_2 = QtWidgets.QLabel(self.frame)
        self.Prod_2.setGeometry(QtCore.QRect(190, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(12)
        self.Prod_2.setFont(font)
        self.Prod_2.setObjectName("Prod_2")
        self.manual_chck = QtWidgets.QCheckBox(self.frame)
        self.manual_chck.setGeometry(QtCore.QRect(170, 40, 101, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.manual_chck.setFont(font)
        self.manual_chck.setObjectName("manual_chck")
        self.aud_chck = QtWidgets.QCheckBox(self.frame)
        self.aud_chck.setGeometry(QtCore.QRect(170, 60, 101, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.aud_chck.setFont(font)
        self.aud_chck.setObjectName("aud_chck")
        self.trafe_chck = QtWidgets.QCheckBox(self.frame)
        self.trafe_chck.setGeometry(QtCore.QRect(170, 80, 121, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.trafe_chck.setFont(font)
        self.trafe_chck.setObjectName("trafe_chck")
        self.inva_chck = QtWidgets.QCheckBox(self.frame)
        self.inva_chck.setGeometry(QtCore.QRect(170, 100, 121, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.inva_chck.setFont(font)
        self.inva_chck.setObjectName("inva_chck")
        self.expo_chck = QtWidgets.QCheckBox(self.frame)
        self.expo_chck.setGeometry(QtCore.QRect(170, 120, 121, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.expo_chck.setFont(font)
        self.expo_chck.setObjectName("expo_chck")
        self.down_chck = QtWidgets.QCheckBox(self.frame)
        self.down_chck.setGeometry(QtCore.QRect(170, 140, 81, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.down_chck.setFont(font)
        self.down_chck.setObjectName("down_chck")
        self.imprimir_chck = QtWidgets.QCheckBox(self.frame)
        self.imprimir_chck.setGeometry(QtCore.QRect(280, 40, 71, 17))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(9)
        self.imprimir_chck.setFont(font)
        self.imprimir_chck.setObjectName("imprimir_chck")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(180, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("OMEGLE")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Testes"))
        self.cte_chck.setText(_translate("Form", "CTe"))
        self.nfe_chck.setText(_translate("Form", "NFe"))
        self.mdfe_chck.setText(_translate("Form", "MDFe"))
        self.nfse_chck.setText(_translate("Form", "NFSe"))
        self.Doc.setText(_translate("Form", "Documento"))
        self.emissao_chck.setText(_translate("Form", "Emissão"))
        self.recep_chck.setText(_translate("Form", "Recepção"))
        self.event_chck.setText(_translate("Form", "Evento"))
        self.Prod.setText(_translate("Form", "Produto"))
        self.Prod_2.setText(_translate("Form", "Validação"))
        self.manual_chck.setText(_translate("Form", "Enviar ao ERP"))
        self.aud_chck.setText(_translate("Form", "Aud. Usuário"))
        self.trafe_chck.setText(_translate("Form", "Tráfego de docs"))
        self.inva_chck.setText(_translate("Form", "Doc Inválido"))
        self.expo_chck.setText(_translate("Form", "Exportar Excel"))
        self.down_chck.setText(_translate("Form", "Download"))
        self.imprimir_chck.setText(_translate("Form", "Imprimir"))
        self.pushButton.setText(_translate("Form", "Testar"))
import template.tela_teste


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

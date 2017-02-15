# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'heat_flow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1248, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.temp_chart = QtWidgets.QWidget(self.centralwidget)
        self.temp_chart.setGeometry(QtCore.QRect(220, 50, 1011, 521))
        self.temp_chart.setAutoFillBackground(False)
        self.temp_chart.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.temp_chart.setObjectName("temp_chart")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 100, 151, 240))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.ports_comboBox = QtWidgets.QComboBox(self.splitter)
        self.ports_comboBox.setObjectName("ports_comboBox")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setObjectName("label_2")
        self.speed_comboBox = QtWidgets.QComboBox(self.splitter)
        self.speed_comboBox.setObjectName("speed_comboBox")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.speed_comboBox.addItem("")
        self.btn_parar = QtWidgets.QPushButton(self.splitter)
        self.btn_parar.setObjectName("btn_parar")
        self.btn_iniciar = QtWidgets.QPushButton(self.splitter)
        self.btn_iniciar.setObjectName("btn_iniciar")
        self.chkb_sensor_1 = QtWidgets.QCheckBox(self.splitter)
        self.chkb_sensor_1.setObjectName("chkb_sensor_1")
        self.chkb_sensor_2 = QtWidgets.QCheckBox(self.splitter)
        self.chkb_sensor_2.setObjectName("chkb_sensor_2")
        self.chkb_sensor_3 = QtWidgets.QCheckBox(self.splitter)
        self.chkb_sensor_3.setObjectName("chkb_sensor_3")
        self.chkb_sensor_4 = QtWidgets.QCheckBox(self.splitter)
        self.chkb_sensor_4.setObjectName("chkb_sensor_4")
        self.btn_conectar = QtWidgets.QPushButton(self.splitter)
        self.btn_conectar.setObjectName("btn_conectar")
        self.btn_desconectar = QtWidgets.QPushButton(self.splitter)
        self.btn_desconectar.setObjectName("btn_desconectar")
        self.temp_chart.raise_()
        self.splitter.raise_()
        self.splitter.raise_()
        self.splitter.raise_()
        self.btn_iniciar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1248, 19))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setGeometry(QtCore.QRect(315, 166, 130, 146))
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionIniciar_Conexao = QtWidgets.QAction(MainWindow)
        self.actionIniciar_Conexao.setObjectName("actionIniciar_Conexao")
        self.actionParar_Conexao = QtWidgets.QAction(MainWindow)
        self.actionParar_Conexao.setObjectName("actionParar_Conexao")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.menuArquivo.addAction(self.actionAbrir)
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionIniciar_Conexao)
        self.menuArquivo.addAction(self.actionParar_Conexao)
        self.menuArquivo.addAction(self.actionSair)
        self.menuAjuda.addAction(self.actionSobre)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Porta Serial"))
        self.label_2.setText(_translate("MainWindow", "Velocidade"))
        self.speed_comboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.speed_comboBox.setItemText(1, _translate("MainWindow", "19200"))
        self.speed_comboBox.setItemText(2, _translate("MainWindow", "38400"))
        self.speed_comboBox.setItemText(3, _translate("MainWindow", "57600"))
        self.speed_comboBox.setItemText(4, _translate("MainWindow", "115200"))
        self.btn_parar.setText(_translate("MainWindow", "Parar"))
        self.btn_iniciar.setText(_translate("MainWindow", "Iniciar"))
        self.chkb_sensor_1.setText(_translate("MainWindow", "Sensor 1"))
        self.chkb_sensor_2.setText(_translate("MainWindow", "Sensor 2"))
        self.chkb_sensor_3.setText(_translate("MainWindow", "Sensor 3"))
        self.chkb_sensor_4.setText(_translate("MainWindow", "Sensor 4"))
        self.btn_conectar.setText(_translate("MainWindow", "Conectar"))
        self.btn_desconectar.setText(_translate("MainWindow", "Desconectar"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionIniciar_Conexao.setText(_translate("MainWindow", "Iniciar Conexão"))
        self.actionParar_Conexao.setText(_translate("MainWindow", "Parar Conexão"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))


    def preencher_portas_combobox(self, AvailablePorts):
        vNbCombo = ""
        self.ports_comboBox.clear()
        for value in AvailablePorts:
            self.ports_comboBox.addItem(value)
            vNbCombo += value + " - "
            vNbCombo = vNbCombo[:-3]
        print(("Portas Seriais Disponiveis %s " % (vNbCombo)))

    def attachInitializeEvent(self, event):
        self.btn_iniciar.clicked.connect(event)

    def attachDisconnectEvent(self, event):
        self.btn_desconectar.clicked.connect(event)

    def attachConnectEvent(self, event):
        self.btn_conectar.clicked.connect(
            lambda: event(self.speed_comboBox.currentText(), self.ports_comboBox.currentText())
        )

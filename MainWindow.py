# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 663)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Abrir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Abrir.setGeometry(QtCore.QRect(20, 40, 93, 31))
        self.Abrir.setObjectName("Abrir")
        self.Guardar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Guardar.setGeometry(QtCore.QRect(130, 40, 93, 31))
        self.Guardar.setStyleSheet("")
        self.Guardar.setObjectName("Guardar")
        self.TablaAnalisis = QtWidgets.QTableView(parent=self.centralwidget)
        self.TablaAnalisis.setEnabled(True)
        self.TablaAnalisis.setGeometry(QtCore.QRect(770, 80, 371, 301))
        self.TablaAnalisis.setStyleSheet("QTableView {\n"
"    border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"    border-radius: 10px;    /* Esquinas redondeadas */\n"
"    padding: 1px;           /* Espacio interno */\n"
"}")
        self.TablaAnalisis.setLineWidth(4)
        self.TablaAnalisis.setMidLineWidth(4)
        self.TablaAnalisis.setObjectName("TablaAnalisis")
        self.Editor = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.Editor.setGeometry(QtCore.QRect(10, 80, 441, 301))
        self.Editor.setStyleSheet("border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"border-radius: 10px;    /* Esquinas redondeadas */\n"
"padding: 1px;           /* Espacio interno */")
        self.Editor.setObjectName("Editor")
        self.Compilar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Compilar.setGeometry(QtCore.QRect(780, 40, 131, 31))
        self.Compilar.setObjectName("Compilar")
        self.CodigoAltoNivel = QtWidgets.QLabel(parent=self.centralwidget)
        self.CodigoAltoNivel.setGeometry(QtCore.QRect(130, 0, 221, 31))
        self.CodigoAltoNivel.setStyleSheet("font: 600 10pt \"Segoe UI\";")
        self.CodigoAltoNivel.setObjectName("CodigoAltoNivel")
        self.CodigoEnsamblador = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.CodigoEnsamblador.setGeometry(QtCore.QRect(10, 430, 441, 171))
        self.CodigoEnsamblador.setStyleSheet("border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"border-radius: 10px;    /* Esquinas redondeadas */\n"
"padding: 1px;           /* Espacio interno */")
        self.CodigoEnsamblador.setObjectName("CodigoEnsamblador")
        self.Ensamblar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Ensamblar.setGeometry(QtCore.QRect(250, 390, 191, 31))
        self.Ensamblar.setObjectName("Ensamblar")
        self.Enlazar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Enlazar.setGeometry(QtCore.QRect(500, 390, 201, 29))
        self.Enlazar.setObjectName("Enlazar")
        self.SalidaEnlazarCargar = QtWidgets.QTableView(parent=self.centralwidget)
        self.SalidaEnlazarCargar.setGeometry(QtCore.QRect(740, 430, 401, 171))
        self.SalidaEnlazarCargar.setStyleSheet("QTableView {\n"
"    border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"    border-radius: 10px;    /* Esquinas redondeadas */\n"
"    padding: 1px;           /* Espacio interno */\n"
"}")
        self.SalidaEnlazarCargar.setLineWidth(4)
        self.SalidaEnlazarCargar.setMidLineWidth(4)
        self.SalidaEnlazarCargar.setObjectName("SalidaEnlazarCargar")
        self.RAM = QtWidgets.QLabel(parent=self.centralwidget)
        self.RAM.setGeometry(QtCore.QRect(900, 390, 81, 31))
        self.RAM.setStyleSheet("font: 600 10pt \"Segoe UI\";")
        self.RAM.setObjectName("RAM")
        self.Preprocesar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Preprocesar.setGeometry(QtCore.QRect(480, 40, 93, 31))
        self.Preprocesar.setObjectName("Preprocesar")
        self.Preprocesado = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.Preprocesado.setGeometry(QtCore.QRect(460, 80, 301, 301))
        self.Preprocesado.setStyleSheet("border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"border-radius: 10px;    /* Esquinas redondeadas */\n"
"padding: 1px;           /* Espacio interno */")
        self.Preprocesado.setObjectName("Preprocesado")
        self.Abrir_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Abrir_2.setGeometry(QtCore.QRect(20, 390, 93, 31))
        self.Abrir_2.setObjectName("Abrir_2")
        self.Guardar_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Guardar_2.setGeometry(QtCore.QRect(130, 390, 93, 31))
        self.Guardar_2.setStyleSheet("")
        self.Guardar_2.setObjectName("Guardar_2")
        self.ResultadoEnsamblador = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.ResultadoEnsamblador.setGeometry(QtCore.QRect(460, 430, 271, 171))
        self.ResultadoEnsamblador.setStyleSheet("border: 5px solid black;  /* Cambia el grosor y color del borde */\n"
"border-radius: 10px;    /* Esquinas redondeadas */\n"
"padding: 1px;           /* Espacio interno */")
        self.ResultadoEnsamblador.setObjectName("ResultadoEnsamblador")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Abrir.setText(_translate("MainWindow", "Abrir"))
        self.Guardar.setText(_translate("MainWindow", "Guardar"))
        self.Compilar.setText(_translate("MainWindow", "Analizar"))
        self.CodigoAltoNivel.setText(_translate("MainWindow", "CÓDIGO EN ALTO NIVEL"))
        self.Ensamblar.setText(_translate("MainWindow", "Ensamblar"))
        self.Enlazar.setText(_translate("MainWindow", "Enlazar - Cargar"))
        self.RAM.setText(_translate("MainWindow", "RAM"))
        self.Preprocesar.setText(_translate("MainWindow", "Preprocesar"))
        self.Abrir_2.setText(_translate("MainWindow", "Abrir"))
        self.Guardar_2.setText(_translate("MainWindow", "Guardar"))

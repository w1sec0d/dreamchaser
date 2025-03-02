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
        MainWindow.setEnabled(True)
        MainWindow.resize(1239, 801)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("QGroupBox, QLabel {\n"
"    background-color: #f8f9fa;  /* Fondo más claro */\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Efecto de sombra */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #2980b9; /* Azul más profundo */\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #1f669b;\n"
"    transition: all 0.3s ease-in-out;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2471a3;\n"
"    border: 2px solid #154d75;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1f669b;\n"
"    border: 2px solid #0e4975;\n"
"    padding: 10px; /* Simula una pulsación */\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #ffffff;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 8px;\n"
"    gridline-color: #bdc3c7;\n"
"    font-size: 14px;\n"
"    selection-background-color: #3498db;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2c3e50;\n"
"    color: white;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #1f669b;\n"
"}\n"
"\n"
"QPlainTextEdit, QTextBrowser {\n"
"    background-color: #f0f3f4;\n"
"    border: 2px solid #bdc3c7;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"}\n"
"\n"
"QPlainTextEdit:focus, QTextBrowser:focus {\n"
"    border: 2px solid #3498db;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(1920, 1080))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1704, 760))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ResultadoEnsamblador = QtWidgets.QTextBrowser(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ResultadoEnsamblador.sizePolicy().hasHeightForWidth())
        self.ResultadoEnsamblador.setSizePolicy(sizePolicy)
        self.ResultadoEnsamblador.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.ResultadoEnsamblador.setFont(font)
        self.ResultadoEnsamblador.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.ResultadoEnsamblador.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.ResultadoEnsamblador.setObjectName("ResultadoEnsamblador")
        self.gridLayout_2.addWidget(self.ResultadoEnsamblador, 5, 2, 7, 1)
        self.Codigo_Ensamblador = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setItalic(False)
        self.Codigo_Ensamblador.setFont(font)
        self.Codigo_Ensamblador.setStyleSheet("font: 600 15pt \"Segoe UI\";")
        self.Codigo_Ensamblador.setObjectName("Codigo_Ensamblador")
        self.gridLayout_2.addWidget(self.Codigo_Ensamblador, 0, 3, 1, 2)
        self.Compilar = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Compilar.setAutoDefault(False)
        self.Compilar.setDefault(False)
        self.Compilar.setFlat(False)
        self.Compilar.setObjectName("Compilar")
        self.gridLayout_2.addWidget(self.Compilar, 4, 8, 1, 2)
        self.Tabla_Registros = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_3)
        self.Tabla_Registros.setMinimumSize(QtCore.QSize(356, 0))
        self.Tabla_Registros.setStyleSheet("QScrollBar:vertical {\n"
"    background: #ecf0f1;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #2980b9;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #1f669b;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.Tabla_Registros.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Tabla_Registros.setObjectName("Tabla_Registros")
        self.Tabla_Registros.setColumnCount(2)
        self.Tabla_Registros.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Registros.setItem(3, 0, item)
        self.Tabla_Registros.horizontalHeader().setVisible(True)
        self.Tabla_Registros.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout_2.addWidget(self.Tabla_Registros, 2, 1, 4, 1)
        self.Tabla_Alu = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_3)
        self.Tabla_Alu.setMinimumSize(QtCore.QSize(356, 0))
        self.Tabla_Alu.setStyleSheet("QScrollBar:vertical {\n"
"    background: #ecf0f1;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #2980b9;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #1f669b;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.Tabla_Alu.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Tabla_Alu.setObjectName("Tabla_Alu")
        self.Tabla_Alu.setColumnCount(2)
        self.Tabla_Alu.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Alu.setItem(3, 0, item)
        self.Tabla_Alu.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout_2.addWidget(self.Tabla_Alu, 11, 1, 1, 1)
        self.RAM = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        self.RAM.setFont(font)
        self.RAM.setStyleSheet("QLabel {\n"
"    color: #2c3e50;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.RAM.setObjectName("RAM")
        self.gridLayout_2.addWidget(self.RAM, 0, 0, 1, 1)
        self.Guardar = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Guardar.setStyleSheet("")
        self.Guardar.setObjectName("Guardar")
        self.gridLayout_2.addWidget(self.Guardar, 4, 5, 1, 3)
        self.Ensamblar = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Ensamblar.setObjectName("Ensamblar")
        self.gridLayout_2.addWidget(self.Ensamblar, 4, 4, 1, 1)
        self.Localizacion = QtWidgets.QSpinBox(parent=self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Localizacion.sizePolicy().hasHeightForWidth())
        self.Localizacion.setSizePolicy(sizePolicy)
        self.Localizacion.setMinimumSize(QtCore.QSize(288, 21))
        self.Localizacion.setStyleSheet("QSpinBox {\n"
"    background-color: #ecf0f1;  /* Fondo gris claro */\n"
"    color: #2c3e50;  /* Texto oscuro */\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", Arial, sans-serif;\n"
"    border: 2px solid #bdc3c7;  /* Borde sutil */\n"
"    border-radius: 6px;  /* Bordes redondeados */\n"
"    padding: 6px 10px;  /* Espaciado interno */\n"
"    selection-color: white;  /* Color del texto seleccionado */\n"
"}\n"
"\n"
"/* Cuando está en focus */\n"
"QSpinBox:focus {\n"
"    border: 2px solid #3498db;  /* Azul al enfocarse */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* Estilo cuando el SpinBox está deshabilitado */\n"
"QSpinBox:disabled {\n"
"    background-color: #dfe6e9;\n"
"    color: #7f8c8d;\n"
"    border: 2px solid #bdc3c7;\n"
"}\n"
"")
        self.Localizacion.setObjectName("Localizacion")
        self.gridLayout_2.addWidget(self.Localizacion, 2, 2, 2, 1)
        self.Consola = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.Consola.setStyleSheet("")
        self.Consola.setObjectName("Consola")
        self.gridLayout_2.addWidget(self.Consola, 13, 2, 4, 2)
        self.Saltar_Ultima_Instruccion = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Saltar_Ultima_Instruccion.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Saltar_Ultima_Instruccion.setObjectName("Saltar_Ultima_Instruccion")
        self.gridLayout_2.addWidget(self.Saltar_Ultima_Instruccion, 16, 1, 1, 1)
        self.InputEditor = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.InputEditor.setStyleSheet("")
        self.InputEditor.setObjectName("InputEditor")
        self.gridLayout_2.addWidget(self.InputEditor, 13, 4, 4, 6)
        self.CodigoAltoNivel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.CodigoAltoNivel.setStyleSheet("font: 600 15pt \"Segoe UI\";")
        self.CodigoAltoNivel.setObjectName("CodigoAltoNivel")
        self.gridLayout_2.addWidget(self.CodigoAltoNivel, 0, 6, 1, 4)
        self.Unidad_Control = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.Unidad_Control.setMouseTracking(True)
        self.Unidad_Control.setToolTip("")
        self.Unidad_Control.setObjectName("Unidad_Control")
        self.gridLayout_2.addWidget(self.Unidad_Control, 12, 1, 1, 1)
        self.Reiniciar = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Reiniciar.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Reiniciar.setObjectName("Reiniciar")
        self.gridLayout_2.addWidget(self.Reiniciar, 15, 1, 1, 1)
        self.CodigoEnsamblador = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.CodigoEnsamblador.setStyleSheet("")
        self.CodigoEnsamblador.setObjectName("CodigoEnsamblador")
        self.gridLayout_2.addWidget(self.CodigoEnsamblador, 5, 3, 7, 2)
        self.Editor = QtWidgets.QPlainTextEdit(parent=self.scrollAreaWidgetContents_3)
        self.Editor.setStyleSheet("")
        self.Editor.setObjectName("Editor")
        self.gridLayout_2.addWidget(self.Editor, 5, 5, 7, 5)
        self.Abrir = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Abrir.setStyleSheet("")
        self.Abrir.setObjectName("Abrir")
        self.gridLayout_2.addWidget(self.Abrir, 2, 5, 1, 3)
        self.Registros = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.Registros.setMouseTracking(True)
        self.Registros.setToolTip("")
        self.Registros.setObjectName("Registros")
        self.gridLayout_2.addWidget(self.Registros, 0, 1, 1, 1)
        self.Tabla_Unidad_Control = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_3)
        self.Tabla_Unidad_Control.setMinimumSize(QtCore.QSize(288, 0))
        self.Tabla_Unidad_Control.setStyleSheet("")
        self.Tabla_Unidad_Control.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.Tabla_Unidad_Control.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Tabla_Unidad_Control.setObjectName("Tabla_Unidad_Control")
        self.Tabla_Unidad_Control.setColumnCount(1)
        self.Tabla_Unidad_Control.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Unidad_Control.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Unidad_Control.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Unidad_Control.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Unidad_Control.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabla_Unidad_Control.setItem(1, 0, item)
        self.Tabla_Unidad_Control.horizontalHeader().setDefaultSectionSize(165)
        self.gridLayout_2.addWidget(self.Tabla_Unidad_Control, 13, 1, 1, 1)
        self.INPUT = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.INPUT.setStyleSheet("font: 600 10pt \"Segoe UI\";")
        self.INPUT.setObjectName("INPUT")
        self.gridLayout_2.addWidget(self.INPUT, 12, 4, 1, 1)
        self.Guardar_2 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Guardar_2.setStyleSheet("")
        self.Guardar_2.setObjectName("Guardar_2")
        self.gridLayout_2.addWidget(self.Guardar_2, 4, 3, 1, 1)
        self.Abrir_2 = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Abrir_2.setObjectName("Abrir_2")
        self.gridLayout_2.addWidget(self.Abrir_2, 2, 3, 1, 1)
        self.Indicadores_ALU = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.Indicadores_ALU.setMouseTracking(True)
        self.Indicadores_ALU.setToolTip("")
        self.Indicadores_ALU.setObjectName("Indicadores_ALU")
        self.gridLayout_2.addWidget(self.Indicadores_ALU, 8, 1, 3, 1)
        self.Enlazar = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Enlazar.setObjectName("Enlazar")
        self.gridLayout_2.addWidget(self.Enlazar, 4, 2, 1, 1)
        self.INPUT_2 = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        self.INPUT_2.setStyleSheet("font: 600 10pt \"Segoe UI\";")
        self.INPUT_2.setObjectName("INPUT_2")
        self.gridLayout_2.addWidget(self.INPUT_2, 12, 2, 1, 1)
        self.Codigo_Relocalizable = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        font.setItalic(False)
        self.Codigo_Relocalizable.setFont(font)
        self.Codigo_Relocalizable.setStyleSheet("font: 600 15pt \"Segoe UI\";")
        self.Codigo_Relocalizable.setObjectName("Codigo_Relocalizable")
        self.gridLayout_2.addWidget(self.Codigo_Relocalizable, 0, 2, 1, 1)
        self.Sig_instruccion = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents_3)
        self.Sig_instruccion.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Sig_instruccion.setObjectName("Sig_instruccion")
        self.gridLayout_2.addWidget(self.Sig_instruccion, 14, 1, 1, 1)
        self.SalidaEnlazarCargar = QtWidgets.QTableWidget(parent=self.scrollAreaWidgetContents_3)
        self.SalidaEnlazarCargar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SalidaEnlazarCargar.sizePolicy().hasHeightForWidth())
        self.SalidaEnlazarCargar.setSizePolicy(sizePolicy)
        self.SalidaEnlazarCargar.setMinimumSize(QtCore.QSize(300, 0))
        self.SalidaEnlazarCargar.setAccessibleName("")
        self.SalidaEnlazarCargar.setAccessibleDescription("")
        self.SalidaEnlazarCargar.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.SalidaEnlazarCargar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.SalidaEnlazarCargar.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.SalidaEnlazarCargar.setLineWidth(1)
        self.SalidaEnlazarCargar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.SalidaEnlazarCargar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.SalidaEnlazarCargar.setAutoScrollMargin(16)
        self.SalidaEnlazarCargar.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.SalidaEnlazarCargar.setShowGrid(True)
        self.SalidaEnlazarCargar.setWordWrap(False)
        self.SalidaEnlazarCargar.setCornerButtonEnabled(False)
        self.SalidaEnlazarCargar.setRowCount(1024)
        self.SalidaEnlazarCargar.setObjectName("SalidaEnlazarCargar")
        self.SalidaEnlazarCargar.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setText("Valor Binario")
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.SalidaEnlazarCargar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.SalidaEnlazarCargar.setItem(11, 0, item)
        self.SalidaEnlazarCargar.horizontalHeader().setCascadingSectionResizes(False)
        self.SalidaEnlazarCargar.horizontalHeader().setDefaultSectionSize(210)
        self.gridLayout_2.addWidget(self.SalidaEnlazarCargar, 2, 0, 21, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ResultadoEnsamblador.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\',\'Arial\',\'sans-serif\'; font-size:14px;\">00000000000000000000000000000000</span></p></body></html>"))
        self.Codigo_Ensamblador.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">CÓDIGO ENSAMBALDOR</span></p></body></html>"))
        self.Compilar.setText(_translate("MainWindow", "COMPILAR"))
        item = self.Tabla_Registros.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.Tabla_Registros.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.Tabla_Registros.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.Tabla_Registros.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.Tabla_Registros.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.Tabla_Registros.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.Tabla_Registros.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.Tabla_Registros.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.Tabla_Registros.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        item = self.Tabla_Registros.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DECIMAL"))
        __sortingEnabled = self.Tabla_Registros.isSortingEnabled()
        self.Tabla_Registros.setSortingEnabled(False)
        self.Tabla_Registros.setSortingEnabled(__sortingEnabled)
        item = self.Tabla_Alu.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "C"))
        item = self.Tabla_Alu.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "P"))
        item = self.Tabla_Alu.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "N"))
        item = self.Tabla_Alu.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.Tabla_Alu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        item = self.Tabla_Alu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DECIMAL"))
        __sortingEnabled = self.Tabla_Alu.isSortingEnabled()
        self.Tabla_Alu.setSortingEnabled(False)
        self.Tabla_Alu.setSortingEnabled(__sortingEnabled)
        self.RAM.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">RAM</span></p></body></html>"))
        self.Guardar.setText(_translate("MainWindow", "Guardar"))
        self.Ensamblar.setText(_translate("MainWindow", "ENSAMBLAR"))
        self.Saltar_Ultima_Instruccion.setText(_translate("MainWindow", "Saltar a última intrucción"))
        self.CodigoAltoNivel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">CÓDIGO EN ALTO NIVEL</span></p></body></html>"))
        self.Unidad_Control.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:700;\">UNIDAD DE CONTROL</span></p></body></html>"))
        self.Reiniciar.setText(_translate("MainWindow", "Reiniciar"))
        self.Abrir.setText(_translate("MainWindow", "Abrir"))
        self.Registros.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:700;\">REGISTROS</span></p></body></html>"))
        item = self.Tabla_Unidad_Control.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "IC"))
        item = self.Tabla_Unidad_Control.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CP"))
        item = self.Tabla_Unidad_Control.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BINARIO"))
        __sortingEnabled = self.Tabla_Unidad_Control.isSortingEnabled()
        self.Tabla_Unidad_Control.setSortingEnabled(False)
        self.Tabla_Unidad_Control.setSortingEnabled(__sortingEnabled)
        self.INPUT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">INPUT</span></p></body></html>"))
        self.Guardar_2.setText(_translate("MainWindow", "Guardar"))
        self.Abrir_2.setText(_translate("MainWindow", "Abrir"))
        self.Indicadores_ALU.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:700;\">INDICADORES ALU</span></p></body></html>"))
        self.Enlazar.setText(_translate("MainWindow", "Enlazar - Cargar"))
        self.INPUT_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">CONSOLA</span></p></body></html>"))
        self.Codigo_Relocalizable.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">CÓDIGO RELOCALIZABLE</span></p></body></html>"))
        self.Sig_instruccion.setText(_translate("MainWindow", "Siguiente instrucción"))
        self.SalidaEnlazarCargar.setSortingEnabled(False)
        __sortingEnabled = self.SalidaEnlazarCargar.isSortingEnabled()
        self.SalidaEnlazarCargar.setSortingEnabled(False)
        self.SalidaEnlazarCargar.setSortingEnabled(__sortingEnabled)

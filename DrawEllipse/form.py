# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Okno(object):
    def setupUi(self, Okno):
        Okno.setObjectName("Okno")
        Okno.setEnabled(True)
        Okno.resize(438, 360)
        Okno.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Okno.setMouseTracking(True)
        Okno.setTabletTracking(True)
        Okno.setWindowOpacity(1.0)
        self.label_2 = QtWidgets.QLabel(Okno)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label_2.setText("")
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(Okno)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 471, 271))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.label_4 = QtWidgets.QLabel(self.tab_7)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 251, 16))
        self.label_4.setObjectName("label_4")
        self.doubleSpinBox_33 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_33.setGeometry(QtCore.QRect(20, 30, 151, 21))
        self.doubleSpinBox_33.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.doubleSpinBox_33.setDecimals(3)
        self.doubleSpinBox_33.setMinimum(-10000000000.0)
        self.doubleSpinBox_33.setMaximum(10000000000.0)
        self.doubleSpinBox_33.setObjectName("doubleSpinBox_33")
        self.doubleSpinBox_34 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_34.setGeometry(QtCore.QRect(20, 50, 151, 21))
        self.doubleSpinBox_34.setDecimals(3)
        self.doubleSpinBox_34.setMinimum(-10000000000.0)
        self.doubleSpinBox_34.setMaximum(10000000000.0)
        self.doubleSpinBox_34.setObjectName("doubleSpinBox_34")
        self.doubleSpinBox_35 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_35.setGeometry(QtCore.QRect(20, 100, 151, 22))
        self.doubleSpinBox_35.setDecimals(3)
        self.doubleSpinBox_35.setMinimum(-10000000000.0)
        self.doubleSpinBox_35.setMaximum(10000000000.0)
        self.doubleSpinBox_35.setObjectName("doubleSpinBox_35")
        self.doubleSpinBox_36 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_36.setGeometry(QtCore.QRect(20, 120, 151, 22))
        self.doubleSpinBox_36.setDecimals(3)
        self.doubleSpinBox_36.setMinimum(-10000000000.0)
        self.doubleSpinBox_36.setMaximum(10000000000.0)
        self.doubleSpinBox_36.setObjectName("doubleSpinBox_36")
        self.label_11 = QtWidgets.QLabel(self.tab_7)
        self.label_11.setGeometry(QtCore.QRect(20, 80, 251, 16))
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox_37 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_37.setGeometry(QtCore.QRect(20, 170, 151, 22))
        self.doubleSpinBox_37.setDecimals(3)
        self.doubleSpinBox_37.setMinimum(-10000000000.0)
        self.doubleSpinBox_37.setMaximum(10000000000.0)
        self.doubleSpinBox_37.setObjectName("doubleSpinBox_37")
        self.doubleSpinBox_38 = QtWidgets.QDoubleSpinBox(self.tab_7)
        self.doubleSpinBox_38.setGeometry(QtCore.QRect(20, 190, 151, 22))
        self.doubleSpinBox_38.setDecimals(3)
        self.doubleSpinBox_38.setMinimum(-10000000000.0)
        self.doubleSpinBox_38.setMaximum(10000000000.0)
        self.doubleSpinBox_38.setProperty("value", 0.0)
        self.doubleSpinBox_38.setObjectName("doubleSpinBox_38")
        self.label_20 = QtWidgets.QLabel(self.tab_7)
        self.label_20.setGeometry(QtCore.QRect(20, 150, 251, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 210, 111, 21))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.tab_7)
        self.label_3.setGeometry(QtCore.QRect(270, 40, 161, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/plugins/DrawEllipse/1.PNG"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_7 = QtWidgets.QLabel(self.tab_8)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 251, 16))
        self.label_7.setObjectName("label_7")
        self.label_21 = QtWidgets.QLabel(self.tab_8)
        self.label_21.setGeometry(QtCore.QRect(20, 60, 191, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_8.setGeometry(QtCore.QRect(310, 210, 111, 21))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_8.setObjectName("pushButton_8")
        self.doubleSpinBox_39 = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_39.setGeometry(QtCore.QRect(30, 80, 111, 21))
        self.doubleSpinBox_39.setDecimals(3)
        self.doubleSpinBox_39.setMinimum(0.0)
        self.doubleSpinBox_39.setMaximum(10000000000.0)
        self.doubleSpinBox_39.setObjectName("doubleSpinBox_39")
        self.doubleSpinBox_40 = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_40.setGeometry(QtCore.QRect(30, 30, 111, 21))
        self.doubleSpinBox_40.setDecimals(3)
        self.doubleSpinBox_40.setMinimum(0.0)
        self.doubleSpinBox_40.setMaximum(10000000000.0)
        self.doubleSpinBox_40.setObjectName("doubleSpinBox_40")
        self.label_22 = QtWidgets.QLabel(self.tab_8)
        self.label_22.setGeometry(QtCore.QRect(20, 110, 211, 16))
        self.label_22.setObjectName("label_22")
        self.doubleSpinBox_41 = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_41.setGeometry(QtCore.QRect(30, 150, 151, 22))
        self.doubleSpinBox_41.setDecimals(3)
        self.doubleSpinBox_41.setMinimum(-10000000000.0)
        self.doubleSpinBox_41.setMaximum(10000000000.0)
        self.doubleSpinBox_41.setProperty("value", 0.0)
        self.doubleSpinBox_41.setObjectName("doubleSpinBox_41")
        self.doubleSpinBox_42 = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_42.setGeometry(QtCore.QRect(30, 130, 151, 22))
        self.doubleSpinBox_42.setDecimals(3)
        self.doubleSpinBox_42.setMinimum(-10000000000.0)
        self.doubleSpinBox_42.setMaximum(10000000000.0)
        self.doubleSpinBox_42.setObjectName("doubleSpinBox_42")
        self.doubleSpinBox_43 = QtWidgets.QDoubleSpinBox(self.tab_8)
        self.doubleSpinBox_43.setGeometry(QtCore.QRect(30, 200, 111, 21))
        self.doubleSpinBox_43.setDecimals(4)
        self.doubleSpinBox_43.setMinimum(0.0)
        self.doubleSpinBox_43.setMaximum(10000000000.0)
        self.doubleSpinBox_43.setObjectName("doubleSpinBox_43")
        self.label_23 = QtWidgets.QLabel(self.tab_8)
        self.label_23.setGeometry(QtCore.QRect(20, 180, 191, 16))
        self.label_23.setObjectName("label_23")
        self.label_5 = QtWidgets.QLabel(self.tab_8)
        self.label_5.setGeometry(QtCore.QRect(250, 30, 171, 161))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/plugins/DrawEllipse/2.PNG"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.label_40 = QtWidgets.QLabel(self.tab_9)
        self.label_40.setGeometry(QtCore.QRect(20, 10, 231, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_9)
        self.label_41.setGeometry(QtCore.QRect(20, 60, 211, 16))
        self.label_41.setObjectName("label_41")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_9)
        self.pushButton_9.setGeometry(QtCore.QRect(310, 210, 111, 21))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setObjectName("pushButton_9")
        self.doubleSpinBox_45 = QtWidgets.QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_45.setGeometry(QtCore.QRect(30, 30, 111, 21))
        self.doubleSpinBox_45.setSuffix("")
        self.doubleSpinBox_45.setDecimals(5)
        self.doubleSpinBox_45.setMinimum(0.0)
        self.doubleSpinBox_45.setMaximum(1.0)
        self.doubleSpinBox_45.setSingleStep(0.01)
        self.doubleSpinBox_45.setObjectName("doubleSpinBox_45")
        self.doubleSpinBox_46 = QtWidgets.QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_46.setGeometry(QtCore.QRect(30, 100, 151, 21))
        self.doubleSpinBox_46.setDecimals(3)
        self.doubleSpinBox_46.setMinimum(-10000000000.0)
        self.doubleSpinBox_46.setMaximum(10000000000.0)
        self.doubleSpinBox_46.setObjectName("doubleSpinBox_46")
        self.doubleSpinBox_47 = QtWidgets.QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_47.setGeometry(QtCore.QRect(30, 80, 151, 21))
        self.doubleSpinBox_47.setDecimals(3)
        self.doubleSpinBox_47.setMinimum(-10000000000.0)
        self.doubleSpinBox_47.setMaximum(10000000000.0)
        self.doubleSpinBox_47.setObjectName("doubleSpinBox_47")
        self.label_42 = QtWidgets.QLabel(self.tab_9)
        self.label_42.setGeometry(QtCore.QRect(20, 130, 191, 16))
        self.label_42.setObjectName("label_42")
        self.doubleSpinBox_48 = QtWidgets.QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_48.setGeometry(QtCore.QRect(30, 150, 111, 21))
        self.doubleSpinBox_48.setDecimals(3)
        self.doubleSpinBox_48.setMinimum(0.0)
        self.doubleSpinBox_48.setMaximum(10000000000.0)
        self.doubleSpinBox_48.setObjectName("doubleSpinBox_48")
        self.doubleSpinBox_44 = QtWidgets.QDoubleSpinBox(self.tab_9)
        self.doubleSpinBox_44.setGeometry(QtCore.QRect(30, 200, 111, 21))
        self.doubleSpinBox_44.setDecimals(4)
        self.doubleSpinBox_44.setMinimum(0.0)
        self.doubleSpinBox_44.setMaximum(10000000000.0)
        self.doubleSpinBox_44.setObjectName("doubleSpinBox_44")
        self.label_24 = QtWidgets.QLabel(self.tab_9)
        self.label_24.setGeometry(QtCore.QRect(20, 180, 191, 16))
        self.label_24.setObjectName("label_24")
        self.label_6 = QtWidgets.QLabel(self.tab_9)
        self.label_6.setGeometry(QtCore.QRect(250, 30, 171, 171))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/plugins/DrawEllipse/3.PNG"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_9, "")
        self.label = QtWidgets.QLabel(Okno)
        self.label.setGeometry(QtCore.QRect(80, 10, 281, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label.setMouseTracking(True)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(10)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(-5)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Okno)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 330, 211, 23))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(Okno)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 31, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/plugins/DrawEllipse/icon.png"))
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Okno)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Okno)

    def retranslateUi(self, Okno):
        _translate = QtCore.QCoreApplication.translate
        Okno.setWindowTitle(_translate("Okno", "DrawEllipse"))
        self.label_4.setText(_translate("Okno", "Wprowadź współrzędne pierwszej ogniskowej (f1)"))
        self.doubleSpinBox_33.setPrefix(_translate("Okno", " X: "))
        self.doubleSpinBox_33.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_34.setPrefix(_translate("Okno", " Y: "))
        self.doubleSpinBox_34.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_35.setPrefix(_translate("Okno", " X: "))
        self.doubleSpinBox_35.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_36.setPrefix(_translate("Okno", " Y: "))
        self.doubleSpinBox_36.setSuffix(_translate("Okno", " m "))
        self.label_11.setText(_translate("Okno", "Wprowadź współrzędne drugiej ogniskowej (f2)"))
        self.doubleSpinBox_37.setPrefix(_translate("Okno", " X: "))
        self.doubleSpinBox_37.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_38.setPrefix(_translate("Okno", " Y: "))
        self.doubleSpinBox_38.setSuffix(_translate("Okno", " m "))
        self.label_20.setText(_translate("Okno", "Wprowadź współrzędne końca krótszej półosi (f3)"))
        self.pushButton_4.setText(_translate("Okno", "Rysuj elipsę"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Okno", "Współrzędne ogniskowych elipsy"))
        self.label_7.setText(_translate("Okno", "Wprowadź długość krótszej półosi (b)"))
        self.label_21.setText(_translate("Okno", "Wprowadź długość dłuższej półosi (a)"))
        self.pushButton_8.setText(_translate("Okno", "Rysuj elipsę"))
        self.doubleSpinBox_39.setPrefix(_translate("Okno", " a = "))
        self.doubleSpinBox_39.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_40.setPrefix(_translate("Okno", " b = "))
        self.doubleSpinBox_40.setSuffix(_translate("Okno", " m"))
        self.label_22.setText(_translate("Okno", "Wprowadź współrzędne środka elipsy (pc)"))
        self.doubleSpinBox_41.setPrefix(_translate("Okno", " Y: "))
        self.doubleSpinBox_41.setSuffix(_translate("Okno", " m"))
        self.doubleSpinBox_42.setPrefix(_translate("Okno", " X: "))
        self.doubleSpinBox_42.setSuffix(_translate("Okno", " m "))
        self.doubleSpinBox_43.setPrefix(_translate("Okno", "  φ = "))
        self.doubleSpinBox_43.setSuffix(_translate("Okno", "°"))
        self.label_23.setText(_translate("Okno", "Wprowadź kąt skręcenia elipsy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("Okno", "Długości półosi elipsy"))
        self.label_40.setText(_translate("Okno", "Parametr ekscetryczności - mimośród elipsy (e)"))
        self.label_41.setText(_translate("Okno", "Wprowadź współrzędne środka elipsy (pc)"))
        self.pushButton_9.setText(_translate("Okno", "Rysuj elipsę"))
        self.doubleSpinBox_45.setPrefix(_translate("Okno", " e = "))
        self.doubleSpinBox_46.setPrefix(_translate("Okno", " Y: "))
        self.doubleSpinBox_46.setSuffix(_translate("Okno", " m"))
        self.doubleSpinBox_47.setPrefix(_translate("Okno", " X: "))
        self.doubleSpinBox_47.setSuffix(_translate("Okno", " m"))
        self.label_42.setText(_translate("Okno", "Wprowadź długość dłuższej półosi (a)"))
        self.doubleSpinBox_48.setPrefix(_translate("Okno", " a = "))
        self.doubleSpinBox_48.setSuffix(_translate("Okno", " m"))
        self.doubleSpinBox_44.setPrefix(_translate("Okno", "  φ = "))
        self.doubleSpinBox_44.setSuffix(_translate("Okno", "°"))
        self.label_24.setText(_translate("Okno", "Wprowadź kąt skręcenia elipsy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Okno", "Ekscentryczność elipsy"))
        self.label.setText(_translate("Okno", "  Rysowanie elipsy w oparciu o:"))
        self.pushButton_2.setText(_translate("Okno", "Zapisz warstwę"))

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DrawEllipse
                                 A QGIS plugin
 Narzędzie do rysowania elipsy w oparciu o podane parametry.
                              -------------------
        begin                : 2020-05-25
        copyright            : (C) 2020 by Adrian&Filip
        email                : adriannowak000@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""



from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.core import *
from .form import Ui_Okno
from qgis.utils import *
from qgis.gui import *
from qgis.PyQt.QtCore import QVariant
from qgis.PyQt.QtCore import QDir
import math
from .resources import *


class DrawEllipse:

    def __init__(self, iface):
        """
        Inicjalizacja
        :param iface: QgisInterface
        :return:
        """

        # Zapisanie odniesienia do interefejsu QGISa
        self.iface = iface

    def initGui(self):

        # Stworzenie akcji, która rozpocznie konfigurację wtyczki

        self.action = QAction(QIcon(":\plugins\DrawEllipse\icon.png"), "DrawEllipse", self.iface.mainWindow())

        # Dodanie przycisku do paska narzędzi

        self.iface.addToolBarIcon(self.action)

        # Oprogramowanie funkcjonalności uruchamiania okna

        self.action.triggered.connect(self.run)

    def unload(self):

        # Usunięcie ikony wtyczki z paska narzędzi

        self.iface.removeToolBarIcon(self.action)
        del self.action


    def run(self):

        # Oprogramowowanie uruchamiania okna po kliknięciu na wtyczkę

        self.window = QDialog()
        self.form = Ui_Okno()
        self.form.setupUi(self.window)

        # Zapis warstwy

        self.form.pushButton_2.clicked.connect(self.klikniecie)

        # Zaprogramowanie przycisków do generowania elipsy

        self.form.pushButton_4.released.connect(self.rysuj_elipse_1)
        self.form.pushButton_8.released.connect(self.rysuj_elipse_2)
        self.form.pushButton_9.released.connect(self.rysuj_elipse_3)

        self.window.show()

    def klikniecie(self):

        msg = QMessageBox.question(None, "Zapis", "Czy zapisać warstwę?", QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:

            sciezka = QFileDialog.getSaveFileName(self.window, "Zapisz", "C:\\")

            if QFileDialog.accepted:

                QgsVectorFileWriter.writeAsVectorFormat(self.iface.activeLayer(), sciezka[0], "UTF-8")

                self.window.hide()
        else:
            QMessageBox.critical(None, "Odrzucono", "Warstwa niezapisana")

            self.window.hide()

    # Metoda tworzenia elipsy poprzez zdefiniowanie współrzędnych ogniskowych oraz końca krótszej półosi

    def rysuj_elipse_1(self):

        temp_vlayer = QgsVectorLayer("LineString", "Elipsa_1", "memory")
        QgsProject.instance().addMapLayer(temp_vlayer)

        feat = QgsFeature(temp_vlayer.fields())

        temp_vlayer.dataProvider().addAttributes \
        ([QgsField("id", QVariant.Int)])

        temp_vlayer.updateFields()
        a=self.form.doubleSpinBox_33.value()
        b=self.form.doubleSpinBox_34.value()
        c=self.form.doubleSpinBox_35.value()
        d=self.form.doubleSpinBox_36.value()
        e=self.form.doubleSpinBox_37.value()
        f=self.form.doubleSpinBox_38.value()
        
        if a==b==c==d==e==f: 
		
            self.iface.messageBar().pushMessage("Współrzędne punktów nie mogą być takie same.", "", level=Qgis.Critical, duration=30)
            QgsProject.instance().removeMapLayer(temp_vlayer)
            
        else:
		

            f1 = QgsPoint(a, b)
            f2 = QgsPoint(c, d)
            f3 = QgsPoint(e, f)

            dist_f1f2 = math.sqrt((self.form.doubleSpinBox_35.value() - self.form.doubleSpinBox_33.value()) ** 2 + (
                        self.form.doubleSpinBox_36.value() - self.form.doubleSpinBox_34.value()) ** 2)
            dist_f1f3 = math.sqrt((self.form.doubleSpinBox_37.value() - self.form.doubleSpinBox_33.value()) ** 2 + (
                        self.form.doubleSpinBox_38.value() - self.form.doubleSpinBox_34.value()) ** 2)
            dist_f2f3 = math.sqrt((self.form.doubleSpinBox_37.value() - self.form.doubleSpinBox_35.value()) ** 2 + (
                        self.form.doubleSpinBox_38.value() - self.form.doubleSpinBox_36.value()) ** 2)

            dist_tot = dist_f1f3 + dist_f2f3

            delta_x = self.form.doubleSpinBox_35.value() - self.form.doubleSpinBox_33.value()
            delta_y = self.form.doubleSpinBox_36.value() - self.form.doubleSpinBox_34.value()

            kat = math.degrees(math.atan2(delta_y, delta_x))

            if kat < 0:
                kat += 360
            elif kat > 360:
                kat = 360 - kat

            kat = math.radians(kat)

            X_srodek = delta_x/2
            Y_srodek = delta_y/2

            polos_a = dist_tot / 2.0

            polos_b = math.sqrt((dist_tot / 2.0) ** 2.0 - (dist_f1f2 / 2.0) ** 2.0)

            def iteracja():

                segments = 144

                punkty = []

                for t in [(2 * math.pi) / segments * i for i in range(segments + 1)]:
                    p = QgsPoint(X_srodek +
                                polos_a * math.cos(t) * math.cos(kat) -
                                polos_b * math.sin(t) * math.sin(kat),

                                Y_srodek +
                                polos_a * math.cos(t) * math.sin(kat) +
                                polos_b * math.sin(t) * math.cos(kat))

                    punkty.append(p)

                return punkty

            Elipsa_1 = iteracja()

            feat.setGeometry(QgsGeometry.fromPolyline(Elipsa_1))

            feat.setAttributes([0])

            temp_vlayer.dataProvider().addFeatures([feat])

            temp_vlayer.triggerRepaint()


    # Metoda tworzenia elipsy poprzez zdefiniowanie współrzędnych środka elipsy, długości półosi oraz kąta skręcenia

    def rysuj_elipse_2(self):

        temp_vlayer = QgsVectorLayer("LineString", "Elipsa_2", "memory")
        QgsProject.instance().addMapLayer(temp_vlayer)

        feat = QgsFeature(temp_vlayer.fields())

        temp_vlayer.dataProvider().addAttributes \
        ([QgsField("id", QVariant.Int)])

        temp_vlayer.updateFields()

        X_srodek = self.form.doubleSpinBox_42.value()
        Y_srodek = self.form.doubleSpinBox_41.value()

        polos_a = self.form.doubleSpinBox_39.value()

        polos_b = self.form.doubleSpinBox_40.value()


        if polos_a == 0 and polos_b == 0:

            self.iface.messageBar().pushMessage("Brak podanej długości minimum jednej z półosi.", "", level=Qgis.Critical, duration=30)
            QgsProject.instance().removeMapLayer(temp_vlayer)

        else:

            kat = self.form.doubleSpinBox_43.value()

            kat = math.radians(kat)

            def iteracja():

                segments = 144

                punkty = []

                for t in [(2 * math.pi) / segments * i for i in range(segments + 1)]:
                    p = QgsPoint(X_srodek +
                                polos_a * math.cos(t) * math.cos(kat) -
                                polos_b * math.sin(t) * math.sin(kat),

                                Y_srodek +
                                polos_a * math.cos(t) * math.sin(kat) +
                                polos_b * math.sin(t) * math.cos(kat))

                    punkty.append(p)

                return punkty

            Elipsa_2 = iteracja()

            feat.setGeometry(QgsGeometry.fromPolyline(Elipsa_2))

            feat.setAttributes([0])

            temp_vlayer.dataProvider().addFeatures([feat])

            temp_vlayer.triggerRepaint()


    # Metoda tworzenia elipsy poprzez zdefiniowanie współrzędnych środka elipsy oraz końców półosi

    def rysuj_elipse_3(self):

        temp_vlayer = QgsVectorLayer("LineString", "Elipsa_3", "memory")
        QgsProject.instance().addMapLayer(temp_vlayer)

        feat = QgsFeature(temp_vlayer.fields())

        temp_vlayer.dataProvider().addAttributes \
            ([QgsField("id", QVariant.Int)])

        temp_vlayer.updateFields()

        X_srodek = self.form.doubleSpinBox_47.value()
        Y_srodek = self.form.doubleSpinBox_46.value()

        polos_a = self.form.doubleSpinBox_48.value()
		
        if polos_a == 0:

            self.iface.messageBar().pushMessage("Brak podanej długości półosi.", "", level=Qgis.Critical, duration=30)
            QgsProject.instance().removeMapLayer(temp_vlayer)

        else:




            kat = self.form.doubleSpinBox_44.value()

            kat = math.radians(kat)

            e = self.form.doubleSpinBox_45.value()

            polos_b = math.sqrt(-polos_a** 2 * e ** 2 + polos_a ** 2)

            def iteracja():

                segments = 144

                punkty = []

                for t in [(2 * math.pi) / segments * i for i in range(segments + 1)]:

                    p = QgsPoint(X_srodek +
                                 polos_a * math.cos(t) * math.cos(kat) -
                                 polos_b * math.sin(t) * math.sin(kat),

                                 Y_srodek +
                                 polos_a * math.cos(t) * math.sin(kat) +
                                 polos_b * math.sin(t) * math.cos(kat))

                    punkty.append(p)

                return punkty

            Elipsa_3 = iteracja()

            feat.setGeometry(QgsGeometry.fromPolyline(Elipsa_3))

            feat.setAttributes([0])

            temp_vlayer.dataProvider().addFeatures([feat])

            temp_vlayer.triggerRepaint()
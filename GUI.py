# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'srk-design1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(955, 560)
        MainWindow.setMinimumSize(QSize(955, 560))
        MainWindow.setMaximumSize(QSize(955, 560))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 941, 481))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.line_20 = QFrame(self.layoutWidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_20)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_14)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.file_button = QPushButton(self.layoutWidget)
        self.file_button.setObjectName(u"file_button")
        self.file_button.setAutoRepeatDelay(300)

        self.horizontalLayout_3.addWidget(self.file_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.file_BIPS_button = QPushButton(self.layoutWidget)
        self.file_BIPS_button.setObjectName(u"file_BIPS_button")

        self.horizontalLayout_4.addWidget(self.file_BIPS_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.export_button = QComboBox(self.layoutWidget)
        self.export_button.addItem("")
        self.export_button.addItem("")
        self.export_button.addItem("")
        self.export_button.setObjectName(u"export_button")

        self.horizontalLayout_5.addWidget(self.export_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_8.addWidget(self.label_15)

        self.roundbox = QSpinBox(self.layoutWidget)
        self.roundbox.setObjectName(u"roundbox")
        self.roundbox.setMinimum(1)
        self.roundbox.setMaximum(10)

        self.horizontalLayout_8.addWidget(self.roundbox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")

        self.verticalLayout_5.addLayout(self.horizontalLayout_39)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.line_17 = QFrame(self.layoutWidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_17)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_5)

        self.temp = QLabel(self.layoutWidget)
        self.temp.setObjectName(u"temp")
        self.temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.temp)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_4)

        self.pressure = QLabel(self.layoutWidget)
        self.pressure.setObjectName(u"pressure")
        self.pressure.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.pressure)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.line_12 = QFrame(self.layoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_5)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_6)

        self.from_temp = QDoubleSpinBox(self.layoutWidget)
        self.from_temp.setObjectName(u"from_temp")
        self.from_temp.setMinimum(230.000000000000000)

        self.horizontalLayout_11.addWidget(self.from_temp)

        self.line_8 = QFrame(self.layoutWidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_8)

        self.from_pres = QDoubleSpinBox(self.layoutWidget)
        self.from_pres.setObjectName(u"from_pres")
        self.from_pres.setMinimum(0.200000000000000)

        self.horizontalLayout_11.addWidget(self.from_pres)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_7)

        self.to_temp = QDoubleSpinBox(self.layoutWidget)
        self.to_temp.setObjectName(u"to_temp")
        self.to_temp.setMinimum(230.000000000000000)
        self.to_temp.setMaximum(400.000000000000000)

        self.horizontalLayout.addWidget(self.to_temp)

        self.line_9 = QFrame(self.layoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_9)

        self.to_pres = QDoubleSpinBox(self.layoutWidget)
        self.to_pres.setObjectName(u"to_pres")
        self.to_pres.setMinimum(0.200000000000000)
        self.to_pres.setMaximum(61.000000000000000)

        self.horizontalLayout.addWidget(self.to_pres)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.step_temp = QLabel(self.layoutWidget)
        self.step_temp.setObjectName(u"step_temp")
        self.step_temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.step_temp)

        self.line_16 = QFrame(self.layoutWidget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_16)

        self.step_pressure = QLabel(self.layoutWidget)
        self.step_pressure.setObjectName(u"step_pressure")
        self.step_pressure.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.step_pressure)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.line_11 = QFrame(self.layoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.dots_temp = QSpinBox(self.layoutWidget)
        self.dots_temp.setObjectName(u"dots_temp")
        self.dots_temp.setMinimum(1)

        self.horizontalLayout_10.addWidget(self.dots_temp)

        self.line_10 = QFrame(self.layoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_10)

        self.dots_pres = QSpinBox(self.layoutWidget)
        self.dots_pres.setObjectName(u"dots_pres")
        self.dots_pres.setMinimum(1)

        self.horizontalLayout_10.addWidget(self.dots_pres)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.line_13 = QFrame(self.layoutWidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_13)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.diag_check_full = QCheckBox(self.layoutWidget)
        self.diag_check_full.setObjectName(u"diag_check_full")
        self.diag_check_full.setLayoutDirection(Qt.LeftToRight)
        self.diag_check_full.setTristate(False)

        self.horizontalLayout_19.addWidget(self.diag_check_full)

        self.diag_check = QCheckBox(self.layoutWidget)
        self.diag_check.setObjectName(u"diag_check")
        self.diag_check.setLayoutDirection(Qt.LeftToRight)
        self.diag_check.setTristate(False)

        self.horizontalLayout_19.addWidget(self.diag_check)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_11)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_14.addWidget(self.line)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.line_19 = QFrame(self.layoutWidget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_19)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.line_22 = QFrame(self.layoutWidget)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_22)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_11)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.line_21 = QFrame(self.layoutWidget)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_21)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.at_temp = QDoubleSpinBox(self.layoutWidget)
        self.at_temp.setObjectName(u"at_temp")
        self.at_temp.setMinimum(230.000000000000000)
        self.at_temp.setMaximum(394.000000000000000)

        self.horizontalLayout_12.addWidget(self.at_temp)

        self.line_23 = QFrame(self.layoutWidget)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.VLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_23)

        self.at_pres = QDoubleSpinBox(self.layoutWidget)
        self.at_pres.setObjectName(u"at_pres")
        self.at_pres.setMinimum(0.200000000000000)
        self.at_pres.setMaximum(61.000000000000000)

        self.horizontalLayout_12.addWidget(self.at_pres)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.textBrowser = QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_10.addWidget(self.textBrowser)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.line_14 = QFrame(self.layoutWidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_14)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.line_18 = QFrame(self.layoutWidget)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.l_check = QCheckBox(self.layoutWidget)
        self.l_check.setObjectName(u"l_check")

        self.horizontalLayout_17.addWidget(self.l_check)

        self.w_check = QCheckBox(self.layoutWidget)
        self.w_check.setObjectName(u"w_check")

        self.horizontalLayout_17.addWidget(self.w_check)


        self.verticalLayout_12.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.l_ent = QCheckBox(self.layoutWidget)
        self.l_ent.setObjectName(u"l_ent")

        self.horizontalLayout_33.addWidget(self.l_ent)

        self.w_ent = QCheckBox(self.layoutWidget)
        self.w_ent.setObjectName(u"w_ent")

        self.horizontalLayout_33.addWidget(self.w_ent)


        self.verticalLayout_12.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.l_dens = QCheckBox(self.layoutWidget)
        self.l_dens.setObjectName(u"l_dens")

        self.horizontalLayout_35.addWidget(self.l_dens)

        self.w_dens = QCheckBox(self.layoutWidget)
        self.w_dens.setObjectName(u"w_dens")

        self.horizontalLayout_35.addWidget(self.w_dens)


        self.verticalLayout_12.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.l_z = QCheckBox(self.layoutWidget)
        self.l_z.setObjectName(u"l_z")

        self.horizontalLayout_36.addWidget(self.l_z)

        self.w_z = QCheckBox(self.layoutWidget)
        self.w_z.setObjectName(u"w_z")

        self.horizontalLayout_36.addWidget(self.w_z)


        self.verticalLayout_12.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.s_stable = QCheckBox(self.layoutWidget)
        self.s_stable.setObjectName(u"s_stable")

        self.horizontalLayout_34.addWidget(self.s_stable)

        self.s_ent = QCheckBox(self.layoutWidget)
        self.s_ent.setObjectName(u"s_ent")

        self.horizontalLayout_34.addWidget(self.s_ent)


        self.verticalLayout_12.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.s_density = QCheckBox(self.layoutWidget)
        self.s_density.setObjectName(u"s_density")

        self.horizontalLayout_18.addWidget(self.s_density)

        self.s_z = QCheckBox(self.layoutWidget)
        self.s_z.setObjectName(u"s_z")

        self.horizontalLayout_18.addWidget(self.s_z)


        self.verticalLayout_12.addLayout(self.horizontalLayout_18)


        self.verticalLayout_9.addLayout(self.verticalLayout_12)

        self.line_15 = QFrame(self.layoutWidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_15)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.calcul_type = QComboBox(self.layoutWidget)
        self.calcul_type.addItem("")
        self.calcul_type.addItem("")
        self.calcul_type.setObjectName(u"calcul_type")

        self.verticalLayout_8.addWidget(self.calcul_type)

        self.calculate_button = QPushButton(self.layoutWidget)
        self.calculate_button.setObjectName(u"calculate_button")

        self.verticalLayout_8.addWidget(self.calculate_button)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)


        self.horizontalLayout_14.addLayout(self.verticalLayout_10)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 955, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PVT-PR - \u041c\u043e\u0434\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0437\u043e\u0432\u043e\u0433\u043e \u0440\u0430\u0432\u043d\u043e\u0432\u0435\u0441\u0438\u044f \u0443\u0433\u043b\u0435\u0432\u043e\u0434\u043e\u0440\u043e\u0434\u043d\u044b\u0445 \u0441\u043c\u0435\u0441\u0435\u0439 \u043d\u0430 \u043e\u0441\u043d\u043e\u0432\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u041f\u0435\u043d\u0433\u0430-\u0420\u043e\u0431\u0438\u043d\u0441\u043e\u043d\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0446\u0438\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0430\u0432\u0435-\u0420\u0435\u0434\u043b\u0438\u0445\u0430-\u041a\u0432\u043e\u043d\u0433\u0430 (SRK)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.file_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BIPS", None))
        self.file_BIPS_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.export_button.setItemText(0, QCoreApplication.translate("MainWindow", u"Excel", None))
        self.export_button.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u044d\u043a\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.export_button.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0411\u043b\u043e\u043a\u043d\u043e\u0442", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0433\u043b\u0438\u0442\u044c \u0434\u043e...", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Phase Envelope", None))
        self.label_13.setText("")
        self.temp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 [\u041a]", None))
        self.pressure.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435 [\u041c\u041f\u0430]", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.step_temp.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0447\u0435\u043a (\u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430)", None))
        self.step_pressure.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0447\u0435\u043a (\u0434\u0430\u0432\u043b\u0435\u043d\u0438\u0435)", None))
        self.diag_check_full.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u0430\u044f \u0444\u0430\u0437\u043e\u0432\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.diag_check.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u0438\u0447\u043d\u0430\u044f \u0444\u0430\u0437\u043e\u0432\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430 (\u043f\u043e \u0442\u043e\u0447\u043a\u0430\u043c)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"PTFlash", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 [\u041a]", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0432\u043b\u0435\u043d\u0438\u0435 [\u041c\u041f\u0430]", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.l_check.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u044f \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.w_check.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u044f \u043f\u0430\u0440\u0430", None))
        self.l_ent.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0430\u043b\u044c\u043f\u0438\u044f \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.w_ent.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0430\u043b\u044c\u043f\u0438\u044f \u043f\u0430\u0440\u0430", None))
        self.l_dens.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.w_dens.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0430\u0440\u0430", None))
        self.l_z.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u0445\u0441\u0436\u0438\u043c\u0430\u0435\u043c\u043e\u0441\u0442\u044c \u0436\u0438\u0434\u043a\u043e\u0441\u0442\u0438", None))
        self.w_z.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u0445\u0441\u0436\u0438\u043c\u0430\u0435\u043c\u043e\u0441\u0442\u044c \u043f\u0430\u0440\u0430", None))
        self.s_stable.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.s_ent.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043d\u0442\u0430\u043b\u044c\u043f\u0438\u044f \u0441\u043c\u0435\u0441\u0438", None))
        self.s_density.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0441\u0438", None))
        self.s_z.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u0445\u0441\u0436\u0438\u043c\u0430\u0435\u043c\u043e\u0441\u0442\u044c \u0441\u043c\u0435\u0441\u0438", None))
        self.calcul_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Phase Envelope", None))
        self.calcul_type.setItemText(1, QCoreApplication.translate("MainWindow", u"PTFlash", None))

        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
    # retranslateUi


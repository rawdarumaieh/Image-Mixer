# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1235, 440)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.image2GV = PlotWidget(self.centralwidget)
        self.image2GV.setObjectName("image2GV")
        self.gridLayout_3.addWidget(self.image2GV, 3, 0, 1, 1)
        self.image1GV = PlotWidget(self.centralwidget)
        self.image1GV.setObjectName("image1GV")
        self.gridLayout_3.addWidget(self.image1GV, 1, 0, 1, 1)
        self.components2 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.components2.setFont(font)
        self.components2.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.components2.setObjectName("components2")
        self.gridLayout_3.addWidget(self.components2, 2, 1, 1, 1)
        self.image1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.image1.setFont(font)
        self.image1.setObjectName("image1")
        self.gridLayout_3.addWidget(self.image1, 0, 0, 1, 1)
        self.components1 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.components1.setFont(font)
        self.components1.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.components1.setObjectName("components1")
        self.gridLayout_3.addWidget(self.components1, 0, 1, 1, 1)
        self.image2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.image2.setFont(font)
        self.image2.setObjectName("image2")
        self.gridLayout_3.addWidget(self.image2, 2, 0, 1, 1)
        self.image2EditedGV = PlotWidget(self.centralwidget)
        self.image2EditedGV.setObjectName("image2EditedGV")
        self.gridLayout_3.addWidget(self.image2EditedGV, 3, 1, 1, 1)
        self.Imag1EditedGV = PlotWidget(self.centralwidget)
        self.Imag1EditedGV.setObjectName("Imag1EditedGV")
        self.gridLayout_3.addWidget(self.Imag1EditedGV, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 4, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.ComImg1 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ComImg1.setFont(font)
        self.ComImg1.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.ComImg1.setObjectName("ComImg1")
        self.gridLayout.addWidget(self.ComImg1, 1, 1, 1, 1)
        self.slider1 = QtWidgets.QSlider(self.centralwidget)
        self.slider1.setMaximum(100)
        self.slider1.setSingleStep(10)
        self.slider1.setProperty("value", 50)
        self.slider1.setOrientation(QtCore.Qt.Horizontal)
        self.slider1.setObjectName("slider1")
        self.gridLayout.addWidget(self.slider1, 1, 2, 1, 1)
        self.combo3 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.combo3.setFont(font)
        self.combo3.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.combo3.setObjectName("combo3")
        self.gridLayout.addWidget(self.combo3, 2, 0, 1, 4)
        self.component2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(9)
        self.component2Label.setFont(font)
        self.component2Label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.component2Label.setObjectName("component2Label")
        self.gridLayout.addWidget(self.component2Label, 3, 0, 1, 1)
        self.ComImg2 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.ComImg2.setFont(font)
        self.ComImg2.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.ComImg2.setObjectName("ComImg2")
        self.gridLayout.addWidget(self.ComImg2, 3, 1, 1, 1)
        self.slider2 = QtWidgets.QSlider(self.centralwidget)
        self.slider2.setMaximum(100)
        self.slider2.setSingleStep(10)
        self.slider2.setProperty("value", 50)
        self.slider2.setOrientation(QtCore.Qt.Horizontal)
        self.slider2.setObjectName("slider2")
        self.gridLayout.addWidget(self.slider2, 3, 2, 1, 1)
        self.combo4 = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.combo4.setFont(font)
        self.combo4.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.combo4.setObjectName("combo4")
        self.gridLayout.addWidget(self.combo4, 4, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(14)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.S1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S1Label.setFont(font)
        self.S1Label.setObjectName("S1Label")
        self.gridLayout.addWidget(self.S1Label, 1, 3, 1, 1)
        self.S2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Orbitron")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S2Label.setFont(font)
        self.S2Label.setObjectName("S2Label")
        self.gridLayout.addWidget(self.S2Label, 3, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Output2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Output2Label.setFont(font)
        self.Output2Label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Output2Label.setObjectName("Output2Label")
        self.gridLayout_2.addWidget(self.Output2Label, 1, 2, 1, 1)
        self.outpu1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.outpu1Label.setFont(font)
        self.outpu1Label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.outpu1Label.setObjectName("outpu1Label")
        self.gridLayout_2.addWidget(self.outpu1Label, 1, 0, 1, 1)
        self.Output1 = PlotWidget(self.centralwidget)
        self.Output1.setObjectName("Output1")
        self.gridLayout_2.addWidget(self.Output1, 2, 0, 1, 1)
        self.Output2 = PlotWidget(self.centralwidget)
        self.Output2.setObjectName("Output2")
        self.gridLayout_2.addWidget(self.Output2, 2, 2, 1, 1)
        self.OutputsComponents = QtWidgets.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Poor Richard")
        font.setPointSize(10)
        self.OutputsComponents.setFont(font)
        self.OutputsComponents.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.OutputsComponents.setObjectName("OutputsComponents")
        self.gridLayout_2.addWidget(self.OutputsComponents, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1235, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFTReal1 = QtWidgets.QAction(MainWindow)
        self.actionFTReal1.setObjectName("actionFTReal1")
        self.actionFTReal2 = QtWidgets.QAction(MainWindow)
        self.actionFTReal2.setObjectName("actionFTReal2")
        self.actionFTImag1 = QtWidgets.QAction(MainWindow)
        self.actionFTImag1.setObjectName("actionFTImag1")
        self.actionFTImag2 = QtWidgets.QAction(MainWindow)
        self.actionFTImag2.setObjectName("actionFTImag2")
        self.actionFTMag1 = QtWidgets.QAction(MainWindow)
        self.actionFTMag1.setObjectName("actionFTMag1")
        self.actionFTMag2 = QtWidgets.QAction(MainWindow)
        self.actionFTMag2.setObjectName("actionFTMag2")
        self.actionFTPhase1 = QtWidgets.QAction(MainWindow)
        self.actionFTPhase1.setObjectName("actionFTPhase1")
        self.actionFTPhase2 = QtWidgets.QAction(MainWindow)
        self.actionFTPhase2.setObjectName("actionFTPhase2")
        self.actionimage1C1 = QtWidgets.QAction(MainWindow)
        self.actionimage1C1.setObjectName("actionimage1C1")
        self.actionimageC2 = QtWidgets.QAction(MainWindow)
        self.actionimageC2.setObjectName("actionimageC2")
        self.actionimage2C1 = QtWidgets.QAction(MainWindow)
        self.actionimage2C1.setObjectName("actionimage2C1")
        self.actionimage2C2 = QtWidgets.QAction(MainWindow)
        self.actionimage2C2.setObjectName("actionimage2C2")
        self.actionimage1C2 = QtWidgets.QAction(MainWindow)
        self.actionimage1C2.setObjectName("actionimage1C2")
        self.actionoutput1 = QtWidgets.QAction(MainWindow)
        self.actionoutput1.setObjectName("actionoutput1")
        self.actionoutput2 = QtWidgets.QAction(MainWindow)
        self.actionoutput2.setObjectName("actionoutput2")
        self.actionc1Mag = QtWidgets.QAction(MainWindow)
        self.actionc1Mag.setObjectName("actionc1Mag")
        self.actionc1Phase = QtWidgets.QAction(MainWindow)
        self.actionc1Phase.setObjectName("actionc1Phase")
        self.actionc1Real = QtWidgets.QAction(MainWindow)
        self.actionc1Real.setObjectName("actionc1Real")
        self.actionc1UnitMag = QtWidgets.QAction(MainWindow)
        self.actionc1UnitMag.setObjectName("actionc1UnitMag")
        self.actionc1UnitPhase = QtWidgets.QAction(MainWindow)
        self.actionc1UnitPhase.setObjectName("actionc1UnitPhase")
        self.actionc2Mag = QtWidgets.QAction(MainWindow)
        self.actionc2Mag.setObjectName("actionc2Mag")
        self.actionc2Phase = QtWidgets.QAction(MainWindow)
        self.actionc2Phase.setObjectName("actionc2Phase")
        self.actionc2Real = QtWidgets.QAction(MainWindow)
        self.actionc2Real.setObjectName("actionc2Real")
        self.actionc2Imag = QtWidgets.QAction(MainWindow)
        self.actionc2Imag.setObjectName("actionc2Imag")
        self.actionc2UnitMag = QtWidgets.QAction(MainWindow)
        self.actionc2UnitMag.setObjectName("actionc2UnitMag")
        self.actionc2UnitPhase = QtWidgets.QAction(MainWindow)
        self.actionc2UnitPhase.setObjectName("actionc2UnitPhase")
        self.actionc1Imag = QtWidgets.QAction(MainWindow)
        self.actionc1Imag.setObjectName("actionc1Imag")

        self.retranslateUi(MainWindow)
        self.slider1.valueChanged['int'].connect(self.S1Label.setNum)
        self.slider2.valueChanged['int'].connect(self.S2Label.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.components2.setText(_translate("MainWindow", "components of image2"))
        self.image1.setText(_translate("MainWindow", "image1"))
        self.components1.setText(_translate("MainWindow", "components of image1"))
        self.image2.setText(_translate("MainWindow", "image2"))
        self.label_2.setText(_translate("MainWindow", "Component1"))
        self.ComImg1.setText(_translate("MainWindow", "Img1,Img2"))
        self.combo3.setText(_translate("MainWindow", "Imaginary,Real,Phase,Magnitude,Unit-Magnitude,Unit-Phase"))
        self.component2Label.setText(_translate("MainWindow", "Component2"))
        self.ComImg2.setText(_translate("MainWindow", "Img1,Img2"))
        self.combo4.setText(_translate("MainWindow", "Imaginary,Real,Phase,Magnitude,Unit-Magnitude,Unit-Phase"))
        self.label.setText(_translate("MainWindow", "Mixer Output to:"))
        self.S1Label.setText(_translate("MainWindow", "50"))
        self.S2Label.setText(_translate("MainWindow", "50"))
        self.Output2Label.setText(_translate("MainWindow", "OutPut2"))
        self.outpu1Label.setText(_translate("MainWindow", "OutPut1"))
        self.OutputsComponents.setText(_translate("MainWindow", "Outputs"))
        self.actionFTReal1.setText(_translate("MainWindow", "FTReal1"))
        self.actionFTReal2.setText(_translate("MainWindow", "FTReal2"))
        self.actionFTImag1.setText(_translate("MainWindow", "FTImag1"))
        self.actionFTImag2.setText(_translate("MainWindow", "FTImag2"))
        self.actionFTMag1.setText(_translate("MainWindow", "FTMag1"))
        self.actionFTMag2.setText(_translate("MainWindow", "FTMag2"))
        self.actionFTPhase1.setText(_translate("MainWindow", "FTPhase1"))
        self.actionFTPhase2.setText(_translate("MainWindow", "FTPhase2"))
        self.actionimage1C1.setText(_translate("MainWindow", "image1C1"))
        self.actionimageC2.setText(_translate("MainWindow", "image1C2"))
        self.actionimage2C1.setText(_translate("MainWindow", "image2C1"))
        self.actionimage2C2.setText(_translate("MainWindow", "image2C2"))
        self.actionimage1C2.setText(_translate("MainWindow", "image1C2"))
        self.actionoutput1.setText(_translate("MainWindow", "output1"))
        self.actionoutput2.setText(_translate("MainWindow", "output2"))
        self.actionc1Mag.setText(_translate("MainWindow", "c1Mag"))
        self.actionc1Phase.setText(_translate("MainWindow", "c1Phase"))
        self.actionc1Real.setText(_translate("MainWindow", "c1Real"))
        self.actionc1UnitMag.setText(_translate("MainWindow", "c1UnitMag"))
        self.actionc1UnitPhase.setText(_translate("MainWindow", "c1UnitPhase"))
        self.actionc2Mag.setText(_translate("MainWindow", "c2Mag"))
        self.actionc2Phase.setText(_translate("MainWindow", "c2Phase"))
        self.actionc2Real.setText(_translate("MainWindow", "c2Real"))
        self.actionc2Imag.setText(_translate("MainWindow", "c2Imag"))
        self.actionc2UnitMag.setText(_translate("MainWindow", "c2UnitMag"))
        self.actionc2UnitPhase.setText(_translate("MainWindow", "c2UnitPhase"))
        self.actionc1Imag.setText(_translate("MainWindow", "c1Imag"))

from pyqtgraph import PlotWidget
from PyQt5.Qt import *
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import *
import os, sys
import numpy as np
from task3 import Ui_MainWindow
import pyqtgraph as pg
from PIL import Image
import cv2
from numpy import asarray
from imageModel import ImageModel
from matplotlib import pyplot as plt
from matplotlib import image as im
from modesEnum import Modes
import logging

logging.basicConfig(filename='LogFile.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Photoshop without using photoshop is now in action ')


class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(600, 300, 400, 200)
        self.setWindowTitle('whatever')
        pg.setConfigOption('background', 'w')
        # hiding axis
        self.ui.image1GV.getPlotItem().hideAxis('bottom')
        self.ui.image1GV .getPlotItem().hideAxis('left')
        self.ui.image2EditedGV.getPlotItem().hideAxis('bottom')
        self.ui.image2EditedGV .getPlotItem().hideAxis('left')
        self.ui.image2GV.getPlotItem().hideAxis('bottom')
        self.ui.image2GV .getPlotItem().hideAxis('left')
        self.ui.Imag1EditedGV.getPlotItem().hideAxis('bottom')
        self.ui.Imag1EditedGV.getPlotItem().hideAxis('left')
        self.ui.Output1.getPlotItem().hideAxis('bottom')
        self.ui.Output1.getPlotItem().hideAxis('left')
        self.ui.Output2.getPlotItem().hideAxis('bottom')
        self.ui.Output2.getPlotItem().hideAxis('left')
        # rest of functions
        self.ui.image1.clicked.connect(self.UploadImage)
        self.ui.image2.clicked.connect(self.UploadImage)
        # adding the actions
        # phase
        self.ui.components1.addAction(self.ui.actionFTPhase1)
        self.ui.components2.addAction(self.ui.actionFTPhase2)
        # magnitude
        self.ui.components1.addAction(self.ui.actionFTMag1)
        self.ui.components2.addAction(self.ui.actionFTMag2)
        # imaginary
        self.ui.components1.addAction(self.ui.actionFTImag1)
        self.ui.components2.addAction(self.ui.actionFTImag2)
        # real
        self.ui.components1.addAction(self.ui.actionFTReal1)
        self.ui.components2.addAction(self.ui.actionFTReal2)
        #Images
        self.ui.ComImg1.addAction(self.ui.actionimage1C1)
        self.ui.ComImg1.addAction(self.ui.actionimage2C1)

        self.ui.ComImg2.addAction(self.ui.actionimage2C2)
        self.ui.ComImg2.addAction(self.ui.actionimage1C2)
        #outputs
        self.ui.OutputsComponents.addAction(self.ui.actionoutput1)
        self.ui.OutputsComponents.addAction(self.ui.actionoutput2)
        #OutputComponents
        self.ui.combo3.addAction(self.ui.actionc1Imag)
        self.ui.combo3.addAction(self.ui.actionc1Real)
        self.ui.combo3.addAction(self.ui.actionc1Phase)
        self.ui.combo3.addAction(self.ui.actionc1Mag)
        self.ui.combo3.addAction(self.ui.actionc1UnitMag)
        self.ui.combo3.addAction(self.ui.actionc1UnitPhase)
        self.ui.combo4.addAction(self.ui.actionc2Imag)
        self.ui.combo4.addAction(self.ui.actionc2Real)
        self.ui.combo4.addAction(self.ui.actionc2Phase)
        self.ui.combo4.addAction(self.ui.actionc2Mag)
        self.ui.combo4.addAction(self.ui.actionc2UnitMag)
        self.ui.combo4.addAction(self.ui.actionc2UnitPhase)
        self.ui.OutputsComponents.addAction(self.ui.actionoutput1)
        self.ui.OutputsComponents.addAction(self.ui.actionoutput2)


        #connecting the actions with the functions
        # phase
        self.ui.actionFTPhase1.triggered.connect(self.FOURIERPhase)
        self.ui.actionFTPhase2.triggered.connect(self.FOURIERPhase)
        # magnitude
        self.ui.actionFTMag1.triggered.connect(self.FOURIERTMag)
        self.ui.actionFTMag2.triggered.connect(self.FOURIERTMag)
        #real
        self.ui.actionFTReal1.triggered.connect(self.FOURIERReal)
        self.ui.actionFTReal2.triggered.connect(self.FOURIERReal)
        #imaginary
        self.ui.actionFTImag1.triggered.connect(self.FOURIERImaginary)
        self.ui.actionFTImag2.triggered.connect(self.FOURIERImaginary)
        #outputPlotting
        # self.ui.actionoutput1.triggered.connect(self.PlotOutput)
        # self.ui.actionoutput2.triggered.connect(self.PlotOutput)
        #mixing function
        self.ui.actionimage1C1.triggered.connect(self.GetWhichImageIncomponent1)
        self.ui.actionimage1C2.triggered.connect(self.GetWhichImageIncomponent2)
        self.ui.actionimage2C1.triggered.connect(self.GetWhichImageIncomponent1)
        self.ui.actionimage2C2.triggered.connect(self.GetWhichImageIncomponent2)
        self.ui.actionoutput1.triggered.connect(self.MixingFunction)
        self.ui.actionoutput2.triggered.connect(self.MixingFunction)

        self.ui.actionc2Imag.triggered.connect(self.GetWhichFourierIncomponent2)
        self.ui.actionc2Real.triggered.connect(self.GetWhichFourierIncomponent2)
        self.ui.actionc2Phase.triggered.connect(self.GetWhichFourierIncomponent2)
        self.ui.actionc2Mag.triggered.connect(self.GetWhichFourierIncomponent2)
        self.ui.actionc2UnitMag.triggered.connect(self.GetWhichFourierIncomponent2)
        self.ui.actionc2UnitPhase.triggered.connect(self.GetWhichFourierIncomponent2)
        # .........................................................#
        self.ui.actionc1Imag.triggered.connect(self.GetWhichFourierIncomponent1)
        self.ui.actionc1Real.triggered.connect(self.GetWhichFourierIncomponent1)
        self.ui.actionc1Phase.triggered.connect(self.GetWhichFourierIncomponent1)
        self.ui.actionc1Mag.triggered.connect(self.GetWhichFourierIncomponent1)
        self.ui.actionc1UnitMag.triggered.connect(self.GetWhichFourierIncomponent1)
        self.ui.actionc1UnitPhase.triggered.connect(self.GetWhichFourierIncomponent1)




    def UploadImage(self):
        self.senderOBJ = self.sender()
        print(self.senderOBJ.text())
        filePaths = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File',"~/Desktop/DSPTASK3",'*.jpg')   
        for filePath in filePaths:
            for self.f in filePath:
                if self.f == '*':
                     break
                if (self.senderOBJ.text()=='image1'):               
                    self.Imagemodel1=ImageModel(self.f)
                    self.image1=self.Imagemodel1.OpenImage()
                    # gettin the size
                    self.a=Image.open(self.f)
                    self.width,self.hight=self.a.size

                        
                        #  message=QtWidgets.QMessageBox()
                        #  message.setIcon(QtWidgets.QMessageBox.Critical)
                        #  message.setText("Error! Second Image is not the same size as the first one")
                        #  message.setInformativeText("More Info")
                        #  message.setWindowTitle(" Error message")
                        #  message.exec_()
                    # ..................#
                    self.ui.image1GV.clear()
                    self.ui.image1GV.addItem(self.image1)
                    self.image1.rotate(270)
                    logging.info('User chooses Image 1 and showed successfully')

                if(self.senderOBJ.text()=='image2'):                    
                    self.Imagemodel2=ImageModel(self.f)
                    self.image2=self.Imagemodel2.OpenImage()
                    #size of second image #
                    self.b=Image.open(self.f)
                    width,hight=self.b.size
                    if(self.b.size==self.a.size):
                        self.ui.image2GV.clear()
                        self.ui.image2GV.addItem(self.image2)
                        self.image2.rotate(270)
                        logging.info('User chooses Image  and showed successfully')
                        logging.info('they are of the same size')
                    else:
                         message=QtWidgets.QMessageBox()
                         logging.info('they are not of the same size')
                         message.setIcon(QtWidgets.QMessageBox.Critical)
                         message.setText("Error! Second Image is not the same size as the first one")
                         message.setInformativeText("Dont Panic :) pick 2 images of the same size and try again later")
                         message.setWindowTitle(" Error message")
                         message.exec_()





            
                    

    def FOURIERTMag(self):
        senderOBJ1 = self.sender()
        if (senderOBJ1.text()=='FTMag1'):
            self.ui.Imag1EditedGV.clear()
            self.FourierMagImage1=self.Imagemodel1.FTMag()  
            self.magnitude_spectrum1=20*np.log(self.FourierMagImage1)
            print(self.magnitude_spectrum1,'1')
            img = pg.ImageItem(asarray(self.magnitude_spectrum1))
            print(img,'2')
            logging.info('User chooses magnitude of first image')

            self.ui.Imag1EditedGV.addItem(img)
            img.rotate(270)
        if (senderOBJ1.text()=='FTMag2'):
            self.ui.image2EditedGV.clear()
            self.FourierMagImage2=self.Imagemodel2.FTMag()
            self.magnitude_spectrum2=20*np.log(self.FourierMagImage2)
            img1 = pg.ImageItem(asarray(self.magnitude_spectrum2))
            logging.info('User chooses magnitude of second image')

            self.ui.image2EditedGV.addItem(img1)
            img1.rotate(270)


    def FOURIERPhase(self):
        senderOBJ2 = self.sender()
        if(senderOBJ2.text()=='FTPhase1'):
            self.ui.Imag1EditedGV.clear()
            self.FourierPhaseImage1=self.Imagemodel1.FTPhase()
            PhaseImage1Array = pg.ImageItem(asarray(self.FourierPhaseImage1))
            logging.info('User chooses phase of first image')
            self.ui.Imag1EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)
        if(senderOBJ2.text()=='FTPhase2'):
            self.ui.image2EditedGV.clear()
            self.FourierPhaseImage2=self.Imagemodel2.FTPhase()
            PhaseImage1Array = pg.ImageItem(asarray( self.FourierPhaseImage2))
            logging.info('User chooses phase of second image')
            self.ui.image2EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)

    def FOURIERReal(self):
        senderOBJ3=self.sender()
        if(senderOBJ3.text()=='FTReal1'):
            self.ui.Imag1EditedGV.clear()
            self.FourierRealImage1=self.Imagemodel1.FTReal()
            PhaseImage1Array = pg.ImageItem(asarray(self.FourierRealImage1))
            logging.info('User chooses real of first image')
            self.ui.Imag1EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)
        if(senderOBJ3.text()=='FTReal2'):
            self.ui.image2EditedGV.clear()
            self.FourierRealImage2=self.Imagemodel2.FTReal()
            PhaseImage1Array = pg.ImageItem(asarray(self.FourierRealImage2))
            logging.info('User chooses real of second image')
            self.ui.image2EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)

    def FOURIERImaginary(self):
        senderOBJ4=self.sender()
        if(senderOBJ4.text()=='FTImag1'):
            self.ui.Imag1EditedGV.clear()
            self.FourierImaginaryImage1=self.Imagemodel1.FTImag()
            PhaseImage1Array = pg.ImageItem(asarray(self.FourierImaginaryImage1))
            logging.info('User chooses fourier of first image')
            self.ui.Imag1EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)
        if(senderOBJ4.text()=='FTImag2'):
            self.ui.image2EditedGV.clear()
            self.FourierImaginaryImage2=self.Imagemodel2.FTImag()
            logging.info('User chooses fourier of second image')
            PhaseImage1Array = pg.ImageItem(asarray(self.FourierImaginaryImage2))
            self.ui.image2EditedGV.addItem(PhaseImage1Array)
            PhaseImage1Array.rotate(270)

    def GetWhichImageIncomponent1(self):
        senderObject1=self.sender()
        senderObject1=str(senderObject1.objectName())
        if(senderObject1=='actionimage1C1'):
            logging.info('User chooses image1 in the first component')
            self.whichImage1=self.Imagemodel1
        if(senderObject1=='actionimage2C1'):
            logging.info('User chooses image2 in the first component')
            self.whichImage1=self.Imagemodel2
        return self.whichImage1
    def GetWhichImageIncomponent2(self):
        senderObject=self.sender()
        senderObject=str(senderObject.objectName())
        if(senderObject=='actionimage1C2'):
            logging.info('User chooses image1 in the second component')
            self.whichImage2=self.Imagemodel1
        if(senderObject=='actionimage2C2'):
            logging.info('User chooses image2 in the second component')
            self.whichImage2=self.Imagemodel2
        return self.whichImage2
    def GetWhichFourierIncomponent1(self):
        self.senderObject_C1_fourier=self.sender()
        self.senderObject_C1_fourier=str(self.senderObject_C1_fourier.objectName())

    def GetWhichFourierIncomponent2(self):
        self.senderObject_C2_fourier=self.sender()
        self.senderObject_C2_fourier=str(self.senderObject_C2_fourier.objectName())


    def MixingFunction(self):
        self.whichoutput=self.sender()
        self.whichimage=self.sender()
        Imagemodel3=ImageModel()
        self.Slider1Value=int(self.ui.S1Label.text())/100
        self.Slider2Value=int(self.ui.S2Label.text())/100
        print(self.Slider2Value)
        self.IMG1=self.GetWhichImageIncomponent1()
        self.IMG2=self.GetWhichImageIncomponent2()
        #...................defining some variables...................#
        self.UM_IMG1_IMGModel1=self.Imagemodel1
        self.UM_IMG1_IMGModel1.magnitude=np.ones((self.width,self.hight))
        self.UM_IMG2_IMGModel1=self.UM_IMG1_IMGModel1
        #..............................................................#
        self.UM_IMG1_IMGModel2=self.Imagemodel2
        self.UM_IMG1_IMGModel2.magnitude=np.ones((self.width,self.hight))
        self.UM_IMG2_IMGModel2=self.UM_IMG1_IMGModel2
        #..............................................................#
        self.UP_IMG1_IMGModel1=self.Imagemodel1
        self.UP_IMG1_IMGModel1.phase=np.zeros((self.width,self.hight))
        self.UP_IMG2_IMGModel1=self.UP_IMG1_IMGModel1

        #..............................................................#
        self.UP_IMG1_IMGModel2=self.Imagemodel1
        self.UP_IMG1_IMGModel2.phase=np.zeros((self.width,self.hight))
        self.UP_IMG2_IMGModel2=self.UP_IMG1_IMGModel2
        #.............end of defining the variables.....................#

        if(self.senderObject_C1_fourier=='actionc1Mag'or self.senderObject_C1_fourier=='actionc1Real'or self.senderObject_C1_fourier=='actionc1UnitMag'):
                self.Ratio1=self.Slider1Value
        if (self.senderObject_C1_fourier=='actionc1Phase'or self.senderObject_C1_fourier=='actionc1Imag'or self.senderObject_C1_fourier=='actionc1UnitPhase'):
                self.Ratio2=self.Slider1Value
        if (self.senderObject_C2_fourier=='actionc2Mag'or self.senderObject_C2_fourier=='actionc2Real'or self.senderObject_C2_fourier=='actionc2UnitMag'):
                self.Ratio1=self.Slider2Value
        if (self.senderObject_C2_fourier=='actionc2Phase'or self.senderObject_C2_fourier=='actionc2Imag'or self.senderObject_C2_fourier=='actionc2UnitPhase'):
                self.Ratio2=self.Slider2Value
                
        if(self.senderObject_C1_fourier=='actionc1Mag'and self.senderObject_C2_fourier=='actionc2Phase'):
            logging.info('User chooses mixing magnitude of first component with phase of second component')
            self.InverseFourier=self.IMG1.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
        if(self.senderObject_C2_fourier=='actionc2Mag'and self.senderObject_C1_fourier=='actionc1Phase'):
            logging.info('User chooses mixing magnitude of first second with phase of second first')
            self.InverseFourier=self.IMG2.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)


        if(self.senderObject_C1_fourier=='actionc1Imag'and self.senderObject_C2_fourier=='actionc2Real'):
            logging.info('User chooses mixing imaginary of first component with real of second component')
            self.InverseFourier=self.IMG2.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.realAndImaginary)
        if( self.senderObject_C2_fourier=='actionc2Imag'and self.senderObject_C1_fourier=='actionc1Real'):
            logging.info('User chooses mixing imaginary of second component with real of first component')
            self.InverseFourier=self.IMG1.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.realAndImaginary)
        #unit magnitude :)
        if(self.senderObject_C1_fourier=='actionc1UnitMag'and self.senderObject_C2_fourier=='actionc2Phase'):
            if(self.IMG1==self.Imagemodel1):
                logging.info('User chooses mixing uniform magnitude of first component which is image1 component with phase of second component')
                self.InverseFourier =  self.UM_IMG1_IMGModel1.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
            elif(self.IMG1==self.Imagemodel2):
                logging.info('User chooses mixing uniform magnitude of first component which is image2 component with phase of second component')
                self.InverseFourier =  self.UM_IMG1_IMGModel2.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
        elif(self.senderObject_C1_fourier=='actionc1Phase'and self.senderObject_C2_fourier=='actionc1UnitMag'):
            if(self.IMG2==self.Imagemodel1):
                self.UM_IMG2_IMGModel1=self.Imagemodel1
                self.UM_IMG2_IMGModel1.magnitude=np.ones((self.width,self.hight))
                logging.info('User chooses mixing uniform magnitude of second component which is image1 component with phase of first component')
                self.InverseFourier = self.UM_IMG2_IMGModel1.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
            elif(self.IMG2==self.Imagemodel2):
                self.UM_IMG2_IMGModel2=self.Imagemodel2
                self.UM_IMG2_IMGModel2.magnitude=np.ones((self.width,self.hight))
                logging.info('User chooses mixing uniform magnitude of second component which is image2 component with phase of first component')
                self.InverseFourier = self.UM_IMG2_IMGModel2.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)        
        #unit phase :) 
        if(self.senderObject_C1_fourier=='actionc1UnitPhase'and self.senderObject_C2_fourier=='actionc2Mag'):
            if(self.IMG1==self.Imagemodel1):
                logging.info('User chooses mixing uniform phase of first component which is image1  with magnitude of second component')
                self.InverseFourier =  self.UP_IMG1_IMGModel1.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
            if(self.IMG1==self.Imagemodel2):
                logging.info('User chooses mixing uniform phase of first component which is image2  with magnitude ofsecond component')
                self.InverseFourier = self.UP_IMG1_IMGModel2.mix(self.IMG2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
        elif(self.senderObject_C1_fourier=='actionc1Mag'and self.senderObject_C2_fourier=='actionc2UnitPhase'):
                if(self.IMG2==self.Imagemodel1):
                    self.UP_IMG2_IMGModel1=self.Imagemodel2
                    self.UP_IMG2_IMGModel1.phase=np.zeros((self.width,self.hight))
                    logging.info('User chooses mixing uniform phase of second component which is image1  with  magnitude of first  component')
                    self.InverseFourier = self.UP_IMG2_IMGModel1.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
                if(self.IMG2==self.Imagemodel2):
                    self.UP_IMG2_IMGModel2=self.Imagemodel2
                    Imagemodel3.phase=np.zeros((self.width,self.hight))
                    logging.info('User chooses mixing uniform phase of second component which is image2  with  magnitude of first  component')
                    self.InverseFourier = Imagemodel3.mix(self.IMG1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
        #unit mag and unit phase

        if(self.senderObject_C1_fourier=='actionc1UnitPhase'and self.senderObject_C2_fourier=='actionc2UnitMag'):
            if(self.IMG1==self.Imagemodel1 and self.IMG2==self.Imagemodel1):
                logging.info('User chooses mixing uniform phase of first component which is image1  with unit magnitude of second component which is image1')
                self.InverseFourier =  self.UP_IMG1_IMGModel1.mix(self.UM_IMG2_IMGModel1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)

            if(self.IMG1==self.Imagemodel1 and self.IMG2==self.Imagemodel2):
                logging.info('User chooses mixing uniform phase of first component which is image1  with unit magnitude of second component which is image2')
                self.InverseFourier =  self.UP_IMG1_IMGModel1.mix(self.UM_IMG2_IMGModel2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)

            if(self.IMG1==self.Imagemodel2 and self.IMG2==self.Imagemodel1):
                logging.info('User chooses mixing uniform phase of first component which is image2  with unit magnitude ofsecond component which is image 1')
                self.InverseFourier = self.UP_IMG1_IMGModel2.mix(self.UM_IMG2_IMGModel1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)

            if(self.IMG1==self.Imagemodel2 and self.IMG2==self.Imagemodel2):
                logging.info('User chooses mixing uniform phase of first component which is image2  with unit magnitude ofsecond component which is image 2')
                self.InverseFourier = self.UP_IMG1_IMGModel2.mix(self.UM_IMG2_IMGModel2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)


        elif(self.senderObject_C1_fourier=='actionc1UnitMag'and self.senderObject_C2_fourier=='actionc2UnitPhase'):
                if(self.IMG2==self.Imagemodel1 and self.IMG1==self.Imagemodel1):
                    logging.info('User chooses mixing uniform phase of second component which is image1  with  unit magnitude of first  component which is image 1')
                    self.InverseFourier = self.UM_IMG1_IMGModel1.mix(self.UP_IMG2_IMGModel1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
                if(self.IMG2==self.Imagemodel1 and self.IMG1==self.Imagemodel2):
                    logging.info('User chooses mixing uniform phase of second component which is image1  with  unit magnitude of first  component which is image 1')
                    self.InverseFourier = self.UM_IMG1_IMGModel2.mix(self.UP_IMG2_IMGModel1,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)

                if(self.IMG2==self.Imagemodel2 and self.IMG1==self.Imagemodel1):
                    logging.info('User chooses mixing uniform phase of second component which is image2  with unit magnitude of first  component which is image1')
                    self.InverseFourier = self.UM_IMG1_IMGModel1.mix(self.UP_IMG2_IMGModel2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
                if(self.IMG2==self.Imagemodel2 and self.IMG1==self.Imagemodel2):
                    logging.info('User chooses mixing uniform phase of second component which is image2  with unit magnitude of first  component which is image2')
                    self.InverseFourier = self.UM_IMG1_IMGModel2.mix(self.UP_IMG2_IMGModel2,self.Ratio1,self.Ratio2,Modes.magnitudeAndPhase)
                else:

                    message=QtWidgets.QMessageBox()
                    logging.info('the client chose 2 unrelated components')
                    message.setIcon(QtWidgets.QMessageBox.Critical)
                    message.setText("Error! two unrelated components")
                    message.setInformativeText("Dont Panic :) pick 2 proper components and try again later")
                    message.setWindowTitle(" Error message")
                    message.exec_()


        # elif(self.senderObject_C1_fourier=='actionc1UnitMag'and self.senderObject_C2_fourier=='actionc2UnitMag' or self.senderObject_C1_fourier=='actionc1UnitMag'and self.senderObject_C2_fourier=='actionc2UnitMag' )

                



        self.InverseFourierArray = pg.ImageItem(asarray(self.InverseFourier))

        if(self.whichoutput.text()=='output1'):
            logging.info('user chooses to display result at output1')
            self.ui.Output1.addItem(self.InverseFourierArray)
        if(self.whichoutput.text()=='output2'):
            logging.info('user chooses to display result at output2')
            self.ui.Output2.addItem(self.InverseFourierArray)     
        self.InverseFourierArray.rotate(270)

def main():

    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()
    
    

if __name__ == '__main__':
    main()


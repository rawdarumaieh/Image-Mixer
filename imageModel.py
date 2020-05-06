import os, sys
import numpy as np
from PIL import Image
import cv2
from numpy import asarray
from modesEnum import Modes
import numpy as np
import pyqtgraph as pg
from PIL import Image
from matplotlib import image as im
import scipy
import scipy.fftpack
from scipy import signal
from scipy.fftpack import fft, fftshift
from numpy.fft import fft,fftfreq,ifft
class ImageModel():

    """
    A class that represents the ImageModel"
    """

    # def __init__(self):
    #     pass

    def __init__(self, imgPath: str ="test"):
        if imgPath != "test":

            self.imgPath = imgPath
            ###
            # ALL the following properties should be assigned correctly after reading imgPath 
            ###
            self.imgByte = cv2.imread(imgPath,0)
            self.dft = np.fft.fft2(self.imgByte)
            self.real = np.real(self.dft)
            self.imaginary = np.imag(self.dft)
            self.magnitude = abs(self.dft)
            self.phase = np.angle(self.dft)
            self.UnitMagnitude=None
            self.UnitPhase=None
        else:
            self.magnitude=None
            self.phase=None
    
    def OpenImage(self):
        self.theimage=cv2.imread(self.imgPath,0)
        image = pg.ImageItem(self.theimage)      
        return image

    def FTMag(self):
        theImage=cv2.imread(self.imgPath,0)
        f = np.fft.fft2(theImage)
        self.magnitude = abs(f)
        return self.magnitude
    
    def FTPhase(self):
        theImage=cv2.imread(self.imgPath,0)
        fourier=np.fft.fft2(theImage)
        self.phase=np.angle(fourier)
        return self.phase

    def FTReal(self):
        theImage=cv2.imread(self.imgPath,0)
        fourier=np.fft.fft2(theImage)
        self.real=np.real(fourier)
        return self.real

    def FTImag(self):
        theImage=cv2.imread(self.imgPath,0)
        fourier=np.fft.fft2(theImage)
        # fshift = np.fft.fftshift(fourier)
        self.imaginary=np.imag(fourier)
        return self.imaginary

    def UniformMagnitude(self):
        rows,cols=self.magnitude.shape
        self.UnitMagnitude=np.ones((rows,cols))
        return self.UnitMagnitude
    def UniformPhase(self):
        rows,cols=self.phase.shape
        self.UnitPhase=np.zeros((rows,cols))
        return self.UnitPhase

    def mix(self, imageToBeMixed: 'ImageModel', magnitudeOrRealRatio: float, phaesOrImaginaryRatio: float, mode: 'Modes') -> np.ndarray:
        if(mode==mode.magnitudeAndPhase):
            TempMag=self.magnitude*magnitudeOrRealRatio+imageToBeMixed.magnitude*(1-magnitudeOrRealRatio)
            TempPhase=self.phase*magnitudeOrRealRatio+imageToBeMixed.phase*(1-phaesOrImaginaryRatio)
            self.fourier=np.multiply(TempMag,np.exp(1j*TempPhase))
        if(mode==mode.realAndImaginary):
            TempReal=self.real*magnitudeOrRealRatio+imageToBeMixed.real*(1-magnitudeOrRealRatio)
            TempImag=self.imaginary*phaesOrImaginaryRatio+imageToBeMixed.imaginary*(1-phaesOrImaginaryRatio)
            self.fourier=TempReal+1j*TempImag

        if(mode==mode.UnitMagnitude):
            TempUnitMagnitude=self.magnitude
            TempUnitMAGphase=self.phase*magnitudeOrRealRatio+imageToBeMixed.phase*(1-phaesOrImaginaryRatio)
            self.fourier=np.multiply(TempUnitMagnitude,np.exp(1j*TempUnitMAGphase))

        self.InverseImage=np.real(np.fft.ifft2(self.fourier))
        return self.InverseImage            

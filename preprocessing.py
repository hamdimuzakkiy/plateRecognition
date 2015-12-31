__author__ = 'hamdiahmadi'

import cv2

#class Image, untuk membaca gambar, show gambar, convert apapun menggunakan library cv2
class Image:

    def __init__(self):
        pass

    def readImage(self,path):
        return cv2.imread(path)

    def imageToGray(self,image):
        return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

    def medianBluring(self,image,filter_size):
        return cv2.medianBlur(image,filter_size)

    def saveImage(self,file_name,image):
        return cv2.imwrite(file_name,image)

    def edgeDetection(self,image):
        return cv2.Canny(image,100,200)

class DeNoising(Image):

    def __init__(self):
        pass

    #using median bluring
    def medianFilter(self,image,filter_size):
        return Image.medianBluring(self,image,filter_size)

class EdgeDetection(Image):

    def __init__(self):
        pass

    def cannyEdgeDetection(self,image):
        return Image.edgeDetection(self,image)
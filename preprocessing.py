__author__ = 'hamdiahmadi'

import cv2
import copy
import os
from PIL import Image as Images
import statistics as stat
import numpy as np

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

    def imageToBinary(self,image):
        return cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)

    def imageToInverseBinary(self,image):
        return cv2.threshold(image,0,127,cv2.THRESH_BINARY)

class DeNoising(Image):

    def __init__(self):
        pass

    #using median bluring
    def medianFilter(self,image,filter_size):
        return Image.medianBluring(self,image,filter_size)

class Binarization(Image):

    def __init__(self):
        pass

    def binarization(self,image):
        return Image.imageToBinary(self,image)[1]

class EdgeDetection(Image):

    def __init__(self):
        pass

    def cannyEdgeDetection(self,image):
        return Image.edgeDetection(self,image)

class Data:
    def __init__(self):
        pass

    def clockWise(self):
        clocks = []
        clocks.append([-1,-1])
        clocks.append([-1,0])
        clocks.append([-1,1])
        clocks.append([0,-1])
        clocks.append([0,1])
        clocks.append([1,-1])
        clocks.append([1,0])
        clocks.append([1,1])
        return clocks

class Localization(Image, Data):

    def __init__(self):
        pass

    def localization(self,image):
        background_counter = dict()
        background_counter[0] = 0
        background_counter[255] = 0
        is_visit = copy.copy(image)*0
        region_number = 0
        region = []
        for x in range(0,len(image[0])):
            for y in range(0,len(image)):
                background_counter[image[y][x]]+=1
                if is_visit[y][x] == 0:
                    stack = []
                    region_number+=1
                    stack.append([y,x])
                    is_visit[y][x] = int(region_number)
                    coordinate,is_visit = self.growing(image,is_visit,stack,region_number)
                    img = image[coordinate[2]:coordinate[0],coordinate[3]:coordinate[1]]
                    if (coordinate[0]-coordinate[2])>= len(image)/3 and (coordinate[1]-coordinate[3])>=len(image[0])/50 and (coordinate[0]-coordinate[2])<= len(image)/1.5 and (coordinate[1]-coordinate[3])<=len(image[0])/1.5:
                        region.append(img)
        if background_counter[255] > background_counter[0]:
            result = region
        else :
            result = []
            cntr = 0
            for x in region:
                cntr+=1
                for row in range(0,len(x)):
                    for col in range(0,len(x[row])):
                        if x[row][col] == 255:
                            x[row][col] = 0
                        else :
                            x[row][col] = 255
                result.append(x)
        return result

    def growing(self,image,is_visit,stack,region_number):
        listsY = []
        listsX = []
        clock = Data.clockWise(self)
        while len(stack)!=0:
            coory,coorx = stack[0]
            stack.pop(0)
            listsY.append(coory)
            listsX.append(coorx)
            for x in clock:
                try :
                    if coory+x[0] < 0 or coory+x[0] > len(is_visit) or coorx+x[1] <0 or coorx+x[1] > len(is_visit[0]):
                        pass
                    elif is_visit[coory+x[0]][coorx+x[1]] == 0 and image[coory][coorx] == image[coory+x[0]][coorx+x[1]]:
                        is_visit[coory+x[0]][coorx+x[1]] = region_number
                        stack.append([coory+x[0],coorx+x[1]])
                except :
                    pass
        return [max(listsY),max(listsX),min(listsY),min(listsX)],is_visit

class File:

    def __init__(self):
        pass
    def deleteFileInFolder(self,path):
        for files in os.listdir(path):
            files_ = os.path.join(path, files)
            try :
                if os.path.isfile(files_):
                    os.unlink(files_)
            except:
                pass
        return

    def readFileFolder(self,path):
        return os.listdir(path)

class GetColor:
    def __init__(self):
        pass

    def avgColor(self,image):
        w,h = image.size
        data = []
        pixel = image.load()
        for x in range(w):
            for y in range(h):
                data.append(pixel[x,y])
        return np.mean(data[0:x][0]), np.mean(data[0:x][1]),np.mean(data[0:x][2])

    def getDataTesting(self,path):
        image = Images.open(path)
        return self.avgColor(image)

    def getDatabase(self,hitam,kuning,merah):
        h = os.listdir(hitam)
        k = os.listdir(kuning)
        m = os.listdir(merah)
        lenGroup = [len(h),len(k),len(m)]
        group = [[j for i in range(lenGroup[j])] for j in range(3)]
        group = np.reshape(group,sum(lenGroup))
        dbData = []
        for listHitam in h:
            db = Images.open(hitam + listHitam)
            dbData.append(self.avgColor(db))
        for listKuning in h:
            db = Images.open(kuning + listKuning)
            dbData.append(self.avgColor(db))
        for listMerah in h:
            db = Images.open(merah + listMerah)
            dbData.append(self.avgColor(db))
        return group,dbData


    def KNN(self,color,train,test,k):
        CD = []
        if test[0] <= 80 and test[1] <= 80 and test[2] <= 80:
            pass

        for j in range(len(train)):
            sub = abs(np.subtract(test,train[j]))
            res = np.power(sub,2)
            CD.append(res[0]*res[1]*res[2])
        CD = np.array(CD)

        nearest= sorted(range(len(CD)), key=lambda k: CD[k])
        color = np.array(color)
        sortedColor = color[nearest]
        nearestColor = sortedColor[0:k]
        try:
            return stat.mode(nearestColor)
        except:
            return sortedColor[0]

    def category(self,result):
        if result==0:
            return 'hitam'
        elif result==1:
            return 'kuning'
        else:
            return 'merah'
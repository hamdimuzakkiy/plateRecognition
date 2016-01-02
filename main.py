__author__ = 'hamdiahmadi'

import preprocessing as pr
import time

if __name__ == '__main__':
    Image = pr.Image()
    DeNoising = pr.DeNoising()
    EdgeDetection = pr.EdgeDetection()
    Binarization = pr.Binarization()
    Localization = pr.Localization()
    File = pr.File()
    GetColor = pr.GetColor()

    File.deleteFileInFolder('result')
    file_name = 'Screenshot_1.png'
    image_path = 'data training/'+file_name
    print file_name

    image = Image.readImage(image_path)

    #extracting image, and put the result on result folder
    gray_image = Image.imageToGray(image)
    blur_image = DeNoising.medianFilter(gray_image,9)
    binary_image = Binarization.binarization(gray_image)
    splited_image = Localization.localization(binary_image)
    for x in range(0,len(splited_image)):
        Image.saveImage('result/'+file_name+'_'+str(x)+'.png',splited_image[x])

    #get color of plate number and assign the result on kategori variable
    data_testing = GetColor.getDataTesting(image_path)
    hitam = 'color/hitam/'
    kuning = 'color/kuning/'
    merah = 'color/merah/'

    group,data_training = GetColor.getDatabase(hitam,kuning,merah)
    result = GetColor.KNN(group,data_training, data_testing, 3)
    kategori = GetColor.category(result)
    print kategori
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

    lists = File.readFileFolder('data training')
    File.deleteFileInFolder('result')
    for path in lists:
        file_name = path
        image_path = 'data training/'+file_name
        print path

        image = Image.readImage(image_path)

        gray_image = Image.imageToGray(image)
        blur_image = DeNoising.medianFilter(gray_image,9)

        binary_image = Binarization.binarization(gray_image)
        start = time.time()
        splited_image = Localization.localization(binary_image)
        for x in range(0,len(splited_image)):
            Image.saveImage('result/'+file_name+'_'+str(x)+'.png',splited_image[x])
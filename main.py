__author__ = 'hamdiahmadi'

import preprocessing as pr

if __name__ == '__main__':
    Image = pr.Image()
    DeNoising = pr.DeNoising()
    EdgeDetection = pr.EdgeDetection()

    image_path = 'data gambar/car1.jpg'

    image = Image.readImage(image_path)
    gray_image = Image.imageToGray(image)

    blur_gray_image = DeNoising.medianFilter(gray_image,5)
    edge_gray_image = EdgeDetection.cannyEdgeDetection(blur_gray_image)
    Image.saveImage('new.png',edge_gray_image)
__author__ = 'hamdiahmadi'

import preprocessing as pr

if __name__ == '__main__':
    Image = pr.Image()
    DeNoising = pr.DeNoising()
    EdgeDetection = pr.EdgeDetection()
    Binarization = pr.Binarization()
    Contour = pr.Contour()

    image_path = 'data gambar/7.jpg'

    image = Image.readImage(image_path)
    gray_image = Image.imageToGray(image)


    blur_gray_image = DeNoising.medianFilter(gray_image,5)
    edge_image = EdgeDetection.cannyEdgeDetection(blur_gray_image)
    binary_edge_image = Binarization.binarization(edge_image)

    Image.saveImage('res.png',edge_image)
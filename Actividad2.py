#Referencias
#By Abhisek Jana
#https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
#http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/
#Modified by Benjamin Valdes

import numpy as np
import cv2
import matplotlib.pyplot as plt

def conv_helper(fragment, kernel):
    """ multiplica 2 matrices y devuelve su suma"""
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def convolution(image, h, w):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = (h, w) #asigna alto y ancho del filtro
   
    output = np.zeros(image.shape) #matriz donde guardo el resultado
    kernel = np.ones ((h, w))
   
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
             
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()
 
    return output

path = r'internetgrafi-prom-750x430 - Copy.png'
img = cv2.imread(path) 
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print ("Ingresa el tamano de la vecindad: ")
h = int(input("renglones: "))
w = int(input("columnas: "))
convolution(image, h, w)

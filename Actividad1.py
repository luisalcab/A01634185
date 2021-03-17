import numpy as np
import cv2
import matplotlib.pyplot as plt

#Ingrese el path de la imagen que quiere procesar
path = r'C:\Users\luisa\Downloads\internetgrafi-prom-750x430 - Copy.png'
img = cv2.imread(path) 

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.GaussianBlur(image, (21,21), 0, image)
edges = cv2.Canny(image, 10, 20, apertureSize=3)

window_name = 'image'
cv2.imshow(window_name, edges)
cv2.waitKey(0)  
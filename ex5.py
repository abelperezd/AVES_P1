# -*- coding: utf-8 -*-
'''
Este script cargamos una imagen, le aplicamos la DFT y la IDFT y comparamos
el resultado obtenido con la imagen original.
Ref:
    https://stackoverflow.com/questions/7110899/how-do-i-apply-a-dct-to-an-image-in-python
'''

from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt


# Tanto la DCT como la IDCT las realizamos en 2 dimensiones dado quue se trata de una imagen y
# no de un vector.

# 2D DCT
def dct2D(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


# 2D IDCT
def idct2D(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


im = rgb2gray(imread('fcb.jpeg'))  # cargamos la imagen y la pasamos a rgb para poder calcular la DCT
imF = dct2D(im)  # calculamos la DCT
im1 = idct2D(imF)  # calculamos la IDCT

plt.gray()  # hacemos el plot en escala de grises
plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('Original image', size=10)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('DCT+IDCT image', size=10)
plt.show()

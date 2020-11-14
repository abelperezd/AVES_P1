# -*- coding: utf-8 -*-
'''
Este scipt contiene las funciones rgb2yuv y yuv2rgb, que nos permiten pasar una imagen de RGB a YUB y viceversa.
El argumento de entrada para ambas funciones es un vector de dimensón 3x1.
Ref:
    https://softpixel.com/~cwright/programming/colorspace/yuv/
'''

import numpy as np


# Pasamos de RGB a YUV con la operación encontrada en el el enlace anterior
def rgb2yuv(rgb):
    Y = rgb[0] * .299000 + rgb[1] * .587000 + rgb[2] * .114000
    U = rgb[0] * -.168736 + rgb[1] * -.331264 + rgb[2] * .500000 + 128
    V = rgb[0] * .500000 + rgb[1] * -.418688 + rgb[2] * -.081312 + 128
    return np.array([Y, U, V])


# Pasamos de YUV a RGB con la operación encontrada en el el enlace anterior
def yuv2rgb(yuv):
    R = yuv[0] + 1.4075 * (yuv[2] - 128)
    G = yuv[0] - 0.3455 * (yuv[1] - 128) - (0.7169 * (yuv[2] - 128))
    B = yuv[0] + 1.7790 * (yuv[1] - 128)
    return np.array([R, G, B])


rgb = np.array([255, 255, 255])  # array que pasaremos de RGB a YUV y viceversa

yuv = rgb2yuv(rgb)
rgb_ = yuv2rgb(yuv)

print("RGB", rgb[0], rgb[1], rgb[2])
print("YUV", yuv[0], yuv[1], yuv[2])
print("Recovered RGB", rgb_[0], rgb_[1], rgb_[2])

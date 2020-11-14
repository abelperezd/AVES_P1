# -*- coding: utf-8 -*-
'''
En este script simplemente tenemos una función que llama a ffmpeg desde el sistema
y a través de él cortamos la imagen fcb.jpeg y una vez obtenemos la imagen cortada,
la pasamos a escala de grises.
Ref:
    https://www.rafalinux.com/?p=1613
    https://stackoverflow.com/questions/28806816/use-ffmpeg-to-resize-image
'''

import subprocess


# Realizamos ambas operaciones en la misma línea porque si lo hacemos en 2 líneas
# separadas, la conversión a escala de grises se realiza antes de crear la imagen
# y no la encuentra.
subprocess.call('ffmpeg -i fcb.jpeg -vf scale=200:200 fcb_resized.jpeg && ffmpeg -i fcb_resized.jpeg -vf format=gray fcb_resized_bw.jpeg', shell=True)

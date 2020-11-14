# -*- coding: utf-8 -*-
'''
En este script utilizamos otra función que también nos permite pasar una imagen de color
a una imagen en blanco y negro, pero esta vez sin recortarla.
Ref:
    https://video.stackexchange.com/questions/28758/ffmpeg-convert-video-to-black-white-with-threshold/28759
'''

import subprocess


subprocess.call('ffmpeg -i fcb.jpeg -f lavfi -i color=gray:s=2000x2000 -f lavfi -i color=black:s=2000x2000 -f lavfi -i color=white:s=2000x2000 -filter_complex threshold fcb_bw.jpeg', shell=True)

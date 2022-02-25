#!/usr/bin/env python 
from __future__ import print_function, unicode_literals
import qrcode

img = qrcode.make('I love you crazy')
type(img)  # qrcode.image.pil.PilImage
img.save("ilu.png")
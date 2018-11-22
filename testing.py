# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 14:56:39 2018

@author: Albert
"""

from PIL import Image

img = Image.open("./IMG_0305.JPG")
newImg = img.resize((224,224))
newImg.save("temporary.jpg")
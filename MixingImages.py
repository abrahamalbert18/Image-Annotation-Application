# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 15:42:30 2018

@author: Albert
"""

import os, time
from shutil import copyfile, move

# A:\Drinking Project\downloads\Beer

workingDirectory = "A:\Drinking Project\downloads\Mixed"
listOfDirectories = os.listdir(workingDirectory)
listOfDirectories.remove('MixedImages')
t1 = time.time()
for r in range(6):    
    globalId = len(os.listdir("A:\Drinking Project\downloads\Mixed\MixedImages"))
    print("Global Id =", str(globalId))     
    dictOfDirectoryImages = {}
    for l in listOfDirectories:
        listOfDirectoryImages = os.listdir(workingDirectory+"\\"+ l)
        dictOfDirectoryImages[l] = listOfDirectoryImages
        os.chdir(workingDirectory+"\\"+l)
        for n in range(100): #range(50)
            try:
                img = dictOfDirectoryImages[l][n]
            except IndexError:
                break    
            try:
                print(" Moving Image", str(globalId)+ ".jpg")
                move("./"+img, "../MixedImages/"+str(globalId)+".jpg")
                globalId += 1
            except:
                continue

t2 = time.time()
print("Total time taken to copy 2000 images =", str(round(t2-t1,3)), "seconds" )
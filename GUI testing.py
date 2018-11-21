# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:37:49 2018

@author: Albert
"""
import os
import numpy as np
from PIL import Image

import tkinter as tk
from tkinter import ttk, scrolledtext, Menu
from shutil import copyfile

#Initialising and title of the app.
app = tk.Tk()
app.title("Image Annotation Application")
app.configure(background="snow")


def saveFileFirstTime():
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    with open("DrinkingDataLabels.csv","w+") as file:
        firstLine = file.read()
        if len(firstLine) == 0:
            new_line = "originalFileName,globalIndex,label"
            file.write(new_line)
    
    pass    
        
def backupFile():
    '''
    This file saves a backup file just incase if the original file is accidentally deleted.
    '''
    try:
        os.mkdir("./backup")
        copyfile("./DrinkingDataLabels.csv", "./backup/DrinkingDataLabelsBackup.csv")
        os.chmod("./backup/DrinkingDataLabelsBackup.csv", stat.S_IRUSR | stat.S_IROTH)
    except OSError:
        copyfile("./DrinkingDataLabels.csv", "./backup/DrinkingDataLabelsBackup.csv")
    pass

def loadImages():
    """
    This function is used to load images from the directory.
    """
    workingDirectory = os.getcwd()
    imagesList = os.listdir(workingDirectory)
    
    pass
    
def saveLabel():
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    labels = ["beer","wine","other"]
    with open("DrinkingDataLabels.csv","a") as file:
        label = radioLabel.get()
        if label == 0: app.configure(background="light goldenrod")
        elif label == 1: app.configure(background="brown4")
        else : app.configure(background="steel blue")
        file.writelines("\n"+str(label))
        backupFile()
    pass
                

#Creating a label frame for dynamic control of GUI 
lFrame = ttk.LabelFrame(app, text = "Image Labelling")
lFrame.grid(column = 0, row = 0, sticky = "W")
#Labels
label = ttk.Label(lFrame,text="Please enter the path: ")
label.grid(column=0, row=0, sticky = "W")

#Class Labels
classLabel = ttk.Label(lFrame,text="Class Labels: ")
classLabel.grid(column=0, row=3, sticky = "W")

#Defining a Button Click event
def clickMe():
    action.configure(text="I've been clicked.")
    label.configure(foreground="red")
    label.configure(text="I'm a red label")
    
def textBoxClick():
    action.configure(text="Hi "+ text.get()+ "!")    


#Creating a textbox
text = tk.StringVar()
textEntered = ttk.Entry(app, width=16, textvariable=text)
textEntered.grid(column=1,row=0)

    
#Adding a button
action = ttk.Button(app, text="Click Me!", command = textBoxClick)
action.grid(column=1, row = 4,padx = 4, pady = 4)


#Adding open button
actionOpen = ttk.Button(app, text="Open Folder",)
actionOpen.grid(column=2,row =0)

#Adding next button
actionNext = ttk.Button(app, text="Next Image",)
actionNext.grid(column=2,row =10)


#Adding prev button
actionPrev = ttk.Button(app, text="Previous Image",)
actionPrev.grid(column=0,row =10)

#Adding save label button
actionSaveLabel = ttk.Button(app, text="Save Label", command = saveLabel)
actionSaveLabel.grid(column=1,row =12)


#Creating a radio button for class "beer"
radioLabel = tk.IntVar()
radioLabel.set(99)

radioLabel1 = tk.Radiobutton(app, variable = radioLabel, text = "Beer", value = 0, command = saveLabel)
radioLabel1.grid(column=1, row = 3)

radioLabel2 = tk.Radiobutton(app, variable = radioLabel, text = "Wine", value = 1, command = saveLabel)
radioLabel2.grid(column=2, row = 3)

radioLabel3 = tk.Radiobutton(app, variable = radioLabel, text = "Others", value = 2, command = saveLabel)
radioLabel3.grid(column=3, row = 3)


# #Creating a scrolled text
# scrolHeight = 4
# scrolWidth = 40

# scroll = scrolledtext.ScrolledText(app, height = scrolHeight, width = scrolWidth, wrap = tk.WORD)
# scroll.grid(column = 0, row = 20, padx = 40, pady =60)

#Creating a menu bar


#Placing the cursor
textEntered.focus()

#run the window
app.mainloop()
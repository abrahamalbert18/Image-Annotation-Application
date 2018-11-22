# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:37:49 2018

@author: Albert
"""
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, messagebox as mBox, filedialog as fd
from shutil import copyfile

#Initialising and title of the app.
app = tk.Tk()
app.geometry("900x800")
app.title("Image Annotation Application")
background = "cyan4"
app.configure(background=background)

workingDirectory = os.getcwd()
imagesList = []
tkImage = None
currentImageIndex = 0
df = pd.read_csv("DrinkingDataLabels.csv")

try:
    df = df[df['label'] != 99]
except:
    pass

try:
    globalIndex = df.count()['originalFileName']
except:
    globalIndex = 1

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


def loadImage(event=None):
    """
    This function is used to load images from the directory.
    """
    global workingDirectory, imagesList, currentImageIndex
    workingDirectory = fd.askdirectory()
    imagesList = os.listdir(workingDirectory)
    currentImageIndex = 0
    pass


# def firstImage():
#     img = imagesList[currentImageIndex]
#     print(img)
#     imgPath = workingDirectory+"/"+img
#     img = Image.open(imgPath)
#     tkImage = ImageTk.PhotoImage(img)
#     imageLabel = tk.Label(app, image = tkImage)
#     imageLabel.pack()    



def loadNextImage(event=None):    
    """
    Loads the next image in the GUI.
    """
    try:    
        global currentImageIndex, tkImage
        print(currentImageIndex)
        if currentImageIndex == 0:
            currentImageIndex = 0        
        currentImageIndex += 1 
        img = imagesList[currentImageIndex]    
        print(img)
        imgPath = workingDirectory+"/"+img
        img = Image.open(imgPath)
        img = img.resize((850, 550), Image.ANTIALIAS)
        tkImage = ImageTk.PhotoImage(img)
        imageLabel = ttk.Label(app, image = tkImage)
        imageLabel.grid(row = 4, column =0, columnspan = 4)
        saveLabel()
        if currentImageIndex >= len(imagesList):
             mBox.showwarning("End of Directory", "Images in the folder are annotated. Try annotating images from another folder. ")
        pass
    except OSError:
        imagesList.pop(currentImageIndex)
        os.remove(imgPath)

def loadPrevImage(event=None):      
    """
    Loads the previous image in the GUI.
    """
    global currentImageIndex, tkImage
    currentImageIndex -= 1
    print(currentImageIndex)
    img = imagesList[currentImageIndex]
    print(img)
    imgPath = workingDirectory+"/"+img
    try:
        img = Image.open(imgPath)
        img = img.resize((850, 550), Image.ANTIALIAS)
        tkImage = ImageTk.PhotoImage(img)
        imageLabel = ttk.Label(app, image = tkImage)
        imageLabel.grid(row = 4, column =0, columnspan = 4)
        if currentImageIndex <= 0:
             mBox.showwarning("Warning", "Cannot load previous image. This is the first image in the folder. Please try next image.")
        pass
    except OSError:
        imagesList.pop(currentImageIndex)
        os.remove(imgPath)
        # currentImageIndex -= 1
    
def save(event=None):
    """
    Saves a backup file in backup directory.
    """
    backupFile()
    
def saveLabel(event=None):
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    global globalIndex, background
    with open("DrinkingDataLabels.csv","a") as file:
        label = radioLabel.get()
        if label == 0: 
            background="light goldenrod"
            app.configure(background=background)
        elif label == 1: 
            background="brown4"
            app.configure(background=background)
        else : 
            background="steel blue"
            app.configure(background=background)
        imageName = imagesList[currentImageIndex]
        
        file.writelines("\n"+imageName+","+str(globalIndex)+","+str(label))
        globalIndex += 1
        save()
    pass
                
def _messageBox(event=None):
    """
    Displays a message box with instructions.
    """
    mBox._show("Help","By default an image is displayed for layout purpose.\
                  Instructions: \n1. Open the folder with all the images. \
                                \n2. Press next image.\
                                \n3. Select the class label either beer or wine or other.\
                                \n4. Continue untill the last image in the folder.\
                                \n5. Press save button before you exit.")
    pass

def _messageShorcut(event=None):
    """
    Displays a message box with instructions.
    """
    mBox._show("Shortcuts","These simple keyboard shortcuts should reduce the mouse usage.\
                            \n 1. o --> open folder \
                            \n 2. w, p, <Left>, <Down> --> Previous image\
                            \n 3. e, n, <Right>, <Up> --> Next image\
                            \n 4. s --> Shortcuts\
                            \n 5. h --> Help\
                            \n 6. x --> Save and Exit.o")
    pass

def _saveMessage():
    """
    Displays a small message box
    """
    mBox.showinfo("Save", "Saved Successfully. Have a good time :)")    
        
def about():
    """
    Displays a small message box with details about.
    """
    mBox.showinfo("About","This is a very basic application created for labelling images. @2018")

#Creating a label frame for dynamic control of GUI 
# lFrame = ttk.LabelFrame(app, text = "Image Labelling")
# lFrame.grid(column = 0, row = 0, sticky = "W")

#Labels
label = ttk.Label(app,text="Open Folder")
label.grid(column=0, row=0, sticky = "W")
label.config(font=("Tahoma","20", "bold"))
label.configure(background = background)

#Class Labels
classLabel = ttk.Label(app,text="Class Labels: ")
classLabel.grid(column=0, row=5, sticky = "W")
classLabel.config(font=("Tahoma","20", "bold"))
classLabel.configure(background = background)

imgPath = "./IMG_0305.JPG"
img = Image.open(imgPath)
img = img.resize((850, 550), Image.ANTIALIAS)
tkImage = ImageTk.PhotoImage(img)
imageLabel = ttk.Label(app, image = tkImage)
imageLabel.grid(row = 4, column = 0, columnspan = 4)
#Defining a Button Click event
# def clickMe():
#     action.configure(text="I've been clicked.")
#     label.configure(foreground="red")
#     label.configure(text="I'm a red label")
#     pass
    
# def textBoxClick():
#     action.configure(text="Hi "+ text.get()+ "!")    
#     pass

def _exitGUI(event=None):
    """
    Exit GUI cleanly.
    """
    _saveMessage()
    app.quit()
    app.destroy()

#Creating a textbox
# text = tk.StringVar()
# textEntered = ttk.Entry(app, width=16, textvariable=text)
# textEntered.grid(column=1,row=0)

    
#Adding a button
# action = ttk.Button(app, text="Click Me!", command = textBoxClick)
# action.grid(column=1, row = 4,padx = 4, pady = 4)


#Adding open button
actionOpen = tk.Button(app, text="Open Folder", bg = "deepskyblue4", command = loadImage)
actionOpen.grid(column=0,row =1, sticky= tk.W)
actionOpen.config(font= ("Tahoma",16))

#Adding next button
actionNext = tk.Button(app, text="Next Image", command=loadNextImage, bg = "deepskyblue4")
actionNext.grid(column =2 , row = 10, sticky=tk.W)
actionNext.config(font= ("Tahoma",16))

#Adding prev button
actionPrev = tk.Button(app, text="Previous Image", command = loadPrevImage, bg = "deepskyblue4")
actionPrev.grid(column=0,row =10,sticky=tk.E)
actionPrev.config(font= ("Tahoma",16))

#Adding save label button
actionSaveLabel = tk.Button(app, text="Save Label", command =_saveMessage, bg = "deepskyblue4")
actionSaveLabel.grid(column=1,row =12)
actionSaveLabel.config(font= ("Tahoma",16))

#Creating a radio button for class "beer"
radioLabel = tk.IntVar()
radioLabel.set(99)

radioLabel1 = tk.Radiobutton(app, variable = radioLabel, text = "Beer", value = 0, command = saveLabel)
radioLabel1.grid(column=1, row = 5)
radioLabel1.config(font=("Tahoma",16))
radioLabel1.configure(background = background)

radioLabel2 = tk.Radiobutton(app, variable = radioLabel, text = "Wine", value = 1, command = saveLabel)
radioLabel2.grid(column=2, row = 5)
radioLabel2.config(font=("Tahoma",16))
radioLabel2.configure(background = background)

radioLabel3 = tk.Radiobutton(app, variable = radioLabel, text = "Others", value = 2, command = saveLabel)
radioLabel3.grid(column=3, row = 5)
radioLabel3.config(font=("Tahoma",16))
radioLabel3.configure(background = background)
# #Creating a scrolled text
# scrolHeight = 4
# scrolWidth = 40

# scroll = scrolledtext.ScrolledText(app, height = scrolHeight, width = scrolWidth, wrap = tk.WORD)
# scroll.grid(column = 0, row = 20, padx = 40, pady =60)

#Creating a menu bar
menuBar = Menu(app)
app.configure(menu = menuBar)

#Adding file menu items
fileMenu = Menu(menuBar, tearoff = 0)
fileMenu.add_command(label="Save",command = save)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = _exitGUI)
menuBar.add_cascade(label="File", menu=fileMenu)


#Adding help menu items
helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label="Help", command= _messageBox)
helpMenu.add_command(label="About", command = about)
menuBar.add_cascade(label="Help", menu= helpMenu)



#Placing the cursor
# textEntered.focus()

#Adding Primary keyboard shortcuts
app.bind("n",loadNextImage)
app.bind("p",loadPrevImage)
app.bind("s",_messageShorcut)
app.bind("h",_messageBox)
app.bind("x",_exitGUI)
app.bind("o",loadImage)

#Adding Secondary keyboard shortcuts
app.bind("<Right>",loadNextImage)
app.bind("<Left>",loadPrevImage)
app.bind("e",loadNextImage)
app.bind("w",loadPrevImage)
app.bind("<Up>",loadNextImage)
app.bind("<Down>",loadPrevImage)

#run the window
app.mainloop()
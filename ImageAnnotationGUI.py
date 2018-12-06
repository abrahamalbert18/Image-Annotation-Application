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
tkImage = None
imagesList = []
currentImageIndex = 0
annotationLabels = ["Beer Cup!!!!!", "Beer Bottle", "Beer Can!!!!!", "Wine!!!!!!!!!!", "Champagne!!", "Undecided!!", "Other!!!!!!!!!!"]
previousLabel = None
previousLabels = []
df = pd.read_csv("DrinkingDataLabels.csv")

try:
    df = df[df['label'] != 998]
    df.drop_duplicates(subset="originalFileName", keep = "last", inplace=True)
    df.to_csv("PreprocessedDrinkingDataLabels.csv", index=False, header = True)
except:
    pass

try:
    index = df.last_valid_index()
    lastImage = df['originalFileName'].loc[index]
    lastImageId = lastImage[:-4]
    previousLabel = annotationLabels[df['label'].loc[index]]
except:
    lastImage = ""

def saveFileFirstTime():
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    with open("DrinkingDataLabels.csv","w+") as file:
        firstLine = file.read()
        if len(firstLine) == 0:
            new_line = "originalFileName,label"
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
    global workingDirectory, imagesList, currentImageIndex, globalIndex, lastImage
    workingDirectory = fd.askdirectory()
    imagesList = os.listdir(workingDirectory)
    imagesList = sorted(imagesList, key = lambda x: int(x[:-4]))
    # try:
    #     os.mkdir(workingDirectory+"/beer")
    #     os.mkdir(workingDirectory+"/wine")
    #     os.mkdir(workingDirectory+"/other")
    #     saveTempFileFirstTime()
        
    # except FileExistsError:
    #     imagesList.remove("beer")
    #     imagesList.remove("wine")
    #     imagesList.remove("other")
        
    try:
        currentImageIndex = imagesList.index(lastImage)-1
    except:
        currentImageIndex = -1
    loadNextImage()
    pass


# def firstImage():
#     img = imagesList[currentImageIndex]
#     print(img)
#     imgPath = workingDirectory+"/"+img
#     img = Image.open(imgPath)
#     tkImage = ImageTk.PhotoImage(img)
#     imageLabel = tk.Label(app, image = tkImage)
#     imageLabel.pack()    

def displayPrevLabel():
    global previousLabel
    
    label = ttk.Label(app,text=previousLabel)
    label.grid(column= 3, row=0, sticky = "W")
    label.config(font=("Tahoma","20", "bold"))
    label.configure(background = background)
    
    previousLabel = None
    label = ttk.Label(app,text=previousLabel)
    label.grid(column= 3, row=0, sticky = "W")
    label.config(font=("Tahoma","20", "bold"))
    label.configure(background = background)
    
    pass


def loadNextImage(event=None):    
    """
    Loads the next image in the GUI.
    """
    try:    
        global currentImageIndex, tkImage
        print(currentImageIndex)
        
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
        
        if currentImageIndex >= len(imagesList)-1:
             mBox.showwarning("End of Directory", "Images in the folder are annotated. Try annotating images from another folder. ")
        pass
    except OSError:
        imagesList.pop(currentImageIndex)
    except IndexError:
        pass
        # os.remove(imgPath)

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
        # os.remove(imgPath)
        # currentImageIndex -= 1
    
    
    
def saveLabel(event=None):
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    global globalIndex, background, previousLabel, annotationLabels, previousLabels
    # tempFile = open(workingDirectory+"/tempDrinkingDataLabels.csv","a")
    if len(imagesList) != 0:
        with open("DrinkingDataLabels.csv","a") as file:
            label = radioLabel.get()
            imageName = imagesList[currentImageIndex]
            
            if label == 1: 
                background="light goldenrod"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/beer/"+str(globalIndex)+".jpg")
                
            elif label == 2: 
                background="brown4"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/wine/"+str(globalIndex)+".jpg")
                
            elif label == 3: 
                background="brown4"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/wine/"+str(globalIndex)+".jpg")
                
            elif label == 4: 
                background="brown4"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/wine/"+str(globalIndex)+".jpg")    
            
            elif label == 5: 
                background="brown4"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/wine/"+str(globalIndex)+".jpg")
            
            elif label == 6: 
                background="brown4"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/wine/"+str(globalIndex)+".jpg")
            
            else : 
                background="steel blue"
                app.configure(background=background)
                # copyfile(workingDirectory+"/"+imageName, workingDirectory+"/others/"+str(globalIndex)+".jpg")
                
            file.writelines("\n"+imageName+","+str(label-1))
            previousLabels.append(label-1)
            try:
                # print(previousLabels)
                previousLabels = previousLabels[-2:]
                previousLabel = annotationLabels[previousLabels[-2]]
            except IndexError:
                pass
            displayPrevLabel()
            # print("Previous Label = ", previousLabel)
            # tempFile.writelines("\n"+imageName+","+str(label))
            # globalIndex += 1
    # tempFile.close()
        # save()
    pass
        
def saveRadioButtonLabel(label, event=None):
    '''
    This function should open the file and write  "originalFileName,\tglobalIndex,\tlabel" 
    '''
    global globalIndex, background, imagesList
    # tempFile = open(workingDirectory+"/tempDrinkingDataLabels.csv","a")
    
    if radioLabel.get() == 999:
        radioLabel.set(label)    
        saveLabel()
    else:
        radioLabel.set(label)
    loadNextImage()
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
                            \n 6. x --> Save and Exit.")
    pass

def _saveMessage():
    """
    Displays a small message box
    """
    saveLabel()
    backupFile()
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

label = ttk.Label(app,text="Previous Image Label : ")
label.grid(column= 2, row=0, sticky = "W")
label.config(font=("Tahoma","20", "bold"))
label.configure(background = background)


label = ttk.Label(app,text=previousLabel)
label.grid(column= 3, row=0, sticky = "W")
label.config(font=("Tahoma","20", "bold"))
label.configure(background = background)


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
actionOpen = tk.Button(app, text="Open Folder", bg = "peach puff", command = loadImage)
actionOpen.grid(column=0,row =1, sticky= tk.W)
actionOpen.config(font= ("Tahoma",16))

#Adding next button
actionNext = tk.Button(app, text="Next Image", command=loadNextImage, bg = "peach puff")
actionNext.grid(column =2 , row = 10, sticky=tk.W)
actionNext.config(font= ("Tahoma",16))

#Adding prev button
actionPrev = tk.Button(app, text="Previous Image", command = loadPrevImage, bg = "peach puff")
actionPrev.grid(column=0,row =10,sticky=tk.E)
actionPrev.config(font= ("Tahoma",16))

#Adding save label button
actionSaveLabel = tk.Button(app, text="Save Label", command =_saveMessage, bg = "peach puff")
actionSaveLabel.grid(column=1,row =12)
actionSaveLabel.config(font= ("Tahoma",16))

#Creating a radio button for class "beer"
radioLabel = tk.IntVar()
radioLabel.set(999)

radioLabel1 = tk.Radiobutton(app, variable = radioLabel, text = "Beer Cup", value = 1, command = saveLabel)
radioLabel1.grid(column=1, row = 5, sticky = tk.W)
radioLabel1.config(font=("Tahoma",16))
radioLabel1.configure(background = background)

radioLabel2 = tk.Radiobutton(app, variable = radioLabel, text = "Beer Bottle", value = 2, command = saveLabel)
radioLabel2.grid(column=1, row = 6, sticky = tk.W)
radioLabel2.config(font=("Tahoma",16))
radioLabel2.configure(background = background)

radioLabel3 = tk.Radiobutton(app, variable = radioLabel, text = "Beer Can", value = 3, command = saveLabel)
radioLabel3.grid(column=1, row = 7, sticky = tk.W)
radioLabel3.config(font=("Tahoma",16))
radioLabel3.configure(background = background)


radioLabel4 = tk.Radiobutton(app, variable = radioLabel, text = "Wine", value = 4, command = saveLabel)
radioLabel4.grid(column=2, row = 5, sticky = tk.W)
radioLabel4.config(font=("Tahoma",16))
radioLabel4.configure(background = background)


radioLabel5 = tk.Radiobutton(app, variable = radioLabel, text = "Champagne", value = 5, command = saveLabel)
radioLabel5.grid(column=2, row = 6, sticky = tk.W)
radioLabel5.config(font=("Tahoma",16))
radioLabel5.configure(background = background)


radioLabel6 = tk.Radiobutton(app, variable = radioLabel, text = "Undecided", value = 6, command = saveLabel)
radioLabel6.grid(column=3, row = 5, sticky = tk.W)
radioLabel6.config(font=("Tahoma",16))
radioLabel6.configure(background = background)


radioLabel7 = tk.Radiobutton(app, variable = radioLabel, text = "Other", value = 7, command = saveLabel)
radioLabel7.grid(column=3, row = 6, sticky = tk.W)
radioLabel7.config(font=("Tahoma",16))
radioLabel7.configure(background = background)
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
fileMenu.add_command(label="Shortcut",command = _messageShorcut)
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

#defining keyboard shortcuts
def keyPressed(event):
    key = event.char
    
    if key in ["n","e"]:
        loadNextImage()
    elif key in ["p", "w"]:
        loadPrevImage()
    elif key == "s":
        _messageShorcut()
    elif key == "h":
        _messageBox()
    elif key == "x":
        _exitGUI()
    elif key == "o":
        loadImage()
    elif key in ["1", "2", "3", "4", "5", "6", "7"]:
        saveRadioButtonLabel(label= int(key))
    else:
        pass
    
# #Adding Primary keyboard shortcuts
# app.bind("n",loadNextImage)
# app.bind("p",loadPrevImage)
# app.bind("s",_messageShorcut)
# app.bind("h",_messageBox)
# app.bind("x",_exitGUI)
# app.bind("o",loadImage)

#Adding Radiobutton Shortcuts
app.bind("<Key>", keyPressed)

#Adding Secondary keyboard shortcuts
app.bind("<Right>",loadNextImage)
app.bind("<Left>",loadPrevImage)
# app.bind("e",loadNextImage)
# app.bind("w",loadPrevImage)
app.bind("<Up>",loadNextImage)
app.bind("<Down>",loadPrevImage)

# app.option_add('*show.msg.font', 'Calibri -24')
#run the window
app.mainloop()



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 03:42:18 2023

@author: iqbal
"""

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# Create a new Tkinter window
window = Tk()

# Set the window title
window.title("Multi Label Object Recognition")

# Set the window size
window.geometry("900x600")

class ImageViewer:
    def __init__(self, window):
        self.window = window
        self.imageLabel = None
        self.imageFilePath = None
        self.image = None
        self.textLabel = None 
        # Create a button to browse for an image file
        browseButton = Button(window, text="Browse", command=self.browseImage)

        
        # Create a button to add text to the window
        detectButton = Button(window, text="Detect Objects", command=self.runModel)

        # Create a button to clear the image and label
        clearButton = Button(window, text="Clear", command=self.clearImage)


        # Add the buttons to the main window using pack geometry manager
        browseButton.pack(side=LEFT, padx=10)
        detectButton.pack(side=LEFT, padx=10)
        clearButton.pack(side=LEFT, padx=10)

    # Create a function to browse for an image file
    def browseImage(self):
        imageViewer.clearImage()
        # Show a file dialog to allow the user to select an image file
        filetypes = [("Image files", "*.png;*.jpeg;*.jpg")]
        self.imageFilePath = filedialog.askopenfilename()

        # Open the image file using PIL
        self.image = Image.open(self.imageFilePath)

        # Resize the image to fit within a 400x400 pixel bounding box
        self.image = self.image.resize((400, 400))

        # Convert the PIL image to a Tkinter-compatible PhotoImage object
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create a label widget to display the image
        self.imageLabel = Label(self.window, image=self.tk_image, width=400, height=400)

        # Add the label to the main window using pack geometry manager
        self.imageLabel.pack()

 

    def clearImage(self):
        if self.imageLabel:
            self.imageLabel.pack_forget()
            self.imageLabel = None
            self.imageFilePath = None
            self.image = None
        if self.textLabel:
            self.textLabel.pack_forget()
            self.textLabel = None
            self.textLabel = Label(self.window, text="", font=("Helvetica", 18))
            self.textLabel.pack()
                
    def runModel(self):
        # Create a label widget with the text "Hello, world!"
        from keras.models import Sequential
        """Import from keras_preprocessing not from keras.preprocessing, because Keras may or maynot contain the features discussed here depending upon when you read this article, until the keras_preprocessed library is updated in Keras use the github version."""
        from keras_preprocessing.image import ImageDataGenerator
        from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
        from keras.layers import Conv2D, MaxPooling2D
        from keras import regularizers, optimizers
        import pandas as pd
        import numpy as np
        from keras.models import load_model
        from keras.preprocessing.image import load_img, img_to_array
        
        # Load the saved model
        model = load_model('ml_model.h5')
        
        # Define the labels
        labels = ['desert', 'mountains', 'sea', 'sunset', 'trees']
        
        # Load the test image
        img = load_img(self.imageFilePath, target_size=(100, 100))
        x = img_to_array(img)
        x = x / 255.
        x = np.expand_dims(x, axis=0)
        
        # Make predictions on the test image
        pred = model.predict(x)[0]
        pred_bool = (pred > 0.5)
        predictions = pred_bool.astype(int)
        label_list = list()
        # Display the predicted labels for the test image
        for i in range(len(labels)):
            if predictions[i] == 1:
                print(labels[i])
                label_list.append(labels[i])
                
        
        label_string = ','.join(label_list)

        # Add the label to the main window using pack geometry manager
        textLabel = Label(self.window, text=label_string, font=("Helvetica", 18))
        textLabel.pack()

# Create an instance of the ImageViewer class
imageViewer = ImageViewer(window)

# Start the Tkinter main event loop
window.mainloop()


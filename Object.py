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
window.title("Image Viewer")

# Set the window size
window.geometry("900x600")

class ImageViewer:
    def __init__(self, window):
        self.window = window
        self.imageLabel = None
        self.imageFilePath = None
        self.image = None

        # Create a button to browse for an image file
        browseButton = Button(window, text="Browse", command=self.browseImage)

        # Create a button to add text to the window
        textButton = Button(window, text="Add Text", command=self.addText)
        
        # Create a button to add text to the window
        detectButton = Button(window, text="Detect Objects", command=self.runModel)

        # Add the buttons to the main window using pack geometry manager
        browseButton.pack(side=LEFT, padx=10)
        textButton.pack(side=LEFT, padx=10)
        detectButton.pack(side=LEFT, padx=10)

    # Create a function to browse for an image file
    def browseImage(self):
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

    # Create a function to add text to the window
    def addText(self):
        # Create a label widget with the text "Hello, world!"
        textLabel = Label(self.window, text="Hello, world!", font=("Helvetica", 24))

        # Add the label to the main window using pack geometry manager
        textLabel.pack()
    # Create a function to add text to the window
    def detect(self):
        # Create a label widget with the text "Hello, world!"
        textLabel = Label(self.window, text="Hello, world!", font=("Helvetica", 24))

        # Add the label to the main window using pack geometry manager
        textLabel.pack()
    # Create a function to add text to the window
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
        df=pd.read_csv("./miml_dataset/miml_labels_1.csv")
        columns=["desert", "mountains", "sea", "sunset", "trees"]
        datagen=ImageDataGenerator(rescale=1./255.)
        test_datagen=ImageDataGenerator(rescale=1./255.)
        train_generator=datagen.flow_from_dataframe(
        dataframe=df[:1800],
        directory="./miml_dataset/images",
        x_col="Filenames",
        y_col=columns,
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="raw",
        target_size=(100,100))
        valid_generator=test_datagen.flow_from_dataframe(
        dataframe=df[1800:1900],
        directory="./miml_dataset/images",
        x_col="Filenames",
        y_col=columns,
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="raw",
        target_size=(100,100))
        test_generator=test_datagen.flow_from_dataframe(
        dataframe=df[1900:],
        directory="./miml_dataset/images",
        x_col="Filenames",
        batch_size=1,
        seed=42,
        shuffle=False,
        class_mode=None,
        target_size=(100,100))
        from keras.models import load_model
        model = load_model('my_model.h5')
        test_generator.reset()
        pred=model.predict_generator(test_generator,
        steps=STEP_SIZE_TEST,
        verbose=1)           
        pred_bool = (pred >0.5)        
        from tensorflow.keras.preprocessing.image import load_img
        from tensorflow.keras.preprocessing.image import img_to_array
        import numpy as np
        
        # Load an image for testing
        img_path = 'test1.jpg'
        img = load_img(img_path, target_size=(100, 100))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x / 255.
        
        # Make predictions on the test image using the trained model
        pred = model.predict(x)[0]
        pred_bool = (pred > 0.5)
        predictions = pred_bool.astype(int)
        
        # Display the predicted labels for the test image
        labels = ['desert', 'mountains', 'sea', 'sunset', 'trees']
        for i in range(len(labels)):
            if predictions[i] == 1:
                print(labels[i])                                                                                                                                                                   

# Create an instance of the ImageViewer class
imageViewer = ImageViewer(window)

# Start the Tkinter main event loop
window.mainloop()


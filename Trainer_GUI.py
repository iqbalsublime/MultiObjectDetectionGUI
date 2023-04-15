#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 02:38:02 2023

@author: iqbal
"""
import tkinter as tk
from tkinter import filedialog

class Gui:
    def __init__(self, master):
        self.master = master
        master.title("Sample GUI")

        # Button to select dataset folder
        self.select_dataset_button = tk.Button(master, text="Select Dataset", command=self.select_dataset_folder)
        self.select_dataset_button.pack()

        # Button to train model
        self.train_button = tk.Button(master, text="Train", command=self.train_model)
        self.train_button.pack()

        # Button to browse saved model
        self.browse_model_button = tk.Button(master, text="Browse Model", command=self.browse_saved_model)
        self.browse_model_button.pack()

        # Label to show training epoch steps
        self.training_epoch_steps = tk.Label(master, text="Training epoch steps")
        self.training_epoch_steps.pack()

        # Button to select an image for testing
        self.select_test_image_button = tk.Button(master, text="Test", command=self.select_test_image)
        self.select_test_image_button.pack()

    def select_dataset_folder(self):
        dataset_folder_path = filedialog.askdirectory()
        print("Selected dataset folder:", dataset_folder_path)

    def train_model(self):
        print("Training model...")

    def browse_saved_model(self):
        saved_model_path = filedialog.askopenfilename()
        print("Selected saved model:", saved_model_path)

    def select_test_image(self):
        test_image_path = filedialog.askopenfilename()
        print("Selected test image:", test_image_path)

root = tk.Tk()
gui = Gui(root)
root.mainloop()

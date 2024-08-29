import os
import sys
import datetime
import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler
from tensorflow.keras import backend as keras
import tensorflow.keras.backend as K
from tensorflow import argmax
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model
from sklearn.model_selection import train_test_split

# Utils
import h5py

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# from keras.models import load_model

#2chamber

# Load the pre-trained UNet model
model_unet = tf.keras.models.load_model("models/Unet_model_2ch.hdf5", compile=False)

# Function to process images from the input folder and save segmented masks into the output folder
def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Check if the file is an image file
            # Load the image
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Resize the image to dimensions divisible by 32 and match the expected input shape of the model
            resized_img = cv2.resize(img, (384, 384))

            # Normalize the image
            normalized_img = resized_img.astype(np.float32) / 255.0

            # Expand dimensions to add channel dimension
            input_img = np.expand_dims(normalized_img, axis=-1)

            # Predict mask using the UNet model
            prediction = model_unet.predict(np.expand_dims(input_img, axis=0))
            predicted_mask = tf.argmax(prediction, axis=-1).numpy().squeeze()

            # Save the predicted mask as an image
            mask_filename = f"{os.path.splitext(filename)[0]}_mask.png"
            mask_path = os.path.join(output_folder, mask_filename)
            plt.imsave(mask_path, predicted_mask, cmap='gray')


# Define the input and output folders
# input_folder = "/content/drive/MyDrive/all work-BACKUP/automation folder/image processed images/2ch"
# output_folder = "/content/drive/MyDrive/all work-BACKUP/automation folder/segmented masks/2ch"

# # Process images from the input folder and save segmented masks into the output folder
# process_images(input_folder, output_folder)

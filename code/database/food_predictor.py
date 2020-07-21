import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import os
import pathlib
from pathlib import Path
from tensorflow.keras import datasets, layers, models

model = tf.keras.models.load_model('../image_recognition/saved_model/my_model2')
# Check its architecture
# print(model.summary())

def predict(image_path, delete=True):
     # Get image from path
     image = get_image(image_path)

     # Make prediction
     class_names = ['chicken_wings', 'french_fries', 'grilled_cheese_sandwich',
       'hamburger', 'hot_dog', 'ice_cream', 'macaroni_and_cheese',
       'ramen', 'steak', 'waffles']
     prediction = model.predict(np.array([np.asarray(image)]))
     predicted_class = class_names[np.argmax(prediction)]

     #Delete image at path
     if delete:
          delete_image(image_path)

     return predicted_class

def get_image(image_path):
     try:  
          img  = Image.open(image_path)
          img = img.resize((224, 224)) # Resize to training size
          return img
     except IOError: 
          print("IOError: Image file issue 1")

def delete_image(image_path):
     try:  
          os.remove(image_path)
          print("Image removed")
     except IOError: 
          print("IOError: Image file issue")

# if __name__ == "__main__":
#      print("THE FOOD IS: ", predict('images/food_picture.jpg', False))  

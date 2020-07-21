import numpy as np
from PIL import Image
import os
import pathlib
from pathlib import Path
import tflite_runtime.interpreter as tflite


interpreter = tflite.Interpreter(model_path='converted_model.tflite')
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict(image_path, delete=True):
     # Get image from path
     image = get_image(image_path)

     # Make prediction
     class_names = ['chicken_wings', 'french_fries', 'grilled_cheese_sandwich',
       'hamburger', 'hot_dog', 'ice_cream', 'macaroni_and_cheese',
       'ramen', 'steak', 'waffles']
     
     input_data = np.array([np.asarray(image)], dtype=np.float32)
     interpreter.set_tensor(input_details[0]['index'], input_data)
     interpreter.invoke()

     output_data = interpreter.get_tensor(output_details[0]['index'])

     predicted_class = class_names[np.argmax(output_data)]

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

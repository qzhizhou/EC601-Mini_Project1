import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()


for file in os.listdir(): #file is the image name of current_dir
    if file.endswith(".jpg"): 
        pic = file #image path + name +label
        file_name = os.path.join(os.path.dirname(__file__), pic)
        
        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        #print labels in every picture
        print(pic)
        for label in labels:
            print(label.description)
        print('\n')


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.keras.engine import training
import os
import numpy as np
import pandas as pd
import cv2
import base64
from pathlib import Path
from PIL import Image
import requests
from tensorflow.keras.preprocessing.image import load_img, save_img, img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.preprocessing import image as img_process

#load model
model_path = "/content/arcface_weights.h5"
model = loadModel(model_path)

#Extract facial Embeddings
embeddings = []
flags = []
for i in faces:
  embedding = model.predict(i)[0]
  embeddings.append(embedding)

#extract histogram of all faces (eye, eyebrow regions)
#--this part will take long time, consider to use LBP-----

# hists = []
# for face in frames:
#   hist = extract_ROI(face)
#   hists.append(hist)
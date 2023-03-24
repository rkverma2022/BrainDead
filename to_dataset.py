# Import the necessary libraries
from PIL import Image
from numpy import asarray
import os
from os import listdir
import numpy as np


def to_dataset(folder_dir, label_value):
    # get the path/directory
    img_data = []

    for images in os.listdir(folder_dir):

        # check if the image ends with png
        if (images.endswith(".png")):
            img_data.append(folder_dir + images)

    #converting .png to array
    count = 0
    data_set = []
    for img_path in img_data:
        
        count +=1
        img = Image.open(img_path)
        
        img = img.convert('L')
        img = img.resize((28, 28))
        numpydata = asarray(img)
        data_set.append(numpydata)

    label = np.arange(start=0, stop=count)
    for i in range(label.shape[0]):
        label[i] = label_value
    data_set = np.array(data_set)

    return data_set, label



# a, b = to_dataset('Train/happy/',1)
# print(a.shape)
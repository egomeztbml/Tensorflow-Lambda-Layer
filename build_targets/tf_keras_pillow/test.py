#! /usr/bin/python3

import tensorflow as tf
import keras
import numpy as np
from PIL import Image

print(np.zeros((10,)))
with tf.Session() as sess:
    print('hi')

simple_model = keras.models.load_model('simple_model.h5')

im = Image.open('test.png')
print(im.size)

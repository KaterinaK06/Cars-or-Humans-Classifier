import numpy as np
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
import tensorflow as tf
import matplotlib.pyplot as plt


model = tf.keras.models.load_model('saved_model/model')
model.summary()

i = input('Image name: ')

img = load_img('test_images/image_1/'+ i, target_size=(300, 300))

img = img_to_array(img)

img /= 255
img = np.expand_dims(img, axis=0)

img = np.vstack([img])

classes = model.predict(img, batch_size=16)

if classes[0] > 0.5:
    print('This is a human')
else:
    print('This is a car')


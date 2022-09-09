
#Classification model that distinguises humans from cars.
#Note that in images that contain both classes, the more prominent features will be detected.


import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import losses



car_dir = os.path.join('./training_images/cars' )

human_dir = os.path.join('./training_images/humans')


#Defines a custom callback.
class Callback(tf.keras.callbacks.Callback):
    #Stops the training when accuracy reaches a value higher than 0.95
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.95:
            print('\n Training reached an accuracy of 95%.')
            print('\n Cancelling training...')

            self.model.stop_training = True

#Defines the architecture of the model
def create_model():


    model = tf.keras.models.Sequential([

    #Convolutions are applied to the images for better results
    
    tf.keras.layers.Conv2D(16, (3,3), activation=tf.nn.relu, input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Conv2D(32, (3, 3), activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D(2,2),

    tf.keras.layers.Conv2D(64, (3,3), activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D(2,2),


    tf.keras.layers.Conv2D(64, (3,3), activation=tf.nn.relu),
    tf.keras.layers.MaxPooling2D(2,2),

    #After four convolutions the images have been reduced to 16x16
    
    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    
    
    #Last Dense layer using the sigmoid function, value 1 is for humans and 0 for cars
    
    tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)


    ])

    model.compile(loss='binary_crossentropy',
    optimizer=RMSprop(learning_rate=0.001),
    metrics=('accuracy')
    )

    


    return model



#Made an instance of the create_model function and the callback class
model= create_model()
callback = Callback()

#Divide the pixels by 255 so their values will fluctuate from 1 to 0.
gen = ImageDataGenerator(rescale=1/255)


train_gen = gen.flow_from_directory(
            './training_images/',
            target_size=(300, 300),  
            batch_size=16,
            class_mode='binary')

#model.summary()
#Uncomment the above to view the architecture of the model.


#100 epochs are hardcoded for the sake of higher accuracy but the training will possibly stop before 100 epochs.
model.fit(
        x=train_gen,
        steps_per_epoch=8,  
        epochs=100,
        callbacks=[callback])



#Saves the model so it can be used for testing, use tf.keras.models.load_model('saved_model/model') to load the pretrained model
#model.save('saved_model/model')
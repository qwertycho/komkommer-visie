# TensorFlow and tf.keras
import tensorflow as tf
import os

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
import json

def predict(filename):
    model = tf.keras.models.load_model('model.h5')

    inputPath = "./uploads/predict"

    dir_list = os.listdir(inputPath)


    testAfbeelding = tf.keras.utils.load_img((inputPath + "/" + filename))
    inputArray = tf.keras.utils.img_to_array(testAfbeelding)
    inputArray = np.array([inputArray])

    # de afbeelding instellingen
    # predictions = model.predict(inputArray)

    class_names = []


    with open('labels.json') as f:
        print("labels.json is geladen")
        data = json.load(f)
        print(data)
        class_names = data



    # #de voorspellingen van het model
    probability_model = tf.keras.Sequential([model,
                                                tf.keras.layers.Softmax()])
    predictions = probability_model.predict(inputArray)


    # output printen van de voorspellingen
    print (predictions[0])
    print ("het is een: " + class_names[np.argmax(predictions[0])])
    print ("de voorspelling is: " + str(np.max(predictions[0])*100) + "% zeker")
    print(predictions)

    return class_names[np.argmax(predictions[0])]
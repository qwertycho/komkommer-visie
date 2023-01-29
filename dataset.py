import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import matplotlib.pyplot as plt

# afbeeldings grootte
img_height = 500
img_width = 500
batch_size = 1

# Het model instellen
model = keras.Sequential([
    layers.Input((img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding="same"),
    layers.Conv2D(32, 3, padding="same"),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(10),
])

# de training data
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'trainSet', # de map waar de training data in staat
    labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height, img_width),
    shuffle=True, # de data wordt door elkaar gehaald
    seed=123, # de seed voor de randomizer
    validation_split=0.2, # 20% van de data wordt gebruikt voor de validatie
    subset="training",
)

# de validatie data
validation_ds = tf.keras.preprocessing.image_dataset_from_directory(
    'trainSet', # de map waar de data in staat
    labels='inferred',
    label_mode='int',
    color_mode='rgb',
    batch_size=batch_size,
    image_size=(img_height, img_width),
    shuffle=True, # de data wordt door elkaar gehaald
    seed=123,  # de seed voor de randomizer
    validation_split=0.2, # 20% van de data wordt gebruikt voor de validatie
    subset="validation",
)

# de instellingen van het model
model.compile(
    optimizer='adam',
    loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'],
)


epochs = int(input("Hoeveel epochs wil je trainen? "))

# het model trainen
history = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=epochs,
    verbose=1,

)

class_names = train_ds.class_names
print(class_names)


model.save('model.h5') # het opslaan van het model

# eDe labels exporteren naar een json file
import json
with open('labels.json', 'w') as outfile:
    json.dump(class_names, outfile)


# code om de training te visualiseren

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

# -*- coding: utf-8 -*-
"""Handwritten_Digit_Classifier.py
"""

!pip install streamlit

!pip install ipykernel>=5.1.2
!pip install python_version>="3.4"

import streamlit as st

st.title('Customizable Neural Network')

# num_layers = st.sidebar.slider('Number of hidden layers: ', 1, 5)
num_neurons = st.sidebar.slider('Number of neurons in hidden layer:', 1, 64)
num_epochs = st.sidebar.slider('Number of epochs:', 1, 10)


if st.button('Train the model'):
  import tensorflow as tf
  from tensorflow.keras.datasets import mnist
  from tensorflow.keras.layers import *
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.callbacks import ModelCheckpoint

  (X_train, y_train), (X_test, y_test) = mnist.load_data()

  def preprocess_images(images):
    images = images / 255
    return images


  X_train = preprocess_images(X_train)
  X_test = preprocess_images(X_test)


  model = Sequential()
  model.add(InputLayer((28, 28)))
  model.add(Flatten())
  model.add(Dense(32, 'relu'))
  model.add(Dense(10))
  model.add(Softmax())
  model.compile(loss='mse', optimizer="adam", metrics=['accuracy'])

  cp = ModelCheckpoint('model', save_best_only=True)
  history_cp=tf.keras.callbacks.CSVLogger('history.csv', separator=",", append=False)
  model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20, callbacks=[cp, history_cp])


if st.button('Evaluate the model'):
  import pandas as pd
  import matplotlib.pyplot as plt
  history = pd.read_csv('history.csv')
  fig = plt.figure()
  plt.plot(history['epoch'], history['accuracy'], )
  plt.plot(history['epoch'], history['val_accuracy'])
  plt.title('Model Accuracy')
  plt.ylabel('accuracy')
  plt.xlabel('epoch')
  plt.legend(['Train', 'Val'], loc='lower right')
  fig

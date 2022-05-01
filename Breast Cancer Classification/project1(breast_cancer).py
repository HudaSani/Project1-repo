# -*- coding: utf-8 -*-
"""Project1(Breast Cancer).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vsf8wSuiejIXig1sUD7LiF09BXHgu_jH
"""

from google.colab import files
upload = files.upload()

import pandas as pd 
df = pd.read_csv("data.csv")

df.info()
df.head()

#Data cleaning
#drop  unnecessary column
df = df.iloc[:,:-1]
df.drop(['id'], axis=1, inplace=True)

#one hot encoder
diagnose = {'M': 1, 'B': 0}
df['diagnosis'] = df['diagnosis'].map(diagnose)
 
df['diagnosis'] = df['diagnosis'].astype(float, errors = 'raise')
df['diagnosis'] = pd.to_numeric(df['diagnosis'],errors = 'coerce')

df.info()
df.head()

#prepare data
from sklearn.model_selection import train_test_split
import numpy as np

SEED = 12345

features = df.drop(['diagnosis'], axis=1)
labels = df['diagnosis']

x_train,x_test,y_train,y_test = train_test_split(features, labels, test_size=0.3, random_state=SEED)
nClass= len(np.unique(y_test))

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
scaler.transform(x_train)
scaler.transform(x_test)

#Feed-forward Neural Network for Classification

import tensorflow as tf

model = tf.keras.Sequential()

model.add(tf.keras.Input(shape=features.shape[1]))
model.add(tf.keras.layers.Dense(16,activation='relu'))
model.add(tf.keras.layers.Dense(nClass, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.summary()

#open tensorboard and save in directory
log_dir="logs/fit/"
tb_callback=tf.keras.callbacks.TensorBoard(log_dir=log_dir)

#train model
B_SIZE = 15
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), batch_size=B_SIZE, epochs=20, callbacks=[tb_callback])

# Commented out IPython magic to ensure Python compatibility.
# %reload_ext tensorboard
# %tensorboard --logdir logs

#Evaluate the result using test data 
test_result = model.evaluate(x_test,y_test,batch_size=B_SIZE)
print(f"Test loss = {test_result[0]}")
print(f"Test accuracy = {test_result[1]}")
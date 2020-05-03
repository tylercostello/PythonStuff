import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
df = pd.read_csv('molecular_activity.csv')
properties = list(df.columns.values)
properties.remove('Activity')
X = df[properties]
y = df['Activity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(4,)),
    keras.layers.Dense(16, activation=tf.nn.relu),
	keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid),
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
print("x")
print(X_train.shape)
print(X_train)
print("y")
print(y_train.shape)
print(y_train)
X_train = np.asarray(X_train).astype(np.float32)
y_train = np.asarray(y_train).astype(np.float32)
model.fit(X_train, y_train, epochs=50, batch_size=1)
print("here")
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)

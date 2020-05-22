import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
 # tf.keras.layers.Dense(16, activation='relu'),
  #tf.keras.layers.Dropout(0.2),
  #tf.keras.layers.Reshape((128,1)),
  #tf.keras.layers.LSTM(128),
#    tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
  #tf.keras.layers.Dense(10, activation='softmax')
])

predictions = model(x_train[:1]).numpy()
print(predictions)

tf.nn.softmax(predictions).numpy()
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
#print(len(model.layers))
#weights = model.layers[1].get_weights()[0]
#biases = model.layers[0].get_weights()[1]
#print("weights", weights)
#print("biases", biases)
print("x_train")
print(x_train.shape)
print(x_train[0])
print("y_train")
print(y_train[0])
model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

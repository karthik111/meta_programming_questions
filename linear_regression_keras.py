import tensorflow as tf
from numpy.random import default_rng

def prep_data():


    x_train = default_rng(42).random((1000, 3))

    x_test = default_rng(40).random((10,3))

    y_train = x_train[:, 0] + 2 * x_train[:, 1] + 3 * x_train[:, 2]

    y_test = x_test[:, 0] + 2 * x_test[:, 1] + 3 * x_test[:, 2]

    return x_train, y_train, x_test, y_test

x_train, y_train, x_test, y_test = prep_data()
model = tf.keras.models.Sequential([
  tf.keras.layers.Input(shape=(3)),
  tf.keras.layers.Dense(64, activation='relu'),
  tf.keras.layers.Dense(64, activation='relu'),
  #tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(1)
])

model.compile(loss='mean_absolute_error',
              optimizer=tf.keras.optimizers.Adam(0.001),
              metrics=['mse'])

hist = model.fit(x_train, y_train, epochs=100, validation_split = 0.2)

model.evaluate(x_test,  y_test, verbose=2)


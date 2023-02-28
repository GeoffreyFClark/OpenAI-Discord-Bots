import tensorflow as tf

# Build and train the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10)  # Where X_Train and Y_Train are input and output

# Save the trained model to a HDF5 file
model.save('my_model.h5')

# Load the saved model
loaded_model = tf.keras.models.load_model('my_model.h5')

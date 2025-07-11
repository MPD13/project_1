import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, BatchNormalization
from tensorflow.keras.utils import to_categorical

# Load the FER2013 dataset
data = pd.read_csv('fer2013.csv')
pixels = data['pixels'].str.split().tolist()
X = np.array(pixels, dtype='float32').reshape(-1, 48, 48, 1) / 255.0
y = to_categorical(data['emotion'], num_classes=7)

# Split into training and validation sets
train_idx = data['Usage'] == 'Training'
test_idx = data['Usage'] != 'Training'
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

# Define the CNN model
model = Sequential([
    Conv2D(64, (3,3), activation='relu', input_shape=(48,48,1)),
    BatchNormalization(), MaxPooling2D(),
    Conv2D(128, (3,3), activation='relu'),
    BatchNormalization(), MaxPooling2D(),
    Conv2D(256, (3,3), activation='relu'),
    BatchNormalization(), MaxPooling2D(),
    Dropout(0.5),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(7, activation='softmax')
])

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=25, batch_size=64, validation_data=(X_test, y_test))

# Save the trained model
model.save('emotion_model.h5')
print("Model saved as emotion_model.h5")

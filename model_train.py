import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
def model_train(train_images,train_labels,searches):
    train_images=np.array(train_images)
    train_labels=np.array(train_labels)
    model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(searches), activation='softmax')
])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                metrics=['accuracy'])
    model.fit(train_images, train_labels, epochs=10, batch_size=2)
    return model

import cv2
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
import threading
import multiprocessing
import time
lock = threading.Lock()
numberOfCores = multiprocessing.cpu_count()
activethreads=threading.active_count()
data_generator = ImageDataGenerator(
    rotation_range=20,  # Random rotation in the range [-20, 20] degrees
    width_shift_range=0.1,  # Random horizontal shift by 10% of the image width
    height_shift_range=0.1,  # Random vertical shift by 10% of the image height
    zoom_range=0.2,  # Random zoom between 80% and 120% of the original size
    horizontal_flip=True,  # Randomly flip the image horizontally
    fill_mode='nearest'  # Fill any newly created pixels after rotation or shifting
)
aug_images=[]
aug_label=[]
num_augmented_images = 3
def aug_image_fun(image,label):
    for n in range(num_augmented_images):
        method=data_generator.random_transform
        image=method(image)
        with lock:
            aug_images.append(image)
            aug_label.append(label)
def aug_train(train_images,train_label):
    n=len(train_label)
    for i in range(n):
        t = threading.Thread(target=aug_image_fun , args=(train_images[i],train_label[i],))
        t.start()
        while True:
            if (threading.active_count()-activethreads+1<=5*numberOfCores):
                break
            time.sleep(1)
    while True:
        if (threading.active_count()==activethreads):
            break
        time.sleep(1)
    train_images=train_images+aug_images
    train_label=train_label+aug_label
    return train_images,train_label
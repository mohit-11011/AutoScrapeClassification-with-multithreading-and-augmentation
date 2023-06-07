import os
import cv2
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
def split(labels):
    folder_path = ''
    images = []
    image_labels = []
    for label in labels:
        label_path = os.path.join(folder_path, label)
        image_files = os.listdir(label_path)
        for image_file in image_files:
            image_path = os.path.join(label_path, image_file)
            image = cv2.imread(image_path)
            desired_width = 256
            desired_height = 256
            image = cv2.resize(image, (desired_width, desired_height))
            images.append(image)
            image_labels.append(label)
    images
    len(image_labels)

    train_images, test_images, train_labels, test_labels = train_test_split(images, image_labels, test_size=0.45, stratify=image_labels, random_state=42)
    return train_images, train_labels
def split_test(labels):
    folder_path = ''
    images = []
    image_labels = []
    for label in labels:
        label_path = os.path.join(folder_path, label)
        image_files = os.listdir(label_path)
        for image_file in image_files:
            image_path = os.path.join(label_path, image_file)
            image = cv2.imread(image_path)
            desired_width = 256
            desired_height = 256
            image = cv2.resize(image, (desired_width, desired_height))
            images.append(image)
            image_labels.append(label)
    images
    len(image_labels)

    train_images, test_images, train_labels, test_labels = train_test_split(images, image_labels, test_size=0.45, stratify=image_labels, random_state=42)
    return test_images, test_labels

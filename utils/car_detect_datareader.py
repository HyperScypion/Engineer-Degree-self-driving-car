import cv2
import numpy as np
from glob import glob
from sklearn.model_selection import train_test_split


def return_imgs():
    cars = glob('../data/cars_rear_view/vehicles/**/*.png')
    non_cars = glob('../data/cars_rear_view/non-vehicles/**/*.png')
    
    return cars, non_cars


def create_dataset(cars, non_cars):
    X, y = [], []
    for _, img in enumerate(cars):
        X.append(cv2.imread(img))
        y.append(1)

    for _, img in enumerate(non_cars):
        X.append(cv2.imread(img))
        y.append(0)

    return X, y

def split_data(test_split=0.4, validation_split=0.15):
    cars, non_cars = return_imgs()
    X, y = create_dataset(cars, non_cars)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_split)
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=validation_split)
    return X_train, X_test, X_val, y_train, y_test, y_val


# python3
import cv2
import numpy as np
import math
import os
# from skimage.util import random_noise
# from skimage import io


def show_original(file):
    img = cv2.imread('tests/' + file)
    cv2.imshow('Original', img)


# Multidirectional Wave
def multi_dir(file):
    img = cv2.imread('tests/' + file)
    rows, cols, _ = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            offset_x = int(20.0 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(20.0 * math.cos(2 * 3.14 * j / 150))
            if i+offset_y < rows and j+offset_x < cols:
                img_output[i,j] = img[(i+offset_y)%rows,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    # cv2.imshow('Multidirectional wave', img_output)
    # io.imshow(img_output)
    # io.show()
    cv2.imwrite('./tests/multidir/' + file, img_output)


# Concave effect
def concave(file):
    img = cv2.imread('tests/' + file)
    rows, cols, _ = img.shape
    img_output = np.zeros(img.shape, dtype=img.dtype)
    for i in range(rows):
        for j in range(cols):
            offset_x = int(128.0 * math.sin(2 * 3.14 * i / (2*cols)))
            offset_y = 0
            if j+offset_x < cols:
                img_output[i,j] = img[i,(j+offset_x)%cols]
            else:
                img_output[i,j] = 0
    # cv2.imshow('Concave', img_output)
    # io.imshow(img_output)
    # io.show()
    cv2.imwrite('./tests/concave/' + file, img_output)


def brighter(file):
    # Change brightness
    img = cv2.cvtColor(cv2.imread('tests/' + file), cv2.COLOR_BGR2HSV)
    img[:, :, 2] = np.where(255 - img[:,:,2] < 100, 255, img[:,:,2] + 100)
    img_output = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    # cv2.imshow('Brightness', img_output)
    # io.imshow(img_output)
    # io.show()
    cv2.imwrite('./tests/bright/' + file, img_output)


def add_noise(file):
    # add noise
    img = cv2.imread('tests/' + file)
    img_output = random_noise(img, mode='gaussian', clip=True)
    # io.imshow(img_output)
    # io.show()
    cv2.imwrite('./tests/noise/' + file, img_output)


if __name__ == "__main__":

    print("Note: you need to create directories under ./tests/ first to save images")
    files = os.listdir("tests")
    files = [f for f in files if "png" in f or "jpg" in f]
    for file in files:
        multi_dir(file)
        concave(file)
        brighter(file)
        #add_noise(file)


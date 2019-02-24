# python3
import cv2
import numpy as np
import math


file = "test.png"

# Multidirectional Wave

img = cv2.imread(file)
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
cv2.imshow('Multidirectional wave', img_output)


# Concave effect

img = cv2.imread(file)
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
cv2.imshow('Concave', img_output)


# Change brightness
img = cv2.cvtColor(cv2.imread(file), cv2.COLOR_BGR2HSV)
img = np.where(255 - img[:,:,2] < 100, 255, img[:,:,2] + 100)
img_output = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow('Brightness', img_output)


cv2.waitKey()

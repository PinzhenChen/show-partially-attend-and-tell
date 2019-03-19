import cv2
import numpy as np
from skimage.util import random_noise

def motion_blur(path, size):
    img = cv2.imread(path)
    cv2.imshow('Original', img)

    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size

    # applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_motion_blur)

    cv2.imshow('Motion Blur', output)
    cv2.waitKey(0)


def gaussian_noise(path):
    img = cv2.imread(path)
    cv2.imshow('Original', img)

    output1 = random_noise(img, mode='gaussian', clip=True, var=0.1)
    output2 = random_noise(img, mode='gaussian', clip=True, var=0.5)
    output3 = random_noise(img, mode='gaussian', clip=True, var=0.9)
    output4 = random_noise(img, mode='gaussian', clip=True, var=1.3)

    cv2.imshow('Gaussian Noise1', output1)
    cv2.imshow('Gaussian Noise2', output2)
    cv2.imshow('Gaussian Noise3', output3)
    cv2.imshow('Gaussian Noise4', output4)
    cv2.waitKey(0)

def blur(path, size):
    img = cv2.imread(path)
    cv2.imshow('Original', img)
    blur = cv2.blur(img, (size, size))
    cv2.imshow('Blur', blur)
    cv2.waitKey(0)


if __name__ == '__main__':
    blur('input.jpeg', 5)



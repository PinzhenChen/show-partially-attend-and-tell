import cv2
import numpy as np
from skimage.util import random_noise
import matplotlib.pyplot as plt
from skimage import io

def motion_blur(imgname, path, size):
    # size: 5, 10, 15, 20
    img = cv2.imread(path)
    # cv2.imshow('Original', img)

    # generating the kernel
    kernel_motion_blur = np.zeros((size, size))
    kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
    kernel_motion_blur = kernel_motion_blur / size

    # applying the kernel to the input image
    output = cv2.filter2D(img, -1, kernel_motion_blur)

    # io.imshow(output)
    # io.show()
    cv2.imwrite('./Flickr8k_Dataset/motion_blur_' + str(size) + "/" + imgname, output)


def gaussian_noise(imgname, path, size):
    # size: 0.1, 0.5, 0.9, 1.3
    img = io.imread(path)
    # io.imshow(img)
    # io.show()
    output = random_noise(img, mode='gaussian', clip=True, var=size)
    # cv2.imshow('Gaussian Noise1', output)
    # cv2.waitKey(0)
    # cv2.imwrite('./Flickr8k_Dataset/gaussian_' + str(size) + "/" + imgname, output)
    # plt.imsave('./Flickr8k_Dataset/gaussian_' + str(size) + "/" + imgname, output)
    # io.imshow(output)
    # io.show()
    io.imsave('./Flickr8k_Dataset/gaussian_' + str(size) + "/" + imgname, output)


def blur(imgname, path, size):
    # size: 4, 8, 12, 16
    img = cv2.imread(path)
    # cv2.imshow('Original', img)
    output = cv2.blur(img, (size, size))
    # cv2.imshow('Blur', blur)
    # cv2.waitKey(0)
    cv2.imwrite('./Flickr8k_Dataset/blur_' + str(size) + "/" + imgname, output)


if __name__ == "__main__":
    path = "Flickr8k_Dataset/"
    # print("Note: you need to create empty directories under './tests/' first to save images")
    f = open('Flickr_8k.testImages.txt','r')
    for line in f:
        # print(line)
        for s in [0.01, 0.05, 0.09, 0.13]:
            img = line.strip()
            gaussian_noise(img, path+img, s)

    # files = os.listdir("Flicker8k_Dataset")
    # files = [f for f in files if "png" in f or "jpg" in f]
    # print(len(tests))




import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

class ImageManager(object):
    def __init__(self):
        pass

    @staticmethod
    def open_image(image_path):
        return cv.imread(image_path)

    @staticmethod
    def save_image(image, image_path):
        cv.imwrite(image, image_path)

    @staticmethod
    def display_image(image, image_name='image'):
        cv.imshow(image_name, image)
        cv.waitKey(0)
        cv.destroyWindow(image_name)

    @staticmethod
    def display_images(images):
        if type(images) is not list:
            return

        for image_index in xrange(len(images)):
            print images[image_index][0].ctypes
            print images[image_index][0].shape

            plt.subplot(5, 3, image_index+1)

            plt.imshow(images[image_index][0], cmap='gray')
            plt.title(images[image_index][1])

            plt.xticks([])
            plt.yticks([])


        plt.savefig('foo.png')

    @staticmethod
    def copy_image(image):
        copy = np.zeros(image.shape)
        for x in xrange(image.shape[1]):
            for y in xrange(image.shape[0]):
                copy[y][x] = image[y][x]
        return copy

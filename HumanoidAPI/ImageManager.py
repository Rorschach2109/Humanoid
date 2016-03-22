import cv2 as cv
import matplotlib.pyplot as plt

class ImageManager(object):
    def __init__(self):
        pass

    @staticmethod
    def open_image_as_gray(image_path):
        return cv.imread(image_path, cv.IMREAD_GRAYSCALE)

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
            plt.subplot(4, 3, image_index+1), plt.imshow(images[image_index], cmap='gray', interpolation='bicubic')
            plt.title('a')
            plt.xticks([]), plt.yticks([])

        plt.savefig('foo.png')

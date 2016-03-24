from HumanoidOperations.Operation import Operation

import cv2 as cv

class ContourOperation(Operation):
    def __init__(self):
        super(ContourOperation, self).__init__(self.__class__.__name__)

    def run_operation(self, **kwargs):
        super(ContourOperation, self).run_operation(**kwargs)

        img2 = self._image.copy()

        im, contours, hierarchy = cv.findContours(self._image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        print len(contours)

        for contour_index in xrange(len(contours)):
            area = cv.contourArea(contours[contour_index])
            print area
            cv.drawContours(im, contours, contour_index, (255, 255, 255), cv.FILLED)


        #return im, self._operation_name
        cv.imshow('copy', img2)
        cv.imshow('find contours', im)
        cv.imshow('subtraction', cv.subtract(im, img2))

        cv.waitKey(0)
        cv.destroyWindow('a')

    def run_operation_old(self, **kwargs):
        super(ContourOperation, self).run_operation(**kwargs)

        im, contours, hierarchy = cv.findContours(self._image, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(im, contours, -1, (255, 255, 0), 1)
        return im
        cv.imshow('a', im)
        cv.waitKey(0)
        cv.destroyAllWindows()

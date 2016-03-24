from HumanoidAPI import OperationsBridge, MorphologyEnum
from HumanoidAPI.ImageManager import ImageManager
from HumanoidAPI.OperationsRunner import OperationsRunner

import numpy as np
from pip._vendor.distlib.compat import OrderedDict


def better_run():
    image_path = 'Resources/cap1.png'
    image = ImageManager.open_image(image_path)

    runner = OperationsRunner()
    # runner.add_operation(runner.HISTOGRAM_EQUALIZATION)
    runner.add_operation(runner.CONVERT_TO_GRAY)
    runner.add_operation(runner.THRESH_OTSU_BINARY)
    runner.add_operation(runner.VERTICAL_REMOVAL, 5)
    runner.add_operation(runner.HORIZONTAL_REMOVAL, 5)
    runner.add_operation(runner.ENLARGE, 7, 7)

    #runner.add_operation(runner.CANNY)

    # runner.add_operation(runner.CONTOUR)

    runner.run_operations(image)

    ImageManager.display_images(runner.get_image_history())


import cv2 as cv
import numpy as np

def clear_dist(image, start, end):
    size = end[1]+1 - start[1]
    if size < 4:
        for x in xrange(start[1], end[1]+1):
            image[start[0]][x] = 255

def clear_dist_hor(image, start, end):
    size = end[1]+1 - start[1]
    if size < 4:
        for x in xrange(start[1], end[1]+1):
            image[x][start[0]] = 255

def test2():
    image = cv.imread('Resources/cap2.png')
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    ret, thresh = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
    ret, thresh1 = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)

    no_rows = thresh.shape[0]
    no_cols = thresh.shape[1]
    size = thresh.size

    temp = dict()

    print thresh.shape
    for y in xrange(no_rows):
        start = 0, 0
        end = 0, 0
        start_flag = False

        for x in xrange(no_cols):
            if False == start_flag and thresh[y][x] == 0:
                start = y, x
                #print 'start', start
                start_flag = True
            elif True == start_flag and thresh[y][x] != 0:
                end = y, x
                start_flag = False
                clear_dist(thresh, start, end)
                clear_dist(thresh1, start, end)
                temp[(start, end)] = end[1] - start[1] + 1
                #print 'end', end

    # cv.imshow('First', thresh)

    for x in xrange(no_cols):
        start = 0, 0
        end = 0, 0
        start_flag = False

        for y in xrange(no_rows):
            if False == start_flag and thresh[y][x] == 0:
                start = x, y
                start_flag = True
                print 'Start:', start
            elif True == start_flag and thresh[y][x] != 0:
                end = x, y
                start_flag = False
                clear_dist_hor(thresh, start, end)
                clear_dist_hor(thresh1, start, end)
                print 'End:', end

    # cv.imshow('Second', thresh)

    # cv.imshow('Fourth', thresh)

    import operator
    #ord_dict = OrderedDict(sorted(temp.items(), key=operator.itemgetter(1)))
    #print ord_dict.values()[len(ord_dict.values())/2]

    #corners = cv.goodFeaturesToTrack(thresh, 20, 0.01, 10)
    im, cnt, hier = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt_index in xrange(len(cnt)):
        center, radius = cv.minEnclosingCircle(cnt[cnt_index])

        if radius < 0:
            cv.circle(thresh1, (int(center[0]), int(center[1])), int(radius)+1, 255, -1)

    # for i in corners:l
    #     x, y = i.ravel()
    #     cv.circle(image, (x,y), 2, (0,255,0), -1)

    cv.imwrite('org.png', cv.resize(thresh1,None, fx=2, fy=1, interpolation=cv.INTER_CUBIC))
    import pytesseract as tess
    from PIL import Image
    print tess.image_to_string(Image.open('org.png'))
    # cv.imshow('thresh1', thresh1)
    # cv.imshow('thresh', thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()

def test_otsu():
    image = cv.imread('Resources/cap1.png', cv.IMREAD_GRAYSCALE)

    hist, bins = np.histogram(image.ravel(), 256, [0, 256])
    print hist

    cv.imshow('a', hist)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    better_run()

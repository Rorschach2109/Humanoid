from HumanoidAPI import OperationsBridge, MorphologyEnum
from HumanoidAPI.ImageManager import ImageManager
from HumanoidAPI.OperationsRunner import OperationsRunner

import numpy as np

def run():
    image_path = 'captcha1.jpg'
    #image_path = 'test2.jpg'
    image = ImageManager.open_image_as_gray(image_path)
    # ImageManager.display_image(image)

    bridge = OperationsBridge.OperationsBridge(image)

    image = bridge.enlarge_image(image, 6, 6)
    ImageManager.display_image(image, 'after enlarge')
    image = bridge.thresh_image(image, 200)
    ImageManager.display_image(image, 'after thresh')

    # image = bridge.thresh_image(image, 220)
    # ImageManager.display_image(image, 'after thresh')
    # image = bridge.morph_image(image, MorphologyEnum.MorphologyEnum.OPENING, np.ones((3, 3), np.uint8))

    ImageManager.display_images(bridge.image_history)

def better_run():
    image_path = 'test2.jpg'
    image = ImageManager.open_image_as_gray(image_path)

    runner = OperationsRunner()
    runner.add_operation(runner.THRESH_BINARY_INV, 220)
    runner.add_operation(runner.ENLARGE, 5, 5)

    #runner.add_operation(runner.CANNY)

    runner.add_operation(runner.CONTOUR)

    runner.run_operations(image)

    #ImageManager.display_images(runner.get_image_history())

def test():
    import cv2
    import numpy as np

    img = cv2.imread('games.jpg')
    # img = cv2.resize(img, None, fx=15, fy=15)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,50,220,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,np.pi/360,5)
    for rho,theta in lines[0]:
        print rho, theta
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imshow('a', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test()
